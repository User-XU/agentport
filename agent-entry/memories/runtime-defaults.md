# Runtime Defaults

Use this file for stable runtime defaults that are safe to sync.

## Starter Defaults

- Prefer the target project's own toolchain when it exists.
- If the project has no toolchain preference, use a standard Python 3.10+
  interpreter for these scripts.
- Run audit before syncing generated agent context.
- Keep machine-specific paths in local private memory, not in shared rules.

## Customize

Add local defaults only if they are safe and useful on future machines. Keep
secrets and host-specific details out of this file.
