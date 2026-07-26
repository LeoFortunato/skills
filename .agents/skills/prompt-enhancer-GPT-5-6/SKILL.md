---
name: prompt-enhancer-GPT-5-6
description: Improve, review, or structure prompts for GPT-5.6 Sol, Terra, and Luna, including Codex `/goal` objectives. Use when the user asks to refine a prompt or turn requirements into a ready-to-use prompt. Do not use merely to execute a task, answer a general OpenAI documentation question, or select a model when no prompt work is requested.
---

# Prompt Enhancer for GPT-5.6 and Codex Goals

Transform a draft prompt or task description into the smallest prompt contract
that reliably expresses the intended outcome. Preserve the user's intent,
facts, required structure, language, and target surface.

## Operating Principles

- Describe the desired result before prescribing a process.
- State each instruction once. Remove repetition, obsolete scaffolding, and
  contradictions.
- Keep only context, constraints, examples, tools, and validation rules that
  change behavior.
- Use absolute language only for true invariants. Use decision rules for
  judgment calls.
- Do not claim that a rewrite improves quality, latency, or cost without
  representative evaluation evidence.
- Treat official OpenAI documentation as authoritative for current model names,
  API fields, feature availability, and Codex behavior. Treat community advice
  as anecdotal unless it is validated by official guidance or evaluations.

## Workflow

### 1. Identify the Prompt Surface

Determine whether the requested artifact is:

- a standard ChatGPT or Codex prompt;
- an OpenAI API prompt, possibly with request configuration; or
- a Codex `/goal` objective for long-running work.

Preserve an explicitly requested model or surface. If the user asks for a
current model recommendation or API configuration, verify it against current
official OpenAI documentation when live documentation is available. Otherwise,
avoid claims of currentness and label any unverified recommendation.

Keep surface controls separate:

- `reasoning.effort`, `reasoning.mode`, `text.verbosity`, and Programmatic Tool
  Calling are API configuration or runtime capabilities, not prose that must be
  inserted into every prompt.
- Codex model and reasoning choices are surface settings. Do not present API
  request fields as Codex `/goal` syntax.

### 2. Resolve Only Material Gaps

Check for the information that can change the result:

- outcome or artifact;
- relevant context and inputs;
- required constraints or permission boundaries;
- success criteria and validation;
- output format, audience, or language.

Ask one to three concise questions only when the missing answer would materially
change the prompt and a safe assumption is not available. Otherwise, state the
important assumption briefly and continue. Do not require an interview or make
the user complete a fixed questionnaire.

### 3. Select One Route

Choose by task shape, risk, and execution surface rather than prompt length.
Read only the matching reference:

- **Level 1 — focused and repeatable:** `references/level-1-low-complexity.md`
- **Level 2 — routine multi-step work:** `references/level-2-medium-complexity.md`
- **Level 3 — complex or high-consequence work:**
  `references/level-3-high-complexity.md`
- **Codex `/goal`:** `references/goal-mode-codex.md`

If the user provides a working production prompt and failure traces or evals,
preserve its architecture and make the smallest targeted change that addresses
the measured failure. Do not rewrite the complete prompt stack by default.

### 4. Construct the Prompt

Use only the sections the task needs. A useful order for non-trivial prompts is:

1. goal;
2. context or evidence;
3. success criteria;
4. constraints and side-effect boundaries;
5. tools or retrieval rules, when relevant;
6. output requirements;
7. validation and stopping conditions.

Add a role only when domain framing changes behavior. Add personality or
collaboration guidance only when user experience or interaction policy matters.
Keep both short.

For editing, rewriting, or summarization, state what must be preserved before
describing improvements. For grounded work, require support for material claims
and define what to do when evidence is missing.

### 5. Add Configuration Only When Useful

If the user requests model or API guidance, use the loaded route reference.
Prefer the lowest setting that meets the quality bar. Recommend higher effort,
Pro mode, or Programmatic Tool Calling only when the task shape or
representative evaluations justify the additional cost and complexity.

## Output

Default to:

1. **Enhanced Prompt** — ready to copy and use.
2. **Notes** — only material assumptions, surface-specific configuration, or
   substantive changes that the user should know.

Omit classification labels, model settings, and rationale when they do not help
the user. If settings are included, label whether they apply to the OpenAI API
or to a Codex surface.

For a Codex goal, return the `/goal` objective in Technical English as this
skill's output convention. Keep the goal objective non-empty and within 4,000
characters. Put longer implementation details in a referenced file.

## Routing Examples

Use this skill for:

- "Improve this support-agent system prompt."
- "Turn these API workflow requirements into a GPT-5.6 prompt."
- "Create a `/goal` objective from this implementation brief."
- "Review this prompt against GPT-5.6 guidance."

Do not use this skill for:

- executing the task described by an already-final prompt;
- general OpenAI product documentation with no prompt artifact;
- a model migration that requires code or API changes beyond prompt text;
- ordinary copyediting when the text is not a prompt.

## Quality Check

Before delivery, confirm that the prompt:

- preserves the user's intent and explicit values;
- has an observable outcome and completion bar;
- contains no duplicate or contradictory instructions;
- uses only material constraints and available capabilities;
- labels surface-specific settings and does not overstate unverified facts;
- is no longer than necessary.
