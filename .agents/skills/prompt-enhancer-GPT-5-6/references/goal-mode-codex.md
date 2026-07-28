# Codex `/goal` Prompt Reference

Use this route for one persistent, long-running objective in a Codex task. The
goal text acts as both the first prompt and the completion criteria.

## Product Constraints

- Keep the goal objective non-empty and no longer than 4,000 characters.
- Put longer requirements in a file and point the goal to that file.
- Starting a goal does not expand permission, credential, or access boundaries.
- Keep the model and reasoning-effort recommendation outside the `/goal` text.
- Write the generated goal in Technical English as this skill's convention.

## Discover Exact Targets Before Drafting

Complete a bounded, read-only discovery pass before generating the Goal prompt:

1. Read the user's referenced plan, brief, issue, attachment, or other source of
   truth when it is available.
2. Read the applicable `AGENTS.md` instruction chain and only the repository
   documentation routed by those instructions.
3. Resolve the exact existing files and directories relevant to the requested
   change. Start from paths, routes, components, symbols, or behavior named by
   the user or source of truth. Use targeted file and text search rather than a
   broad repository sweep.
4. Inspect enough current implementation, tests, documentation, and repository
   scripts to confirm the likely touch set and the exact validation commands.
5. Stop discovery as soon as the prompt can name the relevant targets and
   verification without guessing.

Do not edit files, implement the task, or run side-effecting commands during
this discovery. Do not invent paths, scripts, tests, or commands.

If a referenced source is unavailable, or the material target files cannot be
resolved safely, ask one to three concise questions and wait for the user's
answer before drafting the Goal prompt.

Carry the discovery into the prompt:

- list the authoritative plan or brief first;
- list confirmed source, test, and documentation paths;
- identify confirmed new file paths separately when the source of truth
  requires them;
- list exact repository-native validation commands when confirmed;
- allow additional files only when current code shows they are necessary for
  the approved objective, and require the agent to report the reason before
  expanding the touch set.

## Construction Rules

- State one outcome rather than combining unrelated backlog items.
- Include constraints only when they prevent a material failure.
- Define verification that lets Codex determine when the goal is complete.
- Include the exact context and expected touch set confirmed during discovery.
- Allow safe in-scope local work when the user's request authorizes changes.
- Require confirmation for external, destructive, costly, or materially
  scope-expanding actions that the user has not already authorized.
- Add milestones or progress rules only when they help the user supervise the
  task.
- Do not add generic requirements unrelated to the goal.

If the outcome is materially ambiguous, ask the smallest necessary question and
wait for the answer before drafting the goal.

## Required Recommendation

Select exactly one model and effort from the underlying task:

- Use `gpt-5.6-luna` with low effort for a clear, repeatable goal whose
  completion criteria are fully specified.
- Use `gpt-5.6-terra` with medium effort for everyday implementation and
  tool-using goals.
- Use `gpt-5.6-sol` with medium effort for complex but well-defined goals.
- Raise Sol to high or extra-high effort only when the goal requires difficult
  reasoning, several sources, or material tradeoffs.
- Reserve maximum effort for the hardest quality-first goal.

## Prompt Template

```markdown
/goal [Complete one observable outcome]. Done when [verification criteria].

Context:
- Source of truth: [Exact plan, brief, issue, or attachment path.]
- Primary targets: [Exact existing source file or directory paths.]
- Tests: [Exact relevant test paths.]
- Documentation: [Exact relevant documentation paths.]

Expected touch set:
- Modify: [Exact confirmed existing paths.]
- Add: [Exact confirmed new paths, if any.]
- Touch additional files only when required by the approved objective and
  current code; report the reason before expanding this set.

Scope:
- Do: [Authorized work needed for the outcome.]
- Do not: [Material non-goals only.]

Constraints:
- [Compatibility, policy, architecture, data, or design invariant.]
- Ask before [external, destructive, costly, or scope-expanding action not
  already authorized].

Verification:
- Run [Exact confirmed repository-native validation command.]
- Confirm [Targeted measurement, review criterion, or rendered behavior.]
- If a check cannot run, report why and provide the next-best evidence.

Stop and ask:
- A required user decision, credential, authorization, or conflicting
  requirement is missing.
- The completion criteria cannot be met within the stated scope.
```

Remove empty sections. For a simple goal, one outcome sentence with a clear done
condition can be sufficient.
