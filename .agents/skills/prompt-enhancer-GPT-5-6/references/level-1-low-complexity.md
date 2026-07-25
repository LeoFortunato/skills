# Level 1: Low Complexity Prompt Reference Guide

This reference defines the model, parameters, rules, and prompt architecture for **Level 1 (Low Complexity)** tasks.

---

## 1. Task Scope & Characteristics

- **Use Cases**: Single-step operations, formatting, simple data extraction, function refactoring, classification, code snippet generation, or direct Q&A.
- **Primary Objective**: Maximum execution speed, minimal cost, and zero prompt bloat.

---

## 2. Model & Parameter Configuration

- **Recommended Model**: `gpt-5.6-luna` (or `gpt-5.6-terra` if high language precision is needed).
- **Reasoning Effort (`reasoning.effort`)**: `none` (latency baseline) or `low` (minimal decision logic).
- **Reasoning Mode (`reasoning.mode`)**: `"standard"`.
- **Text Verbosity (`text.verbosity`)**: `low` (direct, concise responses without redundant filler).

---

## 3. Rules & Omissions

To comply with OpenAI's *Lean Prompts* principle (improving accuracy by 10-15% and reducing token costs by up to 67%):

- **OMIT** `# Personality` and `# Collaboration Style` blocks.
- **OMIT** `# Tools` and `<tool_orchestration>` blocks.
- **OMIT** `# Context & File Access Guardrails`.
- **OMIT** `# Stop Rules & Retrieval Budget`.
- **OMIT** `# Validation Directive`.

---

## 4. Minimalist Prompt Template

Use this minimal structure for Level 1 prompts:

```text
Role: [1 sentence defining the model's function and domain context]

# Goal
[Direct, clear description of the target outcome]

# Output Format
[Output schema, code block, or format preference]
```
