---
name: design-runbooks
description: Use when designing, redesigning, auditing, or revising a web UI — landing pages, marketing sites, app surfaces, dashboards — including when a site is already built and the user wants a variation on it ("same design, different fonts", "try another palette", "change the fonts on this site"). Routes to one of four runbooks (revamp existing code, create a new surface, audit read-only, revise a built design) and holds every visual decision to a shared PRODUCT.md / DESIGN.md contract, a catalogue of 21 macrostructures, 192 product-type palettes, 74 type pairings, and a merged deterministic rule set. Draws the SVG brand kit — mark, favicon, og-card — and labelled placeholders for imagery the user has not supplied. Learns the user's taste across runs through a confirmed, skill-local history.
---

# Web UI design

Four runbooks over one shared contract. Route first, load one runbook, never re-derive
direction mid-run. Runbooks 1 and 2 then hand to 3 to verify and 4 to revise — that sequence is
the run, not a second route.

## Route

**Step 1 — does `DESIGN.md` exist at the project root?**

- **Yes** → every runbook **inherits from it**. Do not invent direction. Read it before
  anything else. A visual decision that contradicts it is drift, and drift is reported, not
  silently applied.
- **No** → only Runbook 2 (CREATE) may create one.

*Visual authority is evidence, not a filename.* A missing DESIGN.md alone does not make a
project greenfield — existing code is authority too.

**Step 2 — pick the runbook.**

| Situation | Runbook | Edits source? |
|---|---|---|
| Existing code, user wants it changed | **1 · REVAMP** → `reference/runbook-revamp.md` | yes, after REVAMP.md |
| No existing UI, or a genuinely new surface | **2 · CREATE** → `reference/runbook-create.md` | yes |
| User wants findings, not edits | **3 · AUDIT** → `reference/runbook-audit.md` | **no** |
| Built site with a recorded direction, user wants a variation on it | **4 · REVISE** → `reference/runbook-revise.md` | yes |

**Ambiguous — ask once.** "Improve my landing page", "make this better", "look at this" do not
route. One runbook edits files and one does not; guessing between revamp and audit is not a
recoverable mistake. Ask, in one message, and wait.

A new surface inside an established site is **CREATE for the surface, inheriting DESIGN.md** —
not a revamp, and not a new identity exercise.

**REVAMP or REVISE?** REVISE varies a direction that is already recorded — a different type
pairing, another palette, tighter spacing — and needs a `DESIGN.md` to vary. REVAMP derives a
direction, from the existing code when nothing is written down. No `DESIGN.md` and no run in
flight is not revisable; it is a revamp.

Runbook 3 also runs as the **VERIFY** step at the end of Runbooks 1 and 2. It is the same
read-only pass, re-reading the rules from disk. Runbook 4 then runs as the **terminal step** of
those two, after VERIFY reports clean — a build that stops at VERIFY has skipped it.

**Step 3 — the taste gate.** Once the route is known and before the first design decision, run
the two gates in § Taste history. Skipped when the route is Runbook 3, when no rule in
`history/TASTE.md` fits this brief, or when the caller instructed `history: off`.

## Taste history

`history/` records what the user asked to change after earlier designs were delivered, and
distils it into rules. It is **skill-local** — it lives here, not in anyone's project, and it
outlives every project the skill touches. Shapes, promotion and demotion:
`history/README.md`. The procedures that write it: `reference/runbook-revise.md` § 6.

**Rules are offered, never applied.** Two gates, both before the first design decision, both
waiting for an answer.

### When the gates run

After the route resolves, before Step 2 of Runbook 1 or 2, or Step 1 of Runbook 4. **Runbook 3
skips both** — an audit makes no design decisions, so there is nothing for a rule to steer
(`runbook-audit.md` § Read-only).

Where the route itself is ambiguous and you are already asking, fold Gate 1 into that message
so it costs no extra round trip.

### Gate 1 — opt in at all

> I have N learned taste rules that fit this brief. Apply them to this project, or start clean?

**N counts the rules whose `scope` tag matches this brief**, not the whole file — the number in
this question and the list in Gate 2 must agree. **No `TASTE.md`, or no rule applies → skip both
gates and do not mention them.** Announcing an empty notebook is noise.

### Gate 2 — confirm the set

Only if they opted in. The same filtered set Gate 1 counted: a rule's `scope` tag must match
the brief, so an `editorial` rule stays out of the list on a SaaS dashboard brief. Use `all`
for a rule that applies regardless.

List them **in one message**, numbered, and **wait**:

> These apply to this brief. Say which to drop, or "all".
> 1. **Type.** Prefer a serif display face over a geometric sans on editorial briefs.
> 2. **Motion.** One authored moment; no section-entrance animations.
> 3. **Color.** Avoid near-black backgrounds below L 0.20.

**Never one rule per message.** Selection is per-rule and both directions are accepted:

