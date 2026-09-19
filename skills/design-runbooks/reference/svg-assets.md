# SVG assets — the brand kit and picture surfaces

> **Extraction note.** Original to this skill, except two marked blocks — § 1's logo-wall bullet
> and § 2's *Placeholder strategy* — which are **verbatim** from
> [nutlope/hallmark](https://github.com/nutlope/hallmark) v1.1.0 at commit
> `13ac0ec7e148655948100b6396439e481361d690` — MIT, (c) 2026 Hallmark contributors
> (`licenses/hallmark-MIT.txt`). File: `skills/hallmark/references/assets.md`. Each verbatim
> block opens with its own *Extraction note*; anything else in a blockquote is commentary.
> Full record: `MANIFEST.md` § 11b.

What a CREATE or REVAMP run draws when the user has not supplied it: the **brand kit** — a mark
and the pieces derived from it — and the **picture surfaces** a layout needs. Two kinds of SVG and
nothing else: **geometry** a session can specify exactly, and **placeholders** that hold a slot
open for a real asset.

| Called from | Section |
|---|---|
| CREATE step 1 · REVAMP step 1 — the asset check | § 0 |
| CREATE step 2c · REVAMP step 2 — the image-led gate | § 1 |
| CREATE step 3b · REVAMP step 2 — the mark | § 3 |
| CREATE step 4 · REVAMP step 3 — picture surfaces | §§ 1–2 |
| CREATE step 4b · REVAMP step 4 — the kit | § 4 |
| VERIFY — Runbook 3 | § 6 |

---

## § 0 · When it runs

**Only for gaps.** A logo, photograph, screenshot or illustration the user supplied is never
replaced, regenerated, redrawn, recoloured or "cleaned up". A supplied asset is evidence
(PRODUCT.md § Evidence on Hand), and evidence is not a design variable.

**The asset check** is mechanical — at intake (CREATE step 1) or inventory (REVAMP step 1). It
adds no question; it reads what the repository and the brief already answer:

- Is there a logo or mark? A file, an inline SVG in the nav, a favicon that is not a framework
  default.
- Is there photography, or are there product screenshots, for the surfaces being built?
- Absences are written to PRODUCT.md § Evidence on Hand **as absences** — *"No product
  photography. No logo; the name is set as live type."* — so later work does not fabricate them.

**First ask whether the surface needs imagery at all.** A fold carried by type is a finished
design, not a gap. The slot rule below resolves the rest.

---

## § 1 · The slot rule

Every image slot resolves to exactly one of three, before anything is drawn:

| Resolution | When the subject is | Drawn as |
|---|---|---|
| **Geometry** | something a session can specify exactly — the product's own mechanism, data, notation, structure, sequence or map; the mark | authored SVG from DESIGN.md tokens |
| **Placeholder** | a real-world thing only the user can supply — people, a place, a physical product, a real screenshot of the product, a team, a venue | a labelled slot (§ 2), replaced later |
| **None** | neither — the slot exists because a template had one | nothing. Drop the slot and let the type carry it |

**The test for geometry is exactness, not style.** The piano roll a music-coding tool produces,
the routing graph of a logistics API, the floor plan of a co-working space — the product defines
each shape, so a session can draw it correctly. A barista, a storefront and a dashboard
screenshot are not like that; drawing them is fabrication, however clean the lines.

Geometry is still bound by the ban list and the gates:

- **Real illustration or none** (`impeccable-anti-patterns.md`) — no sketch scenes, no
  `feTurbulence` grain, no figure-bearing or perspectived drawing, even in line-art style.
- **Gate 47** — no re-drawn browser, phone, terminal or IDE chrome. A screenshot slot is a
  placeholder, never a drawing of the UI.
- **Gate 31** — hand-built SVG before Lottie.
- **Gate 30** — one icon library. Geometry is not a back door for a second icon set.
- **Gate 46** — geometry that shows data shows the product's real behaviour, or demonstration
  data labelled synthetic. Never a metric dressed as a chart.

**Customer logos are never a placeholder.** A logo wall of stand-ins is fabricated social proof.

> **Extraction note** — verbatim, hallmark `assets.md` § Brand / company logos › *Avoid*, one
> bullet.

- **Placeholder customer logos from template kits** ("ACME", "Initech", "Hooli"). Use real customer logos, or skip the wall entirely — fake social proof is worse than no social proof.

### The image-led selection gate

Four macrostructures are made of imagery: **05 Workbench** and **16 Feature Stack**
(screenshots), **08 Photographic**, and **18 Portfolio Grid** (the work itself). On placeholders
they are a page of grey boxes. The gate has the same shape as C1 for Stat-Led
(`merged-rules.md` § 3):

- **Selection.** Available only when the user has supplied the imagery or confirms it is coming.
  Absent that, pick another shape — CREATE step 2c, REVAMP step 2.
- **Execution.** Selected on a promise, every slot is a placeholder per § 2, and PRODUCT.md
  § Evidence on Hand records what is owed.

08 Photographic already says *"Avoid without real photography."* The gate turns that sentence
into a selection rule.

---

## § 2 · Placeholders

> **Extraction note** — verbatim, hallmark `assets.md` § Placeholder strategy, whole (its heading
> dropped). How its tiers map here: tier 1, the hallmark imagery kit (`imagery-kit.md`), was not
> extracted; tier 2 is this skill's **geometry** (§ 1); tiers 3 and 4 are remote hosts and do not
> apply; tier 5 is the placeholder, drawn as *In this skill* below describes. Under
> *Swappability*, the HTML `TODO` comment is superseded by `merged-rules.md` § C6, and the
> "single constant" is the `assets/placeholders/` directory — a local file per slot needs no base
> URL. The rest binds as written.

When imagery is needed *and* the user hasn't supplied real assets, pick from this canon — in order. Skipping tiers is the slop move.

| # | Source | When |
| --- | --- | --- |
| 1 | **Hallmark imagery kit** ([`imagery-kit.md`](imagery-kit.md)) | Brief allows non-photographic imagery: SaaS landings, manifestos, agency / studio splash, type-led portfolio, editorial-led marketing. **Always preferred** when the kit's register fits. |
| 2 | **Hand-built SVG composition** (Tier B from custom-craft.md) | Editorial-typographic brief where "imagery" can be a stamp / wordmark / colour-blocked composition. Use when the kit doesn't carry the register. |
| 3 | **Picsum** — `https://picsum.photos/seed/<seed>/<w>/<h>` | Generic photo slot, keyword anchoring not critical. Use a deterministic seed (brand-name + slot-name) so the same render produces the same image. |
| 4 | **Unsplash Source** — `https://source.unsplash.com/<w>x<h>/?<keywords>` | Keyword-anchored photo slot — food, travel, portrait, real product. Pass 1–2 specific keywords, never zero. |
| 5 | **Local `public/placeholder-<type>.{jpg,svg}`** | Self-contained projects with no third-party deps. Single neutral grey-block SVG checked into the repo. |

**Swappability — non-negotiable:**

- Every placeholder image carries an HTML comment immediately above it: `<!-- TODO: Replace with real <thing>, target size: <WxH> -->`.
- All placeholder URLs reference a single constant — a `--placeholder-base` CSS variable or `PLACEHOLDER_BASE` config constant. User edits one place to swap the entire site.
- Alt text describes the **intended** subject ("Hand-thrown ceramic mug, top-down on linen") not the placeholder ("Picsum image"). When the user swaps in the real photo, alt is already correct.

**Remote asset safety:**

- Treat third-party image, logo, video, icon, and font URLs as prototype defaults, not production defaults. Before shipping production code, prefer vendored or self-hosted assets unless the user explicitly wants third-party hosting.
- Do not add a third-party script, tracking pixel, widget, or API dependency as an asset shortcut. Asset sources provide files; they do not get to execute code in the page.
- When remote assets remain in production, state the privacy and availability tradeoff in the handoff: visitors will request those third-party hosts, and the page depends on their uptime and integrity.
- For user-supplied brand or customer logos, prefer official asset pages or checked-in files. Do not hotlink a logo from an unrelated site.

**Anti-patterns:**

- Never inline base64 placeholder images (bloats CSS).
- Never call random Unsplash without keywords (returns un-curated stock-photo-ish results).
- Never use kittens / lorempixel / "tiger.jpg" / cute-default services. The placeholder must read as an obvious slot, not as content.
- Never ship a kit image where the brief actually calls for a real product photo (e.g. abstract bottle for an actual coffee-shop hero). The kit is for atmosphere; photos are for subject.

### In this skill

- **File.** `assets/placeholders/<slot>.svg`, one per slot. `<slot>` names where it sits —
  `hero`, `about-team`, `product-01`. The directory is the single swap point: replace the file at
  the same path, or point `src` at the real asset.
- **Drawing.** `viewBox` at the slot's aspect ratio — `0 0 4 5`, `0 0 16 9`. One full-bleed rect
  in a tinted neutral from DESIGN.md (a sunk or raised surface, never the accent). One centred
  `<text>` label: `<Kind> · <ratio>` — `Photo · 4:5`, `Screenshot · 16:10`, `Team photo · 3:2`.
  Its `font-family` is the label face's **generic fallback** (`ui-monospace, monospace` or
  `system-ui, sans-serif`): an SVG loaded through `<img>` cannot load web fonts. `role="img"` and
  a `<title>` repeating the label. Nothing else — no crop marks, icon, gradient or brief.
