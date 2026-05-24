# Comparison With OpenViking

[OpenViking](https://github.com/volcengine/OpenViking) is an open-source context
database for AI agents. It uses a filesystem-oriented paradigm to manage agent
context such as memories, resources, and skills.

AgentPort is inspired by the same problem but starts from a
different product layer.

| Dimension | OpenViking | AgentPort |
| --- | --- | --- |
| Primary layer | context database | personal/workspace context governance |
| Core object | memories, resources, skills | rules, memories, projects, knowledge, private state |
| Main value | retrieval, loading, context database operations | cross-machine continuity and agent onboarding |
| User | agent developers and system builders | heavy AI users, developers, knowledge workers |
| Storage | service/database-oriented implementation | Git-friendly files and templates |
| Evolution | automatic session/context self-iteration | auditable memory routing and project logs |
| First version | server, CLI, models | repo template, scripts, skill adapter |

## Complementary, Not Competitive

OpenViking can become a future backend for retrieval and indexing. Portable
Agent Context System defines the human-readable governance layer that decides
what should enter memory, where it belongs, and what must remain private.

## Differentiation

AgentPort focuses on:

- new-machine onboarding
- multi-agent shared entrypoints
- project-level rules and memory
- private/public boundary management
- long-term training of a personal AI working partner

