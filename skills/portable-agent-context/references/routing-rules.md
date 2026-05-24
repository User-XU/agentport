# Routing Rules

Route context by scope first, then type.

## Scope

- Global: thin user defaults that apply everywhere.
- Public: shared cross-agent context safe to sync.
- Project: repository-specific rules, memory, and logs.
- Private: local sensitive state that should not be synced.

## Type

- Rules: constraints on future behavior.
- Memory: stable facts or collaboration history.
- Knowledge: formal reusable research or domain content.
- Logs: chronological records of actions.
- Private state: secrets, auth, local-only paths, raw private data.

## Common Decisions

| Candidate | Destination |
| --- | --- |
| "Always verify before claiming completion" | public rules |
| "This repo uses make verify" | project rules |
| "The user prefers concise final summaries" | public memory |
| "The project moved docs to docs/architecture.md" | project memory |
| "API key is ..." | private state or discard |
| "Comparison of OpenViking and this project" | knowledge |
