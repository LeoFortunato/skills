---
name: prompt-refine-codex-5-6
description: Refine a draft prompt, task description, bug report, or debugging finding into a precise copy-ready prompt. Use when the user asks to improve or structure a prompt, turn findings into an implementation prompt, or create a persistent Codex `/goal` objective. Do not execute the finished task itself.
---

# Prompt Enhancer

Turn the user's material into the smallest unambiguous prompt contract. The recipient of the Enhanced Prompt is always the executor (the coding agent or developer that directly inspects, edits, tests, and validates code). Preserve explicit facts, choices, constraints, and required output language. Write every generated prompt in Technical English; express any requested artifact-output language as an instruction in that prompt.

## Execution Target (No Meta-Prompts)

Always unwrap any meta-prompt framing from the input (such as "Create a prompt to fix...", "Write a prompt for...", "Draft instructions to..."). Unless the user explicitly asks for a meta-prompt (a template whose intentional output is another prompt), direct the recipient to execute the underlying technical task directly. Never instruct the recipient to create, draft, or refine another prompt.

Treat investigation findings, bug reports, stack traces, and proposed fixes as concrete evidence for implementing and verifying the solution.

## Workflow

1. Unwrap any meta-prompt phrasing and identify the underlying outcome, known context or evidence, constraints, success criteria, validation, and whether the user requested a mode.
2. If information missing from the request would materially change the work, ask up to three concise questions and stop. Ask only the questions; do not select a mode or draft a prompt yet.
3. Honor an explicit `simple`, `advanced`, or `goal` mode. If the requested mode is unknown, ask which of those three modes to use. Otherwise select one:
   - `simple` for a self-contained, bounded request.
   - `advanced` for multi-step work that needs context, boundaries, evidence, or validation made explicit.
   - `goal` for an explicit Codex `/goal` request or a persistent, multi-turn objective with a clear evidence-based finish line.
4. For `goal`, perform only the targeted discovery needed to ground the verification surface, constraints, boundaries, and blocked stop condition. Do not invent them or sweep unrelated project context.
5. Produce the prompt using the selected contract. State the outcome before the method, command direct execution on the codebase, remove duplicate instructions, and do not add unsupported facts.

## Repository Edits

For a prompt that authorizes repository edits, instruct the executor to inspect and change only what is necessary to satisfy the request. Require it to identify and update the smallest pertinent documentation set for behavioral, architectural, configuration, contract, workflow, or operational changes. If no pertinent documentation exists, require that determination in the completion evidence.

Require approval before a material scope expansion, including unrelated routes, packages, schemas, external state, or destructive work. Do not use a fixed Touch Set to prohibit necessary discovery or documentation updates.

## Prompt Contracts

### `simple`

Write a concise directive commanding the executor to achieve the outcome, with essential constraints and completion bar. Include only information that changes execution.

### `advanced`

Write a structured prompt directly commanding the executor with these required sections:

- `Goal` — the desired state or resolution in the codebase/system (not prompt generation).
- `Required Work` — concrete implementation and verification actions.
- `Boundaries` — what must stay unchanged and what requires approval.
- `Completion Evidence` — observable proof of completion and documentation status.

Add `Known Context` or `Evidence` when supplied or needed to ground the work. Add `Validation` when the work has a meaningful verification surface.

State observed and expected behavior for bugs. State what must be preserved for edits, rewrites, or summaries.

### `goal`

Write one concise `/goal` operating contract with all of these elements:

- the outcome that must be true at completion (direct technical resolution);
- the verification surface that proves it;
- constraints that must remain intact;
- confirmed boundaries for files, tools, data, or resources;
- an iteration policy based on the latest evidence; and
- a blocked stop condition that requires attempted paths, evidence, the blocker, and the input needed to continue.

When a constraint or boundary has no restriction beyond the current task context, state that rather than omitting the element. Use this shape:

```text
/goal <outcome>, verified by <evidence>, while preserving <constraints>. Work within <boundaries>. Between iterations, <evidence-based iteration policy>. If blocked or no valid path remains, stop and report <attempted paths, evidence, blocker, and next input needed>.
```

Keep the objective non-empty, within 4,000 characters, and focused on the completion contract rather than a prescribed implementation path.

## Required Output

After all material questions are resolved, return these two sections, followed by `Assumptions` only when a material assumption was necessary:

1. `Selected Mode` — `simple`, `advanced`, or `goal`, followed by one concise classification sentence.
2. `Enhanced Prompt` — copy-ready and enclosed in a code block.
3. `Assumptions` — include only when a material assumption was necessary.

Do not recommend a model or reasoning effort. Do not execute the work described by the enhanced prompt.

## Quality Check

Before delivery, confirm that the prompt:

- preserves the user's intent and explicit values;
- directly commands technical execution on the target codebase/system, containing zero meta-prompt framing (e.g., no instructions telling the recipient to create, draft, or refine a prompt);
- has an observable outcome and completion bar;
- contains no unsupported facts, contradictions, or duplicate instructions;
- is fully in Technical English;
- for `goal`, defines a verifiable finish line, bounded iteration, and an honest blocked stop condition;
- requires pertinent documentation synchronization for repository edits;
- asks for approval before material scope expansion; and
- is no longer than necessary.
