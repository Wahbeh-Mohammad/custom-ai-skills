# Slop gates — fingerprint + editorial subset

> **Extraction note.** Source: [nutlope/hallmark](https://github.com/nutlope/hallmark) v1.1.0 at
> commit `13ac0ec7e148655948100b6396439e481361d690` — MIT, (c) 2026 Hallmark
> contributors (`licenses/hallmark-MIT.txt`).
> File: `skills/hallmark/references/slop-test.md`.
> Gate text below is **verbatim**, in source order, under its source heading — no gate was
> reworded, renumbered or reordered.
>
> **Count.** Sources disagree: the hallmark README says "fifty-seven", `SKILL.md` says 58 in
> five places. The file is authoritative and carries **58** numbered entries — 1–57 plus an
> inserted **38a**. This extraction keeps **29** of them:
> 1–9, 19, 20–23, 29–32, 37, 38, 38a, 42–47, 54, 55.
>
> **Filter.** Kept: fingerprint gates (what makes a page read as LLM-generated) and editorial
> gates (honest copy, fabricated facts). Dropped: every contrast, focus-ring and accessibility
> gate — `guidelines-and-review.md` in this skill covers those — plus motion/microinteraction
> mechanics, responsive mechanics, performance, spacing/token discipline, and the study-mode
> gate. The appendix at the foot maps every dropped gate to where it went.
>
> Genre notes on kept gates are preserved inline. Cross-references to hallmark files not
> extracted here resolve upstream, not in this skill. Blockquotes like this one are extraction
> commentary, not source text.
>
> **Headings are the source's.** Gate 19 (placeholder names / startup clichés) is filed under
> *Microinteractions* upstream despite being a copy gate; that filing is left as-is. Gates 54
> and 55 are filed under *Mobile-responsiveness*; they are kept as fingerprint gates while the
> rest of that section is dropped.

---

## Pre-emit self-critique (six axes)

Run this **before** the gate list, not after. Score the planned output 1–5 on each axis. Anything **< 3 on any axis triggers a revision pass** before the gate sweep — don't bring known weakness into a fifty-eight-gate review.

Two passes is normal. Three is a sign the brief is wrong, not the design — re-read the brief.

| # | Axis | What you're scoring |
|---|---|---|
| **A** | **Philosophy** | Is there a clear *why* — a position the page is taking? Or is it just a layout? |
| **B** | **Hierarchy** | Can a reader tell, in 2 seconds, what's primary, secondary, tertiary? Or is everything the same weight? |
| **C** | **Execution** | Are the details (rule weight, accent footprint, text-wrap, focus rings, contrast) all in spec, or is there sloppiness even if the bones are right? |
| **D** | **Specificity** | Does this look like *this brief* — or does it look like a generic "page that could be anyone"? |
| **E** | **Restraint** | Have you removed everything that isn't earning its place? Decoration, redundancy, padding-for-padding's-sake? |
| **F** | **Variety** | Does this output share a structural fingerprint with a previous Hallmark output in the project? Score by structural distance, not visual distance — colour-swaps don't count as variety. |

Record the six scores in a one-line stamp comment at the top of the file: `/* Hallmark · pre-emit critique: P5 H4 E5 S4 R5 V5 */`. Future runs should be able to find this and avoid repeating the same weakness.

---

## Visual

1. Is the display font Inter, Roboto, Open Sans, Poppins, Lato, or a system default?

2. Is there a purple-to-blue (or cyan-to-magenta) gradient anywhere — **including a `background-clip: text` gradient headline**? *Genre note: atmospheric allows radial gradients on background only — never on text or pill buttons. No genre allows gradient text.*

3. Is there a 3-equal-column card grid with icon-above-heading tiles?

4. Is any card nested inside another card?

5. Is any card using a thick coloured left/right side-stripe border?

6. **Hero shape — centred-everything.** Is the hero `min-height: 100vh` with everything centred, OR are the eyebrow, title, lede, AND CTA all stacked on the same centred vertical axis? Auto-fail. Pick at most two centred elements and break alignment for the rest; the eyebrow or CTA should sit off-axis (margin-aligned, right-flush, numeral-anchored). *Genre note: atmospheric and playful allow a centred hero when the canvas itself is the design (Suno-style); editorial / atelier allow a centred-narrow hero, but even then the eyebrow or CTA sits off-axis.*

7. Is pure `#000` or pure `#fff` used as a base colour anywhere? *Genre note: modern-minimal allows pure `#fff` paper (the Stripe / ElevenLabs school).*

## Structural

8. Does the page reuse a structure it shouldn't — either the generic AI template (Hero → 3 features → CTA → footer), **or** the *same* structural fingerprint / macrostructure as a previous Hallmark output in this project? Read the file system: if a `.hallmark/log.json` entry or a CSS macrostructure stamp exists, this build's macrostructure must differ from the last.

9. Are sections separated only by equal whitespace, with no rule, no ornament, no colour shift — every section identical in rhythm?

## Microinteractions

19. Is there a placeholder name "Jane Doe / John Smith" or a startup cliché (Acme, Nexus, Seamless, Unleash)?

## Variety

20. Is the `/* Hallmark · macrostructure: <name> · ... */` stamp missing from the top of the CSS? (It must be present.)

21. Did I default to the **Specimen** macrostructure (numbered left-margin labels + huge serif + asymmetric spans + typographic-only CTA) when the brief did not explicitly call for editorial / foundry / specimen energy? (Specimen fall-through is banned.) *Genre note: atmospheric, modern-minimal, and playful never default to Specimen — only editorial does, and only when the brief signals it.*

## Implementation gates

22. Does any neutral / surface colour have `oklch(... 0 ...)` (zero chroma)? Pure greys read as flat. Tint every neutral toward the anchor hue — minimum 0.005 chroma. *Genre note: modern-minimal allows zero-chroma neutrals (the monochrome Stripe / ElevenLabs school).*

23. Does the accent colour cover more than ~5 % of any single viewport (count by area: solid fills, large headings in accent, full-bleed accent backgrounds)? If yes, retreat — accent is for emphasis, not for filling. *Genre note: atmospheric allows accent-tinted radial blooms covering up to ~20 % of the canvas, since the bloom is the design.*

## Hero enrichment gates

(When the page carries enrichment — see [`hero-enrichment.md`](hero-enrichment.md).)

29. If the page has an abstract background, is it more than one accent colour, more than ~5 % footprint, or animating mesh-gradient on the whole page? (Aurora blobs and mesh-on-everything fail this gate.) *Genre note: atmospheric allows up to two warm-toned radial blooms covering ~20–30 % of the canvas, fixed-attached, no animation.*

30. **Icon tells.** Does the page (a) mix two or more icon libraries (Material + Heroicons + Lucide on the same page), OR (b) use an emoji glyph (✨ 🚀 ⚡ 🔥 🎯 ✅) as a feature-card / value-prop / step / pricing-tier icon? Either is an AI-default tell. Pick one icon library (Lucide / Phosphor / Heroicons — see [assets.md](assets.md)), build a custom SVG, or drop the icon and lead with typography.

31. If the page has illustration, did I default to a Lottie library when a hand-built SVG or pure-CSS shape would have worked? (Lottie is last resort, not the default.)

## Diversification gates

(Cross-reference `.hallmark/log.json` when present.)

32. If I used the same archetype as a previous Hallmark output (per `.hallmark/log.json` or the latest macrostructure stamp), did I pick at least one different *variation knob*? Two Bento Grids with `tiles=6, spans=irregular, accent=corner-only` are the same Bento — the within-archetype knobs in [`component-cookbook.md`](component-cookbook.md) exist precisely to prevent that. State the knob deltas in the stamp.

## Typography discipline gates

(Three faces is the ceiling. See [`typography.md` § The 2+1 rule](typography.md).)

37. Does the page use **more than three** distinct `font-family` families? Count: `--font-display`, `--font-body`, and at most one outlier (`--font-outlier` for wordmark / hero stat / pull quote). A fourth family on the page — e.g. body + display + mono in code blocks + a separate display for the hero — is slop. Same family at different weights counts as one family. Mono counts as a family if used in any non-code context (captions, labels, numerals). If you find four, drop one back to the body or display face.

38. Is the **outlier face used in more than two slots** on the page? The outlier is a register, not a third surface — wordmark + hero stat is the canonical pair, or wordmark + masthead, or hero stat + pull quote. Three slots = the outlier is now a third body font; collapse it back to the body face.

38a. Is any **heading or display type italic** (`font-style: italic` on `h1`–`h6`, a `.*__title`, `.hero__title`, a wordmark, a stat figure, a footer statement, or an `<em>`/`<i>` inside a heading)? If yes, fail. Italic headers — above all the single italicised emphasis-word inside an upright headline — are a top AI tell. Headers are roman; emphasis comes from weight, accent colour, or a drawn underline. Italic is allowed *only* as body-copy emphasis inside running paragraphs. (Applies to every theme; Studio / Garden / Sport — historically italic-display — are reworked to roman.)

## Nav · footer · hero structural slop

Universal — apply to every genre. These gates catch the most-recognised AI fingerprints in nav, footer, and hero shape. They sit alongside the structural-fingerprint gate (gate 8): gate 8 catches the *page* fingerprint; 42–45 catch the *chrome* fingerprints that sit on top of it.

42. **Nav fingerprint.** Is the page's `<nav>` (or top-of-page `<header>` with role="banner") the AI default — wordmark-left + 4–5 inline text links centred-or-right + button-right at full viewport width + 1 px hairline border-bottom + white background? If yes, fail unless the brief explicitly justifies N1a (the page has only 2 destinations *and* the routing table for the genre allows N1a). Hallmark output should rotate among N1b, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13 from [`component-cookbook.md`](component-cookbook.md) § Navigation.

43. **Footer fingerprint.** Is the `<footer>` the AI default — 4 columns of links (Product / Company / Resources / Legal) + social-icon row + tiny copyright at the very bottom + 1 px hairline top-border + neutral grey background? If yes, fail unless the page is a genuine docs root or hub. Default to Ft1, Ft2, Ft4, Ft5, Ft6, Ft7, or Ft8 from [`component-cookbook.md`](component-cookbook.md) § Footers.

44. **Hero fit — sits into the page and fits the fold.** Two checks, both on the rendered hero: (a) Is `padding-block-end` ≥ 1.3× `padding-block-start`? Symmetric or top-heavy padding makes the hero float off the page; heavier bottom padding pulls it into the next section's rhythm. (b) On a standard laptop viewport — test at **1280×800** (13″), not just 1440×900 — can the hero's essential content (eyebrow, headline, lede, **and the primary CTA**, plus any hero visual's focal point) all be seen **without scrolling**? This is the other half of gate 6 (which caps the hero's *shape*): this caps its *content*. A hero can satisfy `min-height` and still overflow because the content is intrinsically too tall — usual culprits are an **oversized display clamp**, **loose line-height** (display at ~1.2 instead of 1.0–1.1), a **lede that runs 3+ lines**, or **bloated `padding-block`**. Right-size to the fold: pull the display `clamp()` max down until the headline fits 2–3 lines, set display line-height 1.0–1.1, hold the lede to ~2 lines (≤ ~60 ch), trim hero padding. **Don't overcorrect:** a hero that already fits passes untouched — this never means tiny type or stripped whitespace. Long-form / art-directed statements (a poem broadside, a scroll-poster) may legitimately run taller, but even then the **first screen must read as a complete, deliberate composition** — never a headline sliced in half by the fold.

45. **Decorative-without-purpose.** Does the hero contain a decorative element (cursor, scanline, gradient blob, abstract shape, ornament, badge, sticker) that has no semantic anchor in the content? Fail. Decoration must be motivated: a cursor inside a typed command (signals "you'd type next"), a numeral that names an issue / year / version / chapter, a gradient that responds to interaction (HP3 cursor-spotlight), a stamp that names an authorship or date. Random ornaments — a "42" in the corner with no edition meaning, a cursor floating beside a hero, a Pantone chip with no colour rationale — are slop.

The CSS stamp at Step 6 should record the result alongside contrast: `· nav: N# · footer: Ft# · slop: pass (42–45)`. If any of 42–45 fail, fix before shipping.

## Honest copy · no fabricated content

Universal — apply to every genre. The page must not invent facts about the user's product, team, or market.

46. **Invented metric.** Does the page contain any quantitative claim — "10× faster", "saves 5 hours per week", "trusted by 50,000+ teams", "99.9 % uptime", "+47 % conversion" — that the user did not supply, that has no source, and that the model fabricated to fill a stat-led layout, comparison row, or proof bar? If yes, fail. The fix is one of: replace the number with `—` and a labelled grey block, replace it with a question to the user ("metric to confirm"), or rebuild the section without the proof slot. Stat-led macrostructures are slop the moment their stats become decorative. **A stat is also never the hero's *sole* headline** — a lead figure carries the hero only alongside a worded headline; a giant number with no words as the dominant hero text is a bare-number tell, so pair it with a line that says what it means. *(See [anti-patterns.md § Invented metrics](anti-patterns.md).)*

## Re-drawn UI chrome

Universal. Hallmark must reuse the user's existing chrome (browser, OS, IDE) instead of redrawing it.

47. **Re-drawn chrome.** Did Hallmark hand-build a fake browser bar (URL pill + traffic-light dots), a fake phone frame (rounded rectangle + notch + speaker slit), a fake code-block frame (mock window-chrome around a `<pre>`), a fake terminal frame, or a fake IDE chrome (file tabs + activity bar + sidebar) using HTML/CSS or SVG? If yes, fail. Re-drawn chrome is one of the strongest "looks AI-generated" tells — the model invented a UI that already exists in the user's environment. The fix: use a `<picture>` or `<figure>` containing a real screenshot, or omit the chrome and let the content stand on its own. *(See [anti-patterns.md § Re-drawn UI chrome](anti-patterns.md).)*

## Mobile-responsiveness — the non-negotiables

Universal. Every emitted page must render flawlessly at 320 px, 375 px, 414 px, and 768 px CSS-pixel widths. Gates 34 (no horizontal scroll) and 49 (no two-line clickable text) already cover the headline cases; 50–57 below codify the patterns the marketing-site responsiveness pass uncovered. Eyeball each viewport before marking the output complete.

> Extraction commentary: this section's preamble cites gates 34, 49 and 50–57. Of those,
> only 54 and 55 are kept here — the rest are responsive mechanics, listed in the appendix.

54. **Section eyebrow / tag beside the heading (tag-left, header-right).** Does any section render an eyebrow / number / mono-cap label (`01 · THE TOUR`, `02 / FEATURES`, `Chapter Three`) in a column to the left of, or to the right of, the section heading on the same horizontal row? Auto-fail. The pattern reads as a templated editorial-SaaS tell within seconds. When an eyebrow is used at all (see [`anti-patterns.md § Eyebrow on every section`](anti-patterns.md) — default OFF), the heading goes **directly underneath it in the same column**, vertical stack only. Concretely: **any `<header>`, `<div>`, or `<section>` wrapper — regardless of class name (`.section__head`, `.workbench__head`, `.pricing__head`, `.catches__head`, `.foo__intro`, anything macrostructure- or section-specific)** — that contains both an eyebrow / label / number / kicker element AND a heading element MUST resolve to single-column layout: `display: block`, `display: flex; flex-direction: column`, or `display: grid; grid-template-columns: 1fr` (or `minmax(0, 1fr)`). Any multi-column grid on such a wrapper (`grid-template-columns: 1fr 2fr`, `minmax(0, 0.4fr) minmax(0, 1fr)`, `auto 1fr`, etc.) is banned. **The rule binds on the *content shape* — eyebrow + heading in the same wrapper — not on a specific class-name allowlist.** It supersedes the "Left-margin" axis in [`structure.md`](structure.md) and the "Hanging headers" pattern in [`layout-and-space.md`](layout-and-space.md) for any head that carries an eyebrow. **NOT bypassable by "preserve structural parity" / "mirror this reference" / "match the prior build" instructions** — if a reference build ships the banned pattern (most pre-rule builds do), silently flatten it in the new build. The rules win over parity. Reference builds may pre-date this gate; the gate is authoritative.

55. **All-caps display heads with line-height < 1.0 → cap-collision on wrap.** Does any display-size element (`.hero__display`, `.section__title`, `h1`, `h2`, or anything `≥ --text-2xl`) declare both `text-transform: uppercase` AND a `line-height` (or `--lh-tight`) below `1.0`? If yes, fail. Uppercase glyphs have no descenders and their cap-tops sit at the very top of the line box — at `line-height: 0.94` (the old Manifesto / Sport / Brutal default) the cap-tops of line N+1 visibly collide with the baseline or commas of line N when the title wraps. The condensed display faces (Anton, Inter Tight 900, Bebas Neue) make this worse. **Floor for all-caps display heads is `line-height: 1.0`; recommended `1.02–1.08`.** Either bump `--lh-tight` ≥ 1.0 for the theme, or drop `text-transform: uppercase` on the display element. Most visible when a two-line `.section__title` wraps with a trailing comma on line one ("SAME PROMPT, TWO / DIFFERENT OUTPUTS.") — the comma + cap-D fuse into a single glyph blob.

---

## Appendix — dropped gates and where they went

> Extraction commentary. Kept 29 of 58; dropped the other 29.

| Gates | Reason dropped |
|---|---|
| 15, 26, 39 | Focus-ring and input-state rules → `guidelines-and-review.md` § Focus States, § Forms |
| 18, 27, 33 | Accessibility (pause controls, `prefers-reduced-motion`, SVG `aria`) → § Accessibility, § Animation |
| 40, 41 | Contrast thresholds, button-text-vs-fill, dark-section ink-on-ink → § Accessibility, § Dark Mode & Theming |
| 10–14, 16, 17 | Motion / microinteraction mechanics (`transition: all`, hover-scale, overshoot easings, animating layout properties, success toasts, tooltip delays) → § Animation, § Hover & Interactive States |
| 24, 25 | Spacing-scale and measure discipline — hallmark token-system specific |
| 28 | Demo-video LCP / performance → § Performance |
| 34, 49, 50–53, 56 | Responsive mechanics (horizontal scroll, two-line clickable text, `minmax(0, 1fr)`, long-word wrap, theme section-head collapse, radio-tab scroll-jump, stacked sticky elements) → § Content Handling, § Safe Areas & Layout |
| 35, 36 | Decorative-text-effect placement and flex-row vertical centring — execution nits, not fingerprints |
| 48 | Mid-render token improvisation — hallmark token-system specific |
| 57 | Studied-DNA gate — study mode not extracted |

**Dangling references.** Kept gate text cites gate 6 and gate 8 (both kept) and gate 34 (dropped
— no horizontal scroll between 320 px and 1920 px; `guidelines-and-review.md` § Safe Areas &
Layout covers it). Kept gates also link four upstream reference files that were not extracted:
`component-cookbook.md`, `hero-enrichment.md`, `structure.md`, `layout-and-space.md`. The
`## Archetype name key` section of `hallmark-macrostructures.md` carries enough of
`component-cookbook.md` to act on gates 42 and 43.
