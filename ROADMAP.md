# Roadmap

## v0.1: File-First MVP

- Canonical root `agent-entry/` for machine-level bootstrap.
- Project-level `.agent-context/` template.
- Shared entry files for Codex, Claude, Hermes, and similar agents.
- Context audit for required files and likely secret leakage.
- Candidate memory routing into public, project, knowledge, review, or private
  buckets.
- Optional skill adapter for agents that support local skills.

## v0.2: Operational Polish

- Stronger CLI workflows around initialization, audit, and memory routing.
- Better examples for Obsidian vaults, software repositories, and research
  projects.
- Git sync checklist and bootstrap scripts for new machines.
- More precise policy around what should become public memory versus project
  memory.

## v0.3: Retrieval Layer

- Optional index generation for large context folders.
- Local search helpers for rules, memory, logs, and knowledge.
- Adapter points for systems such as OpenViking or OpenMemory.
- Keep files as the source of truth even when indexes exist.

## Later

- MCP server for agent clients.
- Visual context map.
- Web or desktop inspector.
- Cross-agent compatibility tests.
