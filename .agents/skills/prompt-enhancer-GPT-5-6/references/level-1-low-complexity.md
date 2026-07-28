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

Select exactly one model and effort:

- Prefer `gpt-5.6-luna` for clear, repeatable, or high-volume work.
- Select `gpt-5.6-terra` only when the task needs stronger language judgment or
  non-trivial tool use while remaining tightly scoped.
- Prefer low reasoning effort for quick, well-scoped work. Raise it to medium
  only when ambiguity or checking requirements justify the additional work.

## Prompt Template

```text
Task:
[State the requested result.]

Input:
[Include or point to the necessary input. Omit when already supplied.]

Output:
[State the required format, length, or fields.]

Constraints:
[Include only material invariants. Omit when none are needed.]
```

For a very simple request, collapse the template into one or two natural
language sentences.
