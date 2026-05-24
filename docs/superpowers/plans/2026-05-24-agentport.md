# AgentPort Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a file-first MVP for portable AI agent context governance.

**Architecture:** The project ships a canonical root `agent-entry/`, project
templates, docs, standard-library Python helpers, and a skill adapter. Scripts
copy entry/template files, audit required files, and route candidate context
into durable buckets.

**Tech Stack:** Markdown, Python standard library, unittest.

---

### Task 1: Documentation And Schema

**Files:**
- Create: `README.md`
- Create: `SCHEMA.md`
- Create: `docs/philosophy.md`
- Create: `docs/architecture.md`
- Create: `docs/quickstart.md`
- Create: `docs/comparison-with-openviking.md`

- [x] Write project positioning and quickstart.
- [x] Define scopes and context types.
- [x] Explain relationship to OpenViking.

### Task 2: Agent Entry And Templates

**Files:**
- Create: `agent-entry/...`
- Create: `templates/project-context/...`

- [x] Create canonical root machine-level agent entry.
- [x] Create project-level context templates.
- [x] Keep private placeholders non-sensitive.

### Task 3: Scripts

**Files:**
- Create: `scripts/context_schema.py`
- Create: `scripts/init_machine.py`
- Create: `scripts/init_project.py`
- Create: `scripts/audit_context.py`
- Create: `scripts/evolve_memory.py`
- Create: `scripts/agentport.py`

- [x] Implement template copy helpers.
- [x] Implement required-file audit.
- [x] Implement sensitive-pattern scan.
- [x] Implement heuristic memory routing.
- [x] Implement unified CLI wrapper.

### Task 4: Skill Adapter

**Files:**
- Create: `skills/agentport/SKILL.md`
- Create: `skills/agentport/references/*.md`

- [x] Write a concise skill body.
- [x] Move detailed routing and safety rules into references.

### Task 5: Tests And Verification

**Files:**
- Create: `tests/test_init_project.py`
- Create: `tests/test_audit_context.py`
- Create: `tests/test_evolve_memory.py`
- Create: `tests/test_cli.py`

- [x] Test project initialization.
- [x] Test machine initialization.
- [x] Test audit behavior.
- [x] Test memory routing.
- [x] Test unified CLI behavior.
- [x] Run `make verify`.
- [x] Verify a temporary project can be initialized and audited cleanly.
