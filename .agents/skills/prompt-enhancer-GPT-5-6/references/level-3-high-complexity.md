# Level 3: Complex or High-Consequence Prompts

Use this route for ambiguous architecture work, deep debugging, high-value
reviews, research that needs evidence, long tool-using workflows, or tasks where
incorrect side effects would be costly.

## Construction Rules

- Define one primary outcome and an observable completion bar.
- Provide the evidence, starting paths, policies, and constraints that can
  materially affect the result.
- Distinguish safe in-scope work from external, destructive, costly, or
  scope-expanding actions that require confirmation.
- Let the model choose an efficient path. Prescribe steps only when order is a
  requirement.
- For retrieval, start with the named sources, expand only when required for
  correctness, and stop when the core request has enough evidence.
- For grounded outputs, require citations for material claims, label inference,
  and report missing or conflicting evidence.
- Request a short preamble before the first tool call and sparse updates only at
  major phase changes when visible progress is useful.
- Validate the changed or generated artifact with the most relevant available
  checks. Do not mandate unrelated broad checks.

Avoid arbitrary line-count limits, blanket bans on rereading, fixed search
budgets without a task basis, and universal retry counts. These rules can prevent
the model from collecting evidence needed for correctness.

## Optional Model and API Guidance

Provide this only when the user asks for configuration:

- Start with `gpt-5.6-sol`.
- Use `reasoning.effort: "medium"` as a baseline. Raise it to `"high"` or
  `"xhigh"` when evaluations show that deeper reasoning improves the task.
- Reserve `"max"` for the hardest quality-first workloads.
- Consider `reasoning.mode: "pro"` only for difficult Responses API tasks where
  quality or reliability outweighs latency and cost. Test it against standard
  mode with the same prompt and effort.
- Use `text.verbosity: "medium"` by default, then specify task-specific content
  and length in the prompt.

## Prompt Template

```text
Role:
[Include only when domain framing changes behavior.]

Goal:
[Describe the primary outcome.]

Context and evidence:
- [Starting sources, files, data, policies, or known facts.]

Success criteria:
- [Observable completion condition.]
- [Required evidence, preserved contract, or quality bar.]

Constraints and permissions:
- Proceed with [safe, in-scope actions].
- Ask before [external, destructive, costly, or scope-expanding actions].
- Preserve [data, behavior, compatibility, policy, or design contract].

Tools and retrieval:
[State only task-specific prerequisites, routing decisions, evidence rules, and
fallback behavior.]

Progress and stopping:
[State useful phase updates, retry or fallback limits with a task-specific
reason, and when to ask or abstain.]

Validation:
[Targeted checks first; broader checks only when relevant.]

Output:
[Required structure, evidence, length, and audience.]
```

## Programmatic Tool Calling

Add a PTC block only for the OpenAI Responses API when the runtime exposes
eligible tools and the task contains a bounded stage that can reduce structured
intermediate results without fresh model judgment:

```text
<tool_orchestration>
Use Programmatic Tool Calling only for [bounded stage] with [eligible tools].
Reduce the results to [exact schema] while preserving [required evidence].
Retry transient failures at most [task-specific limit] and stop when [condition].
Use direct tool calls for approval, semantic judgment, citations, and final
validation. Do not repeat completed work.
</tool_orchestration>
```

Multiple or dependent calls alone do not justify PTC. Prefer direct calls when a
result changes the next decision, an action needs approval, or the final answer
must preserve citations or native artifacts.
