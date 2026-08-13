# Goal Mode (`/goal`) Prompt Reference

Use this route for one persistent, long-running objective in an agent workflow. The
goal text acts as both the first prompt and the completion criteria.

## Product Constraints

- Keep the goal objective non-empty and no longer than 4,000 characters.
- Put longer requirements in a file and point the goal to that file.
- Starting a goal does not expand permission, credential, or access boundaries.
- Keep the model tier and reasoning-effort recommendation outside the `/goal` text.
- Write the generated goal in Technical English as this skill's convention.

## Token-Efficient Target Discovery Before Drafting

Complete a lightweight, token-efficient discovery pass to ground the Goal prompt:

1. **Use Provided Context:** If the draft already supplies target paths or validation commands, adopt them directly without re-reading the files.
2. **Verify Paths Lightly:** Use directory listing (`list_dir`) or targeted searches (`grep_search`) to confirm file existence and correct paths. Start with line-range inspection, then expand to broader or full reads when correctness, dependencies, or validation require it.
3. **Focus on Direct Touch Sets and Pertinent Documentation:** Resolve the immediate target files and relevant test commands needed for the goal's completion criteria, plus the smallest set of pertinent documentation required to document the requested edit.
4. **Stop Discovery Early:** Stop as soon as target paths, pertinent documentation paths, and validation commands are confirmed. Do not inspect unrelated files or documentation; inspect broader sources or tests only when required for correctness or validation.

Do not edit files, implement the task, or run side-effecting commands during this discovery. Do not invent paths, scripts, tests, or commands.

If a referenced source is unavailable, or the material target files cannot be resolved safely, ask one to three concise questions and wait for the user's answer before drafting the Goal prompt.

Carry the discovery into the prompt:

- list the authoritative plan or brief first;
- list confirmed source, test, and documentation paths;
- identify confirmed new file paths separately when the source of truth requires them;
- list exact repository-native validation commands when confirmed;
- identify the smallest set of pertinent documentation that must be updated for the requested edit, including documentation outside the initial implementation touch set when necessary;
- allow additional files only when current code shows they are necessary for the approved objective, and require the agent to report the reason before expanding the touch set.

## Construction Rules

- State one outcome rather than combining unrelated backlog items.
- Include constraints only when they prevent a material failure.
- Define verification that lets the executor determine when the goal is complete.
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

Select an appropriate model capability tier and reasoning effort for the task:

- Use a fast/lightweight model with low reasoning effort for a clear, repeatable goal whose completion criteria are fully specified.
- Use a balanced general-purpose model with medium reasoning effort for everyday implementation and tool-using goals.
- Use a high-capacity reasoning model with medium-to-high effort for complex, ambiguous, or architecture-level goals.
- Reserve maximum effort for the hardest quality-first goals requiring deep reasoning across multiple constraints.

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
- Do NOT inspect or edit any files outside this touch set without explicit prior user approval, except for the mandatory documentation synchronization below.
- Documentation synchronization: after every repository edit, identify and update the smallest set of pertinent project documentation that describes the changed behavior, architecture, configuration, contract, workflow, or operations, even when those documentation paths are outside the expected touch set. Treat only those necessary documentation paths as an authorized touch-set extension; unrelated files remain prohibited. If no pertinent documentation exists, report that explicitly.

Scope:
- Do: [Authorized work needed for the outcome.]
- Do not: [Material non-goals; strictly forbid inspecting or editing out-of-scope files.]

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