| User says | Applied |
|---|---|
| `all` | 1, 2, 3 |
| `1, 3` | 1, 3 |
| `drop 2` / `omit 2` / `not 2` | 1, 3 |
| `none` / silence | nothing |
| anything unparseable | ask once, list again, wait |

**Echo the resolved set back in one line before proceeding** — `applying 1, 3 · dropped 2` — so
a misparse is caught before it shapes the design rather than after.

**Silence is not consent here.** Unanswered, no rule is applied. This is the opposite default
from the custom-theme protocol, deliberately: applying constraints the user did not ask for is
worse than skipping constraints they wanted.

### What a confirmed rule does

It steers retrieval candidates and defaults. **Say so out loud when one changes a pick** —
*"serif display per taste rule 1"* — so the user can see their own history acting on the work.
A pinned brief still wins over a taste rule, silently: an explicit instruction outranks an
inferred preference every time.

**A taste rule is never an audit finding.** It does not enter the severity system in
`merged-rules.md` § 2, and Runbook 3 does not read `history/`. A design that ignores a confirmed
rule is a conversation to have with the user, not a BLOCKING or ADVISORY item — the rules are
preferences, and the audit checks correctness and fingerprint against files on disk.

### Dropping is a signal

Record which rules were applied and which dropped in the run's history entry. A rule dropped in
two or more distinct projects earns a demotion proposal at run end
(`runbook-revise.md` § 6c). A store that only ever grows accumulates rules the user skips past
on every run.

### Off

A caller can instruct `history: off`. Then read nothing, write nothing, skip both gates, and
propose no promotion or demotion. **Benchmark and evaluation harnesses must set it** — a
benchmark that reads learned taste is no longer measuring the skill, and one that writes into
the store poisons every later run's evidence.

### The one thing that happens without asking

The log entry at run end. It is appended automatically, it is skill-local, it touches nothing
in the user's project, and the files it changed are named in the final report. Every write that
*binds* future work — a promotion, a demotion, an applied rule — is confirmed first.

## Always true

Regardless of runbook.

**The contract.** `PRODUCT.md` owns durable product truth. `DESIGN.md` owns durable visual
decisions. Strictly separate — schemas and the belongs/does-not-belong lists are in
`reference/contract.md`. Read it before writing either file.

**Plan before you edit someone's code.** Runbook 1 writes `REVAMP.md` — scope, preservation
contract, batch order, per-surface status — **before the first source edit**, and keeps it
current as it goes. It is a run artifact: disposable at the end, never deleted for the user,
and never a home for anything durable.

**One direction per site.** One macrostructure family, one token set, for the whole project.
Macrostructure variety applies **across projects, never across pages of one site**. Establish
the direction once, write it to DESIGN.md, then build against it.

**A retrieved row is a candidate, not a decision.** Every palette, pairing, style, landing
pattern and macrostructure the catalogue returns still has to clear the ban list and the
gates, and still has to be justified against the brief. Retrieval that abstains is telling you
something — *"No matches"* is not a match with an empty value.

**Never invent a palette, macrostructure, style or rule that is not in the resources.** The
one sanctioned path to something new is the custom protocol
(`reference/hallmark-custom-theme.md`), which fires on an enumerated signal list, confirms
with the user, defaults to catalogue on silence, and keeps every gate. It is a rare branch,
not a fallback.

**The restrictive source wins on *whether*; the permissive source governs *how*.** The
catalogue hands you shapes; the ban list refuses some. The refusal decides availability, the
catalogue decides execution. Precedence, severity and the six resolved conflicts are in
`reference/merged-rules.md`.

**Gate 1 is global and unscoped.** Inter, Roboto, Open Sans, Poppins, Lato and system defaults
are not display faces. Retrieval filters the seven flagged pairings out of candidate sets
before selection; they return only on named brief evidence or an incumbent DESIGN.md, and then
with the note attached.

**Truth binds claims, not demonstrations.** Never fabricate a metric, testimonial, customer,
price, benchmark or uptime figure to fill a layout (gate 46). Demonstration content may be
authored at full fidelity and labelled synthetic. Refusing a bold direction because its
demonstration data does not exist yet is timidity wearing honesty's clothes.

**Honour a pinned brief.** Explicit aesthetics, eras, materials, fonts and palettes the user
named are binding even when they collide with a saturated-pattern warning. Redirecting a clear
brief toward your own taste is failure.

**Direction rationale never reaches the browser.** Not in HTML or framework comments, hidden
DOM, `<template>`, `data-*`, rendered output, serialized props, RSC payloads, client bundles,
metadata, JSON-LD, a11y-only text, or files served beside the artifact. The CSS macrostructure
stamp is the one exception and carries names only.

**Draw only what the user has not supplied.** A supplied logo, photograph or screenshot is
evidence, never redrawn. A missing one resolves by the slot rule — exact geometry, a labelled
placeholder, or nothing — never a drawn picture and never a stand-in customer logo
(`reference/svg-assets.md`).

