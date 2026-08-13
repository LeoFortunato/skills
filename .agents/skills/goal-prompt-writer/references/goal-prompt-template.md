# Goal Prompt Template

```markdown
/goal Complete [single observable objective] without stopping until [done condition], while remaining within [scope boundary].

Context to read first:
- [Authoritative instruction, code, test, configuration, plan, issue, or log]

Scope:
- Do: [specific authorized local work]
- Do not: [explicit non-goals, files, systems, or behaviors]

Constraints:
- Treat current code, configuration, tests, and explicit user instructions as truth over stale documentation.
- Preserve [public API, runtime behavior, dependencies, security boundary, or data contract].
- Ask before [destructive action, credentials, remote write, commit, push, deployment, production data, or material scope expansion].

Checkpoints:
1. Audit: report evidence and the exact intended file touch list.
2. Implement: make the smallest coherent change and run focused validation.
3. Finalize: run required broader checks and review the full diff.

Validation:
- Run `[exact focused command]`.
- Run `[exact broader command]` when required.
- Confirm [observable artifact or behavior].

Stop or ask when:
- Required evidence conflicts or a missing decision materially changes the result.
- Work requires an action outside the authorized scope.
- The same blocker remains after three distinct attempts.

Progress reporting:
- Send one short preamble, then report at named checkpoints with evidence, next action, remaining work, and blocker state.
```
