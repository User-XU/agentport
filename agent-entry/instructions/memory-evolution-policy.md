# Memory Evolution Policy

This file tells agents how to decide whether new context should become durable
memory.

## Before Writing Memory

Ask:

1. Is this stable beyond the current chat?
2. Is it safe to sync?
3. Is it global, public, project-specific, formal knowledge, or private state?
4. Would a future agent benefit from this exact fact?

## Routing Rules

- Behavior constraints -> `agent-entry/instructions/` or project
  `.agent-context/rules/`.
- Stable cross-agent preferences and collaboration facts ->
  `agent-entry/memories/`.
- Project decisions and history -> project `.agent-context/memory/`.
- Research, comparisons, and reusable articles -> formal knowledge system.
- Credentials, tokens, local auth state, private paths -> private local storage
  or no durable write.

## Update Rules

- Do not silently overwrite old memory.
- Prefer appending dated notes when memory evolves.
- If a fact conflicts with older memory, preserve both with dates and ask for
  review when the conflict matters.
- Do not turn suggestions into rules without user intent.
- When uncertain, route to an inbox or ask the user before making it durable.
