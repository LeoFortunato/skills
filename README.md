# Reusable Skills

Platform-neutral, reusable skills. Each skill packages its instructions and
any supporting references needed to apply it consistently in different tools,
projects, and execution environments. The repository is maintained directly
from its `.agents/` directory.

## Repository layout

```text
.agents/
└── <skill-name>/
    ├── SKILL.md             # Skill instructions and usage contract
    ├── agents/
    │   └── openai.yaml      # Optional host-specific metadata adapter
    └── references/          # Optional supporting documentation and templates
```

All installable skills live under `.agents/`. Each direct child directory of
`.agents/` is one self-contained skill package.

## Available skills

### `goal-prompt-writer`

Creates, reviews, and refines durable prompts for long-running coding work. It
helps define scope, constraints, validation checkpoints, approval boundaries,
and stopping conditions without assuming a particular assistant, command
syntax, model, or host platform.

### `technical-english-writer-asd-ste100`

Creates, rewrites, reviews, and maintains clear English software documentation
with an adapted ASD-STE100-inspired controlled-language method. It supports
guides, tutorials, API and CLI references, troubleshooting articles,
operational procedures, release notes, and technical messages without claiming
official ASD-STE100 certification or compliance.

## Adding a skill

1. Create `.agents/<skill-name>/` using a short, kebab-case skill name.
2. Add a `SKILL.md` with YAML front matter containing `name` and `description`.
3. Keep references and assets inside `.agents/<skill-name>/`.
4. If a host tool needs metadata, provide it as a separate adapter such as
   `.agents/<skill-name>/agents/openai.yaml`. Do not make the portable skill
   depend on the adapter.
5. Update the available-skills section above and verify all documented paths.

See [AGENTS.md](AGENTS.md) for repository-wide contribution and validation
rules.
