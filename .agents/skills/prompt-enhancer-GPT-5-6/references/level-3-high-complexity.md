# Level 3: High Complexity / Agentic Prompt Reference Guide

This reference defines the model, parameters, rules, and prompt architecture for **Level 3 (High Complexity / Agentic)** tasks.

---

## 1. Task Scope & Characteristics

- **Use Cases**: Complex architectural design, deep multi-file debugging, long-running agentic coding goals, Programmatic Tool Calling (PTC), multi-agent coordination, or high-risk tasks.
- **Primary Objective**: Maximum quality, strict context boundaries, robust safety guardrails, and verifiable completion.

---

## 2. Model & Parameter Configuration

- **Recommended Model**: `gpt-5.6-sol` (flagship frontier capability).
- **Reasoning Effort (`reasoning.effort`)**: `high` (complex debugging), `xhigh` (deep research / long runs), or `max` (demanding quality-first workloads).
- **Reasoning Mode (`reasoning.mode`)**: `"pro"` when quality/reliability on high-risk tasks outranks latency; otherwise `"standard"`.
- **Text Verbosity (`text.verbosity`)**: `medium` or `high`.
- **Programmatic Tool Calling (PTC)**: Recommended for bounded tool stages processing structured data in JS.

---

## 3. Rules & Aggregation

- **INCLUDE** `# Role`, separated `# Personality` and `# Collaboration Style`.
- **INCLUDE** `# Constraints & Approval Boundaries` (autonomous vs approval-required actions).
- **INCLUDE** `# Context & File Access Guardrails` (Anti-Releitura, target file limits, partial line reads, instant search stopping).
- **INCLUDE** `# Tools` or `<tool_orchestration>` block for Programmatic Tool Calling.
- **INCLUDE** `# Stop Rules & Retrieval Budget`.
- **INCLUDE** `# Validation Directive` (tiered testing/linting/build verification).

---

## 4. Full Agentic & Guardrailed Prompt Template

Use this full structure for Level 3 prompts:

```text
Role: [1-2 sentences defining identity, domain expertise, and operational context]

# Personality
[Tone, demeanor, formality, and directness]

# Collaboration Style
[Proactivity, when to make reasonable assumptions vs when to ask for clarification, handling uncertainty]

# Goal
[Target outcome described by destination rather than rigid step-by-step procedures]

# Success Criteria
[Specific, verifiable conditions that must be met before finalizing output]

# Constraints & Approval Boundaries
[Autonomous vs approval-required actions, safety, privacy, and side-effect limits]

# Context & File Access Guardrails
- Inspect ONLY explicitly specified target files: [list paths]. Do NOT perform broad codebase sweeps.
- For files over 100 lines, use targeted line ranges (StartLine/EndLine). Avoid reading full large files unnecessarily.
- Never re-read a file already loaded into conversation memory unless modified by a tool call in an intermediate step.
- Stop retrieval immediately once sufficient evidence is gathered.

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
[Tool loop termination criteria, search limits, and missing evidence fallback]

# Validation Directive
[Tiered verification commands: targeted unit tests -> lint/typecheck -> build/smoke checks]
```
