# Usage Recipes

## 1. Bootstrap A New Machine

```bash
git clone https://github.com/User-XU/agentport.git
cd agentport
/opt/anaconda3/bin/python scripts/agentport.py init-machine --target ~/AgentContext
```

Then give a new agent:

```text
Read ~/AgentContext/agent-entry/init/new-machine-agent-init.md, then orient
yourself from the instructions and memories under ~/AgentContext/agent-entry/.
```

## 2. Add Project Context To A Repository

```bash
/opt/anaconda3/bin/python scripts/agentport.py init-project --target /path/to/project
/opt/anaconda3/bin/python scripts/agentport.py audit --target /path/to/project --json
```

Review generated files before committing them.

## 3. Route A Candidate Memory

```bash
/opt/anaconda3/bin/python scripts/agentport.py route \
  --text "For this project, always run make verify before claiming completion."
```

If the output bucket is:

- `public_rules`: put it under `agent-entry/instructions/`.
- `public_memory`: put it under `agent-entry/memories/`.
- `project_rules`: put it under `.agent-context/rules/`.
- `project_memory`: put it under `.agent-context/memory/`.
- `knowledge`: promote it into a formal knowledge base.
- `private_state`: keep it local and unsynced.
- `review`: ask before making it durable.

## 4. Let An Agent Self-Check The Context

```bash
make verify
```

This runs tests, project audit, and machine-entry audit.

## 5. Use The Skill Adapter

Copy or symlink `skills/agentport/` into an agent skill directory.
The skill is not the product. It is only an adapter that teaches compatible
agents how to operate this repository.
