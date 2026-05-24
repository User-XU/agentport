# Philosophy

Portable Agent Context System is built around one belief:

> The future advantage is not a person using an AI tool once. It is a person and
> a trained AI working partner becoming a durable unit.

That unit breaks when context is scattered across chats, machines, local config,
and project-specific rules. The system exists to make that unit portable.

## What Should Persist

The system preserves:

- rules that constrain future agent behavior
- memories that help the agent understand the user and project
- knowledge that has long-term reuse value
- logs that explain how the system evolved
- explicit private boundaries that prevent unsafe synchronization

## What Should Not Persist Everywhere

The system avoids spreading:

- credentials and tokens
- local machine state
- raw session logs
- private server details
- temporary drafts masquerading as durable memory

## Design Principles

### Context Is Governed Before It Is Stored

Storage is easy. Placement is hard. Every context item is routed by scope and
type before it becomes durable.

### Rules And Memory Are Different

Rules tell the agent how to behave. Memory tells the agent what is true or what
has been learned. Mixing them creates brittle agents.

### Public And Private Are Different

Portable context should sync. Sensitive local state should not. Convenience is
not a reason to collapse that boundary.

### Projects Deserve Autonomy

A project should own its directory rules, validation commands, and history.
Global context should not silently overrule local project constraints.

### Evolution Must Be Auditable

The agent should get better over time, but not by silently rewriting memory.
Changes should be inspectable and reversible.

