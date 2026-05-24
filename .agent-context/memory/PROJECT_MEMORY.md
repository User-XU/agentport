# Project Memory

Curated memory for AgentPort.

## Stable Facts

- Product shape: independent project first, skill adapter second.
- Core value: cross-machine, cross-project, cross-agent context continuity.
- First version: file-first templates and standard-library Python scripts.
- Inspired by OpenViking's agent context problem framing, but positioned as
  file-first portable context governance rather than a context database.

## Decisions

2026-05-24:

- Chose AgentPort as the public project name.
- Included docs, templates, scripts, tests, examples, and an `agentport` skill
  adapter in the MVP.
- Deferred MCP server, vector database, and web UI to later stages.
- Promoted `agent-entry/` to a root-level canonical directory. Machine
  initialization copies from this root entry so public agent rules and generated
  machine context do not drift.
- Renamed the public repository from `portable-agent-context-system` to
  `agentport` because the earlier descriptive name was too long for an
  open-source project identity.
