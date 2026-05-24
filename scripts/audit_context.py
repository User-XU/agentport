#!/usr/bin/env python3
"""Audit a portable agent context workspace."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path

from context_schema import (
    MACHINE_REQUIRED_FILES,
    PROJECT_REQUIRED_FILES,
    SENSITIVE_PATTERNS,
    is_text_candidate,
    should_skip_dir,
)


@dataclass
class Issue:
    severity: str
    kind: str
    path: str
    message: str


def detect_mode(target: Path, requested: str) -> str:
    """Resolve audit mode."""

    if requested != "auto":
        return requested
    if (target / ".agent-context").exists() or (target / "AGENTS.md").exists():
        return "project"
    if (target / "agent-entry").exists():
        return "machine"
    return "project"


def iter_files(target: Path):
    """Yield files under target while skipping common dependency/cache dirs."""

    for path in target.rglob("*"):
        if path.is_dir() and should_skip_dir(path):
            continue
        if any(part in {".git", "node_modules", "__pycache__", ".venv", "venv"} for part in path.parts):
            continue
        if path.is_file():
            yield path


def check_required(target: Path, mode: str) -> list[Issue]:
    """Check required files for mode."""

    required = MACHINE_REQUIRED_FILES if mode == "machine" else PROJECT_REQUIRED_FILES
    issues: list[Issue] = []
    for rel in required:
        if not (target / rel).exists():
            issues.append(Issue("error", "missing_required_file", rel, f"Missing required file: {rel}"))
    return issues


def scan_sensitive(target: Path) -> list[Issue]:
    """Scan text files for likely secrets."""

    issues: list[Issue] = []
    for path in iter_files(target):
        if path.stat().st_size > 1_000_000 or not is_text_candidate(path):
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = str(path.relative_to(target))
        if ".agent-context/private/" in rel:
            continue
        for name, pattern in SENSITIVE_PATTERNS:
            if pattern.search(content):
                issues.append(Issue("error", "possible_secret", rel, f"Possible secret matched pattern: {name}"))
    return issues


def audit(target: Path, mode: str = "auto") -> dict:
    """Run audit and return structured result."""

    target = target.resolve()
    resolved_mode = detect_mode(target, mode)
    issues = check_required(target, resolved_mode)
    issues.extend(scan_sensitive(target))
    return {
        "target": str(target),
        "mode": resolved_mode,
        "ok": not issues,
        "issues": [asdict(issue) for issue in issues],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", default=".", help="Context directory to audit")
    parser.add_argument("--mode", choices=["auto", "machine", "project"], default="auto")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    result = audit(Path(args.target).expanduser(), args.mode)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"target: {result['target']}")
        print(f"mode: {result['mode']}")
        print(f"ok: {result['ok']}")
        for issue in result["issues"]:
            print(f"- [{issue['severity']}] {issue['kind']} {issue['path']}: {issue['message']}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
