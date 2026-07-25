---
name: prompt-enhancer-GPT-5-6
description: Refine, enhance, and structure prompts for OpenAI models (specifically GPT-5.6 Sol, Terra, and Luna) based on official OpenAI documentation and prompting best practices. Trigger whenever the user asks to enhance, refine, optimize, polish, or format a prompt, or calls this skill to improve a prompt draft for GPT models.
---

# Prompt Enhancer (GPT-5.6 - Complexity-Routed Edition)

This skill transforms draft prompts or task descriptions into production-ready prompts by dynamically classifying task complexity, selecting the optimal GPT-5.6 model variant and parameters, and reading the single reference file matching the task's complexity level.

## Workflow Overview

When invoked, execute the following four-phase workflow:

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Input Analysis & Brief Interview                   │
├─────────────────────────────────────────────────────────────┤
│ Phase 2: Complexity Classification & Reference File Loading  │
├─────────────────────────────────────────────────────────────┤
│ Phase 3: Dynamic Rule Aggregation & Prompt Construction     │
├─────────────────────────────────────────────────────────────┤
│ Phase 4: Output Delivery & Rationale                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Input Analysis & Brief Interview

Analyze the user's initial input. If key prompt engineering elements are missing or underspecified, conduct a brief, targeted interview before generating the final prompt.

### 1. Key Information Check
Check if the input specifies:
- **Core Objective**: What specific outcome or artifact should be produced?
- **Context & Inputs**: What data, files, policies, or background details are available?
- **Task Scope & Complexity**: Is this a single-step task, standard feature, or complex agentic workflow?
- **Constraints & Approval Boundaries**: What actions are allowed autonomously vs. requiring explicit approval?
- **Success Criteria & Verification**: How is correctness verified (e.g., tests, inspection)?
- **Output Format & Verbosity**: What structure, style, or verbosity is expected?

### 2. Interview Guidelines
- Ask **3 to 5 concise, direct questions** focusing strictly on missing information needed to construct a high-quality prompt.
- If the user provides a comprehensive draft with all details present, skip the interview and proceed directly to Phase 2.

---

## Phase 2: Complexity Classification & Reference File Loading

Classify the request into one of three complexity levels and load ONLY the single reference file matching that level:

### 1. Level 1: Low Complexity (Minimalist)
- **Scope**: Single-step operations, formatting, simple data extraction, function refactoring, classification, code snippet generation, or direct Q&A.
- **Reference File to Read**: `references/level-1-low-complexity.md`

### 2. Level 2: Medium Complexity (Balanced)
- **Scope**: Standard feature implementation, multi-file routine edits, REST API endpoints, documentation updates, standard customer support agents.
- **Reference File to Read**: `references/level-2-medium-complexity.md`

### 3. Level 3: High Complexity (Agentic & Guardrailed)
- **Scope**: Complex architectural design, deep multi-file debugging, long-running agentic coding goals, Programmatic Tool Calling (PTC), multi-agent coordination, or high-risk tasks.
- **Reference File to Read**: `references/level-3-high-complexity.md`

---

## Phase 3: Dynamic Rule Aggregation & Prompt Construction

Follow the instructions and prompt template from the loaded reference file:

- **If Level 1**: Construct a Minimalist Prompt using the model `gpt-5.6-luna` / `gpt-5.6-terra` and parameters from `references/level-1-low-complexity.md`. Omit all secondary guardrail sections.
- **If Level 2**: Construct a Balanced Prompt using `gpt-5.6-terra` and parameters from `references/level-2-medium-complexity.md`.
- **If Level 3**: Construct a Full Agentic & Guardrailed Prompt using `gpt-5.6-sol` and parameters from `references/level-3-high-complexity.md`. Inject explicit Context & File Access Guardrails (Anti-Releitura), Tool Orchestration (PTC), and Tiered Validation Directives.

---

## Phase 4: Output Delivery

Deliver the refined prompt package structured into four clearly separated sections:

1. **Assessed Complexity Level**: Indicated complexity level (Level 1 - Low, Level 2 - Medium, or Level 3 - High/Agentic) with technical justification.
2. **Recommended Model & Parameters**: Selected GPT-5.6 model slug (`gpt-5.6-sol`, `gpt-5.6-terra`, or `gpt-5.6-luna`) and parameter settings (`reasoning.effort`, `reasoning.mode`, `text.verbosity`, PTC, etc.).
3. **Enhanced Prompt**: The final ready-to-use prompt rendered in a code block, using the specific architecture template for the assessed level.
4. **Key Enhancements & Aggregation Rationale**: Summary explaining which rules were aggregated or omitted to optimize token efficiency and model execution performance.