- **Markup.** `<img src="assets/placeholders/hero.svg" width="1200" height="1500" alt="…">` —
  `width` and `height` at the target size, `alt` describing the subject the real image will show.
  Treatment — `object-fit`, radius, border — comes from DESIGN.md exactly as it would for the real
  image, so the swap changes the picture and nothing else.
- **The shot brief stays off the page.** Subject, crop, ratio, target size and path for every
  slot go in the final report and, on a revamp, in REVAMP.md `## Notes`. Not in the SVG, not in
  an HTML comment, not in a `data-*` attribute — art direction is direction rationale
  (SKILL.md § Always true).
- **What is owed is durable.** Each slot's subject is listed in PRODUCT.md § Evidence on Hand
  when a PRODUCT.md exists — *"Owed: hero photograph, 4:5; three product shots, 1:1."*

A placeholder never pretends. It is obviously a slot, it carries no geometry that could pass for
the picture, and it never becomes a remote stock photo "for now".

---

## § 3 · The mark

### When

| Runbook | Concepts run when |
|---|---|
| 2 · CREATE | no logo was supplied, and no incumbent DESIGN.md records one |
| 1 · REVAMP | logo status is `released`, or `none` and the user opted in at step 0 |
| 4 · REVISE | the user asks for a different mark, and the mark is not a kept incumbent |

