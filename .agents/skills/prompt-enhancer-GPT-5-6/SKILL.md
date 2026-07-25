---
name: prompt-enhancer-GPT-5-6
description: Refine, enhance, and structure prompts for OpenAI models (specifically GPT-5.6 Sol, Terra, and Luna) based on official OpenAI documentation and prompting best practices. Trigger whenever the user asks to enhance, refine, optimize, polish, or format a prompt, or calls this skill to improve a prompt draft for GPT models.
---

# Prompt Enhancer (GPT-5.6)

This skill transforms draft prompts or simple task descriptions into structured, production-ready prompts aligned with OpenAI's GPT-5.6 model family best practices.

## Workflow Overview

When invoked, execute the following four-phase workflow:

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 1: Input Analysis & Brief Interview                   │
├─────────────────────────────────────────────────────────────┤
│ Phase 2: Model & Parameter Selection                        │
├─────────────────────────────────────────────────────────────┤
│ Phase 3: Outcome-First Prompt Construction                   │
├─────────────────────────────────────────────────────────────┤
│ Phase 4: Output Delivery & Rationale                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Input Analysis & Brief Interview

Analyze the user's initial input. If key prompt engineering elements are missing or underspecified, conduct a brief, targeted interview before generating the final prompt.

### 1. Key Information Check
Check if the input specifies:
- **Core Objective**: What specific outcome or artifact should be produced?
- **Context & Inputs**: What data, files, policies, or background details are available?
- **Personality & Tone**: How should the assistant sound (formality, directness, demeanor)?
- **Collaboration Style**: How should the assistant work (when to ask vs assume, proactivity, handling risk)?
- **Tools & Execution Mode**: Are tools available? Is Programmatic Tool Calling (PTC) or direct tool calling appropriate?
- **Constraints & Approval Boundaries**: What actions are allowed autonomously vs. requiring explicit approval?
- **Success Criteria & Verification**: How is correctness verified (e.g., tests, inspection)?
- **Output Format & Verbosity**: What structure, style, or verbosity is expected?

### 2. Interview Guidelines
- Ask **3 to 5 concise, direct questions** focusing strictly on missing information needed to construct a high-quality prompt.
- If the user provides a comprehensive draft with all details present, skip the interview and proceed directly to Phase 2.

---

## Phase 2: Model & Parameter Selection

Consult `references/gpt56-guide.md` to select the optimal model variant and parameter configuration:

### 1. Model Selection Rules
- **`gpt-5.6-sol`**: Choose for complex reasoning, architectural design, advanced coding, deep analysis, multi-agent coordination, high-stakes decision making, or quality-critical tasks.
- **`gpt-5.6-terra`**: Choose for standard production logic, routine code maintenance, structured drafting, general business automation, and balanced performance/cost trade-offs.
- **`gpt-5.6-luna`**: Choose for high-volume workloads, simple data classification, lightweight text extraction, intent routing, or latency-sensitive simple operations.

### 2. Parameter Recommendations
- **Reasoning Effort (`reasoning.effort`)**: Select based on specific task shape:
  - `none`: Text generation without reasoning overhead (latency baseline).
  - `low`: Tool-use, planning, search, or multi-step decision making where latency is sensitive.
  - `medium`: Balanced starting point for tool-using, analytical, and general agentic tasks (API default).
  - `high`: Complex debugging, deep planning, and high-value tasks.
  - `xhigh`: Deep research, asynchronous workflows, and agentic tasks requiring long runs.
  - `max`: Demanding quality-first workloads requiring maximum exploration and verification.
- **Reasoning Mode (`reasoning.mode`)**: Recommend `"pro"` mode only when quality and reliability on difficult tasks justify higher latency and token consumption; otherwise recommend `"standard"`.
- **Text Verbosity (`text.verbosity`)**: Recommend `low`, `medium`, or `high`.
- **Programmatic Tool Calling (PTC)**: Recommend for bounded tool workflows processing structured data without requiring semantic model intervention between calls.

---

## Phase 3: Outcome-First Prompt Construction

Construct the enhanced prompt following OpenAI's recommended prompt structure:

```text
Role: [1-2 sentences defining the model's identity, expertise, and functional context]

# Personality
[Tone, demeanor, formality, directness, and polish]

# Collaboration Style
[Proactivity, when to make reasonable assumptions vs when to ask for clarification, handling uncertainty]

# Goal
[Target outcome described by destination rather than rigid step-by-step procedures]

# Success Criteria
[Verifiable conditions that define successful completion]

# Constraints & Approval Boundaries
[Autonomous vs approval-required actions, safety, privacy, and side-effect limits]

# Tools
[Available tools, usage rules, or explicit <tool_orchestration> block for PTC]

# Output Format & Structure
[Structure, sections, verbosity, length bounds, and content preservation order]

# Stop Rules & Retrieval Budget
[Tool loop termination criteria, search limits, and fallback behavior for missing evidence]
```

### Prompt Engineering Principles to Apply:
1. **Separation of Personality and Collaboration**: Keep tone/demeanor in `# Personality` and operational/clarification rules in `# Collaboration Style`.
2. **Explicit Tools Section**: For tool-using prompts, specify eligible tools, concurrency limits, and when to use direct calling vs. PTC (via `<tool_orchestration>`).
3. **Lean Instructions**: Remove redundant `ALWAYS`/`NEVER` rules. State directives once clearly.
4. **Outcome Focus**: Focus on what success looks like rather than micro-managing step sequences.
5. **Preamble Integration**: For multi-step/tool tasks, require a 1–2 sentence visible preamble before executing tool calls.
6. **Validation Directive**: Include check-your-work instructions (tests, build, visual rendering).

---

## Phase 4: Output Delivery

Deliver the refined prompt package structured into four clearly separated sections:

1. **Recommended Model**: Selected GPT-5.6 model slug (`gpt-5.6-sol`, `gpt-5.6-terra`, or `gpt-5.6-luna`) with a concise technical justification.
2. **Recommended Parameters**: Configuration settings (`reasoning.effort`, `reasoning.mode`, `text.verbosity`, PTC, etc.).
3. **Enhanced Prompt**: The final ready-to-use prompt enclosed in a code block.
4. **Key Enhancements Summary**: Brief explanation of how the original prompt was improved using OpenAI guidelines.
