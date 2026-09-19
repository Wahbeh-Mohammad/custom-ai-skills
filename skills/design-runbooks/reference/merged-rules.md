# The merged rule set

Four rule sources cover overlapping ground with different temperaments. This file is the
**merge policy** — precedence, severity assignment, de-duplication, and the six resolved
conflicts. It does not restate the rules. Runbook 3 reads the sources themselves from disk.

## Sources, and what each one owns

| Source | Count | Owns | Default temperament |
|---|---|---|---|
| `guidelines-and-review.md` | 17 sections + 14 anti-patterns | **Correctness** — a11y, focus, forms, animation, content handling, images, perf, navigation, touch, safe areas, dark mode, i18n, hydration, hover states, copy | BLOCKING |
| `hallmark-slop-gates.md` | 29 gates + the six-axis pre-emit critique | **Fingerprint** — what makes a page read as LLM-generated | ADVISORY |
| `impeccable-anti-patterns.md` | craft-floor ban list + § Verify floor | **Reflex bans and the quality floor** — the numbers other rules reference | mixed, see below |
| `data/impeccable-detector-rules.csv` | 50 rows | **Deterministic checks** — the `Trigger / Threshold` column is the machine-checkable condition | by row |
| `data/ui-reasoning.csv:Anti_Patterns` | 192 rows | **Per-product-type negatives** — only the row matching the product type applies | ADVISORY |
| `scripts/svg_lint.py` (rules in `svg-assets.md` § 6) | 20 rules | **Generated assets** — the SVG kit, placeholders, and the markup that points at them | by rule |

---

## 1. Precedence

**The restrictive source wins on *whether*. The permissive source governs *how*.**

Hallmark wants variety and will hand you a shape. Impeccable wants discipline and will refuse
one. When they meet, the refusal decides availability; once a thing is available, the
catalogue decides its execution. This is the general form of resolution C1 and it settles
every future collision of the same shape.

Two corollaries:

- A catalogue row — a palette, a pairing, a macrostructure, a style — is a **candidate, not a
  decision**. It still has to clear the ban list and the gates, and it still has to be
  justified against the brief.
- craft-floor's own preamble is binding: *"These are the category's defaults, not bans: the
  brief's own words can earn any of them."* Brief evidence lifts a default. Category fit,
  membership in a default sequence, and your own habit do not.

---

## 2. Severity

Two levels, per the audit contract.

**BLOCKING** — accessibility failures, broken keyboard paths, contrast below WCAG 2.2 AA,
design-system violations.
**ADVISORY** — taste, era-specific style, fingerprint / anti-slop findings.

Assignment by source:

| Source | Maps to |
|---|---|
| `guidelines-and-review.md` § Accessibility, § Focus States, § Forms | BLOCKING |
| `guidelines-and-review.md` all other sections + § Anti-patterns | BLOCKING where the rule names an a11y or keyboard failure; ADVISORY otherwise |
| `hallmark-slop-gates.md` all 29 gates | ADVISORY |
| `impeccable-anti-patterns.md` § Refuse (the ban list) | ADVISORY |
| `impeccable-anti-patterns.md` § Verify — Contrast, States (keyboard focus) | BLOCKING |
| `impeccable-anti-patterns.md` § Verify — all other bullets | ADVISORY |
| `ui-reasoning.csv:Anti_Patterns` | ADVISORY |
| `svg_lint.py` | the severity it prints, per the table in `svg-assets.md` § 6 |

**One extension to BLOCKING — a broken or unsafe asset.** `svg_lint.py` raises BLOCKING for the
contract's own categories (`placeholder-alt` is accessibility; `svg-off-palette` is
design-system drift) and for one more: an asset that fails at its only job or can run code —
`svg-parse`, `svg-viewbox`, `svg-script`, `svg-event-handler`, `svg-foreign-object`,
`svg-external-href`, `svg-embedded-raster`, `svg-text-in-mark`, `og-image-svg`. Everything else it
reports is ADVISORY. The extension covers these rule IDs and no others; it is not a door for
promoting taste findings.

Detector CSV, by its own `Severity` column with three overrides:

| CSV severity | Maps to | Rules |
|---|---|---|
| `error` | BLOCKING | `script-error`, `content-hidden-at-rest` |
| `warning`, category `quality` | BLOCKING when the rule names contrast, text size, or occlusion: `low-contrast`, `gray-on-color`, `tiny-text`, `undersized-ui-text`, `text-occlusion`, `body-text-viewport-edge`, `first-viewport-column-overflow`. ADVISORY for the rest | |
| `warning`, category `slop` | ADVISORY | all 14 |
| `advisory` | ADVISORY | all except the override below |

