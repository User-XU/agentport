# Contributing

AgentPort is intentionally file-first and small. Contributions
should preserve that shape.

## Principles

- Keep context placement explicit: scope first, type second.
- Prefer readable Markdown and standard-library Python.
- Do not add a database, server, UI, or external dependency unless it solves a
  concrete limitation in the current file-first workflow.
- Keep templates generic and safe to publish.
- Do not add secrets, local session state, raw private logs, or machine-specific
  credentials.

## Development

Run the verification suite before proposing changes:

```bash
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python scripts/agentport.py audit --target . --json
```

Or use:

```bash
make verify
```

## Change Checklist

- Update docs when behavior changes.
- Update tests when script behavior changes.
- Update `.agent-context/logs/LOG.md` for durable project changes.
- Keep `.agent-context/private/` local.
- Run audit before syncing public or project context.