A kept incumbent never enters this section; its kit is derived under § 4.

**After DESIGN.md, before the build.** The mark draws from the palette and sits beside the
wordmark, so it needs both settled. It does not need the pages.

### Concepts — two or three, each from a different fact

Each concept starts from **one named fact in PRODUCT.md** — the mechanism (§ Positioning), a
domain object or notation (§ Operating Context), the name itself — and draws that fact as
geometry. Different facts, not three styles of one idea. The model is the music-as-code mark:
three notes as the piano roll draws them, the playhead standing in the gap — the product's own
output, recognisable to anyone who has used it.

**Construction:**

- **32-unit grid.** `viewBox="0 0 32 32"`, integer coordinates, so the favicon lands on whole
  pixels.
- **At most two fills, both DESIGN.md colours.** It must also survive in **one colour** — check
  it as `currentColor` before offering it.
- **Legible at 16px.** Detail that disappears at 16px is not detail; take it out.
- **No text.** The wordmark is live type in the page, and outlined only in the lockup.
- **Flat.** No gradient, filter, shadow or blend mode; no hairline stroke that thins to nothing
  at 16px.
- **Not the category.** No lightbulb, rocket, globe, gear, infinity loop, circuit nodes, swoosh,
  speech bubble, shield-with-check or abstract connected dots. The category's symbol says what
  every competitor says.
