#!/usr/bin/env python3
"""List previous Codex sessions for the current repository."""

from __future__ import annotations

import argparse
import json
import os


def get_current_repo_identifiers(target_dir: str) -> tuple[str, str]:
    """Get absolute path of target dir and git repository url if available."""
    abs_cwd = os.path.abspath(target_dir)
    repo_url = ""

    # Try reading git   remote origin url from .git/config if present
    git_config = os.path.join(abs_cwd, ".git", "config")
    if os.path.isfile(git_config):
        try:
            with open(git_config, "r", encoding="utf-8") as f:
                content = f.read()
                for line in content.splitlines():
                    line = line.strip()
                    if line.startswith("url ="):
                        repo_url = line.split("=", 1)[1].strip()
                        break
        except Exception:
            pass

    return abs_cwd, repo_url


def build_session_cwd_map(sessions_dirs: list[str]) -> dict[str, dict]:
    """Index session files to map session ID to cwd and repository URL."""
    session_map = {}
    for sdir in sessions_dirs:
        if not os.path.isdir(sdir):
            continue
        for root, _, files in os.walk(sdir):
            for fname in files:
                if not fname.endswith(".jsonl"):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        line = f.readline()
                        if not line:
                            continue
                        data = json.loads(line)
                        if data.get("type") == "session_meta":
                            payload = data.get("payload", {})
                            sid = payload.get("session_id") or payload.get("id")
                            if sid:
                                session_map[sid] = {
                                    "cwd": payload.get("cwd", ""),
                                    "repo": (payload.get("git") or {}).get("repository_url", ""),
                                    "file": fpath,
                                }
                except Exception:
                    continue
    return session_map


def main() -> None:
    parser = argparse.ArgumentParser(description="List Codex sessions for current repository.")
    parser.add_argument("--limit", type=int, default=10, help="Number of recent sessions to return (default: 10)")
    parser.add_argument("--target-dir", type=str, default=".", help="Target repository directory (default: current directory)")
    parser.add_argument("--all", action="store_true", help="List all matching sessions without limit")
    parser.add_argument("--include-archived", action="store_true", help="Include archived sessions")
    args = parser.parse_args()

    target_cwd, target_repo = get_current_repo_identifiers(args.target_dir)

    sessions_dirs = [os.path.expanduser("~/.codex/sessions")]
    if args.include_archived:
        sessions_dirs.append(os.path.expanduser("~/.codex/archived_sessions"))
    index_path = os.path.expanduser("~/.codex/session_index.jsonl")

    session_map = build_session_cwd_map(sessions_dirs)

    matched_sessions = []
    if os.path.isfile(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except Exception:
                    continue

                sid = entry.get("id")
                if not sid:
                    continue

                meta = session_map.get(sid)
                if meta:
                    session_cwd = meta.get("cwd", "")
                    session_repo = meta.get("repo", "")
                    # Match by exact cwd, relative subpath, or matching git repo
                    is_match = (
                        session_cwd == target_cwd
                        or (target_repo and session_repo and target_repo.lower() == session_repo.lower())
                    )
                    if is_match:
                        matched_sessions.append({
                            "id": sid,
                            "id_short": sid[:5],
                            "thread_name": entry.get("thread_name", "Untitled"),
                            "updated_at": entry.get("updated_at", ""),
                            "file": meta.get("file", ""),
                        })

    if not matched_sessions:
        print("No sessions found for this repository.")
        return

    # Slices the most recent entries
    if not args.all and args.limit > 0:
        matched_sessions = matched_sessions[-args.limit:]

    # Output formatted as id; thread_name; updated_at
    for s in matched_sessions:
        print(f"{s['id']}; {s['thread_name']}; {s['updated_at']}")


if __name__ == "__main__":
    main()