**Override — design-system drift is BLOCKING.** `design-system-font`,
`design-system-color`, `design-system-radius`, `design-system-font-size` ship upstream as
warning/advisory. Under this skill's severity contract they are design-system violations and
report as BLOCKING whenever a DESIGN.md exists. With no DESIGN.md they do not fire at all.

**One self-escalating rule:** `pulsing-dot` raises its own severity to `error` when the
selector lands in a header or nav landmark.

**`advisory` is droppable as a class.** When the user asks for blocking-only, drop every row
whose CSV severity is `advisory` and every gate — do not drop the BLOCKING overrides above.

---

## 3. The six resolutions — binding

### C1 · Stat-Led vs the hero-metric ban

Not a contradiction: a **selection gate** and an **execution gate**.

- **Selection.** Macrostructure 04 Stat-Led is selectable **only when the brief supplies a
  specific verifiable metric that is the product's own claim.** Membership in the SaaS
  default sequence does not satisfy this. No such metric in the brief → Stat-Led is
  unavailable regardless of category fit; pick another shape.
- **Execution.** Once selected, gate 46 applies independently: the stat is **never the hero's
  sole headline** — it is paired with the claim it supports.

### C2 · Lucide

Gate 30 stands as written. The Phosphor-only abstention stands as behaviour. What changes is
that the abstention stops reading as a judgment:

- `core.py` reason string is now a coverage statement, not a verdict: *"Icon lookup is
  Phosphor-only; Lucide is a fine choice, I just can't name specific glyphs for it. Use
  Lucide's own search."*
- `design_system.py` checklist items lead with Phosphor **because it is the one this skill can
  support end to end**, not because it is better: *"one icon library throughout: Phosphor
  (glyph lookup available in this skill), or Lucide/Heroicons if you prefer."*

The alternatives stay on offer. Only the default steering changes.

### C3 · Pure `#000` / `#fff` and zero-chroma neutrals

`colors.csv` encodes surfaces as **slot markers, not final values**. Gates 7 and 22 stay
global and unscoped. Neutrals are tinted at token-emission time — see `contract.md`
§ Neutral tinting for the transform. `colors.csv` is not modified.

### C4 · Gate 1 font ban vs `typography.csv`

Gate 1 stays global and unscoped. 7 of 74 is not enough to weaken the one anti-slop position
both upstream sources share. **Flag, don't delete** — this is a retrieval filter, so a banned
pairing never reaches selection rather than failing a gate after the fact.

`typography.csv` carries two new columns. Flagged rows are excluded from candidate sets by
default:

| Pairing | Heading | Flag |
|---|---|---|
| Modern Professional | Poppins | `gate1_fail` |
| Minimal Swiss | Inter | `gate1_fail` |
| Spatial Clear | Inter | `gate1_fail` |
| Modern Dark Cinema (Inter System) | Inter | `gate1_fail` |
| Flat Design Mobile (System Bold) | Inter | `gate1_fail` |
| Bold Typography Mobile (Inter Poster) | Inter | `gate1_fail` |
| Material You MD3 (Roboto System) | Roboto | `gate1_fail` + `gate1_platform_exempt` |

**Three ways a flagged row is returnable**, each with the gate-1 note attached, never
silently:

1. the user explicitly names the font — brief evidence, earns it under the craft-floor clause;
2. DESIGN.md already specifies it — an incumbent system outranks the catalogue;
3. `gate1_platform_exempt` and the selected stack is Jetpack Compose — Roboto is
   platform-correct there and the ban is a category error. (Out of scope for this web-only
   skill; the flag is carried so the exemption is recorded, not so it fires here.)

**Gate 1 governs display only.** The body font in each flagged pairing is unaffected. Where
the non-heading half is sound, keep the row usable by **substituting the heading face** rather
than discarding the pairing: return the body font with the nearest non-banned display
alternative from the same pairing cluster.

### C5 · Glassmorphism auto-activation

The craft-floor ban is on **glass-as-decoration**, not glass per se. The defect is the
auto-activation, not the style's availability.

**Demoted from activation to candidate.** `if_data_heavy` no longer sets
`style:glassmorphism`; the style surfaces as one option among the direction candidates,
subject to the same justification requirement as any retrieved row. Selection requires a
**stated purpose the effect serves** — layering depth over a busy data surface, a floating
control reading as above the content — and that purpose is recorded in DESIGN.md. Absent one,
the style is not available and the reflex is what the ban catches.

`if_data_heavy` was the weakest possible trigger: data density argues for legibility and
contrast, not translucency over a busy background, which works against both. The rule was
never well-founded even before the collision.

