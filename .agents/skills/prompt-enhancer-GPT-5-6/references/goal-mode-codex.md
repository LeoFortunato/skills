# Codex `/goal` Prompt Reference

Use this route for one persistent, long-running objective in a Codex task. The
goal text acts as both the first prompt and the completion criteria.

## Product Constraints

- The goal objective must be non-empty and no longer than 4,000 characters.
- Put longer requirements in a file and point the goal to that file.
- Starting a goal does not expand sandbox, approval, credential, or access
  permissions.
- Model and reasoning choices are Codex surface settings, not `/goal` syntax.

Write the generated goal in Technical English as this skill's convention. Do not
present English as a Codex product requirement.

## Construction Rules

- State one outcome rather than combining unrelated backlog items.
- Include constraints only when they prevent a material failure.
- Define verification that lets Codex determine when the goal is complete.
- Point to the context that should be read first when it is not obvious.
- Allow safe in-scope local work when the user's request authorizes changes.
- Require confirmation for external, destructive, costly, or materially
  scope-expanding actions that the user has not already authorized.
- Add milestones or progress rules only when they help the user supervise a
  long task.
- Do not add generic requirements that are unrelated to the goal.

If the outcome is materially ambiguous, ask the smallest necessary question
before drafting the goal. Do not use a long interview by default.

## Optional Codex Model Guidance

Provide this only when the user asks:

- Sol: complex, open-ended, or high-value goals that need additional judgment
  and polish.
- Terra: everyday implementation and tool-using work.
- Luna: clear, repeatable, high-volume work with a well-defined result.
- Start with the lowest reasoning level that meets the quality bar. Medium is a
  balanced starting point; raise it for difficult work when the result justifies
  the added time and usage.

Do not attach API-only fields such as `reasoning.mode` or `text.verbosity` to the
`/goal` command.

## Compact Template

```markdown
/goal [Complete one observable outcome]. Done when [verification criteria].

Context:
- [File, issue, plan, log, screenshot, or command output to inspect first.]

Scope:
- Do: [authorized work needed for the outcome.]
- Do not: [material non-goals only.]

Constraints:
- [Compatibility, policy, architecture, data, or design invariant.]
- Ask before [external, destructive, costly, or scope-expanding action not
  already authorized].

Verification:
- [Targeted test, measurement, review criterion, or rendered behavior.]
- If a check cannot run, report why and provide the next-best evidence.

Stop and ask:
- Required user decision, credential, authorization, or conflicting requirement.
- The completion criteria cannot be met within the stated scope.
```

Remove empty sections. For a simple goal, a single outcome sentence with a clear
done condition can be sufficient.
