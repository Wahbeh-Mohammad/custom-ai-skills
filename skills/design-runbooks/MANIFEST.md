# Extraction manifest

Four upstream skills were extracted into this skill:

| # | Upstream | Licence | Lands in | Fidelity |
|---|---|---|---|---|
| 1 | [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.13.0 [`15de38fb7`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/15de38fb70bc80ae9276fa7703b48ae861a672e6) | MIT | `data/`, `scripts/`, `reference/retrieval-split.md` | byte-identical |
| 2 | [hallmark](https://github.com/nutlope/hallmark) v1.1.0 [`13ac0ec7e`](https://github.com/nutlope/hallmark/tree/13ac0ec7e148655948100b6396439e481361d690) | MIT | `reference/hallmark-*.md`, two marked blocks in `reference/svg-assets.md` | condensed + filtered |
| 3 | [web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) [`e3d624baa`](https://github.com/vercel-labs/web-interface-guidelines/tree/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1) | MIT | `guidelines-and-review.md` | rule text verbatim |
| 4 | [impeccable](https://github.com/pbakaus/impeccable) v4.1.0 [`cb56ed6c1`](https://github.com/pbakaus/impeccable/tree/cb56ed6c19a07329a9fa0cd4e657bee040156593) | **Apache-2.0** | `reference/impeccable-*.md`, `data/impeccable-detector-rules.csv` | schemas + tables verbatim, process prose summarised |

Licence texts are in `licenses/`; the obligations each one places on this distribution are
discharged in `THIRD-PARTY-NOTICES.md` and `NOTICE`. The skill as a whole ships under
Apache-2.0 (`LICENSE`) — the only licence compatible with all four inbound terms.

**Every fidelity claim in this file is reproducible against a pinned commit.** The SHAs above
were not taken on faith: for each upstream, every extracted source file was fetched at that
commit and diffed against what this skill ships. Counts in § Pinned provenance below.

Not everything here came from upstream. `reference/runbook-revise.md`, `history/**`,
`scripts/svg_lint.py` and `reference/svg-assets.md` outside its two marked blocks are **original
to this skill** — see § 18 at the foot of this file.

---

---

# Pinned provenance

Each upstream is pinned to the commit the extraction was taken from. Verification method: fetch
every extracted source file at that commit and diff it against the vendored copy this skill was
built from.

| Upstream | Pinned commit | Date | Files diffed | Result |
|---|---|---|---|---|
| ui-ux-pro-max | [`15de38fb7`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/15de38fb70bc80ae9276fa7703b48ae861a672e6) | 2026-09-15 | 24 (all of `data/`, `data/stacks/`, `scripts/`) | all identical |
| hallmark | [`13ac0ec7e`](https://github.com/nutlope/hallmark/tree/13ac0ec7e148655948100b6396439e481361d690) | 2026-08-06 | 27 (`slop-test`, `custom-theme`, `macrostructures` + all 21 shapes, `component-cookbook`, `hero-enrichment`, `assets` — the last re-diffed 2026-09-18) | all identical |
| web-interface-guidelines | [`e3d624baa`](https://github.com/vercel-labs/web-interface-guidelines/tree/e3d624baaf29dc1fc645aff3e38f03e564d2d6b1) | 2026-08-18 | 1 (`command.md`) | identical |
| impeccable | [`cb56ed6c1`](https://github.com/pbakaus/impeccable/tree/cb56ed6c19a07329a9fa0cd4e657bee040156593) | 2026-09-10 | 10 (`SKILL.src.md`, 4 `reference/`, `registry.rs`, `CLI-CONTRACT.md`, `NOTICE.md`, `LICENSE`) | all identical |

## impeccable has moved since the pin

`cb56ed6c1` is **not** impeccable's current HEAD. Upstream added a `generate` verb on
2026-09-15 (`fc89b0e`), which edits both `skill/SKILL.src.md` and `skill/reference/routing.md`
— the two files `reference/impeccable-commands.md` was extracted from. Consequences:

- The verb table here holds **23 verbs in 6 categories**, correct at `cb56ed6c1`. Upstream now
  has 24; `generate` (Iterate) is the addition.
- `routing.md`'s `devServer.running` row now names `generate` alongside `live`.

Nothing else in the extraction is affected, and neither change alters a rule, gate or schema.
A refresh should re-pin and re-diff rather than assume the delta is still this small.

The other three pins were current HEAD at the time of pinning; they are recorded as SHAs anyway,
so a later upstream change cannot silently invalidate a fidelity claim made here.

## Re-verifying a pin

```bash
SHA=cb56ed6c19a07329a9fa0cd4e657bee040156593
curl -s "https://raw.githubusercontent.com/pbakaus/impeccable/$SHA/skill/reference/craft-floor.md" \
  | diff - <(sed -n '/^## /,$p' reference/impeccable-anti-patterns.md)   # adjust per file
```

Extraction notes name the exact upstream path for every file, so each one can be fetched at its
pinned SHA and compared directly.


# Extraction 1 — ui-ux-pro-max

Upstream: <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill> v2.13.0
Pinned commit: `15de38fb70bc80ae9276fa7703b48ae861a672e6` (2026-09-15)
Licence: MIT, (c) 2024 Next Level Builder — `licenses/ui-ux-pro-max-MIT.txt`
Extracted from: `.claude/skills/ui-ux-pro-max` in a local checkout of that repo
Catalog verified upstream at: 2026-08-26 (`data/catalog-summary.json`)

Every file under `data/` and `scripts/` was **byte-identical to upstream** at extraction time
— verified with `diff -rq` against the source tree. Nothing was rewritten, pruned in-file, or
reformatted. Selection happened at file granularity only.

> **No longer true as of the skill build.** Five conflicts between the four upstream sources
> were resolved by the project owner, and four of them required changes to `data/` or
> `scripts/`. Every deviation is listed in **§ 17 — Deviations from upstream** at the foot of
> this file. The extraction is still auditable: no row was deleted, and every changed line is
> named there.

---

## 1. Product-type → design decision mapping

The mapping is **two joined tables**, not one. Both extracted.

| File | Rows | What it holds |
|---|---|---|
| `data/products.csv` | 192 | Human-facing recommendation per product type |
| `data/ui-reasoning.csv` | 192 | Machine-applied decision rules per product type |

`products.csv` columns:
`Product Type, Keywords, Primary Style Recommendation, Secondary Styles, Landing Page Pattern, Dashboard Style (if applicable), Color Palette Focus, Key Considerations`

`ui-reasoning.csv` columns:
`UI_Category, Recommended_Pattern, Style_Priority, Color_Mood, Typography_Mood, Key_Effects, Decision_Rules, Anti_Patterns, Severity, Reasoning, Confidence`

Join key: `products.csv:Product Type` == `ui-reasoning.csv:UI_Category` (1:1 across all 192).

`Decision_Rules` is the interesting part — a closed, non-executable JSON grammar:

```json
{"if_ux_focused":["style:minimalism-and-swiss-style"],"if_data_heavy":["style:glassmorphism"]}
```

> The example above is the row **as extracted**. The `if_data_heavy` condition was later
> removed by resolution C5 — see § 17.

- Conditions: `must_have` + 35 `if_*` signals, each backed by a literal keyword tuple
  matched against the user query at word boundaries.
- Actions: 4 prefixes — `style:<style-id>`, `constraint:<token>`, `pattern:<name>`, `mode:dark|light`.
- Grammar + validator + applier live in `scripts/reasoning_contract.py` (self-contained, stdlib only).
  Data is never `eval`'d; unknown conditions/actions raise.

### Dependency closure (included, not in the original ask)

`products.csv` and `ui-reasoning.csv` are mostly **foreign keys**. Without their targets the
mapping dangles, so these came along:

| File | Rows | Why |
|---|---|---|
| `data/styles.csv` | 88 (50 active, 29 supplemental, 9 deprecated) | Target of `Primary Style Recommendation`, `Secondary Styles`, `Style_Priority`, and every `style:<id>` action |
| `data/landing.csv` | 34 | Target of `Landing Page Pattern` and every `pattern:<name>` action |

`styles.csv` carries a deprecation graph (`Status`, `Parent Style ID`, `Replacement Domain`,
`Replacement ID`) plus `Implementation Checklist` and `Design System Variables` per style —
the actual token payload. `landing.csv` carries `Section Order`, `Primary CTA Placement`,
`Color Strategy`, `Conversion Optimization`.

---

## 2. Palettes with semantic roles pre-assigned

`data/colors.csv` — **192 palettes, one per product type**, same join key.

16 pre-assigned roles per palette (a superset of the Primary/Secondary/CTA/Background/Text/Border
set — this is the shadcn token vocabulary, with on-colors):

```
Primary        On Primary
Secondary      On Secondary
Accent         On Accent        # Accent == CTA
Background     Foreground       # Foreground == Text
Card           Card Foreground
Muted          Muted Foreground
Border
Destructive    On Destructive
Ring
```

Plus a `Notes` column that records contrast fixes applied upstream, e.g.
`Trust blue + orange CTA contrast [Accent adjusted from #F97316]`.

Role → CSS variable mapping is in `scripts/design_system.py:SEMANTIC_COLOR_ENTRIES`
(`Primary` → `--color-primary`, `Accent/CTA` → `--color-accent`, …).

Palette count was **not** pruned. All 192 kept, since the row identity *is* the product-type join.

### Light/dark resolution

Palettes are single-mode rows. `design_system.py` resolves mode before picking a palette,
so a dark-first style can't ship with a light background:

- `_resolve_color_mode(query, style)` — dark if the query holds one of 8 explicit dark
  phrases (`dark mode`, `dark theme`, `night mode`, `oled`, …) or the chosen style is
  dark-first per `styles.csv:Preferred Mode` / `Light Mode ✓` / `Dark Mode ✓`.
- `_palette_is_dark(palette)` — real WCAG relative luminance of `Background` below 0.18
  (the corpus gap is wide: lightest dark bg ≈ 0.026, darkest light bg ≈ 0.79).
- `_derive_dark_palette(palette)` — keeps brand tokens, replaces surfaces, and picks a `Ring`
  that clears 3:1 against the new background. Tagged `_mode_derivation: derived-dark`.
- `_filter_anti_patterns_for_mode()` — drops "avoid dark mode" anti-patterns once dark is resolved.

Full mechanism in `reference/retrieval-split.md` §6.

---

## 3. Font pairings

`data/typography.csv` — **74 pairings**, all kept.

Columns as extracted: `Font Pairing Name, Category, Heading Font, Body Font, Mood/Style Keywords, Best For, Google Fonts URL, CSS Import, Tailwind Config, Notes`

> Two columns were added by resolution C4 — `gate1_fail`, `gate1_platform_exempt`. See § 17.

Each row ships the ready-to-paste artifacts: a `<link>`-able Google Fonts URL, an `@import`
line, and a Tailwind `fontFamily` fragment.

Category distribution: `Sans + Sans` 25, `Serif + Sans` 13, `Display + Sans` 10,
`Serif + Serif` 2, `Mono + Sans` 2, `Mono + Mono` 2, and 20 one-off categories
(triple stacks, single-family systems, script pairings).

---

## 4. Chart-type selection rules

`data/charts.csv` — **25 rows**, keyed by *data shape*, not chart name.

Columns: `Data Type, Keywords, Best Chart Type, Secondary Options, When to Use, When NOT to Use, Data Volume Threshold, Color Guidance, Accessibility Grade, Accessibility Risk, Accessibility Notes, A11y Fallback, Library Recommendation, Interactive Level`

Data types covered:
Trend Over Time · Compare Categories · Part-to-Whole · Correlation/Distribution ·
Heatmap/Intensity · Geographic · Funnel/Flow · Performance vs Target · Time-Series Forecast ·
Anomaly Detection · Hierarchical/Nested · Flow/Process · Cumulative Changes ·
Multi-Variable Comparison · Stock/Trading OHLC · Relationship/Connection ·
Distribution/Statistical · Performance vs Target (Compact) · Proportional/Percentage ·
Hierarchical Proportional · Root Cause Analysis · 3D Spatial · Real-Time Streaming ·
Sentiment/Emotion · Process Mining

The load-bearing columns are `When NOT to Use` (hard negatives, e.g. "fewer than 4 data
points → use a stat card") and `Data Volume Threshold` (render-strategy switch, e.g.
"<1000 pts: SVG; ≥1000: Canvas + downsampling; >10000: aggregate to intervals").

`Accessibility Grade` is dead — upstream value is the literal string
`deprecated: use Accessibility Risk`. Use `Accessibility Risk` (`risk:low|…`) instead.

---

## 5. Stack rules (selective)

10 of upstream's 22 stacks — the web ones. Shared schema:
`Category, Guideline, Description, Do, Don't, Code Good, Code Bad, Severity, Docs URL, Applies To, Status, Verified At`

| Stack | Rows | Active | Deprecated | Categories | Pinned version |
|---|---|---|---|---|---|
| `react` | 61 | 59 | 2 | 18 | react 19.2.x |
| `nextjs` | 60 | 59 | 1 | 15 | nextjs 16.2 |
| `shadcn` | 68 | 68 | 0 | 26 | shadcn cli 4 |
| `nuxt-ui` | 70 | 70 | 0 | 23 | nuxt-ui 4.10 |
| `nuxtjs` | 67 | 66 | 1 | 16 | nuxtjs 4.5 |
| `html-tailwind` | 59 | 58 | 1 | 16 | html-tailwind 4.3 |
| `svelte` | 55 | 44 | 11 | 15 | svelte 5 |
| `astro` | 53 | 53 | 0 | 14 | astro 7.1.6 |
| `angular` | 50 | 50 | 0 | 8 | angular 22.x |
| `vue` | 49 | 49 | 0 | 17 | vue 3.5.x |

**Not extracted** (available upstream if wanted): `swiftui`, `react-native`, `flutter`,
`jetpack-compose`, `threejs`, `laravel`, `javafx`, `wpf`, `winui`, `avalonia`, `uno`, `uwp`.

Do not strip the `Status` / `Applies To` columns. Stack retrieval picks **one coherent
framework generation** per query from them (`core.py:_stack_row_filter`) — see
`reference/retrieval-split.md` §5. `shadcn` additionally routes on
`Applies To: base=radix|base|aria`.

---

## 6. Icons

`data/icons.csv` — **105 curated icons**, all kept.

Columns: `Category, Icon Name, Keywords, Library, Import Code, Usage, Best For, Style, Semantic Role, Allowed Contexts`

18 categories (Action 12, Navigation 8, Status 8, Media 7, Commerce 7, Files 7, Data 6,
Layout 6, Social 6, Security 6, Communication 5, User 5, Device 5, Location 4, Time 4,
Development 4, Style Config 4, Guideline 1).

Library: Phosphor (100 web, 4 react-native, 1 with a Heroicons fallback). Lucide is
**explicitly unsupported** — `core.py` force-abstains any icon query containing "lucide"
(`reason: unsupported-library`).

The a11y value is in `Semantic Role` (`interactive` 20, `meaningful` 84) ×
`Allowed Contexts` (`decorative|meaningful|interactive`), with the rule restated per-row
in `Usage`: decorative → `aria-hidden="true"`; meaningful → text alternative; interactive →
accessible name on the control + state (`aria-pressed` / `aria-expanded`).

Not extracted: `phosphor-icons-upstream.json` (1512 raw icons, 824 KB) — that's a catalog
dump for the refresh tooling, not guidance.

---

## 7. GSAP motion presets

`data/motion.csv` — **17 presets**, all kept.

Columns: `Category, Intensity Tier, Keywords, Trigger, Duration, Easing, GSAP Snippet, Framework Notes, Do, Don't, Performance Notes`

7 categories: Hover Micro-interaction · Scroll Reveal · Stagger List · Page Transition ·
Parallax Scroll · Loading/Skeleton · Carousel/Auto-Rotation.
3 intensity tiers: Subtle 6 · Standard 7 · Complex 4 — the tier is what the `--motion`
dial selects on.

Every row carries a runnable `GSAP Snippet`, a `prefers-reduced-motion` note in
`Framework Notes`, and a compositor-thread justification in `Performance Notes`.

---

## 8. Querying scripts

`scripts/` — 4 files, stdlib-only Python 3, no external deps.

| File | Role |
|---|---|
| `search.py` | CLI entry: arg parsing, output formatting, truncation policy |
| `core.py` | BM25 index, domain auto-detection, thresholds/abstention, domain + stack search |
| `design_system.py` | Multi-domain aggregation, color-mode resolution, dials, ASCII/MD/MASTER.md renderers, persistence |
| `reasoning_contract.py` | Closed grammar for `Decision_Rules` — parse + validate + apply |

Retrieval architecture is documented in `reference/retrieval-split.md`.

### Verified working in this extraction

```
--design-system                                    ✅ full pipeline
--domain product | style | color | typography
         landing | chart | icons | gsap            ✅
--stack  react nextjs vue svelte astro nuxtjs
         nuxt-ui angular html-tailwind shadcn      ✅
```

Smoke check: `search.py "beauty spa wellness service" --design-system` resolves
Beauty/Spa/Wellness Service → style `soft-ui-evolution`, palette `#EC4899`,
pairing Lora/Raleway, pattern "Hero + Testimonials + CTA".

### Known gap

4 domains in `core.py:CSV_CONFIG` point at CSVs that were **not** extracted. Querying them
fails cleanly with `Error: File not found: …`, it does not crash or return fake data:

| Domain | Missing file | Upstream rows |
|---|---|---|
| `ux` | `ux-guidelines.csv` | 119 |
| `react` | `react-performance.csv` | 44 |
| `web` | `app-interface.csv` | 32 |
| `google-fonts` | `google-fonts.csv` | 1934 (747 KB) |

Note `--domain react` (React *performance* rules) is a different thing from
`--stack react` (React *UI* rules). The stack one works.

Likewise `core.py:STACK_CONFIG` still declares all 22 stacks, so `--stack` accepts e.g.
`flutter` at the argparse level and then returns `Error: Stack file not found: …`. Same
clean failure, no fabricated rows. To hard-limit the surface, delete the 12 unextracted
entries from `STACK_CONFIG` — nothing else reads them.

Also not extracted: `references/quick-reference.md` (full text of the 119 UX guidelines),
`references/pro-rules.md` (native-app pre-delivery checklist), `scripts/validate_data.py`,
`scripts/tests/`, `data/data-provenance.json`, `data/google-font-licenses.json`.

---

# Extraction 2 — hallmark

Upstream: <https://github.com/nutlope/hallmark> v1.1.0
Pinned commit: `13ac0ec7e148655948100b6396439e481361d690` (2026-08-06)
Licence: MIT, (c) 2026 Hallmark contributors — `licenses/hallmark-MIT.txt`
Extracted from: `skills/hallmark` in a local checkout of that repo

**Fidelity: verbatim body, extraction commentary in blockquotes.** Rule text, bullet lists,
tables, palettes, stamps and code blocks are copied byte-for-byte from upstream and left in
source order under their source headings. Nothing was reworded, renumbered or reordered.
Selection happened at the block level: whole blocks are kept or dropped, never edited. Every
addition of ours is either a `>` blockquote or a section explicitly headed *Extraction note* /
*Appendix*, so source text and commentary never mix. Verified by substring-matching every
source line back against the extracted files.

| File | Source | Kept | Dropped |
|---|---|---|---|
| `reference/hallmark-macrostructures.md` | `references/macrostructures.md` + `macrostructures/01–21` + name keys from `component-cookbook.md`, `hero-enrichment.md` | all 21 shapes, all prose, all code skeletons | per-shape *Sample opening lines* only |
| `reference/hallmark-custom-theme.md` | `references/custom-theme.md` | the whole file | nothing (H1 retitled) |
| `reference/hallmark-slop-gates.md` | `references/slop-test.md` | 29 of 58 gates + the pre-emit critique | 29 gates + their section headings |
| `reference/svg-assets.md` (§ 1 one bullet, § 2 one block) | `references/assets.md` | § Placeholder strategy body, whole; one *Avoid* bullet from § Brand / company logos | the rest of the file |

## 9. Macrostructures — page-level structure

The priority item: nothing else in this skill covers page-level structure. `landing.csv` (§1)
carries `Section Order` per landing pattern, which is adjacent but thinner — it names sections,
not a complete page fingerprint.

All **21** shapes, each with its six-part fingerprint bullet list (heading placement, body
composition, divider language, button voice, image treatment, reveal pattern), its
*Reach for it* / *Avoid* / *Reference* lines, and its HTML section skeleton where upstream
ships one (shapes 01–10).

`macrostructures.md` itself is reproduced in full: the intro, the mandatory diversification
rule, the vague-brief rule (pick from the first ten), the Specimen demotion, hero polish
patterns, the nav-and-footer-voice rule, the 21-item index, the SaaS page sequence with its
voice rules, and the *How to pick* procedure.

**Dropped:** the per-shape *Sample opening lines* blocks — three quoted copy fixtures per
shape, ~60 lines total. Copy voice, not structure.

**Added (marked as such):** an *Archetype name key* section holding the N1–N13 / Ft1–Ft8 /
H1–H9 / HP1–HP4 names and the two genre routing tables, verbatim from `component-cookbook.md`
and `hero-enrichment.md`. Without it the nav and footer gates name archetypes this skill
cannot resolve. The per-archetype specs (`references/components/`, 54 files) were not
extracted — the names and routing defaults are enough to know the AI default is banned and
what the alternatives are, not enough to build each archetype to upstream spec.

## 10. Custom theme — the escape hatch

The whole file, verbatim. It is almost entirely lists, palettes and stamps — trigger signals,
the follow-up questions, the bespoke drops/keeps lists, the palette recipe (§ B), font pairing
(§ C), the axis vocabularies (§ D), stamp format (§ E), log shape (§ F), three worked examples
with full OKLCH values (§ G), and the five *what custom does not do* guards.

The requested distillation — how the branch stays rare — is stated up front as a blockquote
that quotes the source rather than paraphrasing it. Three properties: the fork surfaces only on
an enumerated signal list and is never mentioned otherwise; the confirmation question defaults
to the incumbent, so silence routes to catalog; the floor (every gate) fires unchanged at every
depth.

An earlier draft of this file condensed § B and § C into a summary table and dropped § B.6's
contrast verification. Both are restored — the source is a list, so it is copied, not
summarised.

## 11. Slop gates — fingerprint + editorial subset

**Count discrepancy resolved.** Upstream README says "fifty-seven"; `SKILL.md` says 58 in five
places. The file is authoritative: **58** numbered entries, 1–57 plus an inserted **38a**.

**Kept — 29:** 1–9, 19, 20–23, 29–32, 37, 38, 38a, 42–47, 54, 55. Gate text verbatim, under the
source's own headings, in source order, with genre notes intact. Section preambles and
end-of-section stamp lines are kept where their section retained a gate.

| Cluster | Gates |
|---|---|
| Visual fingerprint | 1 banned display fonts · 2 purple-blue / gradient text · 3 icon-tile 3-col grid · 4 nested cards · 5 side-stripe border · 6 centred-everything hero · 7 pure `#000`/`#fff` base |
| Structural fingerprint | 8 generic AI template / repeated macrostructure · 9 undifferentiated section rhythm · 20 missing stamp · 21 Specimen fall-through · 32 same archetype, same knobs |
| Palette tells | 22 zero-chroma neutrals · 23 accent > 5 % footprint |
| Icon / illustration tells | 29 aurora blob / mesh-gradient background · 30 mixed icon libraries **and emoji-as-icon** · 31 Lottie-by-default |
| Typography fingerprint | 37 more than three families · 38 outlier face in 3+ slots · 38a italic headings · 55 all-caps display at `line-height` < 1.0 |
| Nav / footer / hero chrome | 42 nav fingerprint · 43 footer fingerprint · 44 hero fit (padding ratio + 1280×800 fold) · 45 decorative-without-purpose · 54 eyebrow beside heading |
| Editorial / honest copy | 19 placeholder names + startup clichés · 46 invented metric + bare-number hero · 47 re-drawn UI chrome |

The table above is a reading aid in this manifest only; the extracted file does **not**
re-cluster the gates, it leaves them under their upstream headings. That means gate 19 stays
filed under *Microinteractions* and gates 54–55 under *Mobile-responsiveness*, which is where
upstream puts them.

The **pre-emit six-axis self-critique** (Philosophy · Hierarchy · Execution · Specificity ·
Restraint · Variety, score 1–5, anything < 3 forces a revision pass) is kept verbatim — it is
the editorial front-end to the gate list, and axis F is the structural-variety check gates 8 and
32 enforce mechanically.

**Dropped — 29:** every contrast, focus-ring and accessibility gate, plus motion mechanics,
responsive mechanics, performance, spacing/token discipline, and study mode. The file's appendix
maps each dropped gate to the `guidelines-and-review.md` section that covers it, and names the
one dangling reference (kept gate text cites dropped gate 34).

An earlier draft of this file re-clustered and lightly reworded several gates and added
explanatory glosses not in the source (e.g. a "palette tell, not a contrast rule" note on gate
7). All of that is removed; the gates now match upstream byte-for-byte.

Note the overlap this creates with `guidelines-and-review.md` (Vercel's Web Interface
Guidelines), which is the intended split: **that file governs correctness; this one governs
fingerprint.** Gate 30's emoji-as-icon clause and `data/icons.csv`'s `Semantic Role` column also
meet here — icons.csv says *which* icon and how to label it, gate 30 says *don't reach for an
emoji or a second library*.

## 11b. Assets — placeholder strategy

Added 2026-09-18 with the SVG asset procedure. `reference/svg-assets.md` is original to this
skill (§ 18) and embeds two verbatim blocks from `references/assets.md` at the pinned commit,
re-diffed against it on the day — identical:

- **§ Placeholder strategy**, the body under the heading, whole: the five-tier canon table,
  *Swappability*, *Remote asset safety* and *Anti-patterns*. The heading line is dropped; the
  skill's own `## § 2 · Placeholders` heads it.
- **One bullet** from § Brand / company logos › *Avoid* — placeholder customer logos from
  template kits.

The verbatim text is not edited. Where the skill departs from it — tiers 1, 3 and 4 do not
apply; the `TODO` HTML comment is replaced — the departure lives in the block's *Extraction
note* and in `merged-rules.md` § C6, which is recorded under § 17.

Considered and **not** extracted: ui-ux-pro-max's `.claude/skills/brand/references/logo-usage-rules.md`
and the logo CSVs under `.claude/skills/design/data/logo/`. They are print-oriented brand-guide
material, and their generator produces raster images through a hosted model — nothing the SVG
procedure needs.

## Not extracted from hallmark

Per the request: the four verbs (`design` / `redesign` / `audit` / `study` flow in `SKILL.md`,
`references/verbs/`), study mode (`references/study.md`, gate 57), and the named catalog themes
(`references/themes/`, `site/css/tokens.css` — 21 `[data-theme]` blocks; upstream prose says
"21 themes" in `custom-theme.md` but gate 57 lists only 20, omitting Grid).

Also not extracted: `references/components/` (54 archetype files — only the N / Ft / H / HP name
keys and the two routing tables were lifted), the rest of `component-cookbook.md`,
`anti-patterns.md`, `color.md`, `typography.md`, `layout-and-space.md`, `motion.md`,
`microinteractions.md`, `interaction-and-states.md`, `responsive.md`, the rest of
`hero-enrichment.md`, `imagery-kit.md`, the rest of `assets.md` (§ 11b), `copy.md`, `contract.md`, `design-md.md`,
`export-formats.md`, `structure.md`, `genres/`, and the `site/` reference implementation.

Cross-references to those files survive inside the verbatim text as provenance. They resolve in
the upstream tree, not in this skill.

---

# Extraction 3 — web-interface-guidelines (Vercel Labs)

Upstream: <https://github.com/vercel-labs/web-interface-guidelines> (unversioned — no tags)
Pinned commit: `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` (2026-08-18)
Licence: MIT, (c) 2025 Vercel Labs — `licenses/vercel-web-interface-guidelines-MIT.txt`
Extracted from: `command.md` at the repo root

**Fidelity: rule text verbatim.** Every rule is copied byte-for-byte, in source order, under its
source heading. No rule was reworded, reordered, renumbered, added or removed.

## 12. Correctness rules — `guidelines-and-review.md`

The whole of upstream's `## Rules` section lands in `guidelines-and-review.md`, keeping all
seventeen headings in order:

Accessibility · Focus States · Forms · Animation · Typography · Content Handling · Images ·
Performance · Navigation & State · Touch & Interaction · Safe Areas & Layout ·
Dark Mode & Theming · Locale & i18n · Hydration Safety · Hover & Interactive States ·
Content & Copy · Anti-patterns (flag these)

Two mechanical changes, both structural, neither touching a rule:

| Change | Why |
|---|---|
| Headings demoted `###` → `##` | Upstream nests its rules under a `## Rules` parent. That parent is dropped, so its children rise one level. |
| Upstream's YAML frontmatter, `$ARGUMENTS` preamble and `## Output Format` section dropped | They are the command harness, not the rules. This skill routes through `SKILL.md` and Runbook 3 owns the finding format (`reference/runbook-audit.md`). |

Verify the claim with:

```bash
SHA=e3d624baaf29dc1fc645aff3e38f03e564d2d6b1
curl -s "https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/$SHA/command.md" \
  | tail -n +5 | diff - <(sed '2,14d' guidelines-and-review.md)
```

Every hunk it reports is a heading-level line or the dropped Output Format block.

## Not extracted from vercel-web-interface-guidelines

`install.sh`, `README.md`, `AGENTS.md`, and the `## Output Format` block described above. The
repo's `SKILL.md` wrapper is superseded by this skill's own routing.

**Overlap is intentional.** These rules cover the same ground as
`reference/hallmark-slop-gates.md` and `reference/impeccable-anti-patterns.md` with a different
temperament. The split: **this file governs correctness**, hallmark governs fingerprint,
impeccable governs the craft floor. Precedence and de-duplication are in
`reference/merged-rules.md`.

---

# Extraction 4 — impeccable

Upstream: <https://github.com/pbakaus/impeccable> v4.1.0 (engine `ENGINE_VERSION` 0.1.5)
Pinned commit: `cb56ed6c19a07329a9fa0cd4e657bee040156593` (2026-09-10)
Licence: **Apache-2.0**, Copyright 2025 Paul Bakaus — `licenses/impeccable-APACHE-2.0.txt`
Upstream NOTICE reproduced per Apache-2.0 § 4(d): `licenses/impeccable-NOTICE.md`, `NOTICE`
Extracted from: the repo root of a local checkout

> **Apache-2.0 § 4(b) applies to this extraction.** Every file listed below is a *modified*
> derivative and carries a change notice at its head. The changes themselves are recorded per
> file in §§ 13–16 and per conflict in § 17.
>
> Two files outside this extraction also carry notices, because otherwise-original prose embeds
> verbatim impeccable text: `reference/contract.md` (the PRODUCT.md / DESIGN.md schemas and
> their bracketed field prompts) and `reference/runbook-create.md` (the three opening questions
> from `init.md`). `data/impeccable-detector-rules.csv` carries its notice in the sibling file
> `data/impeccable-detector-rules.NOTICE.md` — a comment line inside the CSV would break every
> naive parser.

The canonical skill is `skill/SKILL.src.md` + `skill/reference/*.md` (34 reference files); the
provider folders (`.claude/`, `.cursor/`, `plugin/`, …) are generated copies of it. The
deterministic detector is a Rust engine under `crates/`, ported from the older
`cli/engine/**/*.mjs` and documented in `docs/CLI-CONTRACT.md`.

Fidelity is mixed and stated per item: **every schema, template, table, ban list, and numeric
threshold is verbatim or read directly off the implementation**; the surrounding process prose
(interview flow, decision-page choreography, comp generation) is summarised or dropped.

| File | Source | What it holds |
|---|---|---|
| `reference/impeccable-artifacts.md` | `init.md`, `document.md`, `new-work.md`, `SKILL.src.md`, `docs/CLI-CONTRACT.md` | PRODUCT.md and DESIGN.md schemas, the init question set, the surface-brief layer, and the six mechanisms that hold them apart |
| `data/impeccable-detector-rules.csv` | `crates/foundation/src/registry.rs` + the check implementations | 50 of 61 deterministic rules, one row each |
| `reference/impeccable-detector-rules.md` | same, plus `docs/CLI-CONTRACT.md` | column schema, severity/scope semantics, the suppression surface, and the 11-rule dropped appendix |
| `reference/impeccable-commands.md` | `SKILL.src.md`, `routing.md` | the 23-verb table, routing rules, the visitor-mode axis, meta-verbs |
| `reference/impeccable-anti-patterns.md` | `craft-floor.md`, `document.md`, `init.md`, `SKILL.src.md` | the explicit ban list |

---

## 13. PRODUCT.md / DESIGN.md — the artifact split

The highest-value item. Nothing else in this skill separates **durable product truth** from
**visual direction**; `hallmark-custom-theme.md` (§10) gets closest and is a theme-construction
protocol, not a record format.

Kept verbatim: the PRODUCT.md template with all 11 sections and their bracket prompts · the
schema stamp `<!-- impeccable:product-schema 1 -->` and its regex, insertion rule, and
`PRODUCT_V4_SECTIONS` / `PRODUCT_DEPRECATED_SECTIONS` constants · the DESIGN.md YAML frontmatter
example and its five rules (token refs, color formats, the 8-prop component ceiling, open-ended
scale keys, variants-as-naming-convention) · the eight canonical body sections in order · the
`.impeccable/design.json` sidecar schema at `schemaVersion: 2` with its component-translation
rules, tonal-ramp spec, and narrative mapping · the seed-mode marker comment · the
`parseDesignMd` section-matching contract · the surface-brief frontmatter shape and slug
normalization · the six-block direction contract including the verbatim FINISH line.

Kept as a list: the init interview — the three opening questions verbatim, the four conditional
questions with their triggers and where each answer lands, the three-questions-per-round cap, the
one-real-answer-before-writing rule, and the "probe once before assuming nobody is there"
mechanical test.

**The separation itself** is the part written up rather than copied, because upstream never
states it in one place. Six enforcement mechanisms, each quoted to its source line: separate
writers per artifact · explicit belongs / does-not-belong lists on both sides · visitor mode
persisted per-surface (with the deprecated `## Register` section as the cautionary tale) ·
composition never promoted from a surface brief into the global world · asymmetric
redesign-vs-refinement semantics · one source of truth per value (frontmatter normative over
prose, sidecar extends rather than duplicates, `buildPath` barred from PRODUCT.md).

**Dropped:** the decision-page / `serve-question` choreography, `concept-seed` and the re-roll
protocol, comp-vs-code build paths beyond the one init question that records the preference, live
mode setup, and the doctor/staleness machinery beyond naming it.

---

## 14. Detector rules

`data/impeccable-detector-rules.csv` — **50 rows**. Columns:

`Rule ID, Category, Scope, Severity, Name, Trigger / Threshold, Engines, Description`

`Rule ID`, `Category`, `Scope`, `Name`, and `Description` are verbatim registry fields.
`Severity` is the registry value with the constructor's `warning` default written out explicitly
(upstream stores no severity for 36 of the 50 and defaults at emit time). `Trigger / Threshold`
is the deterministic condition, read out of the Rust check implementations — this is the column
upstream has no prose equivalent for, and the reason the extraction exists. `Engines` names which
of the three detection paths can raise the rule (`browser` live DOM, `static-html` engine,
`text` line-level regex).

Category split across the 50: `slop` 23, `quality` 27. Severity: `error` 2, `warning` 36,
`advisory` 12. Scope: `type` 14, `layout` 11 (2 rules carry both), unscoped 27.

**Not extracted, already covered (9 rules)** — listed with their covering gate in
`reference/impeccable-detector-rules.md`: `side-tab` (gate 5) · `overused-font` (gate 1) ·
`gradient-text` and `ai-color-palette` (gate 2) · `nested-cards` (gate 4) · `icon-tile-stack`
(gate 3) · `italic-serif-display` (gate 38a) · `layout-transition` and `skipped-heading`
(`guidelines-and-review.md`).

**Not extracted, dropped by decision (2 rules)** — `kicker-above-heading` and `hero-eyebrow-chip`.
These two directly contradict `hallmark-slop-gates.md` gate 54: gate 54 bans an eyebrow *beside*
the heading and prescribes stacking it directly underneath in the same column, while Impeccable
bans that stacked form outright ("no brief earns it back"). Both cannot hold while an eyebrow
exists. **This project keeps the eyebrow, so gate 54 wins and the two rules are not carried.**
Gate 54 still governs placement (vertical stack, single-column wrapper, default OFF), and
`numbered-section-labels` is still carried, so a numbered eyebrow still fires.

Two kept rules sit near an existing one and are flagged inline rather than silently merged:
`border-accent-on-rounded` reaches top/bottom borders that gate 5 does not, and `radial-halo` /
`radial-spotlight-glow` test gradient mechanics where gate 29 counts footprint.

Also dropped from every row: the registry's `skillSection` / `skillGuideline` fields, which point
into a skill-prose layout this skill does not have.

---

## 15. Command vocabulary

The 23-verb table is copied verbatim (command, category, description, upstream reference path),
plus the alias and deprecation notes (`teach` → `init`; `craft` deprecated; `shape` owns task
discovery; `bolder` / `quieter` are not the direction-round registers).

Kept alongside it because routing depends on them: the no-argument routing rules, the
signal → command mapping the context-aware menu reasons over, the never-auto-run constraint, and
the four **visitor modes** (Persuade / Operate / Read / Experience) — chosen per surface, not per
product, which is the axis orthogonal to the verb.

Six meta-verbs (`context`, `signals`, `detect`, `doctor`, `hooks`, `pin`) are named with one line
each, since they define the routing surface even though the operations are not portable.

**Dropped:** all 34 command reference bodies. The table is a taxonomy for routing, not an
implementation.

---

## 16. Anti-patterns

`craft-floor.md` is the ban list and is carried whole: the `## Refuse` bullets under their
original *Page scaffolds* / *Surface habits* split, the `## Verify` quality floor (kept because it
carries the numbers the bans reference — measure 65–75ch, display max 6rem, tracking floor
-0.04em, contrast 4.5:1 / 3:1), and the closing "the floor holds the mechanics; it never picks
the direction" line. The preamble is quoted intact because it governs the whole list: these are
category defaults the brief can override, with exactly one stated exception upstream — the
kicker/eyebrow ban, which "no brief earns back". **That one bullet is overridden here**: this
project keeps the eyebrow, so the bullet is struck through rather than deleted (the list stays
auditable against upstream) and carries a note recording the decision and what gate 54 still binds.

The `<codex>` and `<gemini>` blocks are preserved and labelled: upstream emits them only into
that harness's distribution, so they are **model-specific corrections, not universal rules**.
The `<!-- rule:... -->` ids are kept as provenance handles.

Also kept: `document.md`'s 9 `## Pitfalls` bullets verbatim, and a summarised table of the
process-level negatives scattered through `SKILL.src.md`, `init.md`, and `new-work.md`, each with
its quoted source line.

## Not extracted from impeccable

The Rust engine itself (`crates/`, 16 crates), the CLI and its contract document, the browser
extension and `browser-bundle/`, the VS Code and Cursor plugins, live mode (`live.md`,
`live-setup.md`, the overlay), comp fidelity (`comp-spec` / `comp-diff` / `font-match` /
`build-phase`, `docs/COMP-FIDELITY.md`), image generation, the decision-page server
(`serve-question`), `concept-seed` and the catalog of challenger worlds, the design hook, all 34
command reference bodies, the native-platform references (`ios.md`, `android.md`, and the
`.native.md` variants), `critique.md`'s persona and scoring machinery, and the marketing site.

---

# 17. Deviations from upstream — the skill build

Everything above describes the *extraction*. This section records the changes made when the
extraction was built into a skill, so `data/` and `scripts/` remain auditable against their
sources.

Five cross-source conflicts were surfaced during the inventory and resolved by the project
owner; a sixth, C6, arrived with the SVG asset procedure. Full statements of each resolution are in `reference/merged-rules.md` § 3; this is the
diff-level record.

| # | Conflict | Files touched |
|---|---|---|
| C1 | Hallmark macrostructure 04 Stat-Led vs impeccable's hero-metric ban | none — documentation only |
| C2 | Gate 30 names Lucide; `core.py` abstains on it; `design_system.py` recommends it | `scripts/core.py`, `scripts/design_system.py` |
| C3 | Gates 7 and 22 vs `colors.csv` pure-white/black surfaces and zero-chroma neutrals | `scripts/design_system.py` |
| C4 | Gate 1's display-font ban vs 7 of 74 rows in `typography.csv` | `data/typography.csv`, `scripts/core.py` |
| C5 | craft-floor's glass ban vs `ui-reasoning.csv` auto-activating glassmorphism | `data/ui-reasoning.csv` |
| C6 | Hallmark's placeholder `TODO` HTML comment vs this skill's ban on direction rationale in the browser | none — documentation only |

## C1 — no file changed

Resolved as a **selection gate plus an execution gate**, not a contradiction. Stat-Led is
selectable only when the brief supplies a specific verifiable metric that is the product's own
claim; gate 46 then binds independently. Enforced in `reference/runbook-create.md` § 2c.

The general principle it established — **the restrictive source wins on *whether*, the
permissive source governs *how*** — is recorded in `reference/merged-rules.md` § 1 and governs
every future collision of this shape.

## C2 — the Lucide abstention reads as coverage, not judgment

`scripts/core.py` — the icons abstention keeps its behaviour and changes its reason:

- `reason` `"unsupported-library"` → `"phosphor-only-catalog"`
- added a `message` field: *"Icon lookup is Phosphor-only; Lucide is a fine choice, I just
  can't name specific glyphs for it. Use Lucide's own search."*

`scripts/design_system.py` — four checklist lines that steered users to the dead path now lead
with the library the skill can support end to end, while keeping the alternatives on offer:
*"One icon library throughout: Phosphor (glyph lookup available in this skill), or
Lucide/Heroicons if you prefer."* (Lines in `format_ascii`, `format_markdown`, the forbidden-
patterns list, and the MASTER.md pre-delivery checklist.)

## C3 — neutral tinting at token-emission time

`colors.csv` is **unmodified**. Its surfaces are treated as slot markers, not final values, and
transformed in `scripts/design_system.py`:

- new `_tint_neutral_palette()` plus an OKLab/OKLCH conversion pair (`_hex_to_oklch`,
  `_oklch_to_hex`, `_format_oklch`) — stdlib only, sRGB round-trip verified exact.
- every zero-chroma neutral is tinted toward the palette's primary hue at chroma `0.006`, just
  above gate 22's `0.005` floor, lightness preserved.
- a pure-black background lifts to `L = 0.13` (inside the 0.12–0.15 band) for OLED halation.
- gate 7's modern-minimal exception for pure `#fff` paper is honoured by reading the selected
  style (`_style_is_modern_minimal`).
- AA body contrast is **re-verified on the post-transform values**, adjusting ink lightness
  when the transform costs contrast, and recording the adjustment.
- the transform runs once, at palette selection in `generate_design_system`.
- renderers now emit the OKLCH value as normative with the sRGB hex as fallback; the colors
  dict carries `oklch` and `tint_notes`.

Also fixed here: the hardcoded display-font fallback `"Inter"` violated gate 1. Changed to
`"Figtree"`. The body-font fallback is untouched — gate 1 governs display only.

## C4 — gate-1 pairings flagged, filtered, and substituted

`data/typography.csv` — **no row deleted**; two columns added:

- `gate1_fail` — `yes` on the 7 rows whose `Heading Font` is on gate 1's ban list: Modern
  Professional (Poppins), Minimal Swiss, Spatial Clear, Modern Dark Cinema, Flat Design Mobile,
  Bold Typography Mobile (all Inter), Material You MD3 (Roboto).
- `gate1_platform_exempt` — `jetpack-compose` on Material You MD3 only, where Roboto is
  platform-correct and the ban is a category error. Out of scope for this web-only skill; the
  flag records the exemption rather than firing it.

Both columns added to the domain's `output_cols` and stripped from the returned entries after
the policy runs.

`scripts/core.py` — new `_apply_gate1_policy()` and helpers, applied to the `typography` domain
inside `search()`. A flagged row is **not dropped**; its display face is substituted so the
sound body half stays usable:

- substitute picked from the same pairing cluster (`Category`), falling back to the same
  display class (`sans` / `serif` / …), then the whole corpus; never a gate-1 face, never the
  row's own body face, deprioritizing faces named in the dropped `overused-font` rule's
  description; ranked by Jaccard similarity over `Mood/Style Keywords` + `Best For`.
- `Google Fonts URL` / `CSS Import` / `Tailwind Config` are prefixed `[regenerate for <face>]`
  rather than rewritten — emitting an unverified font URL would be worse than flagging it.
- a `_gate1` note is attached to every affected result. Nothing is substituted silently.

Two bypasses, both noted rather than silent: the query **explicitly names the display face**
(brief evidence), or the face appears in `_GATE1_ALLOWED_DISPLAY_FONTS` (an incumbent
DESIGN.md outranks the catalog).

> Implementation note worth keeping: evidence matching deliberately does **not** accept the
> `Font Pairing Name`. BM25 surfaces a flagged row precisely because the query hit its name, so
> accepting the pairing name as evidence made the filter a no-op in testing. Naming the pairing
> is not naming the font.

## C5 — glass demoted from activation to candidate

`data/ui-reasoning.csv` — two `Decision_Rules` conditions removed. No row deleted, no other
column touched. All 192 rows still validate against `reasoning_contract.parse_decision_rules`.

| Row | Was | Now |
|---|---|---|
| SaaS (General) | `{"if_ux_focused":[...],"if_data_heavy":["style:glassmorphism"]}` | `{"if_ux_focused":[...]}` |
| E-commerce | `{"if_luxury":["style:liquid-glass"],"if_conversion_focused":[...]}` | `{"if_conversion_focused":[...]}` |

Both styles remain fully reachable through ordinary retrieval — they are candidates now, not
activations, and selection requires a stated purpose the effect serves, recorded in DESIGN.md.

`liquid-glass` was found by the follow-up sweep the C5 resolution asked for. That sweep checked
all 192 rows for the same shape: 12 style auto-activations, 7 distinct styles. Left active by
decision: `style:brutalism` (`if_creative_field`), since craft-floor's hard-offset-shadow ban
carves out *"a world that is actually neobrutalist"*. No collision: `style:flat-design` ×6,
`style:minimalism-and-swiss-style`, `style:3d-and-hyperrealism`, `style:parallax-storytelling`.
Style activations went 12 → 10.

## C6 — no file changed

The verbatim *Swappability* bullet stays in `reference/svg-assets.md` § 2 unedited. The comment
is superseded by the block's *Extraction note* and by `reference/merged-rules.md` § C6: the swap
signal is the `assets/placeholders/` path plus a visible label, and the shot brief moves to the
final report and REVAMP.md `## Notes`.

## Verification after the changes

- `data/ui-reasoning.csv`: 192/192 rows parse against the closed decision-rule grammar.
- `data/typography.csv`: 74 rows, 13 columns, 7 flagged, 1 platform-exempt.
- OKLCH conversion: exact sRGB round-trip on `#FFFFFF`, `#000000`, `#EC4899`, `#0F172A`,
  `#F1EEF5`.
- `--design-system` verified on 5 briefs; all 8 working `--domain` values and all 10 `--stack`
  values still return.
- Gate-1 policy verified on all three paths: default substitution, brief-names-the-font, and
  incumbent-DESIGN.md allowance.

Nothing above changes the extraction's **known gaps** (§ 8) — the four unextracted domains and
the twelve unextracted stacks still fail cleanly.

---

# 18. Original to this skill — not extracted

Everything in §§ 1–16 traces to an upstream source. These files do not. They have no upstream,
no snapshot commit and nothing to diff against, so they are recorded here to keep the rest of
the manifest's audit claim honest.

| Path | What it is |
|---|---|
| `reference/runbook-revise.md` | Runbook 4 — the post-delivery revision loop, its tier model, and the history write-back procedure |
| `history/README.md` | The taste store's documentation — file shapes, promotion and demotion, how to edit or wipe it |
| `history/TASTE.md` | The distilled taste rules the boot gate offers. Ships empty |
| `history/log/` | Per-project revision records. Ships empty |
| `reference/svg-assets.md` | The SVG brand kit and picture surfaces — everything except the two verbatim hallmark blocks recorded in § 11b |
| `scripts/svg_lint.py` | The asset linter VERIFY runs. Standard library only |
| `scripts/test_svg_lint.py` | Its tests — `python3 -m unittest scripts/test_svg_lint.py` |

The boot gate in `SKILL.md` § Taste history, the route row for Runbook 4, the `## Step 6`
sections of `runbook-revamp.md` and `runbook-create.md`, the non-attachment note in
`runbook-audit.md`, and the fourth lifetime in `contract.md` § 3 are original for the same
reason.

**No upstream behaviour was changed to make room for them.** No gate was relaxed, no ban lifted
and no rule rewritten: the revision loop re-screens every candidate against the gates that
already existed, and a taste rule steers selection only after the user confirms it, beneath a
pinned brief, without entering the BLOCKING / ADVISORY severity system at all.
The first five resolved conflicts in § 17 are unaffected. The SVG asset procedure added
later relaxed nothing either: it tightens — an image-led selection gate beside C1, a narrow
*broken or unsafe asset* extension to BLOCKING — and C6 resolves its one collision.

**`history/` is not part of the extraction** and carries no upstream licence obligation. It is
also runtime state rather than skill content — an evaluation harness should set `history: off`
so a benchmark neither reads it nor writes to it.
