# Memory Evolution

Do not write memory just because a fact appeared in a chat.

## Memory Write Gate

Write only when the candidate is:

- stable beyond the current task
- useful to future agents
- safe for the target scope
- not already represented elsewhere

## Update Pattern

1. Classify candidate context with `scripts/pacs.py route`.
2. Review the recommended bucket.
3. Add a dated entry if the change is durable.
4. Preserve conflicting older memory with dates when the conflict matters.
5. Run `scripts/pacs.py audit`.

## Avoid

- raw chat dumps
- vague "startup summaries"
- sensitive local details
- turning a one-off suggestion into a rule
