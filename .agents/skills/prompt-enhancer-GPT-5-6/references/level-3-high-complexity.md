# Level 3: Complex or High-Consequence Prompts

Use this route for ambiguous architecture work, deep debugging, high-value
reviews, research requiring evidence, long tool-using workflows, or tasks where
incorrect side effects would be costly.

## Construction Rules

- Define one primary outcome and an observable completion bar.
- Provide the evidence, starting paths, policies, and constraints that can
  materially affect the result.
- Distinguish safe in-scope work from external, destructive, costly, or
  scope-expanding actions that require confirmation.
- Let the model choose an efficient path. Prescribe steps only when order is a
  requirement.
- For retrieval, start with named sources and expand only when required for
  correctness.
- For grounded outputs, require support for material claims, label inference,
  and report missing or conflicting evidence.
- Request sparse progress updates only when they help the user supervise a long
  task.
- Validate the artifact with the most relevant available checks.

Avoid arbitrary line-count limits, blanket rereading bans, fixed search budgets,
and universal retry counts.

## Required Recommendation

Select `gpt-5.6-sol` and exactly one effort:

- Use medium when the task is complex but well-defined.
- Use high when the work requires difficult multi-step reasoning, several
  sources, or material tradeoffs.
- Use extra-high reasoning only when exceptional depth is necessary and speed
  is secondary.
- Reserve maximum effort for the hardest quality-first task where a lower level
  is unlikely to meet the completion bar.

## Prompt Template

```text
Role:
[Include only when domain framing changes behavior.]

Goal:
[Describe the primary outcome.]

Context and evidence:
- [Starting sources, files, data, policies, or known facts.]

Touch Set (In-scope files):
- Modify: [Exact target existing paths.]
- Add: [Exact target new paths, if any.]

Success criteria:
- [Observable completion condition.]
- [Required evidence, preserved contract, or quality bar.]

Constraints and permissions:
- Strictly limit work to the declared Touch Set. Do NOT inspect or edit files outside this set without prior explicit user approval, except for the mandatory documentation synchronization below.
- After every repository edit, identify and update the smallest set of pertinent project documentation that describes the changed behavior, architecture, configuration, contract, workflow, or operations, even when those documentation paths are outside the original Touch Set. Treat only those necessary documentation paths as an authorized Touch Set extension; unrelated files remain prohibited. If no pertinent documentation exists, report that explicitly.
- Proceed with [safe, in-scope actions].
- Ask before [external, destructive, costly, or scope-expanding actions].
- Preserve [data, behavior, compatibility, policy, or design contract].

Tools and retrieval:
[State only task-specific prerequisites, evidence rules, and fallback behavior.]

Progress and stopping:
[State useful phase updates and when to ask, abstain, or stop.]

Validation:
[Targeted checks first; broader checks only when relevant.]

Output:
[Required structure, evidence, length, and audience.]
```
