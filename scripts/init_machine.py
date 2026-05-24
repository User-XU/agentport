#!/usr/bin/env python3
"""Initialize a machine-level portable agent context workspace."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from context_schema import agent_entry_root


def copy_tree(template: Path, target: Path, *, force: bool = False, dry_run: bool = False) -> dict[str, list[str]]:
    """Copy template files into target without overwriting unless forced."""

    result = {"created": [], "skipped": []}
    for src in sorted(template.rglob("*")):
        if src.is_dir():
            continue
        rel = src.relative_to(template)
        dst = target / rel
        if dst.exists() and not force:
            result["skipped"].append(str(dst))
            continue
        result["created"].append(str(dst))
        if not dry_run:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
    return result


def init_machine(target: Path, *, force: bool = False, dry_run: bool = False) -> dict[str, list[str]]:
    """Initialize machine context at target."""

    return copy_tree(agent_entry_root(), target / "agent-entry", force=force, dry_run=dry_run)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Target directory for machine context")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    args = parser.parse_args()

    result = init_machine(Path(args.target).expanduser().resolve(), force=args.force, dry_run=args.dry_run)
    for key in ("created", "skipped"):
        print(f"{key}: {len(result[key])}")
        for path in result[key]:
            print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
