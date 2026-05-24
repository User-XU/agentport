# Portable Agent Context System Design

## Goal

Create an independent, file-first project that helps a user carry AI agent
context across machines, projects, and agent clients without losing accumulated
collaboration training.

## Product Positioning

Portable Agent Context System is a personal AI working partner context system.
It is not a single skill and not a memory database. The project includes a
canonical `agent-entry/`, documentation, project templates, scripts, and an
optional skill adapter.

## First Release Scope

The MVP includes:

- project README and conceptual docs
- root machine-level `agent-entry/`
- project context templates
- init scripts for machine and project contexts
- audit script for required files and sensitive leakage
- memory routing script for candidate facts/rules
- unified CLI wrapper
- optional Codex/Claude/Hermes-style skill adapter
- tests for the Python helpers

## Non-Goals

- no MCP server
- no vector database
- no web UI
- no automatic background memory writes
- no credential storage

## Architecture

The project uses four layers:

1. Agent Entry: canonical shared machine-level bootstrap files.
2. Context Registry: scopes and types that decide where context belongs.
3. Initialization Layer: copy templates into new machine/project contexts.
4. Evolution Layer: classify, audit, and review candidate memories.

## Success Criteria

- A new directory can be initialized as a project context.
- A new machine context can be initialized from the root `agent-entry/`.
- Audit reports missing required files and likely secrets.
- Memory routing returns a clear recommended bucket.
- The project can be understood from README and docs without prior chat context.
