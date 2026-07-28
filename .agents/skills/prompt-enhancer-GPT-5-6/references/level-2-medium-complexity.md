# Level 2: Routine Multi-Step Prompts

Use this route for standard feature work, routine multi-file edits,
documentation changes, analysis with several inputs, or customer workflows that
need a small number of behavioral rules.

## Construction Rules

- Lead with the outcome rather than a rigid implementation sequence.
- Name the context that can change the answer.
- Define observable success criteria.
- State permission or side-effect boundaries once when the task can mutate
  files, data, or external systems.
- Add the required output structure and relevant validation.
- Add personality or collaboration guidance only for customer-facing or
  interactive behavior.
- Do not add generic tool instructions or arbitrary limits.

## Required Recommendation

Select exactly one model and effort:

- Prefer `gpt-5.6-terra` for balanced everyday work.
- Select `gpt-5.6-sol` only when ambiguity, consequence, or required polish
  exceeds the ordinary Level 2 case without making the task a Level 3 route.
- Prefer medium reasoning effort. Use low only for an unusually deterministic
  task with a complete specification.

## Prompt Template

```text
Goal:
[Describe the user-visible outcome.]

Context:
[List only the files, data, policies, or prior decisions that matter.]

Success criteria:
- [Observable condition.]
- [Required behavior or preserved contract.]

Constraints and permissions:
- [Material scope, safety, business, or compatibility rule.]
- [Action that requires confirmation, if any.]

Output:
[Required structure, audience, language, or length.]

Validation:
[Most relevant check, or what to report if it cannot run.]
```

Remove any section that does not change the expected behavior.
