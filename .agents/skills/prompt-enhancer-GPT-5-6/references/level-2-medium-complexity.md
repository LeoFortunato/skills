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

- **INCLUDE** `# Role`, `# Personality & Collaboration Style` (unified), `# Goal`, `# Success Criteria`, `# Constraints`, and `# Output Format`.
- **OMIT** heavy file-access guardrails unless multi-file codebase navigation is requested.
- **OMIT** Programmatic Tool Calling (PTC) orchestration unless requested.

---

## 4. Balanced Prompt Template

Use this balanced structure for Level 2 prompts:

```text
Role: [1-2 sentences defining identity and domain context]

# Personality & Collaboration Style
[Tone, directness, and basic clarification rules]

# Goal
[Target outcome described by destination]

# Success Criteria
[Verifiable completion conditions]

# Constraints
[Safety, style, and scope boundaries]

# Output Format & Structure
[Structure, sections, and verbosity preference]
```
