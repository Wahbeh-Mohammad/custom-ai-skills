# Impeccable command vocabulary — a taxonomy of design operations

> **Apache-2.0 change notice.** Derived from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
> v4.1.0 at commit `cb56ed6c19a07329a9fa0cd4e657bee040156593` — **Apache-2.0,
> Copyright 2025 Paul Bakaus** (`licenses/impeccable-APACHE-2.0.txt`;
> upstream NOTICE at `licenses/impeccable-NOTICE.md`).
>
> **Pinned:** 23 verbs, correct at the commit above. Upstream added a 24th (`generate`) on
> 2026-09-15; see `MANIFEST.md` § Pinned provenance.
>
> **This file has been modified from the original.** The 23 verbs and their categories are
> verbatim; they are presented here as a routing vocabulary rather than as commands to run, and
> impeccable's per-verb reference files were not extracted.
>
> Upstream paths named below are impeccable's own and resolve in its tree, not in this skill.
> Full per-file record: `MANIFEST.md` §§ 13–16; every deviation: § 17.

Sources: `skill/SKILL.src.md` and `skill/reference/routing.md`.
This is a **routing vocabulary**, not a set of commands to reimplement: 23 verbs in 6 categories
that name what a design request is actually asking for.

---

## The verb table (verbatim)

> **Path warning.** The `Upstream reference` column holds paths into the **upstream impeccable
> tree**, not this skill. The 34 command reference bodies were not extracted (see
> `MANIFEST.md` § 15) — `reference/audit.md` below is impeccable's file and does not exist
> here. This skill's own audit flow is `reference/runbook-audit.md`.

| Command | Category | Description | Upstream reference |
|---|---|---|---|
| `craft [feature]` | Build | Deprecated alias for an ordinary new-work request | `reference/craft.md` |
| `shape [feature]` | Build | Plan UX/UI before writing code | `reference/shape.md` |
| `init` | Build | Capture durable product context in PRODUCT.md | `reference/init.md` |
| `document` | Build | Generate DESIGN.md from existing project code | `reference/document.md` |
| `extract [target]` | Build | Pull reusable tokens and components into design system | `reference/extract.md` |
| `critique [target]` | Evaluate | UX design review with heuristic scoring | `reference/critique.md` |
| `audit [target]` | Evaluate | Technical quality checks (a11y, perf, responsive) | `reference/audit.md` · native: `reference/audit.native.md` |
| `polish [target]` | Refine | Final quality pass before shipping | `reference/polish.md` |
| `bolder [target]` | Refine | Amplify safe or bland designs | `reference/bolder.md` |
| `quieter [target]` | Refine | Tone down aggressive or overstimulating designs | `reference/quieter.md` |
| `distill [target]` | Refine | Strip to essence, remove complexity | `reference/distill.md` |
| `harden [target]` | Refine | Production-ready: errors, i18n, edge cases | `reference/harden.md` |
| `onboard [target]` | Refine | Design first-run flows, empty states, activation | `reference/onboard.md` |
| `animate [target]` | Enhance | Add purposeful animations and motion | `reference/animate.md` |
| `colorize [target]` | Enhance | Add strategic color to monochromatic UIs | `reference/colorize.md` |
| `typeset [target]` | Enhance | Improve typography hierarchy and fonts | `reference/typeset.md` |
| `layout [target]` | Enhance | Fix spacing, rhythm, and visual hierarchy | `reference/layout.md` |
| `delight [target]` | Enhance | Add personality and memorable touches | `reference/delight.md` |
| `overdrive [target]` | Enhance | Push past conventional limits | `reference/overdrive.md` |
| `clarify [target]` | Fix | Improve UX copy, labels, and error messages | `reference/clarify.md` |
| `adapt [target]` | Fix | Adapt for different devices and screen sizes | `reference/adapt.md` · native: `reference/adapt.native.md` |
| `optimize [target]` | Fix | Diagnose and fix UI performance | `reference/optimize.md` |
| `live` | Iterate | Visual variant mode: pick elements in the browser, generate alternatives | `reference/live.md` |

**Six categories:** Build (5) · Evaluate (2) · Refine (6) · Enhance (6) · Fix (3) · Iterate (1).

The axis that matters for routing is **Refine vs Enhance vs Fix**: Refine changes the *amount* of
a quality already present (bolder/quieter/distill are one dial in three directions); Enhance adds
a dimension the surface does not yet have; Fix repairs a defect against a known standard.
`bolder` / `quieter` are opposites on one axis; `distill` and `overdrive` are the endpoints of a
second; `polish` and `harden` are the same pass aimed at craft and at resilience respectively.

### Aliases and deprecations

