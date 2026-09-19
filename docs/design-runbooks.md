# design-runbooks

A web UI design skill. It designs, redesigns, audits and revises landing pages, marketing
sites, app surfaces and dashboards. Every visual decision is held to a written contract and a
fixed catalogue, not left to the model's own taste.

- **Skill folder:** [`design-runbooks/`](../design-runbooks/)
- **Entry point:** [`SKILL.md`](../design-runbooks/SKILL.md)
- **License:** Apache-2.0, with material from four upstream projects (see [Provenance and license](#provenance-and-license))

## When it triggers

Any request to design, redesign, audit or revise a web UI, including variations on a site that
is already built: "same design, different fonts", "try another palette", "change the fonts on
this site".

It declines, and says why, for:

- backend work (data models, APIs, auth, persistence)
- state management
- single-component tweaks with no design question (a padding value, a copy string). A change to
  the *system*, like the spacing scale or type pairing, is a design question and does route.
- copywriting as the main deliverable
- native platforms (iOS, Android, React Native, Flutter, Compose). Web only.

## How a run works

### 1. Route

The skill first checks for `DESIGN.md` at the project root.

- **Present:** every runbook inherits from it. Anything that contradicts it is reported as
  drift, never applied silently.
- **Absent:** only CREATE may write one. Existing code still counts as visual authority, so a
  missing `DESIGN.md` does not make a project greenfield.

Then it picks one of four runbooks:

| # | Runbook | Use when | Edits files? |
|---|---|---|---|
| 1 | **REVAMP** | Existing code, user wants it changed | Yes, after writing `REVAMP.md` |
| 2 | **CREATE** | No existing UI, or a new surface | Yes |
| 3 | **AUDIT** | User wants findings, not edits | No |
| 4 | **REVISE** | Built site with a recorded direction, user wants a variation | Yes |

Vague requests like "make this better" do not route. The skill asks once, because guessing
between an editing runbook and a read-only one is not a recoverable mistake.

A new page inside an established site is CREATE for that page, inheriting the existing
`DESIGN.md`. It is not a new identity.

### 2. Taste gate

Before the first design decision, the skill offers any learned taste rules that match the brief
and waits for the user to confirm which apply. See [Taste history](#taste-history).

### 3. Run the runbook

REVAMP and CREATE end by handing to AUDIT (as a **VERIFY** step) and then to REVISE. That chain
is one run: build, verify, offer variations.

```
REVAMP or CREATE  ──►  AUDIT as VERIFY  ──►  REVISE
                       (fix BLOCKING, re-verify)
```

## The runbooks

### 1 · REVAMP: change existing code

1. **Preservation contract**, confirmed with the user before any edit:

   | Always keep | Keep by default | Replace |
   |---|---|---|
   | copy, information architecture, routes, behaviour | brand colours, logo, product naming | layout, visual treatment, spacing, type, motion |

   Rewriting copy or IA is a different job and needs explicit sign-off.
2. **Inventory the surfaces and write `REVAMP.md`**: scope, preservation contract, batch order,
   per-surface status. Written before the first source edit and kept current. It is a run
   artifact, never a home for durable decisions.
3. **Establish one direction** and write it to `DESIGN.md`.
4. **Revamp surface by surface, in batches**, with checkpoints. Derive the SVG kit after the last batch.
5. **VERIFY**, then **REVISE**.

### 2 · CREATE: build something new

1. **Intake into `PRODUCT.md`.** Three opening questions (who uses it and for what job, what it
   makes possible, what must be preserved), plus conditional questions only where the brief
   leaves a gap.
2. **Direction.** Decide the visitor mode (Persuade, Operate, Read or Experience, per surface),
   retrieve catalogue candidates, pick a macrostructure, then present **2–3 categorically
   distinct directions**, not three colour-swaps of one layout.
3. **Write `DESIGN.md`**, then draw the mark.
4. **Build** against `DESIGN.md` and derive the brand kit.
5. **VERIFY**, then **REVISE**.

### 3 · AUDIT: findings only

Read-only. It re-reads the rules from disk every time, never from memory, and checks the code
against the merged rule set, the anti-pattern lists, `DESIGN.md` and any generated SVG assets.

Every finding carries five things: severity, `file:line`, the rule it breaks, what is wrong, and
the actual fix.

```
BLOCKING  src/components/Nav.tsx:34
  guidelines-and-review.md § Accessibility — icon-only buttons need `aria-label`
  The menu toggle renders an icon with no accessible name; screen readers announce "button".
  Fix: <button aria-label="Open menu" onClick={toggle}>  — and add aria-expanded={open}.
```

| Severity | Covers |
|---|---|
| **BLOCKING** | accessibility failures, broken keyboard paths, contrast below WCAG 2.2 AA, design-system drift, broken or unsafe SVG assets |
| **ADVISORY** | taste, era-specific style, fingerprint and anti-slop findings |

As VERIFY inside another runbook, any BLOCKING finding means fix and re-verify before reporting
done.

### 4 · REVISE: vary a built design

Opens by naming what is cheap to change (**type, colour, spacing, shape, motion**, plus **mark**
if the run drew one) so the user can see what to ask for. It sets a revert point before the
first change, then classifies the request:

| Tier | Dimension | Handling |
|---|---|---|
| 1 | type, colour, spacing, radius, motion, elevation | Applied in the loop; `DESIGN.md` tokens amended |
| 2 | macrostructure, nav/footer archetype, section order | A re-direction. Announced with its cost, waits for a yes, then rebuilds every affected surface |
| 3 | copy, IA, routes, behaviour | Refused. Out of scope for a visual loop |

Alternatives are offered, the user picks, and only what changed is re-verified. At exit it
writes the taste log entry.

## The contract

Two durable files live in the user's project, strictly separated. Their schemas are in
[`reference/contract.md`](../design-runbooks/reference/contract.md).

| File | Owns |
|---|---|
| `PRODUCT.md` | Product truth: platform, stack, users, purpose, positioning, constraints, brand commitments, evidence on hand, accessibility |
| `DESIGN.md` | Visual decisions: token frontmatter, eight fixed body sections, the macrostructure commitment |
| `REVAMP.md` | Run artifact for Runbook 1 only. Disposable, never deleted for the user, holds nothing durable |

## Rules that hold in every runbook

- **One direction per site.** One macrostructure family and one token set per project. Variety
  applies across projects, never across pages of one site.
- **Retrieved rows are candidates, not decisions.** Every palette, pairing and layout still has
  to pass the ban list and be justified against the brief.
- **No invented palettes, layouts, styles or rules.** The only path to something new is the
  custom-theme protocol, which fires on specific signals and needs user confirmation.
- **The restrictive source decides *whether*, the permissive source decides *how*.** Conflicts
  are resolved in [`reference/merged-rules.md`](../design-runbooks/reference/merged-rules.md).
- **Generic fonts are not display faces.** Inter, Roboto, Open Sans, Poppins, Lato and system
  defaults are filtered out unless the user named them or an existing `DESIGN.md` uses them.
- **No fabricated claims.** No invented metrics, testimonials, customers, prices or uptime
  figures. Demonstration content is allowed if labelled synthetic.
- **A pinned brief wins.** Fonts, palettes and eras the user named are binding.
- **Design rationale never ships to the browser.** Not in comments, hidden DOM, `data-*`,
  bundles or metadata. The CSS macrostructure stamp is the one exception and carries names only.
- **Draw only what the user has not supplied.** Supplied logos and photos are used as-is.
  Missing imagery becomes exact geometry, a labelled placeholder, or nothing.
- **Report drift, don't repair it** as a side effect of another task.
- **Never auto-run.** Recommendations wait for confirmation.

## SVG brand kit

When the user has no logo, the skill proposes two or three mark concepts, each built from a
different product fact, and derives a kit from the chosen one: mark, favicon, og-card. Imagery
the user has not supplied gets a labelled placeholder, never a drawn picture or a stand-in
customer logo. `scripts/svg_lint.py` runs 20 deterministic checks over the kit. Details:
[`reference/svg-assets.md`](../design-runbooks/reference/svg-assets.md).

## Taste history

The skill learns preferences across projects, but only with confirmation.

- **Log** (`history/log/<project>.md`): after every run, the skill appends what the user asked
  to change, or records a clean run. This is the one write that happens without asking. It is
  skill-local and never touches the user's project. **Git-ignored in this repo.**
- **Rules** (`history/TASTE.md`): a preference becomes a rule only when the same kind of request
  shows up in **two or more distinct projects** and the user confirms the promotion. A rule
  dropped in two or more projects gets a removal proposal the same way. Ships empty.
- **Gates**: at the start of a run, matching rules are listed and the user picks which to apply.
  Silence means none are applied. AUDIT never reads history, and a taste rule is never an audit
  finding.
- **`history: off`** disables reads, writes and gates for a run. Benchmark and evaluation
  harnesses must set it.

Full procedure: [`history/README.md`](../design-runbooks/history/README.md) and
[`reference/runbook-revise.md`](../design-runbooks/reference/runbook-revise.md) § 6.

## Data and scripts

Scripts need Python 3 and nothing else. Run them from the skill folder.

```bash
cd design-runbooks

# full design-system recommendation for a brief
python3 scripts/search.py "fintech dashboard" --design-system

# one domain: product, style, color, typography, landing, chart, icons, gsap
python3 scripts/search.py "editorial magazine" --domain typography

# stack-specific rules: react nextjs vue svelte astro nuxtjs nuxt-ui angular shadcn html-tailwind
python3 scripts/search.py "form validation" --stack react

# lint generated SVG assets in a project
python3 scripts/svg_lint.py <project-root> [--kept-incumbent]

# tests
python3 -m unittest scripts/test_svg_lint.py
```

`--variance`, `--motion` and `--density` (each 1–10) bias retrieval without replacing it.

| Catalogue | Rows |
|---|---|
| `products.csv`, `ui-reasoning.csv` | 192 product types each |
| `colors.csv` | 192 palettes × 16 roles |
| `styles.csv` | 88 |
| `typography.csv` | 74 pairings |
| `landing.csv` | 34 |
| `charts.csv` | 25 |
| `icons.csv` | 105 (Phosphor) |
| `motion.csv` | 17 |
| `stacks/` | 10 files, 592 rows |
| `impeccable-detector-rules.csv` | 50 deterministic rules |

**Known gaps.** `--domain ux|react|web|google-fonts` and 12 of the `--stack` values point at
CSVs that were not extracted. They fail with `Error: File not found` rather than returning
invented rows.

## File map

| Path | Holds |
|---|---|
| `SKILL.md` | Routing, taste gates, always-true rules, resource index |
| `guidelines-and-review.md` | Correctness rules: a11y, focus, forms, animation, perf, i18n, hydration, copy |
| `reference/runbook-*.md` | The four runbooks |
| `reference/contract.md` | `PRODUCT.md`, `DESIGN.md` and `REVAMP.md` schemas |
| `reference/merged-rules.md` | Precedence, severity, the six resolved conflicts, de-duplication |
| `reference/hallmark-*.md` | 21 macrostructures, 29 slop gates, custom-theme protocol |
| `reference/impeccable-*.md` | Anti-patterns, artifacts, command taxonomy, detector rules |
| `reference/retrieval-split.md` | How retrieval scores, abstains and aggregates |
| `reference/svg-assets.md` | Brand kit, slot rule, placeholders, asset checks |
| `data/` | The catalogues above |
| `scripts/` | Search, design-system pipeline, SVG linter, tests |
| `history/` | Taste store |
| `MANIFEST.md` | Extraction provenance, pinned commits, every deviation from upstream |

## Provenance and license

The skill is assembled from four upstream projects, each pinned to a commit in
[`MANIFEST.md`](../design-runbooks/MANIFEST.md). Upstream-derived files are byte-identical or
verbatim where the manifest says so. It ships under Apache-2.0, the one license compatible with
all four sources. Obligations are discharged in
[`THIRD-PARTY-NOTICES.md`](../design-runbooks/THIRD-PARTY-NOTICES.md) and
[`NOTICE`](../design-runbooks/NOTICE).

| Upstream | License | Contributes |
|---|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT | `data/`, `scripts/` search pipeline, retrieval notes |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | MIT | Macrostructures, slop gates, custom-theme protocol |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | MIT | `guidelines-and-review.md` rule text |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 | Anti-patterns, artifact schemas, command taxonomy, detector rules |

Original to this skill: `reference/runbook-revise.md`, `history/`, `scripts/svg_lint.py` and
its tests, and `reference/svg-assets.md` outside its two marked blocks (`MANIFEST.md` § 18).
