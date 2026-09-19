# Taste history

What the user asked to change after a design was delivered, and what that taught the skill.

This store is **skill-local**. It lives inside the skill, not inside anyone's project, and it
outlives every project the skill touches. Nothing here is product truth and nothing here is a
project's visual system — a fact worth keeping about a product belongs in that project's
`PRODUCT.md`, a visual decision worth keeping belongs in its `DESIGN.md`.

| File | Kind | Written by |
|---|---|---|
| `TASTE.md` | distilled rules, curated, one line each | promotion, user-confirmed |
| `log/<project-slug>.md` | append-only record of revision requests for that project | automatically, at run end |
| `README.md` | this file | by hand |

**Project slug** is the `name` from the project's `PRODUCT.md`, lowercased and hyphenated.
No `PRODUCT.md`, or no `name` in it → the project directory name. One file per slug; the
same project revised twice appends to the same file.

---

## The two layers

**The log records. `TASTE.md` binds.** A log entry is evidence of one request on one project
and constrains nothing. A `TASTE.md` rule is offered to the user at the start of every run
and shapes the design once they confirm it. Nothing crosses from one to the other except
through the promotion rule below.

### Rule shape — `TASTE.md`

One line, a bolded dimension, then the doctrine. The provenance comment is not decoration: it
is what makes a stale rule auditable a year later.

```markdown
- **Type.** Prefer a serif display face over a geometric sans on editorial briefs.
  <!-- scope: editorial · seen: ink-paths 2026-09-14, music-as-code 2026-09-17 · promoted 2026-09-17 -->
```

`scope` is the tag the boot gate filters on — a rule tagged `editorial` is not offered on a
SaaS dashboard brief. Use `all` for a rule that applies regardless of brief.

### Log entry shape — `log/<project-slug>.md`

One entry per revision request.

```markdown
## 2026-09-17 · music-as-code · CREATE
- **Dimension:** typography
- **Asked:** "same design, different fonts"
- **From → to:** Space Grotesk / IBM Plex Sans → Instrument Serif / Inter Tight
- **Kept:** yes
- **Generalizable:** candidate — editorial brief, display face
```

A run where nothing was asked for still writes an entry:

```markdown
## 2026-09-17 · sweepline · CREATE
- No revisions requested. Direction accepted first pass.
```

**Clean runs are evidence too.** Without them the store only ever records dissatisfaction, and
the repeat detector reads a biased sample.

Which taste rules were applied is recorded on the run's first entry:

```markdown
- **Taste rules:** applied 1, 3 · dropped 2 (motion)
```

---

## Promotion — repeat, then confirm

A log candidate becomes a `TASTE.md` rule only when the **same dimension** carries a
compatible request in **2 or more distinct project slugs**, and only after the user confirms
it. Never on first occurrence. Never silently.

Matching is a judgment made by reading the log, not an algorithm. The honesty mechanism is
that the proposal **quotes both source entries**, so the user can see the evidence and reject
a bad match. A rejected proposal is marked in the log and never re-proposed:

```markdown
- **Promotion:** declined 2026-09-17
```

## Demotion — the same shape, inverted

A rule dropped at the boot gate in **2 or more distinct project slugs** gets a removal
proposal, with the same evidence quoting and the same confirmation. Dropping a rule is a
signal; a store that only ever grows accumulates rules the user skips past on every run.

Full procedure for both: `reference/runbook-revise.md` § 6.

---

## Editing and wiping

These are plain markdown files with no schema stamp and no parser. Edit `TASTE.md` by hand
whenever a rule stops being true — deleting a line is a supported operation, not a corruption.
Delete a `log/<slug>.md` file to forget a project. Delete the whole `log/` directory to reset
the evidence while keeping the rules, or empty `TASTE.md` to drop the rules while keeping the
evidence.

## When history is off

A caller can disable the store for a run by instructing `history: off`. Then the skill neither
reads `TASTE.md` nor writes any log entry, the boot gate is skipped entirely, and no promotion
or demotion is proposed. **Benchmark and evaluation harnesses must set it.** A benchmark that
reads learned taste is no longer measuring the skill, and a benchmark that writes into this
store poisons every later run's evidence.
