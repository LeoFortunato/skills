# Codex Goal Mode Prompt Reference Guide

This reference defines the model, parameters, rules, and prompt architecture for **Codex Goal Mode (`/goal` Mode)** tasks.

---

## 1. Task Scope & Characteristics

- **Use Cases**: Long-running, multi-turn, autonomous coding objectives executed via Codex Goal mode (`/goal <objective>`).
- **Primary Objective**: Provide Codex with one clear outcome, bounded context acquisition, verifiable completion criteria, tiered validation loops, and robust stopping conditions that maintain execution stability across turns without context drift.
- **Key Limit**: The `/goal` command line and core instructions must be non-empty and at most 4,000 characters. If instructions exceed 4,000 characters, create or reference a secondary details file.

---

## 2. Model & Parameter Configuration

- **Recommended Model**: `gpt-5.6-sol` (flagship frontier reasoning model for long-running agentic work).
- **Reasoning Effort (`reasoning.effort`)**: `high` (for standard multi-step coding/TDD goals) or `xhigh` (for complex architectural migrations or refactoring).
- **Reasoning Mode (`reasoning.mode`)**: `"standard"` (or `"pro"` for high-risk mission-critical tasks).
- **Text Verbosity (`text.verbosity`)**: `medium` (concise progress reporting at major checkpoints).
- **Programmatic Tool Calling (PTC)**: Optional; preserve standard tool contracts unless representative validation justifies PTC.

---

## 3. Core Rules & Guardrails

1. **Always Draft in Technical English**: Regardless of the user's input language, the final generated `/goal` prompt MUST be written strictly in English.
2. **Single Outcome & Observable Done Criteria**: State one clear, observable objective. Do not mix unrelated backlog items.
3. **Strict Context Boundaries**: Explicitly instruct Codex to inspect ONLY listed target paths/docs and prohibit broad codebase sweeps.
4. **Autonomous Local Work & Safety Gates**: Allow safe local reads, edits, and non-destructive validation. Require explicit user confirmation before external writes, pushes, merges, remote migrations, credentials, billing, or destructive actions.
5. **Tiered Validation Loop**: Order verification from targeted unit tests first, to typecheck/lint second, to broad canonical builds/checks last.
6. **Stopping Condition & Retries**:
   - If a blocker requires **user input, decision, authorization, or credentials**: block immediately and question the user.
   - If a blocker does **not** depend on the user (e.g., local test/build failure): test 3 times before pausing/blocking.
7. **UI / Frontend Guidelines**: Require preservation of existing design tokens, components, and responsive viewports (light and dark themes) without ad-hoc styling.
8. **Documentation Updates**: Instruct Codex to update relevant project documentation (e.g., plans, PRDs, inline docs) before marking the goal complete.

---

## 4. Codex `/goal` Prompt Structure & Template

Prompts constructed for Codex Goal Mode MUST follow this exact section sequence:

```markdown
/goal Complete [single objective] without stopping until [observable done-when criteria], while staying within [scope boundary].

Context to read first:
- [Explicit target path, issue, plan, log, screenshot, or command output Codex must inspect before editing]
- [AGENTS.md, current branch, and existing validation commands; read docs/SUMMARY.md only if the domain requires repository docs]

Scope:
- Do: [specific allowed implementation, investigation, migration, or repair work], and update relevant documentation.
- Do not: [explicit non-goals, files/systems to leave untouched; prohibit broad codebase sweeps and unrelated context acquisition]

Constraints:
- Follow [repo rules, architecture constraints, UI design system tokens, language/style rules, product requirements].
- Proceed with safe local reads, edits, and non-destructive validation authorized by this goal.
- Ask before [auth policy, payments, permissions, schema, production data, deployment, remote migrations, destructive commands, pushes, merges, PRs, credentials, or other external/high-risk action].
- Preserve [backward compatibility, user data, public API behavior, UI contract, responsive viewports across light/dark themes, etc.].
- Use repository-native commands and follow any repository-specific command requirements.

Checkpoints:
1. [Read/diagnose checkpoint]: report key findings and planned file touch list without reading unrelated context.
2. [Implementation checkpoint]: make the smallest coherent change and verify locally.
3. [Hardening checkpoint]: add or update tests, remove temporary code, and update relevant project documentation.
4. [Final checkpoint]: review diff, summarize changed files, and prove done condition.

Validation:
- Run `[targeted test command for changed behavior first]`.
- Run `[typecheck / lint commands]`.
- Run `[broader canonical command]` if touching shared behavior or before final completion.
- Confirm [artifact/behavior/log/screenshot/viewport] shows [expected result].

Stop or ask when:
- The blocker depends on user input, decision, authorization, credentials, scope expansion, or high-risk actions: block immediately and question the user.
- The blocker does not depend on the user (e.g., local test/build failure): test 3 times before pausing/blocking and asking for guidance.
- Validation cannot run locally or fails for reasons outside this goal.
- Required context is unavailable or conflicts with explicit user instructions.

Progress reporting:
- Send a short preamble before the first tool call, then report only at major phase changes.
- For each checkpoint, report: current checkpoint, evidence gathered, next action, remaining work, and blocker state.
```
