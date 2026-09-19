# custom-ai-skills

A collection of agent skills. Each top-level folder (other than `docs/`) is one self-contained
skill that users install by copying or symlinking it into an agent's skills directory
(`~/.claude/skills/`, `~/.agents/skills/`, ...; full table in the README).

## Layout

```
<skill>/            one skill: SKILL.md plus everything it loads
docs/<skill>.md     the human-facing note that explains that skill
README.md           index only: skill table, install, license pointer
CLAUDE.md           this file
```

## Rules

### Skills

- **Folder name matches the `name:` in `SKILL.md` frontmatter.** That name is how agents find it.
- **A skill is self-contained.** Paths it tells the agent to read or run are relative to its own
  folder. No links to other skills, to `docs/`, to the repo root, or to anything on the
  author's machine. A skill must work after `cp -r <skill>` into any agent's skills directory.
  Links inside verbatim upstream text (e.g. `../../../site/css/tokens.css` in
  `design-runbooks/reference/hallmark-custom-theme.md`) are upstream's and stay as they are.
- **No build step, no runtime dependencies** beyond what the docs note states. Scripts in
  `design-runbooks/scripts/` are Python 3 stdlib only; keep them that way.
- **Never commit runtime state.** Anything a skill writes while running (for example
  `*/history/log/*.md`) is personal data and is git-ignored. Ship templates empty:
  `design-runbooks/history/TASTE.md` has no rules in it, and must stay that way in the repo.
- **Never commit `__pycache__/` or `*.pyc`.** Delete them after running scripts or tests.

### Upstream-derived content

- A skill that includes third-party material keeps its own `LICENSE`, `NOTICE`, license texts
  and provenance record inside its folder.
- In `design-runbooks`, `MANIFEST.md` makes fidelity claims against pinned upstream commits:
  the ui-ux-pro-max files in `data/` and `scripts/` are byte-identical,
  `guidelines-and-review.md` rule text and the impeccable schemas and tables are verbatim. **Do not edit upstream-derived files in
  place.** A change there either breaks a fidelity claim or needs a matching entry in
  `MANIFEST.md` § 17 (Deviations). Ask before touching them. Files original to the skill are
  listed in § 18 and can be edited normally.

### Docs

- Every skill has exactly one note at `docs/<skill>.md`. Adding, renaming or removing a skill
  means adding, renaming or removing its note in the same commit.
- A note explains the skill to a person who has not read `SKILL.md`: what it does, when it
  triggers and when it refuses, how a run works, commands to run, where things live, and
  provenance/license. Link into the skill folder with relative paths (`../<skill>/...`).
- When a skill changes behaviour, counts or commands, update its note in the same commit.
  Counts in notes (palettes, pairings, rules) must match the skill's own files.

### README

- The README is an index. One table row per skill: name linked to the folder, a one-line
  summary, and a link to its docs note.
- **No skill details inline** in the README. Layout trees, commands, feature lists and
  per-skill licensing go in the docs note.

## Adding a skill

1. Copy the skill folder to the repo root, excluding caches (`rsync -a --exclude='__pycache__/'`).
2. Check it has no machine-specific paths: `grep -rn '/home/\|/Users/' <skill>` returns nothing.
3. Add any runtime-state paths it writes to `.gitignore`.
4. Write `docs/<skill>.md`.
5. Add its row to the README table.
6. Run its checks (below), then commit.

## Checks

```bash
# design-runbooks
cd design-runbooks
python3 -m unittest scripts/test_svg_lint.py
python3 scripts/search.py "fintech dashboard" --design-system > /dev/null
find . -name __pycache__ -exec rm -rf {} +
```

When testing a skill that keeps history, run it with `history: off` so tests neither read nor
write the taste store.

## Git

- Commit messages: imperative subject line under ~60 characters, a body that says what changed
  and why.
- Do not push, open PRs, or run any other remote-mutating `git`/`gh` command unless the user
  asks for that specific action in that message.
