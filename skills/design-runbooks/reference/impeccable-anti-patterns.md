# Impeccable anti-patterns — the explicit "don't do this" list

> **Apache-2.0 change notice.** Derived from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
> v4.1.0 at commit `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0,
> Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`;
> upstream NOTICE at `licenses/impeccable-NOTICE.md`).
>
> **This file has been modified from the original.** Ban-list text is verbatim; it was
> re-collected from four upstream files into one, and impeccable's routing prose around it was
> dropped.
>
> Upstream paths named below are impeccable's own and resolve in its tree, not in this skill.
> Full per-file record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

Sources: `skill/reference/craft-floor.md` (the whole file is the ban list), the `## Pitfalls` list
from `skill/reference/document.md`, and the negative clauses from `skill/SKILL.src.md` and
`skill/reference/init.md`.

`craft-floor.md` is loaded **immediately before any UI edit, including small refinements**, and
not at all for planning-only work. Its framing, verbatim:

> Load this after the direction is settled, and build without announcing the checklist. A pinned
> brief or the committed visual world overrides anything here; your own habit does not. When the
> design hook is active it already enforces the mechanical checks below as you edit: act on its
> findings instead of re-auditing each rule.

The `<!-- rule:... -->` markers are the skill's own rule ids, kept as provenance handles.

---

## § Refuse — the ban list (verbatim)

The preamble is load-bearing and is quoted before the list:

> These are the category's defaults, not bans: the brief's own words can earn any of them.
> Reaching for one when the axis is free means you were not deciding; recognizing that means
> rewriting the element, not softening it.

### Page scaffolds

- Same-size cards of icon plus heading plus text as the page structure. Cards are the lazy container; nested cards are always wrong. <!-- rule:skill-ban-identical-card-grids --> <!-- rule:skill-layout-cards-lazy -->
- The hero-metric template: big number, small label, supporting stats, accent. <!-- rule:skill-ban-hero-metric -->
- ~~A kicker or eyebrow above a heading. This one is a ban, not a default: no brief earns it back. The heading carries its own weight; delete the label and let the heading speak.~~ <!-- rule:skill-ban-eyebrow-on-every-section --> **OVERRIDDEN — see below.**
- Section numbers (01 / 02 / 03) unless the sequence itself carries information the reader needs. <!-- rule:skill-ban-numbered-section-markers -->
- A modal for a task that needs neither interruption nor protected focus. <!-- rule:skill-reflex-modal-by-reflex -->

> **Project override — the eyebrow.**
> This project keeps the eyebrow. The bullet above is left verbatim and struck through rather than
> deleted, so the extraction stays auditable against upstream.
>
> Upstream's kicker ban and `hallmark-slop-gates.md` gate 54 cannot both be satisfied while an
> eyebrow exists: gate 54 bans it *beside* the heading and prescribes stacking it directly
> underneath in the same column; upstream bans that stacked form outright. **Gate 54 wins here.**
>
> What stays binding: the eyebrow sits directly above the heading in the same column, vertical
> stack only, never on the same horizontal row. Gate 54's wrapper rule still applies — single-column
> `block` / `flex-direction: column` / `1fr` grid, no multi-column grid, not bypassable by
> "match the prior build" instructions. Gate 54's default is still OFF, so an eyebrow is available,
> not automatic. And `numbered-section-labels` is still carried, so `01 · FEATURES` still fires once
> two appear with distinct indices. The two matching detector rules, `kicker-above-heading` and
> `hero-eyebrow-chip`, were not extracted — see `impeccable-detector-rules.md`.

### Surface habits

