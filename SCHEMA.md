# Context Schema

This schema defines the durable file contracts for AgentPort
System.

## Scopes

### global

Machine-level or user-level defaults that should stay thin. Examples:

- preferred collaboration style
- global safety boundaries
- default tools and verification habits

Do not put project-specific rules here.

### public

Cross-agent context that is safe to sync and useful to multiple agents. Examples:

- shared behavior rules
- memory evolution policy
- collaboration preferences
- durable tool facts with no secrets

### project

Repository-specific context. Examples:

- project startup files
- directory roles
- validation commands
- stable project memory
- operation logs

### private

Machine-local or sensitive context. Examples:

- API keys and tokens
- exact private server details
- local session state
- credentials
- raw private logs

Private context is not copied into public templates and should be excluded from
Git by the consuming project.

## Context Types

| Type | Purpose | Examples |
| --- | --- | --- |
| `rules` | Constrain future agent behavior | must-read files, no-touch paths |
| `memory` | Preserve stable facts | collaboration style, project decisions |
| `knowledge` | Reusable formal content | articles, comparisons, research pages |
| `logs` | Chronological actions | create/update/audit/export records |
| `private-state` | Local sensitive state | tokens, machine paths, auth state |

## Minimum Project Context

A project initialized with this system should contain:

```text
AGENTS.md
CLAUDE.md
HERMES.md
.agent-context/
  rules/project-rules.md
  memory/PROJECT_MEMORY.md
  logs/LOG.md
  private/README.md
```

## Minimum Machine Context

The repository root keeps the canonical `agent-entry/`. A machine-level context
workspace initialized from it should contain:

```text
agent-entry/
  instructions/agent-rules.md
  instructions/memory-evolution-policy.md
  instructions/project-init-policy.md
  memories/MEMORY.md
  memories/collaboration.md
  memories/safety-boundaries.md
  memories/runtime-defaults.md
  init/new-machine-agent-init.md
```
