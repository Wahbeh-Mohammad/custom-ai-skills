#!/usr/bin/env python3
"""Tests for svg_lint.py. Run: python3 -m unittest scripts/test_svg_lint.py -v"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import svg_lint  # noqa: E402

DESIGN = """---
name: Test
colors:
  primary: "#E6443C"
  lane-note: "#FAD4CE"
  paper: "oklch(62.8% 0.2577 29.23)"
typography:
  display:
    fontFamily: "Bodoni Moda, serif"
components:
  button-primary:
    backgroundColor: "#123456"
---

# Design
"""

CLEAN_MARK = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img">
  <title>Test</title>
  <rect x="0" y="20" width="8" height="5" fill="#FAD4CE"/>
  <rect x="20" y="2" width="2" height="27" fill="#E6443C"/>
</svg>
"""


def svg(body, view_box='viewBox="0 0 32 32"', title="<title>T</title>"):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" {view_box} role="img">'
        f"{title}{body}</svg>"
    )


class Project:
    """A throwaway project directory."""

    def __init__(self, design=True):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        if design:
            (self.root / "DESIGN.md").write_text(DESIGN)

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def lint(self, **kw):
        return svg_lint.lint_project(self.root, **kw)

    def close(self):
        self._tmp.cleanup()


def rules(findings):
    return {(f.severity, f.rule) for f in findings}


class ClassifyTest(unittest.TestCase):
    def test_kinds(self):
        cases = {
            "assets/mark.svg": "mark",
            "favicon.svg": "favicon",
            "app-icon.svg": "app-icon",
            "lockup.svg": "lockup",
            "og-card.svg": "og-card",
            "assets/placeholders/hero.svg": "placeholder",
            "logo.svg": "other",
        }
        for rel, kind in cases.items():
            self.assertEqual(svg_lint.classify(Path(rel)), kind, rel)


