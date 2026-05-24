# AGENTS.md

Codex entrypoint for this project.

## Start Here

1. Read `.agent-context/rules/project-rules.md`.
2. Read `.agent-context/memory/PROJECT_MEMORY.md`.
3. Check `.agent-context/logs/LOG.md` for recent durable changes.
4. Inspect live project state before editing.

## Rules

- Project rules override global preferences for this repository.
- Do not write secrets or local machine state into synced files.
- Keep edits scoped to the user's request.
- Update `.agent-context/logs/LOG.md` for durable context changes.

