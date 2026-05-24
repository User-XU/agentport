# Portable Agent Context System

Portable Agent Context System is a lightweight project template and toolset for
making an AI working partner portable across machines, projects, and agent
clients.

It is not a vector database and not just a prompt template. It is a context
governance system: rules, memories, project state, public references, and
machine-local private state each have a durable home.

## Why This Exists

Most agent memory systems start from storage. This project starts from the
human workflow problem:

- A useful agent becomes less useful when you change machines.
- Project rules get mixed with global preferences.
- Temporary chat summaries pretend to be durable memory.
- Sensitive local state leaks into synced folders.
- Every new agent needs to be trained from scratch.

This project turns agent context into a portable working system, so the next
machine or agent can inherit structure instead of relearning everything.

## Core Idea

Every piece of context answers two questions before it is stored:

1. What scope does it belong to?
2. What type of context is it?

Scopes:

- `global`: thin user-level constraints and durable collaboration defaults.
- `public`: shared cross-agent rules and memories safe to sync.
- `project`: repository-specific rules, memory, logs, and knowledge.
- `private`: machine-local state, credentials, paths, and sensitive details.

Types:

- `rules`: instructions that constrain behavior.
- `memory`: stable facts and collaboration history.
- `knowledge`: formal reusable research or domain knowledge.
- `logs`: chronological operation records.
- `private-state`: local configuration that should not be synced.

## Project Shape

```text
portable-agent-context-system/
  agent-entry/                  # canonical machine-level agent entry
  docs/                         # philosophy, architecture, quickstart
  templates/                    # copyable project context layouts
  scripts/                      # init, audit, and memory routing helpers
  skills/portable-agent-context # optional agent skill adapter
  examples/                     # concrete mappings from real workflows
  tests/                        # stdlib unittest coverage for scripts
```

Useful docs:

- [Quickstart](docs/quickstart.md)
- [Architecture](docs/architecture.md)
- [Usage recipes](docs/usage-recipes.md)
- [Roadmap](ROADMAP.md)
- [Security](SECURITY.md)

## Quick Start

Initialize a machine-level context workspace:

```bash
/opt/anaconda3/bin/python scripts/pacs.py init-machine --target ~/AgentContext
```

Initialize a project-level context inside an existing repository:

```bash
/opt/anaconda3/bin/python scripts/pacs.py init-project --target /path/to/project
```

Audit a project context:

```bash
/opt/anaconda3/bin/python scripts/pacs.py audit --target /path/to/project
```

Classify a candidate memory before storing it:

```bash
/opt/anaconda3/bin/python scripts/pacs.py route \
  --text "Always use /opt/anaconda3/bin/python for Python work."
```

Verify the repository:

```bash
make verify
```

## Relationship To OpenViking

This project is inspired by the same broad problem space as
[OpenViking](https://github.com/volcengine/OpenViking): agent context is
fragmented, hard to retrieve, and hard to evolve. OpenViking approaches that as
a context database. This project approaches it as a portable personal work
system: Git-friendly files, explicit scopes, agent entrypoints, templates, and
auditable memory evolution.

## Status

Alpha. The first version is intentionally file-first and local-first. A later
version can add MCP, indexing, visual inspection, or integrations with systems
such as OpenViking/OpenMemory without changing the core governance model.
