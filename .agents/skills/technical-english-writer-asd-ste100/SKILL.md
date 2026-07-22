---
name: technical-english-writer-asd-ste100
description: Create, rewrite, review, and maintain English software documentation with an adapted ASD-STE100-inspired controlled-language method. Use for guides, tutorials, API and CLI references, troubleshooting articles, operational procedures, release notes, and technical messages that must be clear, concise, consistent, and unambiguous.
---

# Technical English Writer ASD-STE100

## Overview

Write software documentation with a practical controlled-language method adapted
from public ASD-STE100 principles. Improve clarity and consistency without
claiming official ASD-STE100 certification or compliance.

## Workflow

1. Identify whether the task is to create, rewrite, review, or maintain content.
2. Classify the document and its audience. Read
   [software documentation patterns](references/software-documentation-patterns.md)
   for the applicable structure.
3. Record the required meaning, prerequisites, constraints, safety information,
   and expected result. Do not invent missing product behavior.
4. Protect literal technical content before editing. Preserve code blocks,
   commands, flags, placeholders, identifiers, configuration keys, API paths,
   UI labels, and error messages unless the user explicitly requests a change.
5. Establish one preferred term for each concept. Keep necessary product-specific
   terms and define unfamiliar terms at first use.
6. Draft or revise the content with the rules in
   [controlled-language rules](references/controlled-language-rules.md).
7. Check the result for technical accuracy, complete steps, consistent
   terminology, unambiguous references, and preserved literals.
8. Return the result in the requested format.

## Core Writing Rules

- Use clear, short sentences.
- Give each sentence an explicit subject, except for direct imperative steps.
- Prefer active voice and name the actor when the actor is important.
- Use one preferred word for one meaning within the document.
- Use the same term for the same component, action, or state.
- Put one action in each procedural step.
- State conditions before the instruction or result that depends on them.
- Use direct instructions and predictable headings.
- Replace vague references with the exact noun or action.
- Keep product-specific terminology when a generic substitute would reduce
  precision.

## Software Safeguards

- Treat literal text as an interface contract. Do not silently correct or
  normalize it.
- Keep parameter names, field names, data types, status codes, and request or
  response examples consistent with the source.
- Distinguish required actions from optional actions.
- Separate user actions, system responses, and verification results.
- Keep warnings and prerequisites next to the action that they control.
- Preserve version, platform, and environment qualifications.
- Flag a technical contradiction or an unsafe omission instead of resolving it
  with an unsupported assumption.

## Review and Maintenance

For a review, evaluate meaning, structure, controlled language, terminology,
procedural completeness, and literal preservation. Give review commentary only
when the user requests it. Make findings specific and include a recommended
revision.

For maintenance, compare the new source facts with the current document. Change
only affected content, and then check cross-references, terminology, examples,
prerequisites, and version statements for secondary effects.

## Output Contract

- By default, return only the completed document. Do not add a preface, change
  log, explanation, or compliance statement.
- If the user requests review commentary, return concise findings in addition to
  the reviewed or revised content, as requested.
- Preserve the source format unless a different format is requested or the
  document type requires a clearer standard structure.
- Ask for clarification only when missing information can materially change the
  technical meaning or make an instruction unsafe. Otherwise, make the smallest
  conservative edit.

## Reference Navigation

- Read [controlled-language rules](references/controlled-language-rules.md) when
  drafting, rewriting, or reviewing wording and terminology.
- Read
  [software documentation patterns](references/software-documentation-patterns.md)
  when selecting a structure or working on a tutorial, procedure, API or CLI
  reference, troubleshooting article, release note, or technical message.

## Standard Boundary

Apply only the adapted guidance included in this skill. Do not represent the
output as certified, validated, or compliant with official ASD-STE100. Do not
reproduce or reconstruct the official dictionary, complete rule set, or
specification text. If formal conformance is required, direct the user to the
current official standard and qualified review.
