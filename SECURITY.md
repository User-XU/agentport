# Security

AgentPort is designed to reduce accidental context leakage,
but it cannot prove that every file is safe.

## What Must Stay Private

- API keys, tokens, passwords, cookies, and auth headers.
- Private keys and certificates.
- Local app state, session files, caches, and raw private logs.
- Internal server details that should not be synced.
- Machine-specific paths when they reveal sensitive local information.

## Built-In Checks

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 /opt/anaconda3/bin/python scripts/agentport.py audit --target . --json
```

Audit checks required files and likely secret patterns. Treat it as a guardrail,
not a complete security scanner.

## Reporting

If you find a context leakage risk, document:

- where the leak can happen
- which file or workflow is involved
- whether the risk affects generated templates, audit logic, or docs
- a minimal reproduction when possible
