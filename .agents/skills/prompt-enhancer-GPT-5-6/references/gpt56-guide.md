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
- `none`: Text generation without reasoning overhead (latency baseline).
- `low`: Tool-use, planning, search, or multi-step decision making where latency is sensitive.
- `medium`: Balanced starting point for tool-using, analytical, and general tasks (API default).
- `high`: Complex debugging, deep planning, and high-value tasks.
- `xhigh`: Deep research, asynchronous workflows, and agentic tasks requiring long runs.
- `max`: Demanding quality-first workloads requiring maximum exploration and verification.

### Pro Mode (`reasoning.mode: "pro"`)
- Applies additional model work before emitting a single final answer to maximize reliability on difficult tasks.
- Use for high-value code reviews, complex optimizations, and deep risk analysis where quality matters more than latency.
- Independent of `reasoning.effort` (can be combined with any supported effort level).

### Text Verbosity (`text.verbosity`)
Options: `low`, `medium`, `high`
- Controls baseline response detail. API default is `medium`. Use `low` for concise, direct responses without adding overly restrictive prompt rules like "be extremely brief".

### Programmatic Tool Calling (PTC)
- Allows the model to write JavaScript code in a hosted runtime to execute tools concurrently, filter data, aggregate results, and eliminate large intermediate payloads.
- Best for bounded data processing (filtering, joining, ranking, deduplication, aggregation, validation) where intermediate outputs don't require fresh model judgment between each step.
- Use direct tool calls when: intermediate outputs are small, individual results change the model's next semantic decision, actions require human approval, or native artifacts/citations must be preserved.

---

## 3. OpenAI Prompting Best Practices

### A. Outcome-First Prompt Design
- Define the desired destination, success criteria, and constraints; allow the model to infer the optimal search or execution strategy.
- Avoid over-specifying step-by-step mechanical procedures unless strict ordering is mandatory.

### B. Lean & Concise Instructions
- State each directive once. Avoid redundant rules or excessive capitalizations (`ALWAYS`, `NEVER`).
- Lean prompts reduce total token cost, decrease latency, and improve instruction-following accuracy by 10–15%.

### C. Personality & Collaboration Style Separation
- **Personality** controls how the assistant sounds: tone, warmth, directness, formality, polish, and demeanor.
- **Collaboration Style** controls how the assistant works: when to ask for clarification, when to make assumptions, proactivity level, how much context to provide, and how to handle risk or uncertainty.

### D. Autonomy & Approval Boundaries
- Explicitly define actions authorized autonomously (e.g., inspecting files, reading docs, local non-destructive edits, running unit tests).
- Specify actions requiring explicit user confirmation (e.g., external API writes, destructive commands, file deletions, scope expansion).

### E. Response Preamble for Streaming & Tool Use
- For multi-step or tool-heavy workflows, include an instruction to emit a 1–2 sentence visible preamble acknowledging the request and stating the first step before launching tool calls.

### F. Retrieval Budgets & Stopping Conditions
- Set explicit limits on search loops (e.g., perform one broad search; retrieve again only if mandatory facts are missing).
- Define clear exit conditions when sufficient evidence is gathered.

### G. Verification & Self-Checking
- Prompt the model to validate its own output using available commands (unit tests, linter checks, build validation, visual rendering inspection).

---

## 4. Standard Prompt Architecture Template

Use this canonical structure for enhanced prompts:

```text
Role: [1-2 sentences defining the model's function, domain context, and core responsibility]

# Personality
[Tone, demeanor, formality, directness, and conversational polish]

# Collaboration Style
[Proactivity, when to make reasonable assumptions vs when to ask for clarification, handling uncertainty]

# Goal
[Clear, outcome-oriented description of the target destination]

# Success Criteria
[Specific, verifiable conditions that must be met before finalizing output]

# Constraints & Approval Boundaries
[Autonomous vs approval-required actions, evidence limits, safety & business rules]

# Tools
[Available tools, usage rules, or explicit <tool_orchestration> block for PTC]
<tool_orchestration>
Use Programmatic Tool Calling for [bounded stage] using only [eligible tools].
Process and reduce intermediate results, then emit exactly [output schema].
Stop when [condition] is met. Retry transient failures at most [R] times.
Use direct tool calls for [semantic judgment, approval, or final validation].
</tool_orchestration>

# Output Format & Structure
[Structure, sections, verbosity, length limits, and content preservation order]

# Stop Rules & Retrieval Budget
[Tool loop termination criteria, search limits, missing evidence fallback]
```
