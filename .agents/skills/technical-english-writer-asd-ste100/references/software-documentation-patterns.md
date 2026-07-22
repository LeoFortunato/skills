# Software Documentation Patterns

Select the smallest pattern that fits the document. Preserve the product's
existing information architecture when it is already clear and consistent.

## Guide or Tutorial

Use this order:

1. Outcome
2. Audience
3. Prerequisites
4. Steps
5. Verification
6. Next step

Example:

```markdown
# Create a local project

This tutorial creates a project named `demo`.

## Prerequisites

- Install Acme CLI 4.2 or later.

## Create the project

1. Open a terminal.
2. Run `acme init demo`.
3. Change to the `demo` directory.
4. Run `acme serve`.

## Verify the project

1. Open `http://localhost:3000`.
2. Confirm that the start page appears.
```

Teach one path first. Put alternatives after the primary path. Explain a concept
immediately before the reader needs it.

## Operational Procedure

Use this order:

1. Purpose
2. Preconditions
3. Safety or data warning
4. Numbered actions
5. Expected results
6. Rollback or recovery, when applicable

Example:

```markdown
# Restart the worker

Use this procedure after you change the worker configuration.

## Preconditions

- Confirm that no migration is in progress.
- Confirm that you have the `operator` role.

## Procedure

1. Run `acme worker stop`.
2. Confirm that the status is `stopped`.
3. Run `acme worker start`.
4. Confirm that the status is `healthy`.
```

Keep one action in each numbered step. Do not combine an action and its fallback
in the same step.

## API Reference

Use a stable entry for each operation:

1. Method and path
2. Purpose
3. Authentication and permissions
4. Path, query, header, and body parameters
5. Request example
6. Response schema and example
7. Status and error codes
8. Limits, idempotency, or version notes

Example:

````markdown
## Get a widget

`GET /v1/widgets/{widget_id}`

Returns one widget.

### Path parameter

| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `widget_id` | string | Yes | Unique widget identifier. |

### Response

The operation returns `200 OK` when the widget exists.

```json
{"id":"w_123","status":"ready"}
```

The operation returns `404 Not Found` when `widget_id` does not identify a
widget.
````

Use the exact schema terms. Do not replace field names with natural-language
synonyms.

## CLI Reference and Procedure

For a command reference, use this order:

1. Command signature
2. Purpose
3. Arguments
4. Options
5. Exit status
6. Examples

For a CLI procedure, state each command in a separate step and state the expected
result when it confirms success.

Example:

```markdown
## Preview a deployment

1. Run `acme deploy --dry-run`.
2. Review the proposed changes.
3. Confirm that the command returns exit status `0`.
```

Preserve command names, flags, metavariables, output, and exit codes exactly.

## Troubleshooting Article

Use this order:

1. Exact symptom
2. Affected environment
3. Probable cause, when verified
4. Diagnostic actions
5. Corrective actions
6. Verification
7. Escalation information

Example:

```markdown
# The CLI returns `config file not found`

This error occurs when the current directory does not contain `acme.yaml`.

## Resolution

1. Run `pwd`.
2. Change to the project directory.
3. Run `acme validate`.

The issue is resolved when `acme validate` returns exit status `0`.
```

Do not paraphrase an error message used for search or matching. Separate verified
causes from possible causes.

## Release Note

Use short sections such as `Added`, `Changed`, `Fixed`, `Deprecated`, `Removed`,
and `Action required`. State the affected version or component. Describe the user
impact before implementation details.

Example:

```markdown
## Changed

- The CLI now retries an interrupted upload two times.

## Fixed

- Fixed an error that returned `403 Forbidden` after a token refresh.

## Action required

- Replace `upload.retry_count` with `upload.max_retries` before version 5.0.
```

Do not use promotional language. Do not claim that an issue is fixed unless the
source confirms the fix.

## Technical Message

Use this order for a status message, warning, or support response:

1. Current state
2. User impact
3. Required action
4. Deadline or next update, when known

Keep the message direct. Preserve UI labels, error text, incident identifiers,
and commands.

## Pattern Check

For every document type, confirm that:

- the title identifies the task or subject;
- prerequisites appear before dependent actions;
- instructions and reference facts are visually distinct;
- examples use protected literals consistently;
- the final section gives a verifiable result or a clear next action.
