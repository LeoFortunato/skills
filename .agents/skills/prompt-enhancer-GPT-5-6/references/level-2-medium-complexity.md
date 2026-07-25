# Level 2: Medium Complexity Prompt Reference Guide

This reference defines the model, parameters, rules, and prompt architecture for **Level 2 (Medium Complexity)** tasks.

---

## 1. Task Scope & Characteristics

- **Use Cases**: Standard feature implementation, routine multi-file edits, REST API endpoints, documentation updates, standard customer support agents.
- **Primary Objective**: Balanced quality, cost efficiency, and structural clarity.

---

## 2. Model & Parameter Configuration

- **Recommended Model**: `gpt-5.6-terra` (balanced performance and cost).
- **Reasoning Effort (`reasoning.effort`)**: `medium` (API default for analytical and tool-using tasks).
- **Reasoning Mode (`reasoning.mode`)**: `"standard"`.
- **Text Verbosity (`text.verbosity`)**: `medium`.

---

## 3. Rules & Aggregation

- **INCLUDE** `# Role`, `# Personality & Collaboration Style` (unified), `# Goal`, `# Success Criteria`, `# Constraints & Approval Boundaries`, and `# Output Format & Structure`.
- **INCLUDE** light file navigation guardrail: Do not re-read unchanged files already in conversation context.
- **OMIT** heavy Programmatic Tool Calling (PTC) orchestration unless explicitly requested.

---

## 4. Balanced Prompt Template

Use this balanced structure for Level 2 prompts:

```text
Role: [1-2 sentences defining identity and domain context]

# Personality & Collaboration Style
[Tone, directness, and basic clarification rules]

# Goal
[Target outcome described by destination rather than rigid micro-steps]

# Success Criteria
[Verifiable completion conditions]

# Constraints & Approval Boundaries
- Autonomous actions: Make in-scope local changes, inspect relevant files, run non-destructive tests.
- Confirmation required: External API writes, destructive file operations, or scope expansion.
- Context rule: Do not re-read files already present in conversation history unless modified by a tool.

# Output Format & Structure
[Structure, sections, and verbosity preference]
```