**Same treatment applied to `style:liquid-glass`** (`if_luxury` → E-commerce), found by the
follow-up sweep: identical defect, identical family, and `if_luxury` is a tone rather than a
purpose for translucency.

**Left active, deliberately:** `style:brutalism` (`if_creative_field` → Portfolio/Personal).
craft-floor bans hard offset shadows *"outside a world that is actually neobrutalist"* — its
own carve-out covers a genuinely selected brutalist world.

**The remaining sweep, for the record.** 12 style auto-activations across 192 rows, 7 distinct
styles. `style:flat-design` ×6, `style:minimalism-and-swiss-style`,
`style:3d-and-hyperrealism`, `style:parallax-storytelling` — no ban-list collision. One
internal tension noted, not resolved: E-commerce's own `Anti_Patterns` reads "Flat design
without depth" while six other rows auto-activate `style:flat-design`. Different rows, so no
contradiction fires; flagged here so a future sweep does not rediscover it.

### C6 · The placeholder `TODO` comment vs the rationale ban

Hallmark's *Swappability* rule (`svg-assets.md` § 2, verbatim) puts an HTML comment above every
placeholder: `<!-- TODO: Replace with real <thing>, target size: <WxH> -->`. This skill bans
direction rationale from HTML comments and from every other surface that reaches the browser
(SKILL.md § Always true). A shot brief — the subject, the crop, the size a photographer should
deliver — is art direction, so the two collide.

**The ban wins on *whether*; hallmark's goal governs *how*.** No comment. The two things the
comment did are kept, moved off the page:

- **The swap signal** is the `assets/placeholders/` path and the visible `<Kind> · <ratio>`
  label. Both are obvious in source and in the rendered page without saying why.
- **The brief** — subject, crop, ratio, target size, path — goes in the final report and, on a
  revamp, in REVAMP.md `## Notes`. What is owed goes to PRODUCT.md § Evidence on Hand.

The rest of *Swappability* binds unchanged: alt text still describes the intended subject, and
the "single constant" is the placeholder directory, since a local file per slot needs no base
URL. The verbatim text is not edited; the override lives in its extraction note and here.

---

## 4. De-duplication — do not report the same defect twice

Nine detector rules were dropped upstream-side because a gate already covers them. Three more
pairs overlap without being duplicates. Report the **gate**, not both.

| Covered by a gate — never report these rule IDs | Gate |
|---|---|
| `side-tab` | 5 |
| `overused-font` | 1 |
| `gradient-text`, `ai-color-palette` | 2 |
| `nested-cards` | 4 |
| `icon-tile-stack` | 3 |
| `italic-serif-display` | 38a |
| `layout-transition` | `guidelines-and-review.md` § Animation |
| `skipped-heading` | `guidelines-and-review.md` § Accessibility |

**Read the pair, not either alone** — these are kept because they reach further than the gate:

- `border-accent-on-rounded` — gate 5 is left/right only; this fires on a **top or bottom**
  accent border combined with a border-radius.
- `radial-halo` / `radial-spotlight-glow` — gate 29 counts accent colours and viewport
  footprint; these test gradient stop chromaticity, stop positions, and background darkness.

**Not carried at all — the eyebrow.** `kicker-above-heading` and `hero-eyebrow-chip` were
dropped by project decision. **This project keeps the eyebrow**; gate 54 wins and governs its
placement: directly underneath, vertical stack only, single-column wrapper
(`block` / `flex-direction: column` / `1fr` grid), never a multi-column grid regardless of
class name, and not bypassable by "match the prior build" instructions. Gate 54's default is
still OFF — the eyebrow is available, not automatic. `numbered-section-labels` still fires, so
`01 · FEATURES` still trips once two appear with distinct indices.

**Dangling reference:** kept gate text cites gate 34 (no horizontal scroll), which was
dropped. `guidelines-and-review.md` § Safe Areas & Layout covers it.

---

## 5. Read order at audit time

Re-read from disk, in this order. Never audit from memory of what you just built.

1. `reference/contract.md` — then `DESIGN.md` and `PRODUCT.md` if they exist
2. `guidelines-and-review.md` — correctness, BLOCKING-heavy
3. `data/impeccable-detector-rules.csv` — the deterministic conditions
4. `reference/impeccable-anti-patterns.md` — ban list + the floor's numbers
5. `reference/hallmark-slop-gates.md` — fingerprint, ADVISORY
6. `reference/svg-assets.md` §§ 1, 6 — the slot rule and the asset checks, when the project has
   SVG files or placeholder slots
7. `data/ui-reasoning.csv` — the one row matching the product type, if known
8. this file — precedence, severity, de-dup
