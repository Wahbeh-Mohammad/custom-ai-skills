# custom-ai-skills

Custom skills for AI coding agents (Claude Code and other agents that read `SKILL.md`).

## Skills

| Skill | What it does |
|---|---|
| [`design-runbooks`](skills/design-runbooks/SKILL.md) | Designs, redesigns, audits and revises web UIs (landing pages, marketing sites, app surfaces, dashboards). Routes to one of four runbooks (revamp, create, audit, revise) and holds every visual decision to a shared `PRODUCT.md` / `DESIGN.md` contract. Ships 21 macrostructures, 192 product-type palettes, 74 type pairings, a merged rule set, an SVG brand kit linter, and a taste history that learns from confirmed revisions. |

## Layout

```
skills/
└── design-runbooks/
    ├── SKILL.md                  entry point: routing between the four runbooks
    ├── guidelines-and-review.md  web interface guidelines and review checklist
    ├── reference/                runbooks, contract, merged rules, upstream extracts
    ├── data/                     palettes, type pairings, styles, stack rules (CSV)
    ├── scripts/                  search.py, design_system.py, svg_lint.py (Python 3, stdlib only)
    ├── history/                  taste history: TASTE.md rules + per-project logs
    ├── licenses/                 upstream license texts
    ├── MANIFEST.md               extraction provenance, pinned upstream commits
    ├── THIRD-PARTY-NOTICES.md
    ├── NOTICE
    └── LICENSE
```

## Install

Copy or symlink the skill folder into your agent's skills directory. For Claude Code:

```bash
# personal, all projects
cp -r skills/design-runbooks ~/.claude/skills/

# or a single project
cp -r skills/design-runbooks <project>/.claude/skills/
```

Symlink instead of copying to pick up `git pull` updates automatically:

```bash
ln -s "$PWD/skills/design-runbooks" ~/.claude/skills/design-runbooks
```

The scripts need Python 3 and nothing else:

```bash
cd skills/design-runbooks
python3 scripts/search.py "fintech dashboard" --design-system
python3 -m unittest scripts/test_svg_lint.py
```

## Taste history

`design-runbooks` keeps a skill-local record of revision requests in `history/log/<project>.md`
and promotes repeated, user-confirmed preferences into `history/TASTE.md`. The log files are
personal run data and are git-ignored; `TASTE.md` ships empty. See
[`history/README.md`](skills/design-runbooks/history/README.md). Benchmark and evaluation
runs should set `history: off`.

## License

`design-runbooks` is licensed under Apache-2.0 ([`LICENSE`](skills/design-runbooks/LICENSE)).
It includes material extracted from four upstream projects, credited with pinned commits in
[`MANIFEST.md`](skills/design-runbooks/MANIFEST.md) and
[`THIRD-PARTY-NOTICES.md`](skills/design-runbooks/THIRD-PARTY-NOTICES.md):

| Upstream | License |
|---|---|
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | MIT |
| [Nutlope/hallmark](https://github.com/Nutlope/hallmark) | MIT |
| [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) | MIT |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Apache-2.0 |
