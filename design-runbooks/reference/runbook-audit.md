# Runbook 3 — AUDIT

The user wants findings, not edits. Also the **VERIFY** step at the end of Runbooks 1 and 2.

## Read-only

**This runbook never edits a file.** Not a "quick fix while I'm here", not a typo, not the
one-line contrast change that is obviously right, not a `Status` cell in `REVAMP.md`. Every
finding carries the fix as *text*; the user applies it, or asks for a revamp run.

If you find yourself reaching for Edit, you have left this runbook.

**Runbook 4 does not attach here.** REVISE is the terminal step of Runbooks 1 and 2, never of
this one. An audit produces findings, not a design, so there is nothing to offer variations on
— and offering them would turn a read-only pass into an editing one through the back door. A
user who reads the findings and wants them applied is asking for a revamp: route, and say so.

**This runbook does not read or write `history/`.** Routed to directly, the taste gate is
skipped — rules learned from revisions steer design decisions and this runbook makes none. A
taste rule is also never a finding: it is not in the read order below, it carries no severity
in `merged-rules.md` § 2, and a design that ignores one is not a defect. Running as VERIFY
inside Runbook 1, 2 or 4 changes nothing here — the gate ran at the caller's boot, and the
history entry is written by Runbook 4 at its exit.

---

## Step 1 — Re-read the rules from disk

**Do not audit from memory of what you just built.** That is self-grading and it passes
everything. The rules on disk are the rules; your recollection of them is not, and the failure
mode is silent — you confirm exactly the subset you were already thinking about.

This applies hardest when Runbook 1 or 2 just called you. Re-read anyway.

Read order (`merged-rules.md` § 5):

1. `reference/contract.md`, then `DESIGN.md` and `PRODUCT.md` if they exist, then `REVAMP.md`
   if a revamp run left one — it names the scope, the preservation contract and the visitor
   mode per surface. Read it; **do not update it**, even when running as VERIFY. Status
   belongs to the runbook doing the editing.
2. `guidelines-and-review.md` — correctness
3. `data/impeccable-detector-rules.csv` — the deterministic conditions
4. `reference/impeccable-anti-patterns.md` — ban list + the floor's numbers
5. `reference/hallmark-slop-gates.md` — fingerprint
6. `reference/svg-assets.md` §§ 1, 6 — the slot rule and the asset checks, when the project has
   SVG files or placeholder slots
7. `data/ui-reasoning.csv` — the one row matching the product type, if known
8. `reference/merged-rules.md` — precedence, severity, de-duplication

---

## Step 2 — Check against

### The merged deterministic rules

`data/impeccable-detector-rules.csv`, 50 rows. The `Trigger / Threshold` column is the
condition — check that, not the prose description. `Engines` tells you which path can raise
it; in a static pass you have `static-html` and `text`, not `browser`.

### The anti-pattern lists

`impeccable-anti-patterns.md` § Refuse and § Verify, plus `guidelines-and-review.md`
§ Anti-patterns, plus the 29 gates in `hallmark-slop-gates.md`, plus the `Anti_Patterns` value
on the matching `ui-reasoning.csv` row.

**Remember the preamble on the ban list:** these are category defaults, and the brief's own
words can earn any of them. A banned-by-default element the user explicitly asked for is not a
finding. A banned-by-default element that arrived by reflex is.

### DESIGN.md, if one exists

Token drift, off-system colours, ad-hoc spacing. This is the highest-yield check on an
existing codebase and the one no generic linter performs:

- a colour, font, radius or size in the code that is not in the frontmatter;
- prose in DESIGN.md restating a different value than the frontmatter (frontmatter is
  normative);
- a renamed canonical section — "Color Palette & Roles" instead of "Colors" silently drops
  the section from parsing;
- the macrostructure in `## Layout` disagreeing with the CSS stamp;
- surface strategy or visitor mode written into DESIGN.md or PRODUCT.md, where neither
  belongs.

**With no DESIGN.md, the four `design-system-*` rules do not fire at all.** Do not invent a
system to measure against.

