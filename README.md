# custom-ai-skills

Custom skills for AI coding agents (Claude Code and other agents that read `SKILL.md`).
Each top-level folder is one self-contained skill. Each skill is explained in its own note in
[`docs/`](docs/).

## Skills

| Skill | Summary | Docs |
|---|---|---|
| [`design-runbooks`](design-runbooks/) | Designs, redesigns, audits and revises web UIs against a shared design contract | [docs/design-runbooks.md](docs/design-runbooks.md) |

## Install

Copy or symlink a skill folder into your agent's skills directory. For Claude Code:

```bash
# personal, all projects
cp -r <skill> ~/.claude/skills/

# or a single project
cp -r <skill> <project>/.claude/skills/

# symlink to pick up `git pull` updates automatically
ln -s "$PWD/<skill>" ~/.claude/skills/<skill>
```

Setup a skill needs beyond copying it is covered in that skill's docs note.

## License

Each skill carries its own license in its folder. See the skill's docs note for provenance and
third-party notices.
