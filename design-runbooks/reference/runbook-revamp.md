# Runbook 1 — REVAMP

Existing code, and the user wants it changed. This runbook edits files.

---

## Step 0 — The preservation contract

**Confirm this with the user before any edit.** Not after the inventory, not "as we go" —
before the first file is touched.

| | |
|---|---|
| **ALWAYS KEEP** | copy, information architecture, routes, functional behaviour |
| **DEFAULT KEEP** unless told otherwise | brand colours, logo, product naming |
| **REPLACE** | layout structure, visual treatment, spacing, type, motion |

**If the user wants copy or IA changed too, that is a different job.** Say so and get explicit
confirmation before taking it on. Silently rewriting headlines under a visual brief is the
failure this contract exists to prevent.

The DEFAULT KEEP row is a default, not a ban. The user can release brand colours, logo or
naming — but they have to say so, and you record it.

### Logo status — record one of three

Read the code for the logo before asking, and state which case holds in the same confirmation
message:

| Status | Means | The SVG step does |
|---|---|---|
| `kept` | a logo exists and the user has not released it | derives only the missing kit pieces from it, never redraws it (`svg-assets.md` § 4) |
| `released` | the user said the logo may change | runs the mark concepts at step 2 (`svg-assets.md` § 3) |
| `none` | no logo — the name is set as type | asks, **in this same message**, whether to draw mark concepts at step 2. Silence is no |

`none` costs no extra round trip: the opt-in rides on the confirmation the contract already
needs.

### Redesign vs refinement — pick one, say which

They are **asymmetric** and mixing them is the most common way a revamp goes bad.

- **Redesign** preserves product truth, content, function and constraints, and **replaces**
  DESIGN.md. The old look is **evidence and anti-reference** — it tells you what was there and
  what not to return to.
- **Refinement** preserves the incumbent identity and everything outside scope. DESIGN.md is
  amended, not replaced.

**Never split the difference into polish on the discarded look.** If you are redesigning, the
old look does not get a vote on the new one.

---

## Step 1 — Inventory the surfaces, and write REVAMP.md

List **every route and surface in scope**. For each: the file path, what the surface is, and
its visitor mode (Persuade / Operate / Read / Experience — chosen from the surface, never from
the product).

Note while inventorying:

- an existing `DESIGN.md` — read it first, it is the incumbent authority;
- an existing `/* … macrostructure: <name> … */` CSS stamp — the diversification rule reads it;
- an existing `PRODUCT.md` — read it, **do not write to it**, except the two confirmed appends
  `contract.md` § 1 allows (an adopted mark, owed assets). This runbook never creates one or edits
  anything else in it;
- a deprecated `## Register` section in PRODUCT.md — report it, delete only if the user agrees;
- any drift between DESIGN.md and the code. **Report it. Do not repair it as a side effect.**
- the assets — the logo and its kit (favicon, touch icon, og-card, manifest), and every image
  slot with no real asset behind it. Imageless slots go in REVAMP.md `## Notes`. Once the user
  confirms the plan, the owed assets are appended to PRODUCT.md § Evidence on Hand when a
  PRODUCT.md exists, and named in the final report either way (`svg-assets.md` § 0).

*Visual authority is evidence, not a filename.* No DESIGN.md does not make this greenfield —
the existing code is the incumbent system whether or not anyone wrote it down.

### Then write the plan — before any source file is edited

`PROJECT_ROOT/REVAMP.md`. One file, plain markdown, no schema beyond the stamp. It is the
thing the user confirms against, the working record during the run, and the resume point if
the run stops early.