- `teach` aliases `init`.
- `craft` is a **deprecated** alias for ordinary new-work and adds nothing.
- `shape` owns task discovery, then enters new-work only for visual-world and surface-concept
  decisions.
- `bolder` / `quieter` are **not** the direction-round registers. "A user saying 'bolder' or
  'safer' while a direction round is open means these registers, never the bolder or harden
  commands."

---

## Routing rules (verbatim)

- **No argument:** read `routing.md` and present its context-aware menu; never auto-run a command.
- **Explicit or clearly implied request to run a command:** load its reference (native variant on
  native platforms) and follow it. Ask once if two commands fit.
- **Workflow or command-selection question:** read *Workflow questions* — give advice without
  executing commands.
- **Otherwise:** treat the request as general design work. Missing PRODUCT.md routes a new surface
  or replacement world through `init`, then new-work; a narrow refinement of existing code
  proceeds on the incumbent implementation, offering `init` afterward rather than blocking on it.

### The no-argument menu is signal-driven, not static

Read `impeccable signals` (JSON), then lead with the **2–3 highest-value next commands**, each
with a one-line reason, followed by the full menu grouped by category. The mapping, verbatim:

| Signal | Route to |
|---|---|
| `setup.hasDesign` false while `setup.hasCode` true | `document` (capture the visual system) |
| `critique.latest` is `null`, on a set-up project with a real surface | `critique <surface>` |
| `critique.latest` with a low `score` or non-zero `p0` / `p1` | `polish` (it reads that snapshot as its backlog) |
| `git.changedFiles` pointing at one surface | scope `audit` or `polish` to those files, naming them |
| `devServer.running` true | `live` is available; if false, don't lead with it |
| `setup.platform` is `ios` / `android` / `adaptive` | never lead with `live` or `detect` — both are web-only |
| otherwise | group by intent (build new / improve what's there / iterate visually) |

Plus: when `scan.targets` is non-empty on a web project, run the detector once and fold the hits
in — "many quality / contrast hits → `audit` or `polish`; a specific slop family → the matching
command (gradient text or eyebrows → `quieter` / `typeset`, flat or gray palette → `colorize`)".
Never block the suggestion on it. **Never auto-run a command; the recommendation is a suggestion
the user confirms.**

---

## The mode axis — orthogonal to the verb

The verb names the operation; the **mode** names what success looks like on the surface it acts
on. Chosen from the requested surface, not the product, and persisted only in that surface's brief.

| Mode | The visitor… | Surfaces | What outranks what |
|---|---|---|---|
| **Persuade** | decides and acts; design is the product | landing pages, marketing, campaigns, pricing | earn attention and action; follow the committed world, not category habit |
| **Operate** | completes a task | app UI, dashboards, editors, admin, settings, tools | scanability, consistency, native expectations, and the real usage scene outrank expression; brand lives in precise details |
| **Read** | understands something | docs, articles, guides, help, changelogs | structure for comprehension first, then make the reading worth staying in |
| **Experience** | is inside the work itself | portfolios, galleries, showcases | the artifact leads from the first viewport; the interface recedes |

"A tool's landing page is still Persuade; a fashion house's documentation is still Read; a docs
index is Read, not Persuade."

---

## Meta-verbs (not design operations)

Kept because they are part of the routing surface, not because the operations are portable.

| Verb | Does |
|---|---|
| `impeccable context` | Session boot: resolves PRODUCT.md / DESIGN.md / the matching surface brief / native-platform guidance, and prints directives. Run once per session; do not rerun. |
| `impeccable signals` | Prints the JSON the no-argument menu reasons over. |
| `impeccable detect` | Runs the deterministic rule engine over local files. No network, no LLM. Web-only. |
| `impeccable doctor` | Reports and repairs drift between the project's artifacts and what the installed version reads. `CONTEXT_STALE` in boot output is the cheap subset. |
| `impeccable hooks <on\|off\|status\|ignore-rule\|ignore-file\|ignore-value\|reset>` | Manages the design detector hook for the project. |
| `impeccable pin <pin\|unpin> <command>` | Creates or removes a standalone `/<command>` shortcut. |

Two standing rules attach here and are worth lifting on their own:

> **Never repair drift as a side effect of a design task.** A `CONTEXT_STALE` finding is reported,
> not acted on, unless the user asks. The one exception is a finding marked `auto`, which the next
> write to that file performs anyway.

> Verify in bounded passes, not a loop, and the ceiling covers the whole cycle: screenshots,
> defect scans, micro-edits, and rebuilds alike. Build fully, inspect once with a batched round
> (desktop and mobile together on the web; the shipped device classes on a native platform), fix
> everything it shows in one batch, confirm with at most one more round, and stop polishing.
> Open-ended self-QA burns the user's money doing worse what the finish handoffs do better.
