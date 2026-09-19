# Impeccable detector rules — how to read `data/impeccable-detector-rules.csv`

> **Apache-2.0 change notice.** Derived from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
> v4.1.0 at commit `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0,
> Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`;
> upstream NOTICE at `licenses/impeccable-NOTICE.md`).
>
> **This file has been modified from the original.** The rule registry was transformed from
> Rust source into the tabular CSV this file documents; `Trigger / Threshold` was written by
> reading the check implementations, and is not upstream prose.
>
> Upstream paths named below are impeccable's own and resolve in its tree, not in this skill.
> Full per-file record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

The rule registry is
`crates/foundation/src/registry.rs` (a port of `cli/engine/registry/antipatterns.mjs`); the
trigger conditions were read out of the check implementations:

| Source | Covers |
|---|---|
| `crates/core/src/checks/rules.rs` | shared element checks (borders, color/contrast, motion, glow, type hierarchy, eyebrow/kicker) |
| `crates/core/src/checks/measures.rs` | pure threshold checks (cream, oversized h1, thin-border/wide-shadow, hidden content, radial spotlight) |
| `crates/core/src/checks/text_rules.rs` | numbered labels, em-dash, kicker candidacy |
| `crates/core/src/checks/html_patterns.rs` | regex-on-HTML page pass |
| `crates/core/src/checks/css_scan.rs` | CSS-text scans (stripes, glow, halo, grid, marquee, pulsing dot, clip-path, buried raster) |
| `crates/core/src/browser/{quality,page_checks,element_checks,text_collectors}.rs` | live-DOM checks |
| `crates/browser/src/{lib,screenshot_contrast}.rs` | page errors and rendered-pixel contrast |
| `crates/detect/src/{regex_matchers,design_system}.rs` | line-level source scan and DESIGN.md drift |
| `crates/foundation/src/constants.rs` | shared constants (`OVERUSED_FONTS`, `EM_DASH_FLOOR = 8`, `EM_DASH_CHARS_PER_DASH = 500`, WCAG large-text sizes) |

The detector runs **without an LLM and without an API key** — that is the whole point of it. LLM
critique is a separate judgment layer in the skill (`critique`), not part of these rules.

Upstream ships **61** rules. This extraction carries **50**; the 11 that were not moved are listed
in the appendix — 9 already covered by this skill, 2 dropped by project decision.

---

## Column schema

