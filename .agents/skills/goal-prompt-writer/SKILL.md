---
name: goal-prompt-writer
description: Create or refine a copy-ready persistent goal or `/goal` mode prompt. Use only when the user explicitly asks for a Goal mode prompt or asks to convert a task, issue, or plan into `/goal` instructions.
metadata:
  author: Leonardo Fortunato
  license: MIT
---

# Goal Prompt Writer

Produce one self-contained objective that can continue across turns without widening authority.

## Workflow

1. Read applicable repository instructions and only the evidence needed to make paths, constraints, and checks accurate.
2. Extract the observable outcome, source-of-truth files, allowed changes, non-goals, safety boundaries, checkpoints, validation, and stopping conditions.
3. Ask only when a missing decision would materially change scope or safety. Otherwise state a conservative assumption.
4. Write the prompt using `references/goal-prompt-template.md`. Keep one coherent objective and avoid copying entire repository instruction files.
5. Verify every named file, command, tool, and success criterion. Remove unavailable-tool instructions, forced commits, automatic archiving, and unconditional documentation work.

## Rules

- The prompt authorizes only the local work it explicitly places in scope.
- Put commits, pushes, deployment, remote writes, credentials, production data, destructive actions, and material scope expansion behind explicit user approval.
- Prefer exact paths and repository-native validation over vague quality goals.
- Separate unrelated objectives into separate prompts.
- Return prompt text only unless the user requests analysis or a persisted artifact.
