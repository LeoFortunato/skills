# AGENTS.md

## Repository purpose

This repository contains reusable, platform-neutral skills installed under
`.agents/`. Each `.agents/<skill-name>/` directory is a self-contained package
that may include a `SKILL.md` and supporting references or assets. Keep
host-specific metadata and adapters outside the versioned skill packages.

## Working rules

- Treat the applicable `SKILL.md` as the source of truth for a skill's behavior.
- Install every skill at `.agents/<skill-name>/`; do not place skill packages at
  the repository root.
- Keep skill instructions concise, actionable, and internally consistent.
- Preserve the required YAML front matter and directory conventions used by
  existing skills.
- Keep reusable templates and reference material inside the applicable
  `.agents/<skill-name>/` directory.
- Do not commit `.agents/<skill-name>/agents/` directories or other
  host-specific adapter metadata inside skill packages.
- Do not add secrets, user-specific paths, generated artifacts, or unrelated
  application code.
- Use technical English in skill instructions and templates unless a skill
  explicitly targets another language.
- Do not require proprietary commands, APIs, models, plugins, runtimes, prompt
  syntaxes, directory names, or instruction files from a particular tool.
- Describe integrations as optional adapters and keep their implementation
  outside the portable skill package.
- Update the relevant README or reference documentation when a structural or
  behavioral change affects how a skill is used.

## Validation

Before considering a change complete:

1. Review the changed files and confirm paths referenced by documentation exist.
2. Validate YAML files with an available YAML parser when they are changed.
3. Check Markdown for broken relative links and obvious formatting errors.
4. Run `git diff --check` and review `git status --short`.

There is currently no repository-wide build or test command. Add focused
validation alongside a skill if its implementation introduces executable code.

## Scope and safety

Keep changes limited to the requested skill or repository documentation. Ask
before adding external integrations, credentials, deployment configuration, or
destructive operations.