- **Not the default.** An initial in a rounded square is what every generator emits. Available
  only when the brief asks for a monogram.
- **No re-drawn chrome** (gate 47), and nothing *real illustration or none* refuses.
- **A pinned brief wins.** A symbol, shape or reference the user named becomes concept A; the
  others vary around it.

### Show them

Write `mark-concepts.html` at the project root: each concept at 16px, 32px and nav size, in
colour and in one colour, on the page background and on the inverse surface. Labels are `A`,
`B`, `C` and nothing else. The fact each one draws on, and why, goes **in the chat message**,
never in the file — rationale never reaches the browser (SKILL.md § Always true), and a file at
a project root can be served.

Ask once, and wait:

> Three marks in `mark-concepts.html`. **A** draws [fact], **B** draws [fact], **C** draws
> [fact]. Pick one, or say none and the name stays type-only.

**Silence is no mark.** The wordmark stays live text, and § 4 builds only the og-card. An identity
nobody chose is worse than none.

`mark-concepts.html` is a **run artifact** with REVAMP.md's lifetime (`contract.md` § 3): report
it safe to delete at the end, and never delete it yourself.

### Adoption — the write-back

On a pick:

1. **DESIGN.md § Components › Mark** — what it draws, its construction (grid, fills as
   `{colors.*}` refs), sizes (nav size, the size below which the favicon drawing takes over),
   placement beside the wordmark, and the kit's file list. The frontmatter is untouched unless a
   colour had to be added — and then deliberately, said out loud.
2. **PRODUCT.md § Brand Commitments**, when a PRODUCT.md exists (a revamp may have none) — one
   line: *"The mark — [one-line description] — was
   designed on [date] and adopted by the user. Its files live in `assets/`."* This is one of the
   two PRODUCT.md writes Runbooks 1 and 2 may make after intake (`contract.md` § 1).

---

## § 4 · The kit

Derived **after the build** — the og-card depicts the built hero, so it cannot come first.
CREATE step 4b; REVAMP step 4, after the last batch.

| Piece | File | Tier | Built when |
|---|---|---|---|
| Mark | `assets/mark.svg` | core | a mark exists |
| Favicon | `assets/favicon.svg` | core | a mark exists |
| Touch icon | `assets/apple-touch-icon.png`, 180×180 | core | a mark exists and a rasterizer is available |
| Link preview | `assets/og-card.svg` → `assets/og-card.png`, 1200×630 | core | always |
| App icon | `assets/app-icon.svg` (maskable) → `app-icon-192.png`, `app-icon-512.png`, `manifest.webmanifest` | extended | the product is installable — a web app, a PWA, an existing manifest |
| Lockup | `assets/lockup.svg` | extended | a mark exists and type outlining is available (§ 5) |

Use the project's static asset directory when it has one (`public/`, `static/`, `src/assets/`);
`assets/` is the default for a plain site. **Keep the file names** — § 6 classifies by them.

### Per piece

- **mark.svg** — the adopted drawing. Fills through CSS custom properties with literal fallbacks,
  `fill: var(--primary, #E6443C)`, so an inline copy follows the tokens and the standalone file
  still renders. `role="img"` and a `<title>` with the product name.
- **favicon.svg** — standalone, literal colours, redrawn on whole pixels at 32 units; the nav
  drawing blurs below ~20px. It may carry its own background square when the mark lacks contrast
  on light or dark browser tabs, or a `@media (prefers-color-scheme: dark)` rule inside the SVG.
- **app-icon.svg** — a full-bleed background from DESIGN.md, and the mark inside the **central
  circle of radius 40%**; platforms crop maskable icons to shapes within it.
  `apple-touch-icon.png` is its 180px export.
