# Project Init Policy

Use this policy when entering a new repository or workspace.

## New Project Checklist

1. Inspect the target directory before writing.
2. Look for existing agent entry files such as `AGENTS.md`, `CLAUDE.md`, and
   `HERMES.md`.
3. Look for existing project docs such as `README.md`, `SCHEMA.md`, and
   contribution or test docs.
4. If no project context exists, initialize `.agent-context/` with the project
   template.
5. Keep generated placeholders generic until the user confirms project-specific
   rules.
6. Run an audit before syncing generated context.

## Do Not

- Do not overwrite an existing project rule file without explicit intent.
- Do not promote local machine paths into project memory.
- Do not store credentials, raw logs, or private session state in synced files.
- Do not treat a temporary task summary as durable memory without review.
