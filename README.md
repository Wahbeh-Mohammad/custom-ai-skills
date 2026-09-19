# custom-ai-skills

Custom skills for AI coding agents (Claude Code and other agents that read `SKILL.md`).
Each top-level folder is one self-contained skill. Each skill is explained in its own note in
[`docs/`](docs/).

## Skills

| Skill | Summary | Docs |
|---|---|---|
| [`design-runbooks`](design-runbooks/) | Designs, redesigns, audits and revises web UIs against a shared design contract | [docs/design-runbooks.md](docs/design-runbooks.md) |

## Install

Skills follow the [Agent Skills](https://agentskills.io) format (a folder with a `SKILL.md`), so
they work in any agent that supports it.

### With the skills CLI

[`npx skills`](https://github.com/vercel-labs/skills) detects the agents you have installed and
puts the skill in each one's skills directory.

```bash
# list skills in this repo
npx skills add Wahbeh-Mohammad/custom-ai-skills --list

# install one skill into the current project
npx skills add Wahbeh-Mohammad/custom-ai-skills --skill <skill>

# install globally, for specific agents only
npx skills add Wahbeh-Mohammad/custom-ai-skills --skill <skill> -g -a claude-code -a codex
```

### Manually

Copy or symlink the skill folder into your agent's skills directory. Project paths are relative
to the project root.

| Agent | Project | Global |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` |
| Gemini CLI | `.gemini/skills/` or `.agents/skills/` | `~/.gemini/skills/` or `~/.agents/skills/` |
| GitHub Copilot | `.github/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` |
| Cursor | `.cursor/skills/` or `.agents/skills/` | `~/.cursor/skills/` or `~/.agents/skills/` |
| OpenCode | `.opencode/skills/` or `.agents/skills/` | `~/.config/opencode/skills/` or `~/.agents/skills/` |
| Windsurf | `.windsurf/skills/` or `.agents/skills/` | `~/.codeium/windsurf/skills/` or `~/.agents/skills/` |

`.agents/skills/` is the shared location: every agent above except Claude Code reads it. One
global symlink there plus one for Claude Code covers them all:

```bash
git clone https://github.com/Wahbeh-Mohammad/custom-ai-skills.git
cd custom-ai-skills

mkdir -p ~/.agents/skills ~/.claude/skills
ln -s "$PWD/<skill>" ~/.agents/skills/<skill>   # Codex, Gemini CLI, Copilot, Cursor, OpenCode, Windsurf
ln -s "$PWD/<skill>" ~/.claude/skills/<skill>   # Claude Code
```

Symlinks pick up `git pull` updates. Use `cp -r` instead for a frozen copy. OpenCode and Cursor
also read `~/.claude/skills/` (Windsurf too, when Claude Code config reading is on). If one of
them lists the skill twice, remove the `~/.agents/skills/` link and let it use the Claude Code one.

Setup a skill needs beyond copying it is covered in that skill's docs note.

## License

Each skill carries its own license in its folder. See the skill's docs note for provenance and
third-party notices.