- **og-card.svg** — 1200×630, depicting the built hero: the real headline, the product's
  geometry, the mark if there is one. **Copy only from the page** — no invented tagline, metric
  or quote (gate 46). Type outlined (§ 5), or rasterized by a renderer that loads the real font.
  A `<title>` and `<desc>` say what it shows. It ships as the PNG; crawlers do not render SVG.
- **lockup.svg** — mark plus wordmark with the type **outlined**, for use off the site: READMEs,
  decks, social. Never used in the page, where the wordmark is live text.

### No mark

When silence left the product without a mark, build the og-card only, with the name set in the
display face. Do not invent a favicon or app icon from an initial — report them as gaps.

### A kept incumbent (REVAMP)

The preservation contract keeps the logo, so its kit is **derived, never redrawn**:

- Reuse the incumbent's paths **verbatim**. Change only the frame — `viewBox`, padding, a
  background square, the maskable inset.
- Colours are the incumbent's. They are brand colours under DEFAULT KEEP; if DESIGN.md does not
  carry them, that is drift to report, not a reason to recolour.
- Illegible at 16px → an ADVISORY finding. Simplifying it would be redrawing it.
- **Raster-only incumbent** — a PNG or JPG, no vector → the SVG kit is skipped and reported.
  Never trace it; a traced logo is a redrawn logo with worse curves.
- Lint with `--kept-incumbent` (§ 6).

### Wiring

In `<head>`, once, in the shared layout. The `manifest` link belongs to the extended tier only.

```html
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#13100F">
<meta property="og:image" content="https://example.com/assets/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="The hero: a short program beside the piano roll it plays.">
<meta name="twitter:card" content="summary_large_image">
```

`og:image` wants an absolute URL in production; a relative path is acceptable only until the
deploy URL is known, and the report says so. `theme-color` matches the page background token
(`guidelines-and-review.md` § Dark Mode & Theming), and the manifest's `theme_color` and
`background_color` come from the same tokens.

In the nav the mark is **inline**, before a live-text wordmark, and hidden from assistive tech —
the wordmark already names the link. Fills come from the stylesheet's tokens, not literals.

```html
<a class="nav__brand" href="/">
  <svg class="nav__mark" viewBox="0 0 32 32" width="22" height="22" aria-hidden="true" focusable="false">…</svg>
  Product Name
</a>
```

---

## § 5 · Tooling

Use whatever the machine has, first found in each list.

**Rasterize** — the PNG exports:

| Tool | Command |
|---|---|
| resvg | `resvg in.svg out.png -w 512 -h 512` |
| rsvg-convert | `rsvg-convert -w 512 -h 512 in.svg -o out.png` |
| Inkscape | `inkscape in.svg --export-type=png -w 512 -h 512 -o out.png` |
| headless Chromium | `chromium --headless --disable-gpu --hide-scrollbars --window-size=1200,630 --screenshot=out.png file:///abs/path/og-card.svg` |

Only Chromium loads web fonts; resvg, rsvg-convert and Inkscape see system fonts. It is the tool
for an og-card whose type is not outlined.

**Outline type** — the lockup, and the og-card when it can be:

| Tool | Command |
|---|---|
| Inkscape | `inkscape in.svg --export-text-to-path --export-plain-svg -o out.svg` |
| fontTools | `pip install fonttools` (add `brotli` for `.woff2`), then the snippet below with the display face's font file |

```python
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

def outline(text, font_path, size, x=0.0, y=0.0):
    """SVG path data for `text` set at `size` px, baseline at (x, y)."""
    font = TTFont(font_path)
    glyphs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    parts = []
    for char in text:
        name = cmap.get(ord(char), ".notdef")
        pen = SVGPathPen(glyphs, ntos=lambda n: f"{n:.2f}".rstrip("0").rstrip("."))
        glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, y)))
        parts.append(pen.getCommands())
        x += glyphs[name].width * scale
    return " ".join(parts)
```

