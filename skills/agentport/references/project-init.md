# Project Init

## New Machine

Run:

```bash
python scripts/agentport.py init-machine --target ~/AgentContext
```

Then tell the new agent to read:

```text
~/AgentContext/agent-entry/init/new-machine-agent-init.md
```

## New Project

Run:

```bash
python scripts/agentport.py init-project --target /path/to/project
```

Then edit:

- `AGENTS.md`
- `CLAUDE.md`
- `HERMES.md`
- `.agent-context/rules/project-rules.md`
- `.agent-context/memory/PROJECT_MEMORY.md`

## Review

Run:

```bash
python scripts/agentport.py audit --target /path/to/project
```
