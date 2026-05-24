# Architecture

Portable Agent Context System has four layers.

## 1. Agent Entry

Agent entry files are the first documents an agent reads when it enters a
machine or project.

Purpose:

- point Codex, Claude, Hermes, and similar agents to the same shared rules
- keep agent-specific bootstrap files thin
- avoid duplicating policy text across every agent entrypoint

Machine template:

```text
agent-entry/
  instructions/
  memories/
  init/
```

The repository root contains this `agent-entry/` directly. It is the canonical
source for machine-level bootstrap files. `scripts/pacs.py init-machine` copies
it into a target workspace as `target/agent-entry/`.

Project template:

```text
AGENTS.md
CLAUDE.md
HERMES.md
.agent-context/
```

## 2. Context Registry

The registry is a file-first map of where context belongs.

| Scope | Stored in | Purpose |
| --- | --- | --- |
| `global` | user-managed agent config | thin personal defaults |
| `public` | syncable shared context | cross-agent rules and memories |
| `project` | repository-local `.agent-context/` | project rules and memory |
| `private` | machine-local ignored paths | sensitive state |

The registry is intentionally compatible with Git and Obsidian-like vaults.

## 3. Initialization Layer

Initialization scripts create consistent starting structures:

- `scripts/pacs.py init-machine` creates machine-level `agent-entry/`.
- `scripts/pacs.py init-project` creates project-level `.agent-context/` files.
- templates are copied without overwriting by default.

New machines should inherit structure, then recalibrate local tools and paths.

## 4. Evolution Layer

Evolution is the process of deciding whether a new fact or instruction should be
stored.

The first version is intentionally conservative:

- `scripts/pacs.py route` classifies candidate context into a recommended
  bucket.
- `scripts/pacs.py audit` checks required files and sensitive leakage.
- humans or agents can review recommendations before committing changes.

Later versions can add MCP, search indexes, embeddings, or OpenViking-style
context storage behind the same file contracts.

## Data Flow

```text
conversation / task / project event
  -> candidate context
  -> scope and type routing
  -> public / project / knowledge / private placement
  -> audit
  -> Git sync or local-only retention
```

## Why File-First

A file-first system is easier to:

- clone to a new machine
- review in Git
- edit by hand
- use from any agent
- back up without vendor lock-in

Databases can be added later. They should accelerate retrieval, not replace the
governance model.
