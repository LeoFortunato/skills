# Adapted Controlled-Language Rules

Use these rules to make software documentation clear and predictable. They are
independent writing guidance. They are not a copy of the official ASD-STE100
standard and do not establish formal compliance.

## Preserve Meaning First

- Keep the technical meaning, scope, and level of obligation.
- Do not convert a possibility into a guarantee.
- Do not convert a recommendation into a requirement.
- Do not add behavior, prerequisites, defaults, or results that the source does
  not support.
- Flag contradictions that cannot be resolved from the source.

## Control Sentences

- Write one main idea in each sentence.
- Use an explicit subject when the sentence is not a direct instruction.
- Prefer subject-verb-object order.
- Prefer active voice when the actor is known and relevant.
- Use the imperative for actions that the reader must perform.
- Keep conditions close to the sentence that they control.
- Split a sentence when multiple conditions, actions, or results can be read in
  more than one way.
- Use positive instructions when they are as accurate as negative instructions.

Example:

- Less clear: "After configuration, it can be restarted and checked."
- Clear: "Restart the service. Then check the service status."

## Control Vocabulary

- Select one preferred term for each concept.
- Use the preferred term throughout the document.
- Avoid stylistic synonyms for components, actions, states, and roles.
- Use common words when they preserve the exact meaning.
- Keep necessary product, domain, and protocol terminology.
- Define an unfamiliar term or abbreviation at first use.
- Use each abbreviation consistently after its definition.
- Maintain a project glossary when the document set is large or changes often.

A project glossary can contain:

| Concept | Preferred term | Avoid | Definition |
| --- | --- | --- | --- |
| A saved deployment configuration | deployment profile | preset, setup | Named configuration used by the deployment command |

This table is an example format, not an approved-word list.

## Make References Explicit

- Replace `it`, `this`, `that`, `they`, or `above` when the referent is not
  immediately clear.
- Name the component, field, step, or result again when repetition prevents
  ambiguity.
- Use stable section names or links instead of relative locations such as
  "below" when content can move.
- State the unit and reference point for quantities and time periods.

Example:

- Ambiguous: "Delete it after this finishes."
- Explicit: "Delete the temporary archive after the upload finishes."

## Write Procedures

- State the goal and prerequisites before the steps.
- Put one reader action in each numbered step.
- Start each action with an imperative verb.
- Put a command directly after the instruction that introduces it.
- State the expected result after the related action when verification matters.
- Identify optional steps as optional.
- Identify branches with an explicit condition.
- Do not hide required actions in notes or descriptive paragraphs.

Example:

1. Open a terminal in the project directory.
2. Run `acme validate --config app.yaml`.
3. Confirm that the command returns `Configuration is valid`.

## Use Predictable Structure

- Give each section one purpose.
- Put prerequisites before tasks.
- Put reference facts in tables or definition lists when readers must scan them.
- Use parallel grammar for headings, list items, and table cells.
- Put warnings before the action that can cause harm or data loss.
- Keep troubleshooting actions in diagnostic order.

## Protect Software Literals

Preserve these items exactly unless the task explicitly requests a technical
change:

- fenced and inline code;
- commands, options, flags, and arguments;
- placeholders and environment-variable names;
- identifiers, symbols, and configuration keys;
- API methods, paths, fields, and status codes;
- filenames and filesystem paths;
- UI labels;
- log output and error messages.

Do not alter capitalization, punctuation, whitespace, or quoting when those
details can affect execution or matching. If a literal appears incorrect,
report the concern instead of silently changing it.

## Final Check

Before delivery, confirm that:

- every sentence has one clear interpretation;
- every procedure step contains one action;
- every condition controls an identifiable action or result;
- terminology is consistent;
- pronouns and cross-references have clear targets;
- requirements and optional behavior remain distinct;
- all protected literals match the source;
- the output does not claim official ASD-STE100 compliance.
