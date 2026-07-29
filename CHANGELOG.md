# Changelog

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog, and this project follows Semantic
Versioning.

## [Unreleased]

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
