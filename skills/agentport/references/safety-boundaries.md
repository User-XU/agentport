# Safety Boundaries

## Never Sync

- API keys
- access tokens
- auth headers
- passwords
- private keys
- local app session files
- raw private logs
- private server details

## Audit

Run:

```bash
python scripts/agentport.py audit --target /path/to/context
```

If the audit flags a likely secret, move it to private local storage or remove
it entirely. Do not "document around" leaked credentials.
