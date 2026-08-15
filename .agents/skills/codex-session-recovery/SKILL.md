---
name: codex-session-recovery
description: List and access previous Codex sessions scoped to the current repository from local ~/.codex logs.
metadata:
  author: Leonardo Fortunato
  license: MIT
---

# Codex Session Recovery

List and inspect previous Codex sessions scoped to the current repository from local `~/.codex` logs (does not list all sessions across the machine).

## Workflow

1. **List sessions**: Run the helper script to list previous sessions for the current repository:
   ```bash
   python3 .agents/skills/codex-session-recovery/scripts/list_sessions.py
   # Or: python <path_to_skill>/scripts/list_sessions.py
   ```
   This returns the last 10 sessions formatted as `<id>; <thread_name>; <updated_at>`. (Use `--limit <n>`, `--all`, or `--include-archived` if needed).

2. **Access & inspect session**: Run the reader script to extract only the user prompts and assistant replies:
   ```bash
   python3 .agents/skills/codex-session-recovery/scripts/read_session.py <session_id>
   # Or: python <path_to_skill>/scripts/read_session.py <session_id>
   ```
   Provide a concise description of the work done and what remains to be done.