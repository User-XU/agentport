#!/usr/bin/env python3
"""Initialize project-level agent context files."""

from __future__ import annotations

import argparse
from pathlib import Path

from context_schema import template_root


def render_template(text: str, project_name: str) -> str:
    """Render simple placeholders in template text."""

    return text.replace("{{PROJECT_NAME}}", project_name)


def copy_project_template(target: Path, *, force: bool = False, dry_run: bool = False) -> dict[str, list[str]]:
    """Copy project template files into target."""

    template = template_root("project-context")
    result = {"created": [], "skipped": []}
    project_name = target.name
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
            content = render_template(src.read_text(encoding="utf-8"), project_name)
            dst.write_text(content, encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Target project directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    result = copy_project_template(target, force=args.force, dry_run=args.dry_run)
    for key in ("created", "skipped"):
        print(f"{key}: {len(result[key])}")
        for path in result[key]:
            print(f"  {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