- Gradient text. Emphasis comes from weight or size. <!-- rule:skill-ban-gradient-text -->
- Glass and blur as decoration rather than as a specific effect. <!-- rule:skill-ban-glassmorphism-default -->
- A colored `border-left` or `border-right` above 1px on cards, list items, callouts, or alerts. <!-- rule:skill-ban-side-stripe-borders -->
- Hard offset shadows (`box-shadow: 4px 4px 0`) outside a world that is actually neobrutalist. The zero-blur block shadow is a costume, not a depth system; a world that did not choose it never earns it as a default. <!-- rule:skill-ban-hard-offset-shadow -->
- Sparklines, progress rings, and soft-shadowed rounded rectangles standing in for content. <!-- rule:skill-reflex-decorative-chrome -->
- Monospace as a costume for "technical" rather than for code, data, or measurement. <!-- rule:skill-reflex-mono-as-technical -->
- A system display face (Impact, Arial Black, the platform sans) as the display voice of an own-world page. Source and self-host a face whose character matches the approved lettering; the closest installed font is a failure, not a fallback. <!-- rule:skill-ban-system-display-face -->
- Unicode glyphs or emoji standing in for an icon system. Icons are drawn, from a real library or authored SVG, in one consistent stroke and weight. <!-- rule:skill-ban-glyph-icons -->
- Geometric masks standing in for organic contours. A circle, polygon, or radial-gradient cutout approximating a photographic subject's edge is the cheap version of the effect and reads worse than omitting it. Derive an alpha matte from the actual image, or produce a cut-out asset. <!-- rule:skill-ban-geometric-occlusion-mask -->
- Light or dark picked by category. Pick it from the use scene: who, where, under what ambient light. <!-- rule:skill-reflex-theme-by-habit -->

### Harness-conditional bans

Upstream wraps these in `<codex>` and `<gemini>` tags: the build emits them only into the
distribution for that harness, because they answer that model's characteristic failure. They are
model-specific corrections, not universal rules — adopt them deliberately.

**`<codex>`**

- Tracking stops at -0.04em. -0.02 to -0.03em usually reads better. <!-- rule:skill-typo-codex-tracking-repeat -->
- Declare elevation once, border or shadow. A 1px border under a wide soft shadow is the ghost card. Card radii stay at 12–16px; pills are for small controls. <!-- rule:skill-codex-elevation-radius --> <!-- rule:skill-ban-codex-ghost-card --> <!-- rule:skill-ban-codex-over-round -->
- Real illustration or none. Sketch-style SVG scenes, `loose-sketch` / `doodle` class names, and `feTurbulence` grain read as amateur. This bans SVG imitating pictures, never SVG doing geometry: crisp vector shapes, diagrams, animated linework, and shader-driven effects remain first-class media. A shaded, perspectived, or figure-bearing illustration is a picture even in line-art style; geometry means shapes a session can specify exactly. <!-- rule:skill-ban-codex-sketchy-svg -->
- Backgrounds are surfaces, textured only from the subject's world. `repeating-linear-gradient` stripes and two-axis grid overlays need an actual canvas, map, blueprint, or measuring tool under them. <!-- rule:skill-ban-codex-stripes --> <!-- rule:skill-ban-codex-grid-backgrounds -->
- Claims and configuration come from supplied truth; label illustrative values honestly. Naming a concept and then ironizing it is not a claim. <!-- rule:skill-codex-material-honesty --> <!-- rule:skill-ban-codex-x-theater -->

**`<gemini>`**

- Never animate an image on hover, directly or through its parent. It is not an action target. Give the container the feedback. <!-- rule:skill-interaction-gemini-no-image-hover -->

### The closing line

> The floor holds the mechanics; it never picks the direction. With every check green, spend the
> page on the committed world, and when torn between refined and committed, commit. <!-- rule:skill-floor-not-ceiling -->

---

## § Verify — the quality floor the bans sit on (verbatim)

Not a don't-list, but it carries the numbers several bans reference (tracking floor, measure,
display cap), so it is kept whole.

> Each of these is a check on the built result, not an intention. Run them together in the batched
> inspection rounds, not as separate screenshot trips; the checks share one render.

