---
name: grilling
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking or uses any "grill" trigger phrases. Enable documentation mode only when the user explicitly asks to capture decisions, ADRs, or glossary entries during the session.
metadata:
  author: Leonardo Fortunato
  license: MIT
  source: https://github.com/mattpocock/skills/tree/main
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

## Optional documentation mode

Use the default mode for the interview only. Do not create or update project documentation during ordinary grilling.

Enable documentation mode for the current session only when the user explicitly asks for it, such as by asking to “grill with docs.” In that mode:

1. Use the `/domain-modeling` skill alongside this skill.
2. Capture resolved domain terms in the project glossary as they settle.
3. Record qualifying architectural decisions as ADRs, following the criteria and formats from `/domain-modeling`.
4. Continue the same round-based interview; document decisions as they become settled rather than treating documentation as a substitute for questioning.

Do not enable documentation mode merely because the topic is architectural or could benefit from written context.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled — the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree — settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent to find it — don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report — ask the rest of the frontier now. The _decisions_ are the user's — put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.
