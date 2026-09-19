# Runbook 4 — REVISE

A design exists and the user wants a variation on it. This runbook edits files.

It is also the **terminal step of Runbooks 1 and 2**. Step 6 of each hands here once VERIFY
reports clean. A build that stops at VERIFY and reports "done" has skipped it.

---

## Step 0 — Entry

**Entered from Runbook 1 or 2.** The direction, the surfaces and the preservation contract are
already settled in this session. Carry them. Do not re-derive and do not re-confirm.

**Entered cold** — a fresh session, no run in flight — read `DESIGN.md` first. It *is* the
direction, exactly as it is for Runbook 1. Read `PRODUCT.md` if one exists, and `REVAMP.md` if
a revamp run left one, for the surface list and the per-surface visitor mode.

**No `DESIGN.md` and no run in flight → the project is not revisable.** There is no recorded
direction to vary, and deriving one is a revamp. Say so and route to Runbook 1.

**The taste gate.** Entered from Runbook 1 or 2, it already ran at their boot — do not run it
again. Entered cold, run it now, before step 1: both gates from `SKILL.md` § Taste history,
filtered to the rules that fit this project.

**One direction per site still binds.** This runbook varies the direction the site already
has; it does not give page 7 a different system from page 2. A variation is applied sitewide
or it is not applied.

---

## Step 1 — The opening question

Asked once, in full, the first time. Handed here from a build:

> Built and verified. Want anything different? Cheap to change with the design intact:
> **type · colour · spacing · shape · motion**. Bigger: the **page shape** itself. Or say done.

Entered cold, the same question against the direction on disk:

> DESIGN.md gives this site *[macrostructure]*, *[type pairing]*, *[palette]*. What do you want
> different? Cheap to change with the design intact: **type · colour · spacing · shape ·
> motion**. Bigger: the **page shape** itself.

When the run drew a mark — CREATE step 3b, REVAMP step 2 — **mark** joins the cheap list: *type ·
colour · spacing · shape · motion · mark*. A kept incumbent logo is never on it.

**Naming the dimensions is load-bearing.** Without them the answer is "looks fine" — not
because the design is right, but because the user cannot see what is cheap to ask for. A bare
"anything else?" collects nothing.

**Do not ask what they already told you.** Someone who arrived here saying "change the fonts on
this site" has named the dimension; go to step 2 with it and ask the opening question on the
way back through the loop. Making a user repeat a request they just made is the same failure as
interrogating them through fields the brief already answered
(`runbook-create.md` § 1).

On each return through the loop, the short form: *"Kept. Anything else, or done?"*

**Wait.** No answer is not consent to keep editing — it ends the loop and takes you to step 6.

---

## Step 2 — The revert point, before the first swap

Established once, before the first change, and stated in one line so the user knows what
"undo" means here.

| Situation | Revert point |
|---|---|
| Git repo, tree clean | `HEAD <sha>`. State the sha. |
| Git repo, tree dirty | Say so. Offer to let the user commit or stash first. Proceed on their word, not on silence. |
| No git | Copy the files you are about to touch to `.design-revise/`. Disclose the path. |

`.design-revise/` is a run artifact with the same lifetime as `REVAMP.md`: disposable at the
end, reported as safe to delete, **never deleted for the user**.

---

## Step 3 — Classify the request

Three tiers. Say which one you are in before you touch a file.

| Tier | Dimension | Handling |
|---|---|---|
| **1** | type, colour, spacing, radius, motion, elevation | Applied in-loop. DESIGN.md frontmatter amended for that token group. |
| **2** | macrostructure, nav / footer archetype, landing section order | A **re-direction**. Announce and wait. DESIGN.md `## Layout` and the CSS stamp rewritten deliberately, every affected surface rebuilt, full re-verify. |
| **3** | copy, information architecture, routes, functional behaviour | **Refused.** `SKILL.md` § Out of scope. Say so and stop. |

### Tier 2 is announced, not absorbed

