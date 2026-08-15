#!/usr/bin/env python3
"""Read and extract clean conversation (user prompts & assistant responses) from a Codex session log."""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys


def find_session_file(session_query: str) -> str | None:
    """Find session file by path, exact filename, session ID, or ID prefix."""
    # Check if direct existing path
    if os.path.isfile(session_query):
        return os.path.abspath(session_query)

    search_dirs = [
        os.path.expanduser("~/.codex/sessions"),
        os.path.expanduser("~/.codex/archived_sessions"),
    ]

    # Search by filename or wildcard pattern
    for sdir in search_dirs:
        if not os.path.isdir(sdir):
            continue
        # Check recursive match
        matches = glob.glob(os.path.join(sdir, f"**/*{session_query}*.jsonl"), recursive=True)
        if matches:
            # Sort by modification time descending to pick most recent if multiple
            matches.sort(key=lambda p: os.path.getmtime(p), reverse=True)
            return matches[0]

    return None


def clean_user_text(text: str) -> str:
    """Strip system injections from user message text if present."""
    # Strip <environment_context>...</environment_context>
    text = re.sub(r"<environment_context>[\s\S]*?</environment_context>", "", text)
    # Strip <recommended_plugins>...</recommended_plugins>
    text = re.sub(r"<recommended_plugins>[\s\S]*?</recommended_plugins>", "", text)
    # Strip <codex_internal_context.*?>...</codex_internal_context>
    text = re.sub(r"<codex_internal_context[\s\S]*?</codex_internal_context>", "", text)
    # Strip # AGENTS.md instructions ... </INSTRUCTIONS>
    text = re.sub(r"# AGENTS\.md instructions[\s\S]*?</INSTRUCTIONS>", "", text)
    return text.strip()


def extract_session_conversation(session_file: str) -> list[tuple[str, str]]:
    """Extract (role, content) pairs from session jsonl file."""
    messages = []
    with open(session_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except Exception:
                continue

            if data.get("type") != "response_item":
                continue

            p = data.get("payload", {})
            if p.get("type") != "message":
                continue

            role = p.get("role")
            if role not in ("user", "assistant"):
                continue

            content = p.get("content", [])
            text_parts = []
            for c in content:
                if isinstance(c, dict):
                    t = c.get("text", "")
                    if t:
                        text_parts.append(t)
                elif isinstance(c, str):
                    text_parts.append(c)

            full_text = "\n".join(text_parts).strip()
            if role == "user":
                full_text = clean_user_text(full_text)

            if full_text:
                messages.append((role, full_text))

    return messages


def main() -> None:
    parser = argparse.ArgumentParser(description="Read clean user & assistant conversation from a Codex session.")
    parser.add_argument("session", help="Session ID (full or prefix), filename, or path to jsonl file")
    args = parser.parse_args()

    session_file = find_session_file(args.session)
    if not session_file:
        print(f"Error: Session '{args.session}' not found in ~/.codex/sessions or ~/.codex/archived_sessions", file=sys.stderr)
        sys.exit(1)

    messages = extract_session_conversation(session_file)
    if not messages:
        print(f"No user/assistant messages found in {session_file}.")
        return

    for role, text in messages:
        print(f"\n=== [{role.upper()}] ===")
        print(text)


if __name__ == "__main__":
    main()
