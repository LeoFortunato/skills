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

Touch Set (In-scope files):
- Modify: [Exact target existing paths.]
- Add: [Exact target new paths, if any.]

Success criteria:
- [Observable condition.]
- [Required behavior or preserved contract.]

Constraints and permissions:
- Strictly limit execution to the declared Touch Set. Do NOT inspect or edit files outside this set without prior explicit approval, except for the mandatory documentation synchronization below.
- After every repository edit, identify and update the smallest set of pertinent project documentation that describes the changed behavior, architecture, configuration, contract, workflow, or operations, even when those documentation paths are outside the original Touch Set. Treat only those necessary documentation paths as an authorized Touch Set extension; unrelated files remain prohibited. If no pertinent documentation exists, report that explicitly.
- [Material scope, safety, business, or compatibility rule.]
- [Action that requires confirmation, if any.]

Output:
[Required structure, audience, language, or length.]

Validation:
[Most relevant check, or what to report if it cannot run.]
```

Remove any section that does not change the expected behavior.
