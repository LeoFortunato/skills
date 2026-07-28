---
name: prompt-enhancer-gpt-5-6
description: Refine, review, or structure a draft prompt for GPT-5.6 Sol, Terra, or Luna, including Codex `/goal` objectives with read-only discovery of the relevant project files. Use when the user invokes this skill with a simple prompt, asks to improve a prompt, or wants requirements turned into a copy-ready prompt with a required route, model, and reasoning-effort recommendation. Do not use merely to execute the task described by a finished prompt.
---

# Prompt Enhancer for GPT-5.6 and Codex Goals

Transform a draft prompt or task description into the smallest reliable prompt
contract. Preserve the user's intent, facts, required structure, language, and
explicit choices.

## Workflow

### 1. Analyze the Draft

Identify the information that can materially change the result:

- intended outcome or artifact;
- relevant context and inputs;
- constraints and permission boundaries;
- success criteria and validation;
- output format, audience, and language;
- whether the user wants a standard prompt or a persistent Codex `/goal`.

Do not execute the task described by the draft. Refine the prompt itself.

### 2. Resolve Material Gaps

Ask one to three concise questions only when a missing answer would materially
change the prompt and no safe assumption is available.

If questions are necessary:

1. ask only the questions;
2. do not select a route or draft the final prompt yet;
3. end the response and wait for the user's answers.

If no material question is necessary, continue without an interview. State a
material assumption in the final output only when it helps the user review the
result.

### 3. Select Exactly One Route

Choose by task shape, consequence, and execution pattern. Read only the matching
reference:

- **Level 1 — focused and repeatable:**
  `references/level-1-low-complexity.md`
- **Level 2 — routine multi-step work:**
  `references/level-2-medium-complexity.md`
- **Level 3 — complex or high-consequence work:**
  `references/level-3-high-complexity.md`
- **Codex `/goal` — persistent long-running objective:**
  `references/goal-mode-codex.md`

The four entries above are the complete creation router. Model choice is an
output of the selected route, not another route.

For the Codex `/goal` route, complete the reference's bounded, read-only target
discovery before constructing the prompt. Do not draft a Goal prompt from
guessed file paths or validation commands.

If the user provides a working production prompt with failure traces or
evaluations, preserve its architecture and make the smallest targeted change
that addresses the demonstrated failure.

### 4. Construct the Prompt

Follow the selected reference and use only sections that change behavior.
Describe the desired result before prescribing a process. State each instruction
once and remove contradictions, obsolete scaffolding, and irrelevant rules.

For editing, rewriting, or summarization, state what must be preserved before
describing improvements. For grounded work, define the required evidence and
what to do when evidence is missing.

Preserve the draft's language unless the user requests another language. For a
Codex `/goal`, write the generated objective in Technical English.

### 5. Select Model and Reasoning Effort

Always select one GPT-5.6 model and one reasoning effort using the loaded route
reference and the actual task. Prefer the lowest effort that reliably meets the
quality bar.

Preserve an explicitly requested model or effort. Keep the recommendation
outside the enhanced prompt: model and effort are execution choices, not prose
to insert into the prompt body.

Do not add setup instructions or unrelated runtime configuration.

## Required Output

After any necessary questions have been answered, return exactly these sections:

1. **Selected Route** — route name plus one concise sentence explaining the
   classification.
2. **Recommended Model** — one of `gpt-5.6-luna`, `gpt-5.6-terra`, or
   `gpt-5.6-sol`.
3. **Reasoning Effort** — one effort suitable for the active Codex surface and
   task.
4. **Enhanced Prompt** — ready to copy and use, enclosed in a code block.
5. **Assumptions** — include only when a material assumption was necessary.

Never omit the selected route, model, reasoning effort, or enhanced prompt.
Keep the route explanation concise and do not add configuration that the user
did not request.

For a Codex goal, keep the objective non-empty and within 4,000 characters. Put
longer implementation details in a referenced file.

## Quality Check

Before delivery, confirm that the result:

- preserves the user's intent and explicit values;
- uses exactly one of the four routes;
- reflects the loaded route reference;
- has an observable outcome and completion bar;
- contains no duplicate or contradictory instructions;
- recommends exactly one model and one reasoning effort;
- for a Codex `/goal`, includes confirmed target paths from the required
  read-only discovery;
- is no longer than necessary.
