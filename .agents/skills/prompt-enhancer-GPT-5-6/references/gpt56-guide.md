# GPT-5.6 Models and Prompting Reference Guide

This reference provides model specifications, parameter guidance, and structural prompting rules for OpenAI's GPT-5.6 model family, aligned with official OpenAI developer documentation.

---

## 1. GPT-5.6 Model Family Capabilities & Selection

Selecting the right model balances capability, latency, and cost for a given task.

| Model Slug | Category | Key Capabilities & Ideal Use Cases |
| :--- | :--- | :--- |
| `gpt-5.6-sol` | Flagship / High-Capability | **Frontier capability, complex reasoning, advanced architecture & coding, multi-step agentic workflows, deep synthesis, and high-stakes visual/UI design judgment.**<br>Use when: Quality and reasoning accuracy outrank latency and cost; task involves complex logic, ambiguous requirements, or intricate code generation. (Default route for alias `gpt-5.6`). |
| `gpt-5.6-terra` | Balanced / Production | **Strong performance and high intelligence at a lower price point.**<br>Use when: Standard production logic, routine code edits, structured drafting, customer service agents, balanced quality/cost requirements, and mid-tier analytical tasks. |
| `gpt-5.6-luna` | Fast / High-Volume | **Efficient, low-cost, high-throughput model.**<br>Use when: High-volume workloads, simple data classification, lightweight text extraction, rapid intent routing, basic formatting, or latency-sensitive simple queries. |

---

## 2. API Parameters & Execution Modes

GPT-5.6 introduces and refines several key execution parameters:

### Reasoning Effort (`reasoning.effort`)
Options: `none`, `low`, `medium`, `high`, `xhigh`, `max`
- `none`: Pure text generation without reasoning overhead (latency baseline).
- `low`: Latency-sensitive tasks requiring minimal decision logic.
- `medium`: Balanced starting point for tool-using and analytical tasks (default).
- `high` / `xhigh`: Complex reasoning, deep verification, and intricate coding.
- `max`: Maximum exploration for demanding, quality-first workloads.

### Pro Mode (`reasoning.mode: "pro"`)
- Applies additional model work before emitting a single final answer to maximize reliability on difficult tasks.
- Use for high-value code reviews, complex optimizations, and deep risk analysis where quality matters more than latency.

### Text Verbosity (`text.verbosity`)
Options: `low`, `medium`, `high`
- Controls baseline response detail. API default is `medium`. Use `low` for concise, direct responses without adding overly restrictive prompt rules like "be extremely brief".

### Programmatic Tool Calling (PTC)
- Allows the model to write JavaScript to execute tools concurrently and reduce large intermediate data payloads inside a hosted runtime.
- Best for bounded data filtering, aggregation, ranking, or multi-tool workflows where intermediate outputs don't require semantic judgment between calls.

---

## 3. OpenAI Prompting Best Practices

### A. Outcome-First Prompt Design
- Define the desired destination, success criteria, and constraints; allow the model to infer the optimal search or execution strategy.
- Avoid over-specifying step-by-step mechanical procedures unless strict ordering is mandatory.

### B. Lean & Concise Instructions
- State each directive once. Avoid redundant rules or excessive capitalizations (`ALWAYS`, `NEVER`).
- Lean prompts reduce total token cost, decrease latency, and improve instruction-following accuracy by 10–15%.

### C. Autonomy & Approval Boundaries
- Explicitly define actions authorized autonomously (e.g., inspecting files, reading docs, local non-destructive edits, running unit tests).
- Specify actions requiring explicit user confirmation (e.g., external API writes, destructive commands, file deletions, scope expansion).

### D. Response Preamble for Streaming & Tool Use
- For multi-step or tool-heavy workflows, include an instruction to emit a 1–2 sentence visible preamble acknowledging the request and stating the first step before launching tool calls.

### E. Retrieval Budgets & Stopping Conditions
- Set explicit limits on search loops (e.g., perform one broad search; retrieve again only if mandatory facts are missing).
- Define clear exit conditions when sufficient evidence is gathered.

### F. Verification & Self-Checking
- Prompt the model to validate its own output using available commands (unit tests, linter checks, build validation, visual rendering inspection).

---

## 4. Standard Prompt Architecture Template

Use this canonical structure for enhanced prompts:

```text
Role: [1-2 sentences defining the model's function, domain context, and core responsibility]

# Personality & Tone
[Directness, warmth, collaboration style, and question-asking threshold]

# Goal
[Clear, outcome-oriented description of the target destination]

# Success Criteria
[Specific, verifiable conditions that must be met before finalizing output]

# Constraints & Approval Boundaries
[Autonomous vs approval-required actions, evidence limits, safety & business rules]

# Output Format & Structure
[Structure, sections, verbosity, length limits, and content preservation order]

# Stop Rules & Retrieval Budget
[Tool loop termination criteria, search limits, missing evidence fallback]
```
