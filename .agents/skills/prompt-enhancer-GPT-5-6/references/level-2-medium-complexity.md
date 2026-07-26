# Level 2: Routine Multi-Step Prompts

Use this route for standard feature work, routine multi-file edits, API
endpoints, documentation changes, analysis with several inputs, or customer
workflows that need a small number of behavioral rules.

## Construction Rules

- Lead with the outcome, not a rigid implementation sequence.
- Name the context that can change the answer.
- Define observable success criteria.
- State permission or side-effect boundaries once when the task can mutate data,
  files, or external systems.
- Add output structure and relevant validation.
- Add personality or collaboration guidance only for customer-facing or
  interactive behavior, and keep it short.
- Do not add arbitrary file-size limits, blanket rereading prohibitions, or
  generic tool instructions.

## Optional Model and API Guidance

Provide this only when the user asks for configuration:

- Start with `gpt-5.6-terra` for balanced everyday work.
- Use `gpt-5.6-sol` when ambiguity, consequence, or polish justifies more model
  capability.
- Start with `reasoning.effort: "medium"` and compare `"low"` on representative
  tasks when latency or cost matters.
- Use `text.verbosity: "medium"` unless the required output calls for another
  level.
- Omit `reasoning.mode` when standard mode is sufficient.

## Template

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