**Report, don't repair, drift.** A stale or self-contradicting artifact is a finding. Never
reconcile it as a side effect of a design task.

**Never auto-run.** A recommendation is a suggestion the user confirms.

## Out of scope — say so and stop

- **Backend** — data models, APIs, auth logic, persistence.
- **State management** — store architecture, caching, data flow.
- **Single-component tweaks with no design question** — a padding change, a copy string, a
  prop rename. Do it if asked; don't route it through a runbook. A change to the *system* —
  the spacing scale, the type pairing, the palette — is a design question and belongs in
  Runbook 4.
- **Copywriting as the primary ask.** Copy is preserved and respected by these runbooks, never
  authored as the deliverable. Voice guidance exists in
  `guidelines-and-review.md` § Content & Copy for text you are already touching.
- **Native platforms** — iOS, Android, React Native, Flutter, Compose. `## Platform` is `web`.

## Resources

**Contract and policy** — read these first.

| File | Holds |
|---|---|
| `reference/contract.md` | PRODUCT.md + DESIGN.md schemas, the REVAMP.md run artifact, neutral-tinting transform, the five mechanisms that hold the split |
| `reference/merged-rules.md` | Precedence, severity (BLOCKING / ADVISORY), the six resolved conflicts, de-duplication map, audit read order |
| `history/README.md` | The taste store — file shapes, the promotion and demotion rules, how to edit or wipe it |
| `history/TASTE.md` | The distilled rules the boot gate offers. Read at § Route step 3; written only on a confirmed promotion |

**Runbooks** — load exactly one to route.

`reference/runbook-revamp.md` · `reference/runbook-create.md` · `reference/runbook-audit.md` ·
`reference/runbook-revise.md`

Runbook 4 is the one exception to "exactly one": Runbooks 1 and 2 hand to it after VERIFY, and
it may be routed to directly on a built site. Runbook 3 stays read-only and never hands to it.

**Rules** — read from disk at audit time, never from memory.

| File | Owns |
|---|---|
| `guidelines-and-review.md` | Correctness — a11y, focus, forms, animation, perf, i18n, hydration, copy |
| `reference/hallmark-slop-gates.md` | Fingerprint — 29 gates + the six-axis pre-emit critique |
| `reference/impeccable-anti-patterns.md` | Reflex bans + the quality floor's numbers (measure 65–75ch, display max 6rem, tracking floor -0.04em, 4.5:1 / 3:1) |
| `data/impeccable-detector-rules.csv` | 50 deterministic rules; `Trigger / Threshold` is the checkable condition |
| `scripts/svg_lint.py` | 20 deterministic checks on the SVG kit, placeholders and `og:image` — rules in `reference/svg-assets.md` § 6 |

**Direction**

| File | Holds |
|---|---|
| `reference/hallmark-macrostructures.md` | The 21 page shapes, diversification rule, SaaS sequence, nav/footer archetype key |
| `reference/hallmark-custom-theme.md` | The custom protocol — trigger signals, tuned vs bespoke, OKLCH palette construction, font pairing |
| `reference/retrieval-split.md` | How retrieval scores, abstains and aggregates; the three dials; the decision-rule grammar |
| `reference/impeccable-commands.md` | Verb taxonomy and the four visitor modes (Persuade / Operate / Read / Experience — per surface, never per product) |
| `reference/svg-assets.md` | The SVG brand kit and picture surfaces — the slot rule, placeholders, mark concepts, the tiered kit, tooling, the asset checks |

**Data** — query through `scripts/search.py`, don't read the CSVs by hand.

`products.csv` 192 · `ui-reasoning.csv` 192 · `colors.csv` 192 palettes × 16 roles ·
`styles.csv` 88 · `typography.csv` 74 · `landing.csv` 34 · `charts.csv` 25 ·
`icons.csv` 105 (Phosphor) · `motion.csv` 17 · `stacks/` 10 files, 592 rows

```bash
python3 scripts/search.py "<brief>" --design-system      # full pipeline
python3 scripts/search.py "<query>" --domain style        # product|style|color|typography
                                                          # landing|chart|icons|gsap
python3 scripts/search.py "<query>" --stack react         # react nextjs vue svelte astro
                                                          # nuxtjs nuxt-ui angular shadcn
                                                          # html-tailwind
```

Dials bias the search, they don't replace it: `--variance` `--motion` `--density`, each 1–10.

**Known gaps.** `--domain ux|react|web|google-fonts` point at CSVs that were not extracted and
fail cleanly with `Error: File not found`. `--stack` accepts 12 native stacks that are not
here and fails the same way. Neither fabricates rows. `MANIFEST.md` records the full
extraction provenance and every deviation from upstream.

**Licensing.** This skill is assembled from four upstream projects and ships under Apache-2.0
(`LICENSE`). `NOTICE` and `THIRD-PARTY-NOTICES.md` name each upstream, its licence and what
derives from it; full licence texts are in `licenses/`.
