---
name: prompt-enhancer-gpt-5-6
description: Refine, review, or structure a draft prompt or turn bug reports, debug findings, and proposed fixes into a precise prompt for GPT-5.6 Sol, Terra, or Luna, including Codex `/goal` objectives with token-efficient discovery of relevant project files. Use when the user asks to improve a prompt, convert debug findings or erroneous behavior into a structured fix prompt, or turn requirements into a copy-ready prompt with a required route, model, and reasoning-effort recommendation. Do not use merely to execute the task described by a finished prompt.
---

# Prompt Enhancer for GPT-5.6 and Codex Goals

Transform a draft prompt, task description, bug report, or debug investigation finding (e.g., erroneous behavior, stack trace, or proposed fix discovered during debugging) into the smallest reliable prompt contract. When the input describes a bug or unexpected behavior discovered during debugging, extract the observed defect, the expected behavior, and the target touch set into a structured prompt instructing how to implement the proposed fix. Preserve the user's intent, facts, required structure, and explicit choices. Generate every enhanced prompt in Technical English, regardless of the draft's language. Preserve any requirement for the task's own output language as an instruction written in Technical English.

## Workflow

### Guardrails for Token-Efficient Discovery

1. **Trust User Inputs:** If the user's draft already specifies exact file paths, target modules, or validation commands, treat them as the initial targets without re-reading solely to confirm them. Inspect additional context when correctness requires it.
2. **Minimal Target Verification:** When target files or validation commands must be resolved (e.g., in Codex `/goal` mode), start with lightweight listing (`list_dir`) or targeted searches (`grep_search`) and expand discovery only when needed for correctness or validation.
3. **Targeted File Reading:** Start with the smallest relevant line ranges (e.g., headers, exports, or target function signatures). Read broader or full files when dependencies, behavior, or validation cannot be established safely from narrower context.
4. **No Unrelated Sweeps:** Avoid general documentation, unrelated dependencies, and large test suites unless they are required for correctness, evidence, or validation.
5. **Targeted Documentation Synchronization:** For prompts that authorize repository edits, require a bounded search for the smallest set of pertinent documentation tied to the changed behavior, architecture, configuration, contract, workflow, or operations. Do not scan unrelated documentation.

### 1. Analyze the Input / Draft

The input may be a draft prompt, raw requirements, or debug findings (e.g., observed errors, stack traces, or proposed bug fixes discovered during debugging). Identify the information that can materially change the result:

- intended outcome, bug fix, or target artifact;
- observed vs. expected behavior (when handling debug findings or bug reports);
- relevant context, inputs, and failure traces;
- constraints, touch set (in-scope files/directories), and permission boundaries;
- pertinent documentation that must stay synchronized with the requested edit;
- success criteria and validation;
- output format, audience, and language;
- whether the user wants a standard prompt or a persistent Codex `/goal`.

Do not execute the task or apply the bug fix directly. Refine the prompt itself.

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

For the Codex `/goal` route, complete a token-efficient target discovery (verifying exact paths and validation commands with targeted reads) before constructing the prompt. Expand beyond targeted reads when correctness or validation requires broader context. Do not draft a Goal prompt from guessed file paths or validation commands.

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

For code modifications or file operations, strictly enforce scope boundaries by
defining an explicit Touch Set (confirmed in-scope paths). Include an explicit
instruction forbidding the recipient from inspecting or modifying files outside
this Touch Set without prior user approval, except for the mandatory
documentation-synchronization requirement below. Require the recipient to
identify and update the smallest set of pertinent project documentation that
describes any behavior, architecture, configuration, contract, workflow, or
operational change made, even when those documentation paths were not in the
original Touch Set. Treat only those necessary documentation paths as an
authorized Touch Set extension; unrelated files remain prohibited. If no
pertinent documentation exists, require the recipient to state that
determination in the completion evidence. This documentation exception
supersedes any route template's blanket prohibition on out-of-Touch-Set edits;
it does not authorize unrelated source, test, or asset changes.

Translate the draft faithfully and write every generated prompt, including a
Codex `/goal` objective, in Technical English. Do not retain or accept a
different language for the enhanced prompt.

### 5. Select Model and Reasoning Effort

Always select one GPT-5.6 model and one reasoning effort using the loaded route
reference and the actual task. Prefer the lowest effort that reliably meets the
quality bar.

Preserve an explicitly requested model or effort. Keep the recommendation
outside the enhanced prompt: model and effort are execution choices, not prose
to insert into the prompt body.

Do not add setup instructions or unrelated runtime configuration.

### Skill-Maintenance Validation

When creating or materially revising this skill, run a representative black-box
validation matrix before claiming completion:

- a direct request that should activate the skill;
- an indirect request expressing the same workflow;
- an incomplete request that should trigger a material follow-up question;
- a negative request that should not execute a finished task; and
- an edge case involving missing paths, evidence, or validation commands.

Review activation, route selection, model and effort recommendation, required
output structure, and no-invention or stop behavior. Record pass/fail evidence;
frontmatter validation alone is not sufficient.

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
- strictly limits scope to the declared Touch Set plus only the mandatory pertinent-documentation extension, prohibiting unrelated out-of-scope inspection or edits without prior approval;
- requires pertinent documentation to be updated for every authorized repository edit, even when those documentation paths are outside the original Touch Set, or requires an explicit no-pertinent-documentation determination;
- has an observable outcome and completion bar;
- contains no duplicate or contradictory instructions;
- writes the enhanced prompt entirely in Technical English;
- recommends exactly one model and one reasoning effort;
- for a Codex `/goal`, includes target paths confirmed via token-efficient discovery;
- when the skill was created or materially revised, representative direct, indirect, incomplete, negative, and edge cases were exercised and reviewed;
- avoided unnecessary full-file reads and broad repository sweeps;
- is no longer than necessary.
