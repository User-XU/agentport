# Project Rules

This repository is the canonical MVP for Portable Agent Context System.

## Scope

- The main product is the independent project: docs, templates, scripts, tests,
  and optional skill adapter.
- The skill under `skills/` is not the product itself. It is an adapter that
  teaches agents how to operate the project.
- Keep the first version file-first and standard-library only.

## Editing Rules

- Keep generated context templates generic and safe to publish.
- Do not embed private paths, credentials, or user-specific secrets.
- Prefer auditable files and scripts over hidden state.
- Update `docs/` when the model or workflow changes.
- Update tests when script behavior changes.

## Verification

Run:

```bash
make verify
```

If `make` is unavailable, run the equivalent commands from `Makefile`.