The snippet applies no kerning and no ligatures. Compare it with the live wordmark; for a long
name, prefer Inkscape, which shapes the text.

**The gap rule.** No rasterizer → the PNGs are skipped and named in the final report with the
install command (`librsvg` provides `rsvg-convert` on every major package manager); the SVG kit
still ships. No outliner → the lockup is skipped; the og-card goes through Chromium if present,
and is skipped otherwise. Never hand-trace glyphs, never ship a lockup with `<text>`, and never
fetch a font from an unofficial mirror to get one.

---

## § 6 · Checking

VERIFY runs it. So may Runbook 3 routed directly — it only reads.

```bash
python3 scripts/svg_lint.py <project-root>                   # DESIGN.md read from the root
python3 scripts/svg_lint.py <project-root> --kept-incumbent  # REVAMP with a kept logo
```

It walks every `*.svg` (skipping `node_modules`, `dist`, `build`, `vendor` and dot-directories)
and the markup (`.html .htm .astro .vue .svelte .jsx .tsx`); classifies each SVG by file name —
`mark`, `favicon*`, `app-icon*`, `lockup*`, `og-card*`, anything under `placeholders/`; and
prints findings in Runbook 3's format. Exit 1 on any BLOCKING.

The **kit** is `mark`, `favicon`, `app-icon`, `lockup` and `og-card`.

| Rule | Check | Applies to | Severity |
|---|---|---|---|
| `svg-parse` | not well-formed XML | all | BLOCKING |
| `svg-script` · `svg-event-handler` · `svg-foreign-object` · `svg-external-href` | `<script>`, an `on*=` attribute, `<foreignObject>`, an `href` to another host | all | BLOCKING |
| `svg-viewbox` | no `viewBox` on the root | all | BLOCKING |
| `svg-embedded-raster` | `<image>` with a `data:` or raster `href` | kit | BLOCKING |
| `svg-text-in-mark` | `<text>` | mark, lockup | BLOCKING |
| `svg-off-palette` | a colour literal not in DESIGN.md `colors` — hex, `rgb()` and `oklch()` compared in sRGB within 3/255 per channel; CSS-variable fallbacks included | kit, when DESIGN.md exists | BLOCKING |
| `placeholder-alt` | placeholder `<img>` with no `alt`, an empty one, or a generic one (`placeholder`, `image`, `photo` …) | markup | BLOCKING |
| `og-image-svg` | `og:image` or `twitter:image` pointing at an `.svg` | markup | BLOCKING |
| `placeholder-dimensions` | placeholder `<img>` missing `width` or `height` | markup | ADVISORY |
| `placeholder-label` | placeholder file with no `<text>` label | placeholders | ADVISORY |
| `og-card-text` | `<text>` in the og-card | og-card | ADVISORY |
| `svg-sketch` | `feTurbulence`, or a `sketch` / `doodle` class | all | ADVISORY |
| `svg-title` | no `<title>` child | kit | ADVISORY |
| `favicon-pixel-grid` | a non-integer coordinate (off with `--kept-incumbent`) | favicon | ADVISORY |
| `og-card-size` | `viewBox` other than `0 0 1200 630` | og-card | ADVISORY |
| `app-icon-safe-zone` | a `rect` or `circle` reaching outside the central circle of radius 40% (the full-bleed background excepted) | app-icon | ADVISORY |
| `svg-byte-budget` | over 2 KB (mark, favicon), 4 KB (app-icon), 16 KB (lockup), 120 KB (og-card) | kit | ADVISORY |

The BLOCKING rows are the audit contract's categories — accessibility, design-system drift — plus
one extension, **a broken or unsafe asset**, recorded in `merged-rules.md` § 2.

**The limit.** It reads source; it does not render. It cannot see a mark that is illegible at
16px, an og-card that crops badly in a feed, a shape transformed out of the safe zone, or a
placeholder whose neutral vanishes against the section behind it. Open the PNGs and look at the
page before calling the kit done.
