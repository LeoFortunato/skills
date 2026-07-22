# Long-Running Task Prompt Template

Use this format when creating a copy-ready prompt for a long-running task.

```markdown
Objective: Complete [single objective] without stopping until [observable done-when criteria], while staying within [scope boundary].

Context to read first:
- [Path, issue, plan, log, screenshot, review, or command output the execution agent must inspect before editing]
- [Any source of truth that overrides older docs]
- [Project instruction files, current branch, and existing validation commands when present]

Scope:
- Do: [specific allowed implementation, investigation, migration, or repair work], and update relevant documentation.
- Do not: [explicit non-goals and files/systems to leave untouched]

Constraints:
- Follow [repo rules, architecture constraints, language/style rules, product requirements].
- Proceed with safe local reads, edits, and non-destructive validation authorized by this prompt.
- Ask before [auth policy, payments, permissions, schema, production data, deployment, remote migrations, destructive commands, pushes, merges, PRs, credentials, or other external/high-risk action].
- Preserve [backward compatibility, user data, public API behavior, UI contract, migration rollback, etc.].
- Use repository-native commands and follow any repository-specific command requirements.

Checkpoints:
1. [Read/diagnose checkpoint]: report key findings and planned file touch list.
2. [Implementation checkpoint]: make the smallest coherent change and verify locally.
3. [Hardening checkpoint]: add or update tests, remove temporary code, and update relevant project documentation to reflect the executed changes.
4. [Final checkpoint]: review diff, summarize changed files, and prove done condition.

Validation:
- Run `[smallest relevant command]`.
- Run `[broader canonical command]` if the change touches shared behavior.
- Confirm [artifact/behavior/log/screenshot] shows [expected result].

Stop or ask when:
- The objective requires changing scope, product behavior, auth, schema, billing, deployment, or production data.
- The same blocker repeats after three attempts.
- Validation cannot run locally or fails for reasons outside this goal.
- Required context is unavailable or conflicts with explicit user instructions.

Progress reporting:
- Send a short preamble before the first tool call, then report only at major phase changes.
- For each checkpoint, report: current checkpoint, evidence gathered, next action, remaining work, and blocker state.
```

## Filled Example: This Repository

```markdown
Objective: Complete the approved authentication proxy migration without stopping until protected routes redirect correctly, public routes remain public, relevant checks pass, and the diff is clean; pause and report if required approval or context is missing.

Context to read first:
- Project instruction files
- Project documentation summary, when present
- `git branch --show-current`
- `git status --short`
- apps/web/src/proxy.ts
- apps/web/src/lib/auth/
- apps/web/src/lib/session/
- Existing auth tests under apps/web

Scope:
- Do: update proxy/auth flow only where needed for the migration, and update relevant auth documentation.
- Do not: change pricing, user roles, database schema, OAuth provider settings, unrelated UI, or files already modified by someone else.

Constraints:
- Treat current repository code and explicit user requirements as the source of truth; use historical PRD text only as context.
- Follow the project's application conventions, current session handling, and applicable nested instruction files.
- Use commands available in the project environment. Detect the current branch before platform-sensitive checks.
- Proceed with approved local reads, edits, tests, and diff review. Ask before changing auth policy, schema, remote migrations, deployment, pushes, merges, PRs, credentials, production data, or destructive state.
- Preserve the health-check endpoint as dependency-free.
- Keep user-facing strings in locale files and write implementation notes in technical English.
- After validation, create a small commit if the repository contract requires it; do not push.

Checkpoints:
1. Read the instruction chain and current auth flow; report the exact failing path and proposed file touch list.
2. Implement the smallest proxy/auth change without changing unrelated behavior.
3. Add or update focused tests for public and protected route behavior; remove temporary code; update relevant project documentation regarding the auth flow.
4. Run validation, review the diff, and create the required atomic commit.

Validation:
- Run `git branch --show-current` before tests or builds.
- If adding routes, route handlers, or proxy/middleware files, run `pnpm --filter @vistase/web exec next typegen` before type checking.
- Run `pnpm --filter @vistase/web run test`.
- Run `pnpm --filter @vistase/web run typecheck`.
- Run `git diff --check` and `git status --short`.
- Confirm protected routes redirect unauthenticated users and public routes do not.

Stop or ask when:
- The fix requires auth policy changes, database schema changes, provider dashboard changes, remote migrations, deployment, pushes, merges, PRs, or production credentials.
- Validation cannot run due to missing local dependencies.
- The same failure remains after three distinct fixes, or required instructions conflict.

Progress reporting:
- Send a short preamble before the first tool call. At each major checkpoint, report evidence, next action, remaining work, and blocker state; omit routine command narration.
```