- **Contrast:** body and placeholder text ≥4.5:1, large text ≥3:1. On colored surfaces tint secondary text from that hue or the foreground; never gray. <!-- rule:skill-color-verify-contrast -->
- **Depth:** shadows carry an offset and a soft blur. A zero-offset colored halo is decoration. <!-- rule:skill-color-no-glow-halo -->
- **Spacing:** tight groups, generous separation, more space above a heading than below it. Read the computed values. <!-- rule:skill-layout-spacing-rhythm -->
- **Type:** body measure 65–75ch, display max 6rem, tracking floor -0.04em, balanced headings, obvious scale and weight steps. Run the real copy at every breakpoint and fix what overflows. <!-- rule:skill-typo-floor --> <!-- rule:skill-ban-text-overflow -->
- **Motion:** one authored moment, not scattered effects and not one identical entrance on every section. Exponential ease-out from an already-visible default. Reach past transform and opacity: blur, backdrop-filter, clip-path, mask, and shadow belong to the palette when they stay smooth. <!-- rule:skill-motion-floor --> <!-- rule:skill-motion-materials-palette --> <!-- rule:skill-motion-no-section-fade -->
- **States:** hover, disabled, loading, error, empty. Plus real content, working controls, responsive composition, keyboard focus. <!-- rule:skill-floor-shipping -->
- **Browser surfaces:** the parts you did not draw still carry the design. Text selection, the caret, custom scrollbars, focus rings, underline offset, and the numerals in tabular data all ship with browser defaults that belong to no design system. Theme them from the palette. This is the cheapest signal that a page was built rather than assembled, and the one models skip most reliably. <!-- rule:skill-craft-browser-surfaces -->
- **Copy:** the product's own language. Controls name their action; errors name the problem and the recovery. <!-- rule:skill-copy-design-material -->
- **Coverage:** every brief requirement present and findable within seconds. <!-- rule:skill-floor-brief-coverage -->

---

## Artifact-writing pitfalls (verbatim, `document.md § Pitfalls`)

- Don't paste raw CSS class names. Translate to descriptive language.
- Don't extract every token. Stop at what's actually reused; one-offs pollute the system.
- Don't invent components that don't exist. If the project only has buttons and cards, only document those.
- Don't overwrite an existing DESIGN.md without asking.
- Don't duplicate content from PRODUCT.md. DESIGN.md is strictly visual.
- Don't replace canonical sections with near-synonyms. Put layout and responsive behavior in `Layout`; put motion with the affected world or component.
- Don't rename sections even slightly. "Colors" not "Color Palette & Roles". "Typography" not "Typography Rules". Tooling parsing depends on exact headers.
- Don't duplicate token values between frontmatter and prose. If a color is in `colors.primary` as hex, the prose can name it and describe its role but should not reassert a different hex. The frontmatter is normative.
- Don't invent frontmatter token groups outside Stitch's schema (no `motion:`, `breakpoints:`, `shadows:` at the top level). Stitch's Zod schema only accepts `colors`, `typography`, `rounded`, `spacing`, `components`. Anything else belongs in the sidecar's `extensions`.

---

## Process anti-patterns

Scattered across `SKILL.src.md`, `init.md`, and `new-work.md` as negative clauses rather than a
list. Summarised, with the load-bearing sentences quoted.

| Don't | Source line |
|---|---|
| Redirect a clear brief toward your own taste | "Honor pinned aesthetics, eras, materials, fonts, and palettes even when they conflict with a saturated-pattern warning. Redirecting a clear brief toward your taste is failure." |
| Split the difference on a redesign | "Never split the difference into polish on the discarded look." |
| Treat a missing DESIGN.md as greenfield | "Visual authority is evidence, not a filename. Missing DESIGN.md alone does not make a project greenfield." |
| Turn a local addition into an identity exercise | "A section, component, feature, or state inside an established surface inherits that surface. Never turn a local addition into a new identity exercise." |
| Ask for aesthetics during init | "Do not ask for an aesthetic direction, emotional feel, visual references, colors, typography, or style during init." |
| Invent product facts to fill a section | "invented testimonials, customers, benchmarks, pricing, licensing, or deployment claims" do not belong in PRODUCT.md; "Record undecided facts instead of inventing them." |
| Let a demonstration-data gap kill a bold direction | "Refusing a bold direction because its demonstration data does not exist yet is the timidity reflex wearing honesty's clothes." Truth binds **claims** — prices, customers, benchmarks, endpoints, capabilities — not demonstrations, which may be authored at full fidelity and labelled synthetic. |
| Ship the direction contract to the browser | Banned from source, comments, hidden DOM, `data-*`, RSC payloads, metadata, a11y-only text, and files served beside the artifact. |
| Repair drift as a side effect | "Never repair drift as a side effect of a design task." |
| Run open-ended self-QA | "Verify in bounded passes, not a loop… Open-ended self-QA burns the user's money doing worse what the finish handoffs do better." |
| Auto-run a command from a bare invocation | "Never auto-run a command; the recommendation is a suggestion the user confirms." |
