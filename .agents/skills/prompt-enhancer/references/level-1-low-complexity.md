# Level 1: Focused and Repeatable Prompts

Use this route for extraction, classification, formatting, transformation,
direct questions, and other well-scoped tasks with an obvious completion point.

## Construction Rules

- State the task directly.
- Include input or context only when it is not already supplied.
- Specify the output shape when format matters.
- Add only constraints whose violation would make the result unusable.
- Omit roles, personality, tool policy, progress reporting, and elaborate
  validation unless they materially change behavior.

## Required Recommendation

Select an appropriate model tier and effort:

- Prefer a fast/lightweight model for clear, repeatable, or high-volume work.
- Select a balanced general-purpose model only when the task needs stronger language judgment or non-trivial tool use while remaining tightly scoped.
- Prefer low reasoning effort for quick, well-scoped work. Raise it to medium only when ambiguity or checking requirements justify the additional work.

## Prompt Template

```text
Task:
[State the requested result.]

Input:
[Include or point to the necessary input. Omit when already supplied.]

Output:
[State the required format, length, or fields.]

Constraints:
- Strictly limit execution to the specified inputs/paths. Do NOT inspect or edit out-of-scope files without prior approval, except for the mandatory documentation synchronization below.
- For any repository edit, identify and update the smallest set of pertinent documentation for the changed behavior, architecture, configuration, contract, workflow, or operations, even when those documentation files are outside the specified paths. Treat only those necessary documentation files as an authorized scope extension; unrelated files remain prohibited. If no pertinent documentation exists, report that explicitly.
- [Include material invariants.]
```

For a very simple request, collapse the template into one or two natural
language sentences.
