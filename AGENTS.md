# AGENTS.md

Project instructions for Codex and Codex-like agents working in this repository.

## Start Here

Before substantial edits, read:

1. `README.md` for product intent and repository shape.
2. `docs/architecture.md` for context scopes and storage rules.
3. `docs/quickstart.md` and `docs/usage-recipes.md` for supported workflows.
4. `SCHEMA.md` for file contracts and validation expectations.

## Project Rules

- Treat this repository as an independent project, not as an `_outputs` draft.
- Keep the core model file-first, Git-friendly, and portable across machines.
- Do not add a database, web app, MCP server, or external dependency unless the
  user asks for that stage.
- Use `/opt/anaconda3/bin/python` for Python commands on this machine.
- Keep scripts standard-library only unless a dependency is explicitly justified.
- Never commit credentials, local tokens, private paths, raw session logs, or
  machine-local state.
- Preserve the distinction between `rules`, `memory`, `knowledge`, `logs`, and
  `private-state`.

## Verification

Before claiming script changes work, run:

```bash
make verify
```

This runs unit tests, project audit, and machine-entry audit.