```markdown
# Revamp plan

<!-- design-runbooks:revamp-plan 1 -->

## Mode

Redesign
<!-- Redesign replaces DESIGN.md and treats the old look as anti-reference.
     Refinement amends DESIGN.md and preserves the incumbent identity. Pick one. -->

## Preservation contract

- **Always keep:** copy, information architecture, routes, functional behaviour
- **Default keep:** brand colours, logo, product naming — *released by the user: none*
- **Replace:** layout structure, visual treatment, spacing, type, motion
- **Logo:** kept
<!-- kept · released · none (mark concepts: opted in | declined) -->


## Direction

- Macrostructure: *[pending step 2]*
- Nav / footer archetype: *[pending step 2]*
- DESIGN.md: *[created | replaced | amended]*

## Surfaces

| # | Route | File | Visitor mode | Batch | Status |
|---|---|---|---|---|---|
| 1 | *(shared chrome)* | `src/layouts/Base.astro` | — | 1 | pending |
| 2 | `/` | `src/pages/index.astro` | Persuade | 2 | pending |
| 3 | `/pricing` | `src/pages/pricing.astro` | Persuade | 2 | pending |
| 4 | `/docs/*` | `src/pages/docs/` | Read | 3 | out of scope |

Status: `pending` · `in progress` · `done` · `out of scope`

## Batches

1. Shared chrome — nav, footer, base layout. Everything else depends on it.
2. …

## Notes

- Drift found, left unrepaired: …
- Findings deferred to the VERIFY report: …
- Imageless slots: `/` hero — placeholder, photo 4:5, `assets/placeholders/hero.svg`; …
```

**Present it. Get confirmation.** The user tells you what is in and what is out. A surface you
assumed was in scope and rewrote is not a recoverable mistake on a live codebase.

**This is where visitor mode lives.** It is per-surface and barred from both durable artifacts
(`contract.md` § 3); the plan is its home for the length of the run.

**REVAMP.md is a run artifact, not a durable one.** Three lifetimes in the project: PRODUCT.md
outlives every redesign, DESIGN.md outlives every page, REVAMP.md dies with the run. A fourth,
`history/`, lives in the skill and outlives every project (`contract.md` § 3). REVAMP.md
carries no product truth and no visual system — anything durable in it belongs in DESIGN.md
instead. On completion, say it is safe to delete; **never delete it yourself.**

---

## Step 2 — Establish ONE direction, and write it down

**One macrostructure family. One token set. For the whole site.**

Macrostructure variety applies **across projects, never across pages of one site**. A site
whose pages each have their own shape is not varied, it is incoherent.

- **DESIGN.md exists** → it *is* the direction. Inherit it. On a redesign, replace it
  wholesale, once, here. On a refinement, amend it here.
- **No DESIGN.md** → derive one direction now: read the existing code as evidence, retrieve
  candidates with `scripts/search.py "<the product in the user's words>" --design-system`,
  apply the macrostructure diversification rule against the existing stamp, and present the
  direction to the user before writing.

**Record the pick in REVAMP.md § Direction** — macrostructure, nav/footer archetype, and
whether DESIGN.md was created, replaced or amended. That is the last thing written before any
source file is edited.

**The image-led gate applies to the pick.** 05 Workbench, 08 Photographic, 16 Feature Stack
and 18 Portfolio Grid need the imagery the inventory found, or the user's word that it is
coming (`svg-assets.md` § 1).

**Write DESIGN.md before touching any page.** Per `contract.md` § 2 — including the neutral
tinting transform, the macrostructure family recorded in `## Layout`, exact section headers in
fixed order, and frontmatter as the normative source.

**Then the mark, if step 0 opened it** — logo `released`, or `none` with the user opted in. Per
`svg-assets.md` § 3: two or three concepts in `mark-concepts.html`, one question, wait. A pick
lands in DESIGN.md § Components › Mark and, when a PRODUCT.md exists, in its § Brand
Commitments (`contract.md` § 1). Silence is no mark. A `kept` logo skips this entirely.

This is the step that makes the rest mechanical. **Never re-derive direction mid-run.** If
building reveals the direction is wrong, stop, change DESIGN.md deliberately, say so, and
restart the affected surfaces — do not let page 7 quietly disagree with page 2.

---

## Step 3 — Revamp surface by surface

Against DESIGN.md. For each surface, in the order REVAMP.md lists them.

**Update the surface's `Status` in REVAMP.md as you go** — `in progress` when you start it,
`done` when it is emitted. The plan is the run's state, and a stale plan is worse than none:
if the run is interrupted, the table is what tells the next session where it stopped.

For each surface:

1. Read the existing surface. Extract copy, IA, routes and behaviour — these are preserved
   verbatim.
2. Rebuild the visual layer: layout structure, spacing, type, treatment, motion.
3. Keep the macrostructure family. Per-surface variation happens inside it — a docs page and a
   pricing page are not the same composition, but they are the same *system*.
4. Nav and footer archetypes stay consistent sitewide (N# / Ft# from
   `hallmark-macrostructures.md` § Archetype name key). Gates 42 and 43 fail the AI defaults.
5. Open the stylesheet with the stamp:
   ```css
   /* <Project> · macrostructure: <name> · nav: N# · footer: Ft# · slop: pass (42–45) */
   ```
6. Hold the quality floor: body measure 65–75ch, display max 6rem, tracking floor -0.04em,
   contrast 4.5:1 / 3:1. Theme the browser surfaces — selection, caret, scrollbars, focus
   rings, underline offset, tabular numerals.
7. Stack rules for the framework in play: `scripts/search.py "<query>" --stack <name>`.
   Retrieval returns **one coherent framework generation** — don't mix generations into one
   file.
8. Picture surfaces. **Existing real images are content and stay.** Only a slot the new layout
   creates, with no asset behind it, resolves by the slot rule (`svg-assets.md` § 1) — geometry,
   a labelled placeholder (§ 2), or nothing. Add each placeholder to REVAMP.md `## Notes`.