A page-shape change is not a variation, and treating it as one is how a site acquires two
design systems. Say what it costs and wait:

> That changes the page shape, so it is a re-direction — DESIGN.md gets rewritten and N
> surfaces rebuilt. Go ahead?

On yes: rewrite DESIGN.md `## Layout` and the stamp **once, deliberately**, then rebuild.
Changing direction because the user asked and said so out loud is not drift; changing it
quietly mid-build is. The diversification rule still reads the stamp, and the new
macrostructure still comes from the 21 in `hallmark-macrostructures.md`.

### The mark is announced too

A new mark is an identity change, not a token swap — it rewrites DESIGN.md § Components › Mark,
PRODUCT.md § Brand Commitments and every kit file. Say so and wait, as for tier 2:

> That replaces the mark — the kit gets redrawn and PRODUCT.md's brand line changes. Go ahead?

On yes: concepts per `svg-assets.md` § 3, a pick, then the kit re-derived per § 4. **Refused**
when the logo is a kept incumbent under Runbook 1's preservation contract — releasing it is the
user's call, made plainly, exactly as step 0 of that runbook says.

### Tier 3 is refused, not half-done

"While you're in there, change the headline" is a copy request. Rewriting it under a visual
brief is exactly the failure Runbook 1's preservation contract exists to prevent, and this
runbook does not have a preservation contract to protect it. Do the change if the user asks
for it plainly as its own job — do not route it through this loop.

---

## Step 4 — Alternatives, then pick

Never one swap presented as the answer. The user asked to *see* something different.

1. **Restate the dimension and what stays fixed.** "Type only — palette, spacing, macrostructure
   and section order unchanged."
2. **Retrieve 2–3 real candidates for that dimension alone:**
   ```bash
   python3 scripts/search.py "<the brief in the user's own words>" --domain typography
   ```
   `typography` · `color` · `style` · `landing` — one domain, the one being varied. **Never
   invent a pairing, palette or style.** The catalogue and the custom protocol
   (`hallmark-custom-theme.md`) remain the only sources, and the custom protocol still fires
   only on its enumerated signals.
3. **Pre-screen every candidate against the gates it touches.** A candidate that fails is
   never offered:

   | Varying | Screen against |
   |---|---|
   | type | gate 1 — the seven flagged pairings are filtered out before they reach the user |
   | colour | neutral tinting transform (`contract.md` § Neutral tinting), then gates 7 and 22, then AA contrast re-verified on the **post-transform** values |
   | style | the ban list — glass, liquid-glass and hard offset shadows are available only with a stated purpose, recorded in DESIGN.md (`merged-rules.md` § C5) |
   | motion | `prefers-reduced-motion` note and the compositor justification on the `motion.csv` row |
   | mark | the construction rules in `svg-assets.md` § 3 — drawn, not retrieved: the catalogue has no marks, so the named PRODUCT.md fact is the source |

   Showing the user something the skill will refuse two steps later wastes their time and
   teaches the history store a preference that cannot be honoured.
4. **Apply them to the real site, one at a time**, each with a one-line reason. Not a mockup,
   not a comparison page — the built pages, so what they judge is what they get. `next` moves
   on, `keep` ends the cycle. A mark goes into the real nav the same way; `mark-concepts.html`
   adds only what the page cannot show — the 16px favicon and the one-colour version.
5. **Keep the winner.** Amend the DESIGN.md frontmatter for that token group and the matching
   prose section. Frontmatter stays normative; prose may name the token and describe its role,
   never restate a different value. The CSS stamp is untouched unless the macrostructure
   changed.

**A pinned brief still wins.** A font, palette or era the user named earlier is binding here
too — do not offer alternatives that contradict it unless they are the ones asking to move off
it.

---

## Step 5 — Re-verify, scoped to what changed

