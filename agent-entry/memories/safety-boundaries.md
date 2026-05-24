# Safety Boundaries

Use this file for stable, non-secret safety preferences.

## Starter Defaults

- Do not persist API keys, tokens, auth headers, passwords, private keys, or
  session cookies.
- Do not commit local app state, caches, private logs, or temporary generated
  files.
- Ask before destructive operations.
- Keep public and private context separate.
- Treat `.agent-context/private/` as local-only unless the user explicitly says
  otherwise.

## Customize

Add organization or machine-specific safety boundaries only when they are safe to
sync.
