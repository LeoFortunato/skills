# Reusable Skills

Platform-neutral, reusable skills. Each skill packages its instructions and
any supporting references needed to apply it consistently in different tools,
projects, and execution environments. The repository is maintained directly
from its `.agents/skills/` directory.

[![skills.sh](https://skills.sh/b/LeoFortunato/skills)](https://skills.sh/LeoFortunato/skills)

## Repository layout

```text
.agents/
└── skills/
    └── <skill-name>/
        ├── SKILL.md        # Skill instructions and usage contract
        ├── references/     # Optional supporting documentation and templates
        └── assets/         # Optional reusable assets
```

All installable skills live under `.agents/skills/`. Each direct child
directory is one self-contained skill package.

## Available skills

### `codex-session-recovery`

Lists and accesses previous Codex sessions from local `~/.codex` logs, matching
by repository path and extracting clean conversation histories.

### `domain-modeling`

Builds and sharpens a project's domain model, ubiquitous language
(`CONTEXT.md`), context maps (`CONTEXT-MAP.md`), and Architectural Decision
Records (ADRs).

*Note: Adapted from [Matt Pocock's skills repository](https://github.com/mattpocock/skills/tree/main).*

### `goal-prompt-writer`

Creates, reviews, and refines durable prompts for long-running coding work. It
helps define scope, constraints, validation checkpoints, approval boundaries,
and stopping conditions without assuming a particular assistant, command
syntax, model, or host platform.

### `grilling`

Stress-tests plans, designs, and decisions through relentless frontier-based
interview rounds, with an optional documentation mode for capturing ADRs and
glossary entries.

*Note: Adapted from [Matt Pocock's skills repository](https://github.com/mattpocock/skills/tree/main).*

### `new-cnpj-validation`

Implements, reviews, or tests Brazilian CNPJ validation supporting both the legacy
numeric format and the Receita Federal alphanumeric format scheduled for July 2026.

### `prompt-enhancer`

Refines, reviews, and structures draft prompts and persistent `/goal` objectives
into Technical English prompt contracts with model tier and reasoning effort
recommendations.

### `prompt-refine`

Refines draft prompts, task descriptions, bug reports, and debug findings into
concise, copy-ready prompt contracts across `simple`, `advanced`, and `goal`
modes without meta-prompt framing.

### `rq-redis-queue`

Implements and reviews RQ (Redis Queue) background jobs, queues, workers,
retries, scheduling, timeouts, registries, heartbeats, cancellation, and graceful
shutdown for Python asynchronous workflows.

*Note: Adapted from [orchestkit](https://github.com/yonatangross/orchestkit).*

### `technical-english-writer-asd-ste100`

Creates, rewrites, reviews, and maintains clear English software documentation
with an adapted ASD-STE100-inspired controlled-language method. It supports
guides, tutorials, API and CLI references, troubleshooting articles,
operational procedures, release notes, and technical messages without claiming
official ASD-STE100 certification or compliance.

## Installation

List the skills available in this repository:

```bash
npx skills add LeoFortunato/skills --list
```

Install a specific skill:

```bash
npx skills add LeoFortunato/skills --skill codex-session-recovery
npx skills add LeoFortunato/skills --skill domain-modeling
npx skills add LeoFortunato/skills --skill goal-prompt-writer
npx skills add LeoFortunato/skills --skill grilling
npx skills add LeoFortunato/skills --skill new-cnpj-validation
npx skills add LeoFortunato/skills --skill prompt-enhancer
npx skills add LeoFortunato/skills --skill prompt-refine
npx skills add LeoFortunato/skills --skill rq-redis-queue
npx skills add LeoFortunato/skills --skill technical-english-writer-asd-ste100
```

The skills.sh catalog discovers skills after the repository is installed with
the Skills CLI and its anonymous telemetry is enabled.

## Adding a skill

1. Create `.agents/skills/<skill-name>/` using a short, kebab-case skill name.
2. Add a `SKILL.md` with YAML front matter containing `name` and `description`.
3. Keep references and assets inside `.agents/skills/<skill-name>/`.
4. Do not commit host-specific `agents/` directories or adapter metadata inside
   a skill package.
5. Update the available-skills section above and verify all documented paths.

See [AGENTS.md](AGENTS.md) for repository-wide contribution and validation
rules.