| Tier | Pass |
|---|---|
| 1 | **Targeted** — the rules that dimension touches, plus the DESIGN.md ↔ code token-drift check |
| 2 | **Full** Runbook 3 across every affected surface |
| mark | **Targeted** — `svg_lint.py`, gates 30 and 47, and the DESIGN.md ↔ kit colour check it runs |

Re-reading the rules from disk applies here exactly as it does in Runbook 3 § 1. A font swap
does not earn the full 50-rule sweep; it does earn gate 1, the type numbers from the quality
floor, and the check that DESIGN.md and the stylesheet now agree.

**A BLOCKING finding on an applied candidate means fix it or drop that candidate.** It is
never kept as the winner. ADVISORY findings are reported, not auto-fixed — a taste call inside
a taste loop is still the user's.

**Report, don't repair, drift** you find that the revision did not cause. It is a finding.

---

## No new project artifact

The loop keeps its state in the session and writes one history entry at exit. **It creates no
new markdown artifact in the user's project** — another file at the project root to record a
font swap is not worth it, and a fourth durable-looking artifact would blur the three lifetimes
`contract.md` § 3 exists to keep apart. Where a `REVAMP.md` exists, iterations land in its
`## Notes`; its `Status` column still means what Runbook 1 says it means.

`.design-revise/` from step 2 is not an artifact — it is a copy of files as they were, taken
only when there is no git to fall back on, carrying no scope, no status and no decision. It is
disclosed when created and reported as safe to delete at exit. `mark-concepts.html`, written only
when the mark is varied, has the same standing: a run artifact, reported, never deleted for the
user.

---

## Step 6 — Exit and write-back

The loop ends when the user says done or declines the opening question.

**If `history: off`, skip this entire step.** Read nothing, write nothing, propose nothing.

### 6a · Log — automatic, no confirmation

Append one entry per revision request to `history/log/<project-slug>.md`, in the shape in
`history/README.md`. Project slug is the `name` from `PRODUCT.md`, lowercased and hyphenated;
absent that, the project directory name.

A run with **zero** revisions still writes its entry. Clean runs are evidence, and a store
that only records dissatisfaction feeds the repeat detector a biased sample.

Record the boot gate's outcome on the run's first entry — `applied 1, 3 · dropped 2 (motion)`.
The demotion detector reads it.

This write is skill-local and disclosed in 6d. It touches nothing in the user's project, which
is why it does not need their confirmation.

### 6b · Promotion — repeat, then confirm

A log candidate becomes a proposal only when the **same dimension** carries a compatible
request in **2 or more distinct project slugs**. **Never on first occurrence.**

Matching is your judgment on reading the log, not an algorithm — so **quote both source
entries** and let the user reject a bad match:

> Promote to TASTE.md?
> **Type.** Prefer a serif display face over a geometric sans on editorial briefs.
> - ink-paths 2026-09-14 — *"the sans feels generic, try something with more voice"* → Instrument Serif
> - music-as-code 2026-09-17 — *"same design, different fonts"* → Instrument Serif
>
> Scope tag: `editorial`. Yes / no / reword.

Confirmed → write the rule to `TASTE.md` with its provenance comment and scope tag. Rejected →
mark the candidate in the log and never propose it again:

```markdown
- **Promotion:** declined 2026-09-17
```

### 6c · Demotion — the same shape, inverted

A rule dropped at the boot gate in **2 or more distinct project slugs** gets a removal
proposal, with the same evidence quoting and the same confirmation:

> Taste rule 2 (motion) has been dropped on the last 2 projects. Remove it from TASTE.md?

Confirmed → delete the line. Rejected → leave it and do not re-propose.

### 6d · One message, then disclose

**Batch every promotion and demotion into a single message.** Not one per rule. The user
answers once, you write, you report.

Then name the history files that changed, by path:

> Wrote `history/log/music-as-code.md` — 1 entry. Wrote `history/TASTE.md` — 1 rule added.

These writes land inside the skill's own directory. A skill that silently edits itself is the
thing to avoid; a skill that says which of its own files it changed is a notebook.
