# Retrieval architecture — ui-ux-pro-max

> **Extraction note.** Describes code from
> [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
> v2.13.0 at commit `15de38fb70bc80ae9276fa7703b48ae861a672e6` — MIT,
> (c) 2024 Next Level Builder (`licenses/ui-ux-pro-max-MIT.txt`). The prose is
> original to this skill; the behaviour it documents is upstream's, with the deviations in
> `MANIFEST.md` § 17 (C2, C4) already folded in.

How the extracted scripts turn a natural-language query into rows. Distilled from
`scripts/core.py`, `scripts/search.py`, `scripts/design_system.py`, `scripts/reasoning_contract.py`.
Everything here is stdlib-only Python 3, no index files on disk, no embeddings.

---

## 1. The retrieval split — searched columns ≠ returned columns

This is the central design decision. Every domain declares two disjoint-ish column lists
(`core.py:CSV_CONFIG`). BM25 indexes **only** `search_cols`; the result projection returns
**only** `output_cols`. Keyword/alias columns feed matching; payload columns (hexes, code,
checklists) feed the answer and are never diluted into the index.

| Domain | File | Searched | Returned |
|---|---|---|---|
| `product` | products.csv | Product Type, Keywords, Primary Style Recommendation, Key Considerations | + Secondary Styles, Landing Page Pattern, Dashboard Style, Color Palette Focus |
| `color` | colors.csv | **Product Type, Notes only** | all 16 roles + Notes |
| `style` | styles.csv | Style ID, Style Category, Aliases, Keywords, Best For, Type, AI Prompt Keywords | + Status, Parent Style ID, Preferred Mode, Primary Colors, Effects & Animation, Light/Dark Mode, Performance, Accessibility, Framework Compatibility, Complexity, CSS/Technical Keywords, Implementation Checklist, Design System Variables |
| `typography` | typography.csv | Font Pairing Name, Category, Mood/Style Keywords, Best For, Heading Font, Body Font | + Google Fonts URL, CSS Import, Tailwind Config, Notes |
| `chart` | charts.csv | Data Type, Keywords, Best Chart Type, When to Use, When NOT to Use, Accessibility Notes | + Secondary Options, Data Volume Threshold, Color Guidance, Accessibility Risk, A11y Fallback, Library Recommendation, Interactive Level |
| `landing` | landing.csv | Pattern ID, Pattern Name, Aliases, Keywords, Conversion Optimization, Section Order | + Primary CTA Placement, Color Strategy |
| `icons` | icons.csv | Category, Icon Name, Keywords, Best For, Library | + Import Code, Usage, Style, Semantic Role, Allowed Contexts |
| `gsap` | motion.csv | Category, Intensity Tier, Keywords, Trigger | + Duration, Easing, GSAP Snippet, Framework Notes, Do, Don't, Performance Notes |
| stacks | stacks/*.csv | Category, Guideline, Description, Do, Don't, Code Good, Code Bad | + Severity, Docs URL, Applies To, Status, Verified At |

Note `color`: the 16 hex columns are **deliberately not searched**. Palettes are retrieved by
product identity, never by hex similarity — which is why `#EC4899` in a query can't pull a
pink palette, and why the `color` domain relies on the product-type join.

### Truncation policy (`search.py`)

Text output truncates field values at 300 chars, **except** an allowlist that would be
destroyed by a mid-token cut (`core.py:UNTRUNCATED_COLS`):

```
Code Example Good, Code Example Bad, Code Good, Code Bad,
Implementation Checklist, Design System Variables,
CSS Import, Tailwind Config, GSAP Snippet
```

`--full` disables truncation entirely; `--json` never truncates.

---

## 2. Scoring

Textbook BM25 (`core.py:BM25`), `k1=1.5`, `b=0.75`, IDF = `log((N-df+0.5)/(df+0.5)+1)`.
One document per CSV row = `" ".join(search_cols)`.

**Tokenize:** lowercase → synonym substitution → strip non-word chars → drop tokens
shorter than 2 chars → drop 22 stopwords.

Stopword list (22 entries) is deliberately tiny so short domain tokens (`ui`, `ux`, `ai`, `css`, `3d`,
`js`, `os`, `md`, `gsap`) stay searchable:
`to in on at is of by or an if no so do be we it as the and for are was`

**Synonyms** — plain dict, longest-first, word-boundary regex (`core.py:_SYNONYMS`):
`q&a→question answer`, `e-commerce→ecommerce`, `dark-mode|darkmode→dark`,
`light-mode|lightmode→light`, `a11y→accessibility`, `nav→navigation`, `sign-up→signup`,
`log-in→login`, `colour(s)→color(s)`, `customisation→customization`,
`organisation→organization`, `behaviour→behavior`, `ux/ui→ux ui`.

**Caching:** `_csv_cache` (path → rows) and `_bm25_cache` (path+fields+version → index),
both keyed on `(mtime_ns, size)`. CSVs are read with a before/after signature check and up
to 3 retries, so a file rewritten mid-read raises instead of yielding a torn snapshot.
Matters because one `--design-system` run fires 6+ searches over overlapping files.

---

## 3. Domain auto-detection

`--domain` omitted → `core.py:detect_domain`. Keyword-phrase voting, not classification.

- Each domain owns a keyword list (`_domain_keywords()`). `product`'s list is **generated
  from products.csv at load time** (192 product labels, parenthetical suffixes stripped,
  ≥4 chars, longest-first) so it can't drift from the data; falls back to a 21-item seed if
  the CSV is missing.
- Score per hit = `2.0 × word_count_of_phrase`, so `"time series"` (2 words) outscores
  `"chart"` (1 word). `product` hits score `1.0 × word_count` — half weight, because its
  list is huge and would otherwise swamp everything.
- A literal hex in the query (`#[0-9a-f]{3,8}`) adds `+2.0` to `color`.
- Ties break on a **fixed priority order**, never dict order:
  `ux, product, style, color, typography, google-fonts, chart, landing, icons, gsap, react, web`
- All-zero scores → default `style`.
- `--json` surfaces `auto_detected: true` and `runner_up_domain`, so a misroute is visible
  rather than silent.

Known overlap to watch: `typography` (pairings) vs `google-fonts` (single families) both
claim font vocabulary. Pass `--domain` explicitly when results look off.

### Query rewriting (`_rewrite_query_for_domain`)

Some terms are pure *routing* vocabulary — they got you to the right domain but don't exist
in that domain's index, so they only add noise. These are dropped or remapped
(`_DOMAIN_QUERY_REWRITES`), but **only if the term isn't in the index vocabulary**:

- `color`: drop `color palette hex rgb token semantic destructive muted foreground`
- `style`: drop `css implementation variable checklist tailwind`
- `icons`: drop `lucide symbol glyph pictogram`
- `gsap`: `gsap→animation`, `scrolltrigger→scroll`; drop `quickto`, `flip plugin`, `splittext`
- `ux`: `ux|usability|wcag → accessibility`
- `landing`: `testimonial→testimonials`
- `google-fonts`: `typography→font`
- `react`: `nextjs→react`, `usecallback→memoization`, `useeffect→effects`
- `web`: `aria→accessibility`, `outline→focus`, `autocomplete→input`; drop `semantic`, `preconnect`

Rewrites are additive (appended, sorted, deduped) and reported in `diagnostics.query_rewrites`.

---

## 4. Abstention — the part worth copying

A retrieval skill that always answers is worse than one that says nothing. Three gates
(`_search_csv_detailed`); tripping any one returns **zero results**, not a weak result:

```
abstain = top_score <= min_score
       or token_coverage < min_coverage
       or (min_margin > 0 and top_score - runner_up < min_margin)
```

`token_coverage` = fraction of query tokens present in the index vocabulary — evidence
first, score second.

Per-domain floors (`_DOMAIN_SCORE_FLOORS`, calibration version `2026-08-12-v1`) —
corpus-specific because document lengths differ wildly:

| Domain | min_score | min_coverage |
|---|---|---|
| `product` | 6.0 | 0.0 |
| `icons` | 5.8 | 0.0 |
| `style` | 4.3 | 0.0 |
| `landing` | 4.0 | **0.5** |
| `react` | 3.3 | 0.0 |
| all others | 0.0 | 0.0 |
| stacks | 3.6 | 1/3 |

On zero results the tool **suggests instead of guessing**:
- `_suggest_terms` — nearest index vocabulary by `difflib` ratio ≥ 0.72, ranked by
  similarity then document frequency, and *filtered to terms that would themselves clear
  the threshold* (so a suggestion can't dead-end).
- `_suggest_identities` (landing) — suggests whole `Pattern ID` / `Pattern Name` / alias
  strings, since those bypass scoring via the exact-identity path below.

`search.py` renders the empty case with explicit anti-hallucination wording: *"No matches.
This is not a match with an empty value — the query did not hit the database."*

### Exact-identity bypass

Thresholds block vague queries but would also block precise ones with low IDF. Four escape
hatches skip BM25 entirely and return one row with `reason: exact-identity`:

1. **Style identity** — query equals a `Style ID` / `Style Category` / alias. Also a
   *contained* form: if a style's identity tokens are a subset of the query tokens, at least
   one token is ≥4 chars, and exactly one style wins on (distinctive tokens, token count),
   that row is returned. Runs **before** domain detection when `--domain` is omitted.
2. **Landing identity** — exact match on `Pattern ID` / `Pattern Name` / alias.
3. **Stack API identifier** — single whitespace-free token ≥6 chars appearing, word-bounded
   and case-insensitively, in exactly one row's Guideline/Description/Do/Don't/Code fields.
   This is what makes `search.py "useSyncExternalStore" --stack react` work.
4. **Legacy successor** — on a legacy-only stack, a "brand new app" query prefers the row
   that names the successor.

### Deprecation routing (`style`)

`style` search filters to `Status == "active"` (49 supplemental/deprecated rows excluded,
cached under variant `active-only`). If the query names a deprecated style, `_style_search_destination`:

- `Parent Style ID` set → silently return the parent;
- `Replacement Domain == "style"` → return the replacement row;
- other `Replacement Domain` → return **zero results plus a `redirect`**, and `search.py`
  prints a domain-transfer message ("this legacy style label is now modeled in the
  `landing` domain as `…`; search that domain instead of treating a page composition as a
  visual style").

### Hard exclusion

`icons` + query containing `lucide` → forced empty, `reason: unsupported-library`. The
catalog is Phosphor; returning a Phosphor row for a Lucide query would produce a wrong import.

---

## 5. Stack retrieval — one generation per answer

Stack CSVs mix framework generations, tagged per row by `Status` (`active` / `deprecated`)
and `Applies To`. Returning a Svelte 4 row next to a Svelte 5 row would be actively harmful,
so `_stack_row_filter` picks **one coherent generation** before scoring.

Current majors (`WEB_STACK_CURRENT_MAJORS` / `STACK_CURRENT_VERSIONS`) are pinned in code:
react 19, nextjs 16, vue 3, svelte 5, astro 7, angular 22, tailwind 4, nuxtjs 4, nuxt-ui 4.
`STACK_CURRENT_APPLICABILITY` holds the display strings (`react 19.2.x`, `shadcn cli 4`, …).

`_stack_query_requests_legacy(query, stack)` decides the generation:

- Stack in `LEGACY_ONLY_STACKS` (`uwp`) → always legacy.
- Parse explicit versions from the query (`react 18`, `next@15`, `v3`, and three.js `r150`).
  All requested versions below the pinned current → legacy. Any at-or-above current **while
  the query also shows migration intent** (`migrate|upgrade|replace|instead|modern|current`)
  → current.
- Bare migration intent with no version → current.
- Bare `legacy` / `deprecated` → legacy.

Then:

| Situation | Filter | Variant | Threshold |
|---|---|---|---|
| legacy requested, deprecated rows exist | `Status == deprecated` | `legacy-only` | **none** (0.0) |
| legacy requested, no deprecated rows | match nothing | `legacy-unavailable` | — |
| otherwise, active rows exist | `Status == active` | `current-only` | 3.6 / cov 1/3 |
| fallback | `Status != deprecated` | `non-legacy` | 3.6 / cov 1/3 |

`legacy-only` drops the threshold to zero: if you explicitly ask about the old generation,
best-effort beats abstention.

**shadcn extra axis** — routes on the primitive base parsed from `Applies To: base=radix|base|aria`:
`"base ui"` → `base`, `"react aria"` → `aria`, `"radix"` or `"aschild"` → `radix`.
Unstated → no base filter. The variant string becomes `current-only;base=radix`.

The filter variant is part of the BM25 cache key, so filtered corpora get their own index.

---

## 6. `--design-system` — the aggregation pipeline

`design_system.py:DesignSystemGenerator.generate()`. Fixed 5-step order; each step's output
narrows the next. This is the retrieval split at the *composition* level: 6 focused searches
beat 1 broad one.

```
1. search(query, "product", max=1)            → category  (the join key)
2. _apply_reasoning(category, query)          → ui-reasoning.csv row for that category
                                                 + parse_decision_rules + apply_decision_rules(query)
                                                 → pattern, style_priority, color_mood,
                                                   typography_mood, key_effects, anti_patterns,
                                                   constraints, preferred_mode, severity
3. _multi_domain_search(...)                  → 4 domain searches, each with an
                                                 enriched, domain-specific query
4. _select_best_match / mode resolution       → one row per domain
5. assemble                                   → design system dict
```

Per-domain result budget (`SEARCH_CONFIG`) — asymmetric on purpose:

```
product 1 · style 3 · color 5 · landing 2 · typography 2
```

`color` gets 5 because step 4 needs headroom to find the row whose `Product Type` equals the
step-1 category, and then a fallback that agrees with the resolved light/dark mode.

**Step 3 query construction.** `resolved_query = query + category + constraints`
(constraints are the `constraint:` tokens fired in step 2, dashes → spaces). Then per domain:

- `style` → `resolved_query + first 2 style_priority entries`
- `color` → `color_mood + resolved_query`
- `typography` → `typography_mood + resolved_query`
- `landing` → **`pattern` alone** if the pattern name is a known landing identity, else
  `pattern + resolved_query`. Mixing the product prompt into an exact pattern name pushes
  token coverage below the 0.5 landing floor and causes abstention on a row that was named
  outright.

**Step 4 authority order.** `_select_best_match` resolves `style_priority` names through the
style lookup **first** and returns that row directly if it's active — canonical reasoning
outranks lexical BM25, so a platform variant in the top-3 can't displace the explicit family
recommendation. Only if no priority name resolves does it fall back to keyword scoring
(exact category-token match +10, keyword-column overlap +3, substring +1).

Color mode is resolved **before** the palette is chosen, so style, palette and anti-patterns
can't disagree:

1. Mode = `reasoning.preferred_mode` (a fired `mode:` action), else `_resolve_color_mode(query, best_style)`,
   which returns dark if the query contains an explicit dark phrase **or** the chosen style is
   dark-first. Dark-first is decided by `styles.csv:Preferred Mode`, then by
   `Light Mode ✓ == not-recommended && Dark Mode ✓ == supported`, then by 9 prose markers
   (`dark mode primary`, `dark primary`, `dark-only`, `dark only`, `dark preferred`,
   `dark focused`, `dark-first`, `dark rich`, `light mode only as exception`).
2. `_select_palette_for_mode` prefers the palette whose `Product Type` **exactly equals the
   step-1 category** — the join beats BM25 rank. If that row is light and dark was resolved,
   it's converted by `_derive_dark_palette`. With no category row, the top *dark* hit wins if
   dark was resolved; otherwise the top hit.
3. `_derive_dark_palette` keeps the brand tokens (Primary/Secondary/Accent + their on-colors)
   and replaces only the surfaces: background `#0F172A`, foreground `#F8FAFC`, card `#111827`,
   card-fg `#F8FAFC`, muted `#1E293B`, muted-fg `#CBD5E1`, border `#334155`. `Ring` is the first
   of `Ring → Accent → Primary → #60A5FA` that clears a **3:1 contrast ratio** against the new
   background. Result is tagged `_mode_derivation: derived-dark` and surfaces as
   `source_derivations.color_mode`.
4. `_filter_anti_patterns_for_mode` drops any `+`-separated anti-pattern clause mentioning
   dark mode/theme once dark is resolved.

Light mode deliberately keeps "top hit wins" so queries that never mention a mode behave
exactly as before.

**Provenance.** The output dict carries `source_identities` (which product / reasoning /
style / color / typography / landing row each field came from), `source_derivations.color_mode`,
`activated_rules` (condition → actions audit trail), `reasoning_default` (true when no
reasoning row matched and built-in defaults were used), and `severity`. Every value is
traceable to a row or explicitly flagged as a default.

---

## 7. Design dials

Three optional 1–10 sliders that **bias the existing search** rather than replacing it.
Each buckets into low(1–3)/mid(4–7)/high(8–10) (`DIAL_TIERS`). Unset = no behavior change.

| Dial | Mechanism |
|---|---|
| `--variance` | Prepends style keywords to `style_priority` before step 3. Low → `Minimalism, Exaggerated Minimalism, centered, symmetric, grid-based`. Mid → `modern, structured, balanced`. High → `Brutalism, Bento Grids, asymmetric, experimental`. |
| `--motion` | Extra `search(query + tier, "gsap", 5)`, then filters to rows whose `Intensity Tier` equals the resolved tier (Subtle/Standard/Complex), falling back to the top hit. Attaches the full preset incl. `GSAP Snippet`. |
| `--density` | Pure override, no search. Replaces the `--space-*` scale: spacious `4/8/24/32/48/64/96`, standard `4/8/16/24/32/48/64`, dense `2/4/8/12/16/24/32` px. |

---

## 8. Decision-rule grammar (`reasoning_contract.py`)

`ui-reasoning.csv:Decision_Rules` is data that mutates the pipeline, so it's a **closed,
non-executable grammar** with a validating parser. Worth copying wholesale.

```
rules   := { condition: [action, ...], ... }     # JSON object, duplicate keys rejected
condition := "must_have" | one of 35 "if_*" signals
action  := "style:<kebab-token>" | "constraint:<kebab-token>"
         | "pattern:<non-empty name>" | "mode:dark" | "mode:light"
```

- `parse_decision_rules` raises on unknown conditions, unknown action prefixes, empty action
  arrays, duplicate actions, duplicate keys, malformed tokens
  (`^[a-z0-9]+(-[a-z0-9]+)*$` for `style`/`constraint`), or a `mode` other than dark/light.
- Each `if_*` condition maps to a literal keyword tuple, pre-compiled to word-boundary
  regexes and matched case-folded against the query. Examples: `if_data_heavy` ←
  `data heavy | data-heavy | analytics | large dataset`; `if_trust_needed` ←
  `trust | secure | verified | authority`; `if_luxury` ← `luxury | premium | high-end`.
- `must_have` always fires.
- `apply_decision_rules` returns `{activated, style_ids, constraints, pattern, mode}`.
  Deduped, order-preserving; `pattern` and `mode` are last-write-wins.
- Nothing is `eval`'d or imported from the data. Worst case for a malformed row is a raised
  `ValueError`, never execution.

---

## 9. Persistence — master + page overrides

`--persist` writes a two-level hierarchy (`persist_design_system`, `format_master_md`,
`format_page_override_md`):

```
<output-dir>/design-system/<project-slug>/
  MASTER.md              # global source of truth: tokens, palette, type scale, spacing,
                         # style rules, anti-patterns, decision-rule audit trail
  pages/<page>.md        # per-page overrides; these win over MASTER.md
```

Retrieval contract: read `pages/<page>.md` first; if absent, use `MASTER.md` exclusively.

Safety behaviors worth keeping:
- Existing `MASTER.md` is **skipped, not overwritten** (`status: skipped_exists`) unless
  `--force`. Prior human decisions don't silently evaporate.
- `--output-dir` defaults to CWD, which for a skill is wrong — the SKILL.md instructs
  always passing it explicitly at the project root.
- Writes go through a tempfile + `fsync`, then publish atomically. `--force` uses
  `os.replace`; the default path uses `os.link`, which only succeeds when the destination is
  absent — so a concurrent second writer loses with `FileExistsError` instead of clobbering.
- `safe_slug()` reduces project/page names to `[a-z0-9_-]`, collapsing `/`, `\` and `.`.
  Path traversal via a project name like `../../etc` is therefore impossible; the slug can
  never leave its parent directory.
- `_generate_intelligent_overrides` / `_detect_page_type` infer page-type-specific override
  content (dashboard vs. marketing vs. auth, …) from the page name and style results.

Output formats: `-f ascii` (default, ANSI-colored 90-col box, hex swatches rendered via
`hex_to_ansi`), `-f markdown`, `--json` (raw design-system dict + persistence status).
