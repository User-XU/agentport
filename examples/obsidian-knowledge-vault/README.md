# Example: Obsidian Knowledge Vault

This example maps a Git-backed Obsidian vault into Portable Agent Context System
terms.

## Mapping

| Existing Area | Portable Context Role |
| --- | --- |
| root agent entry files | project agent entry |
| `public/agent-entry/instructions/` | public rules |
| `public/agent-entry/memories/` | public memory |
| `knowledge/SCHEMA.md` | project rules/schema |
| `knowledge/log.md` | project log |
| `knowledge/_meta/project-memory/` | project memory |
| `knowledge/_outputs/` | temporary outputs and drafts |
| `knowledge/queries/` | formal reusable knowledge |

## Lesson

The important part is not the exact folder names. The important part is that
public rules, public memory, project rules, project memory, outputs, formal
knowledge, and private state do not collapse into one bucket.

