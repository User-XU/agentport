# Project Memory

Curated memory for Portable Agent Context System.

## Stable Facts

- Product shape: independent project first, skill adapter second.
- Core value: cross-machine, cross-project, cross-agent context continuity.
- First version: file-first templates and standard-library Python scripts.
- Inspired by OpenViking's agent context problem framing, but positioned as a
  personal AI working partner context governance system rather than a context
  database.

## Decisions

2026-05-24:

- Chose `portable-agent-context-system` as the local project directory.
- Included docs, templates, scripts, tests, examples, and a portable-agent-context
  skill adapter in the MVP.
- Deferred MCP server, vector database, and web UI to later stages.
- Promoted `agent-entry/` to a root-level canonical directory. Machine
  initialization copies from this root entry so public agent rules and generated
  machine context do not drift.