### Generated assets

When the project has SVG files or placeholder slots:

```bash
python3 scripts/svg_lint.py <project-root>                   # add --kept-incumbent when
                                                             # REVAMP.md records Logo: kept
```

It reads and prints; it writes nothing, so it belongs in a read-only pass. Report its findings
in the format below as they come, with the severity it assigns (`merged-rules.md` § 2) — do not
re-derive them by hand. Then read what it cannot: each image slot against the slot rule
(`svg-assets.md` § 1) — a drawn picture where a placeholder belonged, a placeholder where
geometry was exact, a stand-in customer logo. Those findings cite `svg-assets.md` § 1 and the
gate it names.

A project with no SVG and no placeholder produces no asset findings. An absent favicon or
og-card is not a defect this runbook invents.

### De-duplicate

`merged-rules.md` § 4. Nine detector rule IDs are covered by a gate — report the gate, not
both. Three pairs overlap without duplicating; read the pair note before deciding.

---

## Step 3 — Write the findings

**Every finding gets all five:**

| | |
|---|---|
| **Severity** | BLOCKING or ADVISORY |
| **Location** | `file:line` |
| **Rule** | the rule ID or gate number it violates, named |
| **What's wrong** | the specific defect, on this line, in this file |
| **Fix** | **the actual change** |

The fix is the part that is usually wrong. "Improve contrast" is not a fix. "Add an
aria-label" is not a fix.

```
BLOCKING  src/components/Nav.tsx:34
  guidelines-and-review.md § Accessibility — icon-only buttons need `aria-label`
  The menu toggle renders an icon with no accessible name; screen readers announce "button".
  Fix: <button aria-label="Open menu" onClick={toggle}>  — and add aria-expanded={open}.

ADVISORY  src/styles/app.css:112
  hallmark-slop-gates.md gate 22 — zero-chroma neutrals
  --surface-muted is oklch(96% 0 0). Pure greys read as flat next to the tinted primary.
  Fix: oklch(96% 0.006 25) — chroma just above the 0.005 floor, tinted toward --color-primary's hue.
```

Rank most severe first.

---

## Step 4 — Severity

**BLOCKING** — accessibility failures, broken keyboard paths, contrast below WCAG 2.2 AA,
design-system violations.

**ADVISORY** — taste, era-specific style, fingerprint / anti-slop findings.

Mapping from each source is in `merged-rules.md` § 2, including the one override worth
remembering: **`design-system-*` drift is BLOCKING here** even though it ships upstream as
warning/advisory.

### When run as VERIFY inside Runbook 1, 2 or 4

**Any BLOCKING finding means fix and re-verify.** Do not report "done" with open BLOCKING
items. Re-verify means running this runbook again from step 1 — re-reading the rules — not
re-checking the lines you just changed.

Called from Runbook 4, a **tier 1** revision gets the targeted pass that runbook scopes — the
rules the changed dimension touches, plus the DESIGN.md drift check — not the full sweep. A
**tier 2** re-direction gets this runbook entire, across every affected surface. Either way the
fix belongs to the caller: **this runbook still edits nothing**, and a BLOCKING finding against
an applied candidate is reported so Runbook 4 fixes it or drops that candidate.

**ADVISORY findings are reported, not auto-fixed.** They are taste calls and taste calls
belong to the user. Reporting an ADVISORY and then fixing it anyway is how a revamp acquires
changes nobody asked for.

---

## Step 5 — State the limit

**In every report, plainly:**

> This is static analysis. It does not replace axe, real keyboard testing, screen readers, or
> looking at the rendered page across viewports. A clean report is evidence, not proof.

This is not a disclaimer to bury. The checks here read source; they do not render. They cannot
see computed contrast against an image, a focus order that breaks under a portal, a layout
that collapses at 320px, a sticky header covering the focused element, or anything that only
exists once the page runs.

Name what you could not check. A report that says "no BLOCKING findings" and omits that
nothing was rendered is worse than one finding, because it will be read as clearance.
