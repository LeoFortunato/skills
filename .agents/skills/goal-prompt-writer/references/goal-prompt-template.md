# Goal Prompt Template

Use this format when creating a copy-ready Codex Goal mode prompt. Prompts created using this template must always be written in English.

```markdown
/goal Complete [single objective] without stopping until [observable done-when criteria], while staying within [scope boundary].

Context to read first:
- [Path, issue, plan, log, screenshot, PR, or command output Codex must inspect before editing]
- [Any source of truth that overrides older docs]
- [AGENTS.md, current branch, and existing validation commands; read docs/SUMMARY.md only if the domain requires repository docs]

Scope:
- Do: [specific allowed implementation, investigation, migration, or repair work], and update relevant documentation.
- Do not: [explicit non-goals, files/systems to leave untouched, and do not perform broad codebase sweeps or acquire unrelated context]

Constraints:
- Follow [repo rules, architecture constraints, UI design system tokens, language/style rules, product requirements].
- Proceed with safe local reads, edits, and non-destructive validation authorized by this goal.
- Ask before [auth policy, payments, permissions, schema, production data, deployment, remote migrations, destructive commands, pushes, merges, PRs, credentials, or other external/high-risk action].
- Preserve [backward compatibility, user data, public API behavior, UI contract, responsive viewports across light/dark themes, migration rollback, etc.].
- Use repository-native commands and follow any repository-specific command requirements.

Checkpoints:
1. [Read/diagnose checkpoint]: report key findings and planned file touch list without reading unrelated context.
2. [Implementation checkpoint]: make the smallest coherent change and verify locally.
3. [Hardening checkpoint]: add or update tests, remove temporary code, and update relevant project documentation to reflect the executed changes.
4. [Final checkpoint]: review diff, summarize changed files, and prove done condition.

Validation:
- Run `[targeted test command for changed behavior first]`.
- Run `[typecheck / lint commands]`.
- Run `[broader canonical command]` if the change touches shared behavior or before final completion.
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

## Filled Example: This Repository

```markdown
/goal Complete the approved Next.js auth proxy migration without stopping until protected routes redirect correctly, public routes remain public, relevant web checks pass, and the diff is clean; pause and report if required approval or context is missing.

Context to read first:
- AGENTS.md
- docs/SUMMARY.md
- `git branch --show-current`
- `git status --short`
- apps/web/src/proxy.ts
- apps/web/src/lib/auth/
- apps/web/src/lib/supabase/
- Existing auth tests under apps/web

Scope:
- Do: update proxy/auth flow only where needed for the migration, and update relevant auth documentation.
- Do not: change pricing, user roles, database schema, OAuth provider settings, unrelated UI, or files already modified by someone else.

Constraints:
- Treat current repository code and explicit user requirements as the source of truth; use historical PRD text only as context.
- Follow App Router conventions, current Supabase SSR cookie handling, and applicable nested `AGENTS.md` files.
- Use native shell commands. Detect the current branch before platform-sensitive checks; staging targets arm64 and main targets amd64.
- Proceed with approved local reads, edits, tests, and diff review. Ask before changing auth policy, schema, remote migrations, deployment, pushes, merges, PRs, credentials, production data, or destructive state.
- Preserve `/api/health` as dependency-free.
- Keep user-facing strings in locale files and write implementation notes in technical English.
- After validation, create a small Conventional Commit if the repository contract requires it; do not push.

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
- The blocker depends on user input or authorization (e.g., auth policy changes, database schema changes, provider dashboard changes, remote migrations, deployment, pushes, merges, PRs, or production credentials): block immediately and question the user.
- The blocker does not depend on the user (e.g., local test or build failure): attempt/test 3 times before pausing/blocking.
- Validation cannot run due to missing local dependencies.
- Required instructions conflict.

Progress reporting:
- Send a short preamble before the first tool call. At each major checkpoint, report evidence, next action, remaining work, and blocker state; omit routine command narration.
```
