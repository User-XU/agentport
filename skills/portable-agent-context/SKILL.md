---
name: portable-agent-context
description: Use when working with Portable Agent Context System: initialize machine or project agent context, audit context placement, route candidate memories, or decide where rules, memories, knowledge, logs, and private state should live across machines and agents.
---

# Portable Agent Context

This skill teaches an agent how to operate a Portable Agent Context System
project. The system's main product is the repository, especially `agent-entry/`,
project templates, and scripts; this skill is only an adapter for agents.

## When To Use

Use this skill when the user asks to:

- initialize a new machine or project for portable agent context
- decide whether something is a rule, memory, knowledge item, log, or private state
- audit a context folder for missing files or likely secret leakage
- make AI agent context portable across machines, projects, or agent clients
- evolve project or public memory after a task

## Core Workflow

1. Inspect the target directory before writing.
2. Read `SCHEMA.md` for scope and type contracts.
3. For initialization, use `scripts/pacs.py` instead of hand-building files:
   - `scripts/pacs.py init-machine`
   - `scripts/pacs.py init-project`
4. For candidate memory, run `scripts/pacs.py route` and review the bucket.
5. For safety and completeness, run `scripts/pacs.py audit`.
6. Do not store secrets or local private state in syncable context.

## References

Read only the reference needed for the task:

- `references/routing-rules.md` for where context belongs.
- `references/memory-evolution.md` for durable memory decisions.
- `references/project-init.md` for new project or machine setup.
- `references/safety-boundaries.md` for private/public boundary checks.
