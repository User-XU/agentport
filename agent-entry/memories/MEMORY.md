# Memory Index

This starter index is intentionally generic. A new machine or team can edit the
modules below without changing the rules.

## Modules

- `collaboration.md` — durable collaboration style and working preferences.
- `safety-boundaries.md` — stable privacy, permission, and sync boundaries.
- `runtime-defaults.md` — local tool and runtime defaults that are safe to
  share.

## Memory Rules

- Keep this layer stable, short, and cross-project.
- Put project-specific memory in the project's `.agent-context/memory/`.
- Put private local state outside synced context.
- Record only facts a future agent can act on.
