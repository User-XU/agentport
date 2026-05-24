# Quickstart

Use `/opt/anaconda3/bin/python` for these commands on the author's Mac. On other
machines, use a suitable Python 3.10+ interpreter.

## Initialize A Machine Context

```bash
/opt/anaconda3/bin/python scripts/agentport.py init-machine --target ~/AgentContext
```

This creates:

```text
~/AgentContext/agent-entry/
  instructions/
  memories/
  init/
```

Give a new agent this instruction:

```text
Read ~/AgentContext/agent-entry/init/new-machine-agent-init.md, then follow the
instructions and memories under ~/AgentContext/agent-entry/.
```

## Initialize A Project Context

```bash
/opt/anaconda3/bin/python scripts/agentport.py init-project --target /path/to/project
```

This creates:

```text
/path/to/project/
  AGENTS.md
  CLAUDE.md
  HERMES.md
  .agent-context/
```

## Audit Context Placement

```bash
/opt/anaconda3/bin/python scripts/agentport.py audit --target /path/to/project
```

Audit checks:

- required context files
- likely credential leaks
- private state accidentally stored outside private paths

## Route A New Memory

```bash
/opt/anaconda3/bin/python scripts/agentport.py route \
  --text "For this project, run make verify before claiming completion."
```

The script returns a recommended bucket such as `project_rules`,
`project_memory`, `public_memory`, `knowledge`, or `private_state`.

## Recommended Git Flow

1. Initialize the machine or project context.
2. Review generated files.
3. Edit placeholders.
4. Run `scripts/agentport.py audit`.
5. Commit only reviewed public/project context.
6. Keep `.agent-context/private/` local.
