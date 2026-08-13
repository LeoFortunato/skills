# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project follows Semantic
Versioning.

## [Unreleased]

## [0.3.0] - 2026-08-13

### Added

- Add `domain-modeling` skill for building ubiquitous language (`CONTEXT.md`), context maps, and ADRs (adapted from Matt Pocock's skills repository).
- Add `grilling` skill for relentless iterative plan questioning and alignment interviews (adapted from Matt Pocock's skills repository).
- Add `prompt-refine` skill for multi-mode prompt contract refinement without meta-prompt framing.
- Add `rq-redis-queue` skill for RQ (Redis Queue) background jobs, workers, retries, scheduling, timeouts, registries, and graceful shutdown (adapted from orchestkit).

### Changed

- Rename `prompt-enhancer-gpt-5-6` to `prompt-enhancer` and make prompt templates, routing, model tiers, and reasoning recommendations fully provider-agnostic.
- Rename `prompt-refine-codex-5-6` to `prompt-refine` and remove provider-specific references.
- Remove Codex references from `goal-prompt-writer` and standardize on provider-agnostic goal prompts.
- Update `README.md` and `skills.sh.json` to index and group all 8 installable repository skills with agnostic names.
- Standardize YAML frontmatter metadata across all skills with `author`, `license: MIT`, and upstream `source` attributions.
- Add source references attributing `rq-redis-queue` to `orchestkit`, and `domain-modeling` and `grilling` to Matt Pocock's skills repository.

## [0.2.0] - 2026-07-29

### Added

- Add `new-cnpj-validation` skill supporting both legacy numeric format and Receita Federal alphanumeric format (scheduled for July 2026).
- Add `prompt-enhancer-gpt-5-6` skill to refine draft prompts into structured Technical English prompt contracts for GPT-5.6 (Sol, Terra, Luna) and Codex `/goal` mode.
- Add tiered reference guides for prompt complexity levels (`level-1-low-complexity`, `level-2-medium-complexity`, `level-3-high-complexity`, `goal-mode-codex`).
- Add `skills.sh.json` groupings for skills.sh repository catalog discovery.

### Changed

- Enforce Technical English output for all enhanced prompts in `prompt-enhancer-gpt-5-6`.
- Standardize model and reasoning effort recommendations across prompt complexity levels.
- Modernize and simplify `goal-prompt-writer` skill instructions and prompt templates.
- Keep host-specific `agents/` metadata outside versioned skill packages.
- Move installable skill packages to the standard `.agents/skills/` discovery path.
- Document Skills CLI installation and skills.sh discovery in `README.md`.

## [0.1.0] - 2026-07-21

### Added

- Initial repository structure for reusable skills installed under `.agents/`.
- `goal-prompt-writer` skill.
- `technical-english-writer-asd-ste100` skill.
- Repository documentation and contribution rules.
- MIT license and npm package metadata.
