---
name: goal-prompt-writer
description: Create, review, or refine durable prompts for long-running coding work. Use when the user asks to turn a task, plan, or issue into a bounded execution objective, make long-running work safer, or define stopping conditions, checkpoints, and validation loops.
---

# Long-Running Task Prompt Writer

## Overview

Write compact, outcome-focused prompts that give an execution agent one clear
objective, bounded scope, verifiable completion criteria, and enough context to
keep working across turns without drift. The prompt should name the outcome,
relevant evidence, hard constraints, approval boundaries, and completion bar
without repeating every project rule.

Use the template in `references/goal-prompt-template.md` when the user wants a reusable example, a copy-ready prompt, or a structured artifact to save beside a plan.

## Workflow

1. Read the project's documented instructions when present. Open broader documentation only when the task's domain needs it. Identify the current baseline, applicable nested instructions, source-of-truth files, branch, and existing validation commands before drafting.
2. Extract the user's intended outcome, scope, constraints, validation commands, and stop condition. Preserve explicit user input over historical docs or generated plans.
3. If any business, auth policy, payment, schema, deployment, destructive, or architecture-critical choice is missing, ask one clarifying question before drafting.
4. Keep the primary objective concise. If instructions are longer, create or point to a detail file and make the primary prompt reference that file.
5. Prefer one objective. Split unrelated backlog items into separate goals or a plan followed by one goal.
6. Include independently verifiable checkpoints: tests, builds, logs, screenshots, diffs, migration status, or reviewable artifacts. Use repository-native commands and follow any repository-specific command requirements.
7. Permit safe, in-scope local reads, edits, and non-destructive validation when the goal authorizes implementation. Add approval gates for external writes, pushes, deployments, remote migrations, destructive commands, billing, credentials, production data, or material scope expansion.
8. State what the execution agent must not change. Do not copy the whole project instruction file; reference it and repeat only task-specific rules that affect behavior.
9. Require the agent to always update relevant documentation (e.g. plans, PRDs, architectural notes, or inline docs) to reflect the goal's executed changes before considering the goal complete.
10. End with a concrete stopping condition: complete when validation passes, the diff is reviewed and clean, and required repository artifacts and documentation are updated; pause and report if blocked by repeated failure or missing input.

## Prompt Shape

Write the prompt in this order:

1. Objective line: one sentence with the objective and observable done-when criteria.
2. `Context to read first`: paths, docs, issue links, logs, screenshots, plans, or commands to inspect.
3. `Scope`: allowed work and explicit non-goals.
4. `Constraints`: repo rules, safety gates, style, permissions, language, architecture, and user approvals.
5. `Checkpoints`: ordered milestones with evidence expected after each.
6. `Validation`: exact commands or artifacts that prove completion.
7. `Stop or ask when`: blockers, ambiguity, repeated failures, risky actions, or external dependencies.
8. `Progress reporting`: short updates naming current checkpoint, evidence, next action, remaining work, and blocker state. Report at major phase changes; do not narrate routine tool calls.

## Quality Bar

- Make every success criterion observable.
- Prefer paths and commands over vague references.
- Name the smallest validation loop that can prove progress before broader checks.
- Use accurate repository commands, instruction-file paths, and package names. Do not invent tests, scripts, routes, or migration names.
- Avoid open-ended wording such as "improve everything", "finish the app", or "do all remaining work" unless a linked plan defines those terms.
- Let the execution agent continue safe local work authorized by the prompt without unnecessary approval pauses. Require confirmation for external writes, destructive actions, purchases, credentials, production data, or material scope expansion.
- Do not ask the execution agent to push, deploy, merge, run remote migrations, or perform destructive actions unless the user explicitly requested that action in the prompt.
- If using a plan, make the prompt execute the plan, not reinterpret it.