| Column | Values | Meaning |
|---|---|---|
| `Rule ID` | kebab-case | The stable id. It is what `ignoreRules`, `impeccable-disable`, and `data-impeccable-ignore` name. |
| `Category` | `slop` \| `quality` | `slop` = an AI-generation fingerprint. `quality` = a general design/legibility defect. |
| `Scope` | empty, `type`, `layout`, or both | The design domain filter. `RULE_SCOPES` is exactly `type, layout` (union of the rules' declared scopes, `type` first from `overused-font`, then `layout` from `nested-cards`). A findings filter keeps only findings whose rule declares a requested scope; an empty scope list is no filter. |
| `Severity` | `error` \| `warning` \| `advisory` | Taken from the registry. **The registry stores no severity for most rules; the finding constructor defaults it to `warning`.** The CSV writes that default explicitly. `advisory` rules are droppable as a class (`--no-advisory`, or `detector.advisoryRules: "exclude"`). One rule, `pulsing-dot`, escalates its own severity to `error` at emit time when the selector lands in a header/nav landmark. |
| `Name` | prose | Verbatim registry `name`. |
| `Trigger / Threshold` | prose + numbers | The deterministic condition, read from the implementation. Where a rule has several engines with different tests, each is given. |
| `Engines` | `browser`, `static-html`, `text` | Which detection paths can raise it. `browser` = live DOM over CDP (computed styles, rects, hit-testing, pixels). `static-html` = the HTML/CSS engine with its own cascade, one HTML file at a time. `text` = line-level regex scan of source files. |
| `Description` | prose | Verbatim registry `description` — the message the user sees, including its fix advice. |

The registry also carries `skillSection` and `skillGuideline` per rule (pointers back into the
skill's own prose, e.g. `Typography` / `overused fonts like Inter`). Those were not extracted:
they address a section layout this skill does not have.

---

## Suppression surface

Worth knowing because it is what makes a deterministic ruleset survive contact with a real repo.
Four layers, all read from the CLI contract:

1. **Inline comments**, any comment syntax, matched anywhere on a line, case-insensitive:
   `DIRECTIVE_RE = /impeccable-(disable-next-line|disable-line|disable)\b[ \t]*([^\n\r]*)/gi`.
   Tokens after the directive split on `/[\s,]+/` and lowercase; empty, or containing `*`, means
   all rules. `disable` applies to the whole file; `-line` / `-next-line` are scoped.
   **Findings with no line number (static HTML, browser) match only whole-file directives.**
2. **DOM-scoped:** `data-impeccable-ignore="rule-a rule-b"` on an element waives matching findings
   for it and its subtree, in the browser, extension, and static engines. Empty value or `*` = all.
3. **Config** (`.impeccable/config.json`, plus a gitignored `.impeccable/config.local.json`):
   `detector.ignoreRules[]`, `detector.ignoreFiles[]` (globs), and `detector.ignoreValues[]` —
   `{ rule, value, files?, createdAt?, reason? }` in that key order. A `*` value requires `files`;
   an unscoped wildcard never matches. Value extraction is supported only for
   `overused-font, bounce-easing, design-system-font, design-system-color, design-system-radius,
   design-system-font-size`; `design-system-color` compares by parsed color, not string.
4. **The hook**, configured per project (`hook.enabled`, `hook.limits.maxFindings`,
   `hook.limits.maxChars`), auto-runs the detector after UI file edits and surfaces findings
   inline. The skill's instruction when it is active: *"act on its findings instead of
   re-auditing each rule"*.

Worked example of a value-scoped ignore, from the skill's own `.impeccable/config.json`:

```json
{
  "rule": "design-system-font-size",
  "value": "*",
  "files": ["skill/scripts/live-browser.js"],
  "createdAt": "2026-07-17T00:00:00.000Z",
  "reason": "Live overlay chrome is injected over arbitrary host pages and builds a self-contained UI with its own small type scale; DESIGN.md's ramp describes the impeccable website, not this widget"
}
```

---

## Appendix — the 11 rules not extracted

Listed so the omission is auditable. Nine were already covered by a check this skill carries; two
were dropped by project decision (see the second table).

| Rule ID | Category / severity | Upstream description | Already covered by |
|---|---|---|---|
| `side-tab` | slop / warning | Thick colored border on one side of a card — the most recognizable tell of AI-generated UIs. | `hallmark-slop-gates.md` gate **5** (thick coloured left/right side-stripe border) |
| `overused-font` | slop / warning (scope `type`) | Inter, Roboto, Fraunces, Geist, Plus Jakarta Sans, Space Grotesk … no longer feel distinctive. | gate **1** (banned display fonts) |
| `gradient-text` | slop / warning | Gradient text is decorative rather than meaningful — a common AI tell. | gate **2** (includes `background-clip: text` gradient headlines explicitly; "No genre allows gradient text") |
| `ai-color-palette` | slop / warning | Purple/violet gradients and cyan-on-dark are the most recognizable tells of AI-generated UIs. | gate **2** (purple-to-blue / cyan-to-magenta gradient) |
| `nested-cards` | slop / warning (scope `layout`) | Cards inside cards create visual noise and excessive depth. | gate **4** (any card nested inside another card) |
| `icon-tile-stack` | slop / warning (scope `layout`) | Icon tile above a heading, repeated as page structure. | gate **3** (3-equal-column card grid with icon-above-heading tiles) |
| `italic-serif-display` | slop / warning (scope `type`) | Italic serif display heading. | gate **38a** (any italic heading or display type — strictly broader) |
| `layout-transition` | quality / warning | Transitioning `width`/`height`/`padding`/`margin` instead of `transform`/`opacity`. | `guidelines-and-review.md` § Animation ("Animate `transform`/`opacity` only (compositor-friendly)") |
| `skipped-heading` | quality / warning (scope `type`) | A heading level is skipped (e.g. `<h2>` followed by `<h4>`). | `guidelines-and-review.md` § Accessibility ("Headings hierarchical `<h1>`–`<h6>`") |

(Table above: already covered. Table below: dropped by decision.)

### Dropped by project decision — the eyebrow

Impeccable and `hallmark-slop-gates.md` gate 54 cannot both be satisfied while an eyebrow exists.
Gate 54 bans the eyebrow *beside* the heading and prescribes stacking it **directly underneath in
the same column**. Impeccable bans that stacked form outright — "banned outright, repeated or not
… no brief earns it back" — so its fix is to delete the label entirely.

**This project keeps the eyebrow.** Gate 54 wins; the two rules that would flag the stacked form
are not carried.

| Rule ID | Category / severity | Upstream description | Why dropped |
|---|---|---|---|
| `kicker-above-heading` | slop / warning (scope `type`) | A tiny tracked uppercase or small-caps label sitting as its own block directly above a heading is banned outright, repeated or not. | Project decision: the eyebrow stays. Gate 54 governs its placement. |
| `hero-eyebrow-chip` | slop / warning (scope `type`) | A tiny uppercase letter-spaced label sitting immediately above an oversized hero headline — or the same shape rendered as a pill chip — is now the default AI SaaS hero. | Same. Identical shape, split from `kicker-above-heading` only by heading size (h1 ≥ 48px). |

**What still governs an eyebrow**, with those two gone:

- **Gate 54 is unchanged and still binding.** The eyebrow goes directly underneath, vertical stack
  only. Any wrapper holding both an eyebrow and a heading must resolve to `display: block`,
  `flex-direction: column`, or a single-column grid. Multi-column grids on such a wrapper are
  banned regardless of class name, and the gate is explicitly not bypassable by "match the prior
  build" instructions.
- **Gate 54's default is still OFF.** Keeping the eyebrow means it is available, not automatic.
- **`numbered-section-labels` is still carried and still fires.** An eyebrow rendered as
  `01 · FEATURES` trips it once ≥ 2 appear on a page with ≥ 2 distinct indices. Keeping the
  eyebrow did not buy the numbering.
- The `craft-floor.md` ban on kickers is still reproduced verbatim in
  `reference/impeccable-anti-patterns.md`, marked as overridden. See the note there.

### Two kept rules that sit near an existing one — read the pair, not either alone

- **`border-accent-on-rounded`** was kept although gate 5 covers side stripes: gate 5 is
  left/right only, this rule fires on a **top or bottom** accent border combined with a
  border-radius, which gate 5 does not reach.
- **`radial-halo` / `radial-spotlight-glow`** overlap gate 29 (aurora blob / mesh gradient) in
  spirit but test different things: gate 29 counts accent colors and viewport footprint, these two
  test gradient stop chromaticity, stop positions, and the darkness of the page background.