**Run the six-axis pre-emit critique per surface** before emitting it
(`hallmark-slop-gates.md`): Philosophy · Hierarchy · Execution · Specificity · Restraint ·
Variety, 1–5. Anything **< 3 forces a revision pass**. Record the scores in the stamp.

---

## Step 4 — Batch and checkpoint

**A half-migrated codebase is worse than none.** A site where four pages use the new system
and six use the old one has two design systems and no way to tell which is intentional.

For anything beyond a handful of surfaces:

- work in batches along a **clean boundary** — a route group, a section of the site, a layout
  and everything that uses it. Never split a shared layout from its consumers across a batch
  edge. The batch column in REVAMP.md is where the boundaries are declared, before the work.
- **checkpoint after each batch**: update the `Status` column, then say which surfaces are
  done, which are untouched, and what the next batch is. Let the user stop you there.
- **if you cannot finish, stop at a clean boundary and say so explicitly** — REVAMP.md already
  says which surfaces are `done` and which are still `pending`, so point at it rather than
  reconstructing the list from memory. Stopping cleanly and reporting is a success. Running
  out of room mid-surface is not.
- shared chrome — nav, footer, layout components — migrates **first**, in its own batch,
  because every other batch depends on it.

**Resuming a stopped run:** read REVAMP.md first. The preservation contract, the direction and
the surface table are all already settled — re-confirming them wastes the user's time, and
re-deriving the direction is the failure step 2 exists to prevent. Pick up at the first
`pending` row.

Scaling the work down is the user's call, not yours. Deliver what you can complete and report
the boundary.

### After the last batch — derive the kit

Once every in-scope surface is `done`, per `svg-assets.md` § 4. Not before: the og-card depicts
the revamped hero, and a kit derived mid-run would picture a page that no longer exists.

- **Logo `kept`** → only the pieces the site lacks, built from the incumbent's own paths and
  colours. Reframed, never redrawn. A raster-only incumbent is reported, never traced.
- **A mark adopted at step 2** → the full tier: core always, extended when the product is
  installable or a lockup can be outlined.
- **No mark** → the og-card only.

Wire the `<head>` in the shared layout — the chrome batch already owns it.

---

## Step 5 — VERIFY

Run Runbook 3 (`runbook-audit.md`) across every surface you touched.

**Re-read the rules from disk.** Auditing from memory of what you just wrote is self-grading
and it passes everything.

Audit against DESIGN.md too — token drift, off-system colours, ad-hoc spacing. On a revamp
this is the highest-yield check, because the failure mode is a page that looks fine alone and
disagrees with the system.

**Any BLOCKING finding means fix and re-verify.** Do not report "done" with open BLOCKING
items. ADVISORY findings are reported, not auto-fixed.

Lint the assets too: `python3 scripts/svg_lint.py <project-root>`, with `--kept-incumbent`
when the logo was kept (`svg-assets.md` § 6).

**Final report states:** surfaces completed, surfaces untouched, what was preserved under the
contract, any drift found and left unrepaired, what is owed — every placeholder with its shot
brief, every kit piece skipped for a missing tool or a raster-only logo — and the audit's
standing limit: this is static analysis, not a substitute for looking at the rendered pages.

Reconcile REVAMP.md with reality one last time — every row `done` or `out of scope`, notes
filled in — then tell the user it is a run artifact and safe to delete. **Do not delete it
yourself**, and do not leave a half-true plan on disk: a file claiming four surfaces are done
when three are is worse than no file.

---

## Step 6 — REVISE

**VERIFY is not the end of the run.** Hand to Runbook 4 (`runbook-revise.md`) once it reports
clean, carrying the direction, the surface list and the preservation contract you already
settled — do not re-derive them and do not re-confirm them.

The user sees the revamp for the first time here. A run that emits, verifies and reports "done"
has taken the one round of judgment that matters and thrown it away.

**The preservation contract still binds inside the loop.** Copy, information architecture,
routes and behaviour are tier 3 there and stay refused — releasing them is a different job,
agreed separately, exactly as step 0 says.

If you stopped at a clean batch boundary with surfaces still `pending`, say so and hand to
Runbook 4 only for what is done, or not at all. Offering variations on a half-migrated site
invites a direction change that the untouched surfaces will not carry.
