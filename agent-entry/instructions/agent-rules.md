# Agent Rules

This is the portable entry layer for agents. It is safe to sync, copy to a new
machine, and adapt into a personal or team workspace.

## Purpose

These rules teach a new agent how to behave before it knows a specific project.
Project-specific rules still belong in that project's `.agent-context/rules/`.

## Operating Principles

- Inspect real local state before making claims about files, tools, or runtime.
- Keep changes small and directly tied to the user's goal.
- Preserve user changes and never revert unrelated work.
- Separate durable memory from temporary conversation.
- Treat credentials, tokens, private server data, and local session state as
  private by default.
- Verify before claiming completion.

## Context Placement

- Put cross-agent behavior constraints in `agent-entry/instructions/`.
- Put stable cross-agent facts in `agent-entry/memories/`.
- Put project-specific constraints in `.agent-context/rules/`.
- Put project memory in `.agent-context/memory/`.
- Put sensitive machine-local state outside synced folders, or under ignored
  private paths.

## New Agent Startup

When a new agent enters this context:

1. Read `agent-entry/init/new-machine-agent-init.md`.
2. Read this file.
3. Read `agent-entry/instructions/memory-evolution-policy.md`.
4. Read the memory index at `agent-entry/memories/MEMORY.md`.
5. Inspect the target project before applying project-specific rules.
