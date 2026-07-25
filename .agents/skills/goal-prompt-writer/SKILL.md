---
name: goal-prompt-writer
description: Create, review, or refine durable Codex `/goal` prompts for long-running coding work. Use when the user asks to write a Goal mode prompt, convert a task/plan/issue into `/goal`, make a long-running Codex objective safer, define stopping conditions, checkpoints, validation loops, or prepare instructions that Codex should pursue until completion.
---

# Goal Prompt Writer

## Overview

Write compact, outcome-focused `/goal` prompts in English that give Codex one clear objective, bounded scope, verifiable completion criteria, and enough context to keep working across turns without drift. GPT-5.6 responds best when the prompt names the outcome, relevant evidence, hard constraints, approval boundaries, and completion bar without repeating every repository rule.

Use the template in `references/goal-prompt-template.md` when the user wants a reusable example, a copy-ready prompt, or a structured artifact to save beside a plan.

## Workflow

1. Read `AGENTS.md` when present. Use its conditional router and open `docs/SUMMARY.md` only when the goal's domain needs repository documentation. Identify the current baseline, applicable nested instructions, source-of-truth files, branch, and existing validation commands before drafting.
2. Extract the user's intended outcome, scope, constraints, validation commands, and stop condition. Preserve explicit user input over historical docs or generated plans.
3. Always draft the generated `/goal` prompt in English (technical English), regardless of the user's input language.
4. If any business, auth policy, payment, schema, deployment, destructive, or architecture-critical choice is missing, ask one clarifying question before drafting.
5. Keep the `/goal` objective under 4,000 characters. If instructions are longer, create or point to a detail file and make the `/goal` reference that file.
6. Prefer one objective. Split unrelated backlog items into separate goals or a plan followed by one goal.
7. Include independently verifiable checkpoints: tests, builds, logs, screenshots, diffs, migration status, or reviewable artifacts. Use repository-native commands and follow any repository-specific command requirements.
8. Permit safe, in-scope local reads, edits, and non-destructive validation when the goal authorizes implementation. Add approval gates for external writes, pushes, deployments, remote migrations, destructive commands, billing, credentials, production data, or material scope expansion.
9. Explicitly bound context acquisition: instruct Codex to inspect only listed target files and stop retrieval as soon as necessary task evidence is gathered. Prohibit broad codebase sweeps and reading unrelated documentation.
10. For UI/frontend goals, require preservation of existing design tokens, components, and responsive viewports (e.g. expanded vs rail, light vs dark themes) without ad-hoc styling.
11. State what Codex must not change. Do not copy the whole `AGENTS.md`; reference it and repeat only task-specific rules that affect behavior. State each constraint once in a lean, declarative manner.
12. Require the agent to always update relevant documentation (e.g. plans, PRDs, architectural notes, or inline docs) to reflect the goal's executed changes before considering the goal complete.
13. End with a concrete stopping condition: complete when validation passes, the diff is reviewed and clean, and required repository artifacts and documentation are updated. If the blocking task requires user input, decisions, authorization, or credentials, block immediately and question the user; if the blocking activity does not depend on the user, test 3 times before pausing/blocking.

## Prompt Shape

Write the prompt in this order (always in English):

1. `/goal` line: one sentence with objective and observable done-when criteria.
2. `Context to read first`: paths, docs, issue links, logs, screenshots, plans, or commands to inspect. Note explicitly not to load unrelated context.
3. `Scope`: allowed work and explicit non-goals (including context acquisition boundaries).
4. `Constraints`: repo rules, safety gates, style, permissions, language, architecture, UI design system tokens, and user approvals.
5. `Checkpoints`: outcome-focused milestones with evidence expected after each (avoid micromanaging tool mechanics).
6. `Validation`: tiered commands starting with targeted tests, then typecheck/lint, and broad checks last.
7. Stop or ask when: specify to test 3 times before blocking if the blocker does not depend on the user; if the blocker requires user input, decision, authorization, or credentials, block immediately and question the user.
8. `Progress reporting`: short updates naming current checkpoint, evidence, next action, remaining work, and blocker state. Report at major phase changes; do not narrate routine tool calls.

## Quality Bar

- Always write the generated `/goal` prompt in English.
- Make every success criterion observable and outcome-first.
- Restrict context acquisition explicitly: instruct Codex to read only target paths and avoid broad codebase sweeps.
- Prefer paths and commands over vague references.
- Use a tiered validation loop: targeted tests for changed behavior first, then type checks / lint, then broad checks.
- For UI tasks, preserve existing design tokens and verify responsive states across light and dark themes.
- Use accurate repository commands, instruction-file paths, and package names. Do not invent tests, scripts, routes, or migration names.
- Avoid open-ended wording such as "improve everything", "finish the app", or "do all remaining work" unless a linked plan defines those terms.
- Let Codex continue safe local work authorized by the goal without unnecessary approval pauses. Require confirmation for external writes, destructive actions, purchases, credentials, production data, or material scope expansion.
- Explicitly distinguish stopping behavior: test 3 times before blocking if the blocker does not depend on the user, but block immediately and question the user if the blocking task requires user input, decision, authorization, or credentials.
- Do not ask Codex to push, deploy, merge, run remote migrations, or perform destructive actions unless the user explicitly requested that action in the goal.
- If using a plan, make the goal execute the plan, not reinterpret it.

## Official Guidance To Apply

- Codex Goal mode is for work bigger than one prompt but smaller than an open-ended backlog; goals need achievement, non-goals, validation, and stop criteria.
- `/goal <objective>` sets the active task goal; `/goal`, `/goal edit`, `/goal pause`, `/goal resume`, and `/goal clear` manage it.
- Model selection & effort: For long-running `/goal` execution requiring TDD, layout refactoring, or multi-step changes, recommend **GPT-5.6 Sol** with **High reasoning effort**.
- The goal text becomes the first prompt and the completion criteria. Include outcome, constraints, and verification rather than only a list of activities.
- Starting a goal does not broaden sandbox or approval boundaries. Keep external coordination and high-risk actions behind explicit approval gates.
- Goal objectives must be non-empty and at most 4,000 characters; longer instructions should live in a new file referenced by the goal.
- Strong GPT-5.6 prompts are lean and outcome-oriented: state each instruction once, include only relevant tools and context, and define the evidence and success criteria needed to finish.
- GPT-5.6 can act proactively across multiple steps. Name safe local actions explicitly and require confirmation before external, destructive, costly, or scope-expanding actions.
- For long-running work, give a short preamble before the first tool call and sparse updates at major phase changes. Preserve the goal, constraints, and validation loop across compaction or resumed turns.
- For GPT-5.6 model migrations, preserve the existing endpoint, tool, output, and reasoning contract first. Do not add Pro mode, persisted reasoning, explicit caching, Programmatic Tool Calling, or multi-agent behavior unless the goal explicitly includes it or representative validation justifies it.
- For current OpenAI guidance, see [Using GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model.md) and [Prompting guidance for GPT-5.6 Sol](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6.md).
- For current Goal mode behavior, see [Long-running work](https://learn.chatgpt.com/docs/long-running-work.md).

