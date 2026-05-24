# New Machine Agent Init

Give a fresh agent this file first.

## Goal

Reconstruct enough shared context for a useful working partner without relying
on old chat history.

## Startup Steps

1. Read `agent-entry/instructions/agent-rules.md`.
2. Read `agent-entry/instructions/memory-evolution-policy.md`.
3. Read `agent-entry/instructions/project-init-policy.md`.
4. Read `agent-entry/memories/MEMORY.md`.
5. Open only the memory modules that are relevant to the current task.
6. Inspect the target project's local rules before editing files.
7. Run an audit before syncing new or changed context.

## First Message To A New Agent

```text
Read agent-entry/init/new-machine-agent-init.md, then orient yourself using the
instructions and memories under agent-entry/. After that, inspect the target
project and tell me what context you loaded.
```

## Boundary

This bootstrap layer gives structure, not omniscience. A new machine should
slowly rebuild local private state through explicit inspection and safe memory
updates.