class ColorTest(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(svg_lint.parse_color("#fad4ce"), (250, 212, 206))
        self.assertEqual(svg_lint.parse_color("#abc"), (170, 187, 204))

    def test_rgb(self):
        self.assertEqual(svg_lint.parse_color("rgb(10 20 30)"), (10, 20, 30))
        self.assertEqual(svg_lint.parse_color("rgb(10, 20, 30)"), (10, 20, 30))

    def test_oklch_red(self):
        r, g, b = svg_lint.parse_color("oklch(62.8% 0.2577 29.23)")
        self.assertLessEqual(max(abs(r - 255), abs(g), abs(b)), 3)

    def test_keywords(self):
        self.assertIsNone(svg_lint.parse_color("none"))
        self.assertIsNone(svg_lint.parse_color("currentColor"))

    def test_palette_reads_colors_block_only(self):
        p = Project()
        try:
            palette = svg_lint.load_palette(p.root / "DESIGN.md")
            self.assertEqual(len(palette), 3)
            self.assertIn((230, 68, 60), palette)
            self.assertNotIn((0x12, 0x34, 0x56), palette)
        finally:
            p.close()


class SvgTest(unittest.TestCase):
    def setUp(self):
        self.p = Project()

    def tearDown(self):
        self.p.close()

    def test_clean_mark(self):
        self.p.write("assets/mark.svg", CLEAN_MARK)
        self.assertEqual(self.p.lint(), [])

    def test_script(self):
        self.p.write("assets/mark.svg", svg('<script>alert(1)</script>'))
        self.assertIn(("BLOCKING", "svg-script"), rules(self.p.lint()))

    def test_event_handler(self):
        self.p.write("x.svg", svg('<rect onload="x()" width="1" height="1"/>'))
        self.assertIn(("BLOCKING", "svg-event-handler"), rules(self.p.lint()))

    def test_external_href(self):
        self.p.write("x.svg", svg('<use href="https://evil.example/a.svg#x"/>'))
        self.assertIn(("BLOCKING", "svg-external-href"), rules(self.p.lint()))

    def test_foreign_object(self):
        self.p.write("x.svg", svg("<foreignObject/>"))
        self.assertIn(("BLOCKING", "svg-foreign-object"), rules(self.p.lint()))

    def test_missing_viewbox(self):
        self.p.write("x.svg", svg("", view_box='width="32" height="32"'))
        self.assertIn(("BLOCKING", "svg-viewbox"), rules(self.p.lint()))

    def test_parse_error(self):
        self.p.write("x.svg", "<svg><rect></svg>")
        self.assertIn(("BLOCKING", "svg-parse"), rules(self.p.lint()))

    def test_text_in_lockup(self):
        self.p.write("assets/lockup.svg", svg('<text fill="#E6443C">Name</text>'))
        self.assertIn(("BLOCKING", "svg-text-in-mark"), rules(self.p.lint()))

    def test_text_in_og_card(self):
        self.p.write(
            "assets/og-card.svg",
            svg('<text fill="#E6443C">Name</text>', view_box='viewBox="0 0 1200 630"'),
        )
        found = rules(self.p.lint())
        self.assertIn(("ADVISORY", "og-card-text"), found)
        self.assertNotIn(("BLOCKING", "svg-text-in-mark"), found)

    def test_off_palette(self):
        self.p.write("assets/mark.svg", svg('<rect width="4" height="4" fill="#00FF00"/>'))
        self.assertIn(("BLOCKING", "svg-off-palette"), rules(self.p.lint()))

    def test_off_palette_css_fallback(self):
        body = '<style>.a { fill: var(--x, #00FF00); }</style><rect class="a" width="4" height="4"/>'
        self.p.write("assets/mark.svg", svg(body))
        self.assertIn(("BLOCKING", "svg-off-palette"), rules(self.p.lint()))

    def test_oklch_token_matches_hex(self):
        self.p.write("assets/mark.svg", svg('<rect width="4" height="4" fill="#FF0000"/>'))
        self.assertNotIn(("BLOCKING", "svg-off-palette"), rules(self.p.lint()))

    def test_url_refs_ignored(self):
        body = '<defs><linearGradient id="abc"/></defs><rect width="4" height="4" fill="url(#abc)"/>'
        self.p.write("assets/mark.svg", svg(body))
        self.assertNotIn(("BLOCKING", "svg-off-palette"), rules(self.p.lint()))

    def test_no_design_skips_palette(self):
        q = Project(design=False)
        try:
            q.write("assets/mark.svg", svg('<rect width="4" height="4" fill="#00FF00"/>'))
            self.assertNotIn(("BLOCKING", "svg-off-palette"), rules(q.lint()))
        finally:
            q.close()

    def test_embedded_raster(self):
        body = '<image href="data:image/png;base64,AAAA" width="32" height="32"/>'
        self.p.write("assets/favicon.svg", svg(body))
        self.assertIn(("BLOCKING", "svg-embedded-raster"), rules(self.p.lint()))

    def test_favicon_pixel_grid(self):
        self.p.write("assets/favicon.svg", svg('<rect x="2.5" y="2" width="6" height="4" fill="#E6443C"/>'))
        self.assertIn(("ADVISORY", "favicon-pixel-grid"), rules(self.p.lint()))
        self.assertNotIn(
            ("ADVISORY", "favicon-pixel-grid"), rules(self.p.lint(kept_incumbent=True))
        )

    def test_favicon_path_pixel_grid(self):
        self.p.write("assets/favicon.svg", svg('<path d="M1 1H3.25V4Z" fill="#E6443C"/>'))
        self.assertIn(("ADVISORY", "favicon-pixel-grid"), rules(self.p.lint()))

    def test_app_icon_safe_zone(self):
        body = (
            '<rect width="512" height="512" fill="#E6443C"/>'
            '<rect x="10" y="10" width="80" height="50" fill="#FAD4CE"/>'
        )
        self.p.write("assets/app-icon.svg", svg(body, view_box='viewBox="0 0 512 512"'))
        self.assertIn(("ADVISORY", "app-icon-safe-zone"), rules(self.p.lint()))

    def test_app_icon_inside_safe_zone(self):
        body = (
            '<rect width="512" height="512" fill="#E6443C"/>'
            '<rect x="196" y="221" width="80" height="50" fill="#FAD4CE"/>'
        )
        self.p.write("assets/app-icon.svg", svg(body, view_box='viewBox="0 0 512 512"'))
        self.assertNotIn(("ADVISORY", "app-icon-safe-zone"), rules(self.p.lint()))

    def test_placeholder_label(self):
        self.p.write("assets/placeholders/hero.svg", svg('<rect width="4" height="5"/>'))
        self.assertIn(("ADVISORY", "placeholder-label"), rules(self.p.lint()))

    def test_placeholder_not_palette_checked(self):
        self.p.write(
            "assets/placeholders/hero.svg",
            svg('<rect width="4" height="5" fill="#00FF00"/><text>Photo · 4:5</text>'),
        )
        self.assertEqual(self.p.lint(), [])

    def test_sketch(self):
        self.p.write("x.svg", svg('<filter id="f"><feTurbulence/></filter>'))
        self.assertIn(("ADVISORY", "svg-sketch"), rules(self.p.lint()))

    def test_sketch_class(self):
        self.p.write("x.svg", svg('<path class="loose-sketch" d="M0 0L1 1"/>'))
        self.assertIn(("ADVISORY", "svg-sketch"), rules(self.p.lint()))

    def test_missing_title(self):
        self.p.write("assets/mark.svg", svg('<rect width="4" height="4" fill="#E6443C"/>', title=""))
        self.assertIn(("ADVISORY", "svg-title"), rules(self.p.lint()))

    def test_byte_budget(self):
        body = '<rect width="4" height="4" fill="#E6443C"/>' * 80
        self.p.write("assets/mark.svg", svg(body))
        self.assertIn(("ADVISORY", "svg-byte-budget"), rules(self.p.lint()))

    def test_og_card_size(self):
        self.p.write("assets/og-card.svg", svg('<rect width="4" height="4" fill="#E6443C"/>'))
        self.assertIn(("ADVISORY", "og-card-size"), rules(self.p.lint()))

    def test_skips_node_modules(self):
        self.p.write("node_modules/pkg/x.svg", "<svg><rect></svg>")
        self.assertEqual(self.p.lint(), [])


class MarkupTest(unittest.TestCase):
    def setUp(self):
        self.p = Project()
        self.p.write(
            "assets/placeholders/hero.svg",
            svg('<rect width="4" height="5"/><text>Photo · 4:5</text>', view_box='viewBox="0 0 4 5"'),
        )

    def tearDown(self):
        self.p.close()

    def test_empty_alt(self):
        self.p.write("index.html", '<img src="assets/placeholders/hero.svg" alt="" width="400" height="500">')
        self.assertIn(("BLOCKING", "placeholder-alt"), rules(self.p.lint()))

    def test_generic_alt(self):
        self.p.write("index.html", '<img src="assets/placeholders/hero.svg" alt="Placeholder" width="400" height="500">')
        self.assertIn(("BLOCKING", "placeholder-alt"), rules(self.p.lint()))

    def test_missing_alt(self):
        self.p.write("index.html", '<img src="assets/placeholders/hero.svg" width="400" height="500">')
        self.assertIn(("BLOCKING", "placeholder-alt"), rules(self.p.lint()))

    def test_good_placeholder(self):
        self.p.write(
            "index.html",
            '<img src="assets/placeholders/hero.svg"\n  alt="Barista pouring a flat white, top-down" width="400" height="500">',
        )
        self.assertEqual(self.p.lint(), [])

    def test_missing_dimensions(self):
        self.p.write("index.html", '<img src="assets/placeholders/hero.svg" alt="Barista pouring" width="400">')
        found = rules(self.p.lint())
        self.assertIn(("ADVISORY", "placeholder-dimensions"), found)
        self.assertNotIn(("BLOCKING", "placeholder-alt"), found)

    def test_jsx_dimensions(self):
        self.p.write(
            "src/Hero.jsx",
            '<img src="/assets/placeholders/hero.svg" alt="Barista pouring" width={400} height={500} />',
        )
        self.assertEqual(self.p.lint(), [])

    def test_og_image_svg(self):
        self.p.write("index.html", '<meta property="og:image" content="assets/og-card.svg">')
        found = self.p.lint()
        self.assertIn(("BLOCKING", "og-image-svg"), rules(found))
        self.assertEqual(found[0].line, 1)

    def test_og_image_png(self):
        self.p.write("index.html", '<meta property="og:image" content="assets/og-card.png">')
        self.assertEqual(self.p.lint(), [])


class MainTest(unittest.TestCase):
    def test_exit_codes(self):
        p = Project()
        try:
            self.assertEqual(svg_lint.main([str(p.root)]), 0)  # no SVGs
            p.write("assets/mark.svg", CLEAN_MARK)
            self.assertEqual(svg_lint.main([str(p.root)]), 0)
            p.write("assets/lockup.svg", svg('<text fill="#E6443C">Name</text>'))
            self.assertEqual(svg_lint.main([str(p.root)]), 1)
        finally:
            p.close()

    def test_findings_sorted_blocking_first(self):
        p = Project()
        try:
            p.write("a.svg", svg('<filter><feTurbulence/></filter>'))
            p.write("b.svg", svg("<script/>"))
            found = p.lint()
            self.assertEqual(found[0].severity, "BLOCKING")
        finally:
            p.close()


if __name__ == "__main__":
    unittest.main()
