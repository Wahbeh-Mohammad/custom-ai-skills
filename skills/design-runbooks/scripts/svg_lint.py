#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
svg_lint - deterministic checks for the SVG assets a design-runbooks run generates.

Usage: python3 scripts/svg_lint.py <project-root> [--design DESIGN.md] [--kept-incumbent]

Walks every *.svg under the project and the markup that points at placeholders or og:image.
Rules and their severity: reference/svg-assets.md § 6. Standard library only. Read-only: it
writes nothing. Exit 1 when any BLOCKING finding is reported, 0 otherwise, 2 on bad usage.

  --design          DESIGN.md to read colour tokens from (default: <project-root>/DESIGN.md).
                    With no DESIGN.md the palette check does not fire.
  --kept-incumbent  The logo is a kept incumbent (Runbook 1): it is scaled, never redrawn, so
                    the favicon whole-pixel check is off.
"""

import argparse
import math
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from xml.parsers import expat

KIT = ("mark", "favicon", "app-icon", "lockup", "og-card")
BUDGET = {"mark": 2048, "favicon": 2048, "app-icon": 4096, "lockup": 16384, "og-card": 122880}
SKIP_DIRS = {"node_modules", "dist", "build", "vendor", "__pycache__"}
MARKUP_EXT = {".html", ".htm", ".astro", ".vue", ".svelte", ".jsx", ".tsx"}
COLOR_ATTRS = ("fill", "stroke", "stop-color", "flood-color", "lighting-color", "color", "style")
COLOR_TOLERANCE = 3
PIXEL_ATTRS = ("x", "y", "width", "height", "x1", "y1", "x2", "y2", "cx", "cy", "r", "rx", "ry")
RASTER_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp")

HEX_RE = re.compile(r"^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
COLOR_TOKEN_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|oklch\([^)]*\)", re.I)
URL_RE = re.compile(r"url\([^)]*\)", re.I)
NUMBER_RE = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
EXTERNAL_RE = re.compile(r"^\s*(?:https?:)?//", re.I)
IMG_RE = re.compile(r"<img\b[^>]*>", re.I | re.S)
META_RE = re.compile(r"<meta\b[^>]*>", re.I | re.S)
GENERIC_ALT_RE = re.compile(
    r"(?:placeholder|image|photo|picture|img|screenshot|graphic)"
    r"(?:\s+(?:placeholder|image|here))?",
    re.I,
)
SKETCH_CLASS_RE = re.compile(r"sketch|doodle", re.I)

REF = "svg-assets.md § 6"


@dataclass
class Finding:
    severity: str
    path: str
    line: int
    rule: str
    what: str
    fix: str

    def format(self):
        return (
            f"{self.severity:<9} {self.path}:{self.line}\n"
            f"  {REF} · {self.rule}\n"
            f"  {self.what}\n"
            f"  Fix: {self.fix}"
        )


# --- classification ---------------------------------------------------------


def classify(path):
    """Kind of asset, from its file name: a kit piece, a placeholder, or other."""
    path = Path(path)
    stem = path.stem.lower()
    if path.parent.name.lower() == "placeholders":
        return "placeholder"
    if stem == "mark" or stem.startswith("mark-"):
        return "mark"
    for kind in ("favicon", "app-icon", "lockup", "og-card"):
        if stem.startswith(kind):
            return kind
    return "other"


# --- colour -----------------------------------------------------------------


def _oklch_to_rgb(lightness, chroma, hue):
    a = chroma * math.cos(math.radians(hue))
    b = chroma * math.sin(math.radians(hue))
    l_ = lightness + 0.3963377774 * a + 0.2158037573 * b
    m_ = lightness - 0.1055613458 * a - 0.0638541728 * b
    s_ = lightness - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    linear = (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )

    def encode(c):
        c = max(0.0, min(1.0, c))
        c = 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055
        return round(c * 255)

    return tuple(encode(c) for c in linear)


def _inner(value):
    return value[value.index("(") + 1 : value.rindex(")")].strip()


def parse_color(value):
    """sRGB triple for a hex, rgb() or oklch() literal; None for anything else."""
    value = value.strip()
    match = HEX_RE.match(value)
    if match:
        digits = match.group(1)
        if len(digits) in (3, 4):
            digits = "".join(c * 2 for c in digits[:3])
        return tuple(int(digits[i : i + 2], 16) for i in (0, 2, 4))
    low = value.lower()
    try:
        if low.startswith("rgb"):
            parts = [p for p in re.split(r"[\s,/]+", _inner(low)) if p][:3]
            channels = [
                round(float(p[:-1]) * 2.55) if p.endswith("%") else round(float(p)) for p in parts
            ]
            return tuple(max(0, min(255, c)) for c in channels) if len(channels) == 3 else None
        if low.startswith("oklch"):
            parts = [p for p in re.split(r"[\s/]+", _inner(low)) if p]
            lightness = float(parts[0][:-1]) / 100 if parts[0].endswith("%") else float(parts[0])
            chroma = float(parts[1][:-1]) * 0.004 if parts[1].endswith("%") else float(parts[1])
            hue = float(parts[2].replace("deg", ""))
            return _oklch_to_rgb(lightness, chroma, hue)
    except (ValueError, IndexError):
        return None
    return None


def load_palette(design_md):
    """sRGB values of the `colors:` group in DESIGN.md frontmatter; None when there is none."""
    design_md = Path(design_md)
    if not design_md.is_file():
        return None
    text = design_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    frontmatter = text[3:end] if end != -1 else text[3:]
    palette, in_colors = [], False
    for line in frontmatter.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line[0] not in " \t":
            in_colors = stripped.startswith("colors:")
            continue
        if not in_colors:
            continue
        _, _, raw = stripped.partition(":")
        raw = raw.strip()
        if raw[:1] in "\"'":
            raw = raw[1 : raw.find(raw[0], 1)]
        else:
            raw = raw.split(" #")[0].strip()
        rgb = parse_color(raw)
        if rgb is not None:
            palette.append(rgb)
    return palette or None


def _in_palette(rgb, palette):
    return any(max(abs(a - b) for a, b in zip(rgb, p)) <= COLOR_TOLERANCE for p in palette)


# --- SVG tree ---------------------------------------------------------------


class Node:
    __slots__ = ("tag", "attrs", "line", "children", "text")

    def __init__(self, tag, attrs, line):
        self.tag = tag.split(":")[-1]
        self.attrs = attrs
        self.line = line
        self.children = []
        self.text = ""

    def iter(self):
        yield self
        for child in self.children:
            yield from child.iter()


def parse_svg(data):
    parser = expat.ParserCreate()
    stack, holder = [], []

    def start(tag, attrs):
        node = Node(tag, attrs, parser.CurrentLineNumber)
        if stack:
            stack[-1].children.append(node)
        else:
            holder.append(node)
        stack.append(node)

    def end(_tag):
        stack.pop()

    def chars(text):
        if stack:
            stack[-1].text += text

    parser.StartElementHandler = start
    parser.EndElementHandler = end
    parser.CharacterDataHandler = chars
    parser.Parse(data, True)
    return holder[0]


def _view_box(node):
    parts = NUMBER_RE.findall(node.attrs.get("viewBox", ""))
    return tuple(float(p) for p in parts) if len(parts) == 4 else None


def _float(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# --- SVG checks -------------------------------------------------------------


def _outside_safe_zone(node, view_box):
    min_x, min_y, width, height = view_box
    cx, cy = min_x + width / 2, min_y + height / 2
    radius = 0.4 * min(width, height) + 0.5
    if node.tag == "rect":
        x = _float(node.attrs.get("x", 0), None)
        y = _float(node.attrs.get("y", 0), None)
        w = _float(node.attrs.get("width"), None)
        h = _float(node.attrs.get("height"), None)
        if None in (x, y, w, h):
            return False
        if x <= min_x and y <= min_y and w >= width and h >= height:
            return False  # full-bleed background
        corners = ((x, y), (x + w, y), (x, y + h), (x + w, y + h))
        return any(math.hypot(px - cx, py - cy) > radius for px, py in corners)
    if node.tag == "circle":
        x, y, r = (_float(node.attrs.get(k, 0), None) for k in ("cx", "cy", "r"))
        return None not in (x, y, r) and math.hypot(x - cx, y - cy) + r > radius
    return False


def _off_pixel_grid(node):
    for attr in PIXEL_ATTRS:
        value = _float(node.attrs.get(attr), None)
        if value is not None and value != int(value):
            return f"{attr}={node.attrs[attr]}"
    if node.tag == "path":
        for number in NUMBER_RE.findall(node.attrs.get("d", "")):
            if float(number) != int(float(number)):
                return f"path coordinate {number}"
    return None


def lint_svg(path, root, palette, kept_incumbent=False):
    path, root = Path(path), Path(root)
    rel = path.relative_to(root).as_posix()
    kind = classify(path)
    data = path.read_bytes()
    findings = []

    def add(severity, line, rule, what, fix):
        findings.append(Finding(severity, rel, line, rule, what, fix))

    try:
        svg = parse_svg(data)
    except expat.ExpatError as error:
        add("BLOCKING", error.lineno, "svg-parse",
            f"Not well-formed XML: {expat.ErrorString(error.code)}.",
            "Fix the markup until it parses; a malformed SVG file renders nothing.")
        return findings

    view_box = _view_box(svg)
    if "viewBox" not in svg.attrs:
        add("BLOCKING", svg.line, "svg-viewbox", "The root <svg> has no viewBox, so it cannot scale.",
            'Add viewBox="0 0 <w> <h>" matching the drawing coordinates.')

    has_text = False
    text_reported = sketch_reported = grid_reported = zone_reported = False
    off_palette_seen = set()

    for node in svg.iter():
        tag = node.tag
        if tag == "script":
            add("BLOCKING", node.line, "svg-script", "<script> inside an SVG asset.",
                "Delete it. Assets draw; they never execute.")
        if tag == "foreignObject":
            add("BLOCKING", node.line, "svg-foreign-object", "<foreignObject> embeds HTML in the asset.",
                "Redraw the content as SVG shapes, or drop it.")
        for name, value in node.attrs.items():
            if name.lower().startswith("on"):
                add("BLOCKING", node.line, "svg-event-handler", f"Event handler attribute {name}=.",
                    f"Delete {name}=. Assets never carry behaviour.")
            if name in ("href", "xlink:href") and EXTERNAL_RE.match(value):
                add("BLOCKING", node.line, "svg-external-href", f"External reference {value}.",
                    "Inline the referenced shape; an asset depends on no third-party host.")
        if tag == "image" and kind in KIT:
            href = node.attrs.get("href") or node.attrs.get("xlink:href") or ""
            if href.startswith("data:image") or href.lower().split("?")[0].endswith(RASTER_EXT):
                add("BLOCKING", node.line, "svg-embedded-raster",
                    f"The {kind} embeds a raster image.",
                    "Draw it as vector shapes. A raster inside the kit defeats scaling and the byte budget.")
        if (tag == "feTurbulence" or SKETCH_CLASS_RE.search(node.attrs.get("class", ""))) and not sketch_reported:
            sketch_reported = True
            add("ADVISORY", node.line, "svg-sketch",
                "feTurbulence grain or a sketch/doodle class: SVG imitating a picture.",
                "Remove it. impeccable-anti-patterns.md: real illustration or none; SVG does geometry.")
        if tag == "text":
            has_text = True
            if kind in ("mark", "lockup") and not text_reported:
                text_reported = True
                add("BLOCKING", node.line, "svg-text-in-mark",
                    f"<text> in the {kind}: off-site it renders in whatever font the viewer has.",
                    "Mark: remove the text (the wordmark stays live text in the page). "
                    "Lockup: outline the type (svg-assets.md § 5).")
            if kind == "og-card" and not text_reported:
                text_reported = True
                add("ADVISORY", node.line, "og-card-text",
                    "<text> in the og-card source.",
                    "Outline the type, or rasterize with a renderer that loads the real font "
                    "(headless Chromium) and check the PNG shows it.")
        if kind in KIT and palette:
            sources = [node.attrs[a] for a in COLOR_ATTRS if a in node.attrs]
            if tag == "style":
                sources.append(node.text)
            for source in sources:
                for literal in COLOR_TOKEN_RE.findall(URL_RE.sub("", source)):
                    rgb = parse_color(literal)
                    if rgb is None or literal.lower() in off_palette_seen or _in_palette(rgb, palette):
                        continue
                    off_palette_seen.add(literal.lower())
                    add("BLOCKING", node.line, "svg-off-palette",
                        f"{literal} is not a DESIGN.md colour.",
                        "Use a value from DESIGN.md frontmatter `colors`, or add the token to "
                        "DESIGN.md deliberately and say so.")
        if kind == "favicon" and not kept_incumbent and not grid_reported:
            offender = _off_pixel_grid(node)
            if offender:
                grid_reported = True
                add("ADVISORY", node.line, "favicon-pixel-grid",
                    f"Favicon edge off the pixel grid ({offender}); it blurs at 16px.",
                    "Redraw on whole units of the viewBox grid.")
        if kind == "app-icon" and view_box and not zone_reported and _outside_safe_zone(node, view_box):
            zone_reported = True
            add("ADVISORY", node.line, "app-icon-safe-zone",
                "Shape outside the maskable safe circle (radius 40% of the icon).",
                "Pull the drawing inside the central circle; platforms crop everything outside it.")

    if kind in KIT and not any(child.tag == "title" for child in svg.children):
        add("ADVISORY", svg.line, "svg-title", f"The {kind} has no <title>.",
            'Add <title> with the product name as the first child, and role="img" on <svg>.')
    if kind == "placeholder" and not has_text:
        add("ADVISORY", svg.line, "placeholder-label",
            "Placeholder with no visible label; it can read as finished content.",
            'Add one <text> label, "<Kind> · <ratio>" (e.g. "Photo · 4:5"), in the label face\'s '
            "generic fallback — an SVG loaded through <img> cannot load web fonts.")
    if kind == "og-card" and view_box and view_box != (0, 0, 1200, 630):
        add("ADVISORY", svg.line, "og-card-size",
            f"og-card viewBox is {svg.attrs.get('viewBox')}, not 0 0 1200 630.",
            'Set viewBox="0 0 1200 630"; link previews crop other ratios.')
    if kind in BUDGET and len(data) > BUDGET[kind]:
        add("ADVISORY", svg.line, "svg-byte-budget",
            f"The {kind} is {len(data)} bytes; the budget is {BUDGET[kind]}.",
            "Simplify the geometry, merge paths, drop editor metadata and precision beyond the grid.")
    return findings


# --- markup checks ----------------------------------------------------------


def _attr(tag_text, name):
    """Attribute value from an HTML/JSX tag. None when absent; "" when empty; "{expr}" for JSX."""
    pattern = rf"(?<![\w:-]){name}\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|\{{\s*[\"'`]([^\"'`]*)[\"'`]\s*\}}|(\{{[^}}]*\}})|([^\s>]+))"
    match = re.search(pattern, tag_text, re.I)
    if not match:
        return None
    return next(g for g in match.groups() if g is not None)


def lint_markup(path, root):
    path, root = Path(path), Path(root)
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8", errors="replace")
    findings = []

    def line_of(offset):
        return text.count("\n", 0, offset) + 1

    for match in IMG_RE.finditer(text):
        tag = match.group(0)
        src = _attr(tag, "src") or ""
        if "placeholders/" not in src:
            continue
        alt = _attr(tag, "alt")
        if alt is None or not alt.strip() or GENERIC_ALT_RE.fullmatch(alt.strip()):
            findings.append(Finding(
                "BLOCKING", rel, line_of(match.start()), "placeholder-alt",
                f"Placeholder {src} has alt={alt!r}.",
                "Describe the intended subject, e.g. alt=\"Hand-thrown ceramic mug, top-down on linen\" "
                "— it stays correct when the real photo replaces the file."))
        if _attr(tag, "width") is None or _attr(tag, "height") is None:
            findings.append(Finding(
                "ADVISORY", rel, line_of(match.start()), "placeholder-dimensions",
                f"Placeholder {src} is missing width or height.",
                "Set both to the slot's target size so the real image drops in without layout shift."))

    for match in META_RE.finditer(text):
        tag = match.group(0)
        key = (_attr(tag, "property") or _attr(tag, "name") or "").lower()
        content = (_attr(tag, "content") or "").split("?")[0]
        if key in ("og:image", "twitter:image") and content.lower().endswith(".svg"):
            findings.append(Finding(
                "BLOCKING", rel, line_of(match.start()), "og-image-svg",
                f"{key} points at an SVG; link-preview crawlers do not render SVG.",
                "Point it at the PNG export (og-card.png, 1200x630) with og:image:width/height/alt."))
    return findings


# --- project ----------------------------------------------------------------


def _scan(root, design=None, kept_incumbent=False):
    root = Path(root)
    palette = load_palette(Path(design) if design else root / "DESIGN.md")
    findings, svg_count, markup_count = [], 0, 0
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(files):
            path = Path(directory) / name
            suffix = path.suffix.lower()
            if suffix == ".svg":
                svg_count += 1
                findings += lint_svg(path, root, palette, kept_incumbent)
            elif suffix in MARKUP_EXT:
                markup_count += 1
                findings += lint_markup(path, root)
    findings.sort(key=lambda f: (f.severity != "BLOCKING", f.path, f.line))
    return findings, svg_count, markup_count


def lint_project(root, design=None, kept_incumbent=False):
    return _scan(root, design, kept_incumbent)[0]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check generated SVG assets (svg-assets.md § 6).")
    parser.add_argument("root", help="project root")
    parser.add_argument("--design", help="DESIGN.md path (default: <root>/DESIGN.md)")
    parser.add_argument("--kept-incumbent", action="store_true",
                        help="logo is a kept incumbent: skip the favicon pixel-grid check")
    args = parser.parse_args(argv)
    if not Path(args.root).is_dir():
        print(f"Error: {args.root} is not a directory", file=sys.stderr)
        return 2
    findings, svg_count, markup_count = _scan(args.root, args.design, args.kept_incumbent)
    for finding in findings:
        print(finding.format())
        print()
    blocking = sum(f.severity == "BLOCKING" for f in findings)
    print(f"svg_lint: {blocking} BLOCKING, {len(findings) - blocking} ADVISORY "
          f"across {svg_count} SVG and {markup_count} markup files.")
    print("Static checks only. Look at the rendered PNGs and the page before calling it done.")
    return 1 if blocking else 0


if __name__ == "__main__":
    sys.exit(main())
