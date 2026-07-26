# Level 1: Focused and Repeatable Prompts

Use this route for extraction, classification, formatting, transformation,
direct questions, and other well-scoped tasks with an obvious completion point.

## Construction Rules

- State the task directly.
- Include the input or context only when it is not already supplied.
- Specify the output shape when format matters.
- Add one or two constraints only when violating them would make the result
  unusable.
- Omit roles, personality, tool policy, progress reporting, and elaborate
  validation unless they change behavior.

## Optional Model and API Guidance

Provide this only when the user asks for configuration:

- Start with `gpt-5.6-luna` for clear, repeatable, high-volume work.
- Use `gpt-5.6-terra` when the task needs stronger language judgment or tool use.
- Start with `reasoning.effort: "low"`. Use `"none"` only as a latency baseline
  for tasks that do not benefit from reasoning or tools.
- Use `text.verbosity: "low"` when a concise API response is desired.
- Compare settings on representative inputs before claiming an improvement.

Treat the named fields as API request configuration. For ChatGPT or Codex,
recommend only controls that the target surface exposes. Do not insert settings
into the prompt body unless the user asks for a configuration block.

## Template

```text
Task:
[State the requested result.]

Input:
[Include or point to the necessary input. Omit when already attached.]

Output:
[State the required format, length, or fields.]

Constraints:
[Include only material invariants. Omit this section when none are needed.]
```

For very simple requests, collapse the template into one or two natural-language
sentences.
