---
name: prompt-refine
description: Refine a draft prompt, task description, bug report, or debugging finding into a precise copy-ready prompt. Use when the user asks to improve or structure a prompt, turn findings into an implementation prompt, or create a persistent goal mode objective. Do not execute the finished task itself.
metadata:
  author: Leonardo Fortunato
  license: MIT
---

# Prompt Refine

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
   - `goal` for an explicit `/goal` request or a persistent, multi-turn objective with a clear evidence-based finish line.
4. For `goal`, execute token-efficient target discovery before drafting:
   - **Trust User Inputs:** If the user's draft already specifies exact file paths, target modules, or validation commands, adopt them directly without redundant re-reading.
   - **Targeted Verification:** Verify unconfirmed paths and commands using targeted discovery (`list_dir`, `grep_search`, small line-range reads). Never invent paths, scripts, or validation commands.
   - **Narrow Scope:** Focus strictly on direct touch sets, authoritative sources of truth, native validation commands, and pertinent documentation. Avoid sweeping unrelated files or test suites.
5. Produce the prompt using the selected contract. State the outcome before the method, command direct execution on the codebase, remove duplicate instructions, and do not add unsupported facts.

## Repository Edits

For a prompt that authorizes repository edits, instruct the executor to inspect and change only what is necessary to satisfy the request. Require it to identify and update the smallest pertinent documentation set for behavioral, architectural, configuration, contract, workflow, or operational changes. If no pertinent documentation exists, require that determination in the completion evidence.

Require approval before a material scope expansion, including unrelated routes, packages, schemas, external state, credentials, or destructive work.

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

Produce one self-contained, outcome-first `/goal` operating contract that can continue across turns without widening authority. Focus on the observable destination, verifiable completion criteria, scope boundaries, and stopping rules rather than over-prescribing intermediate steps.

Core requirements for `/goal`:
- **Outcome-First:** Clearly define the observable objective and done criteria.
- **Touch Set Governance:** Enforce confirmed in-scope paths (`Modify` / `Add`). Prohibit inspecting or modifying files outside this touch set without prior approval, with the sole exception of mandatory documentation synchronization.
- **Documentation Synchronization:** Require identifying and updating the pertinent documentation describing changes made, or explicitly stating in the completion evidence that no pertinent documentation exists.
- **Safety Gates (*Ask Before*):** Place commits, pushes, deployments, remote writes, credentials, production data, destructive actions, and material scope expansion behind explicit user approval.
- **Repository-Native Validation:** Specify exact native commands (tests, linter, typecheck, build). Require fallback evidence reporting if a check cannot run.
- **Honest Stopping Conditions:** Require stopping and asking when required decisions/credentials are missing, requirements conflict, or the same blocker persists after three distinct attempts.
- **Length Constraint:** Keep the objective non-empty and strictly within 4,000 characters. Put longer specifications or briefs in a referenced file and point the goal to that file.

#### `/goal` Template

```markdown
/goal [Complete one observable outcome]. Done when [verification criteria].

Context:
- Source of truth: [Exact plan, brief, issue, or authoritative file path.]
- Primary targets: [Exact confirmed source or configuration paths.]

Expected touch set:
- Modify: [Exact confirmed existing paths.]
- Add: [Exact confirmed new paths, if any.]
- Do NOT inspect or edit files outside this touch set without prior user approval, except for mandatory documentation synchronization below.
- Documentation synchronization: identify and update the pertinent documentation describing changes made, or explicitly record that no pertinent documentation exists.

Constraints:
- Treat current code, configuration, tests, and explicit user instructions as truth over stale documentation.
- Preserve [public API, runtime behavior, data contract, or invariants].
- Ask before [destructive action, credentials, remote write, commit, push, deployment, production data, or material scope expansion].

Validation:
- Run `[exact repository-native validation command]`.
- Confirm [observable artifact or behavior].
- If a check cannot run, report why and provide the next-best evidence.

Stop and ask:
- A required user decision, credential, authorization, or conflicting requirement is missing.
- Work requires an action outside authorized scope, or the same blocker persists after three distinct attempts.
```

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
- for `goal`, includes target paths and native validation grounded via token-efficient discovery;
- for `goal`, enforces touch set boundaries with mandatory documentation synchronization;
- for `goal`, defines explicit *ask-before* gates for destructive actions, credentials, remote operations, and scope expansions;
- for `goal`, provides verifiable finish lines with fallback evidence rules and honest stop-and-ask conditions (including a blocker threshold);
- for `goal`, keeps the objective strictly within 4,000 characters;
- requires pertinent documentation synchronization for repository edits;
- asks for approval before material scope expansion; and
- is no longer than necessary.
