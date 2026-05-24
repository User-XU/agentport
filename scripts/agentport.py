#!/usr/bin/env python3
"""Unified CLI for AgentPort."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from audit_context import audit
from evolve_memory import classify_text, write_candidate
from init_machine import init_machine
from init_project import copy_project_template


def print_copy_result(result: dict[str, list[str]]) -> None:
    """Print created/skipped files from an init operation."""

    for key in ("created", "skipped"):
        print(f"{key}: {len(result[key])}")
        for path in result[key]:
            print(f"  {path}")


def cmd_init_machine(args: argparse.Namespace) -> int:
    """Initialize machine-level context."""

    result = init_machine(Path(args.target).expanduser().resolve(), force=args.force, dry_run=args.dry_run)
    print_copy_result(result)
    return 0


def cmd_init_project(args: argparse.Namespace) -> int:
    """Initialize project-level context."""

    result = copy_project_template(Path(args.target).expanduser().resolve(), force=args.force, dry_run=args.dry_run)
    print_copy_result(result)
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    """Audit a machine or project context."""

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


def cmd_route(args: argparse.Namespace) -> int:
    """Route candidate context into a recommended bucket."""

    candidate = args.text if args.text is not None else Path(args.file).read_text(encoding="utf-8")
    route = classify_text(candidate)
    payload = asdict(route)
    if args.write:
        path = write_candidate(Path(args.root).expanduser().resolve(), candidate, route)
        payload["written_path"] = str(path)
    if args.format == "json":
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"bucket: {route.bucket}")
        print(f"confidence: {route.confidence}")
        print(f"safe_to_sync: {route.safe_to_sync}")
        print(f"reason: {route.reason}")
    return 0 if route.bucket != "discard" else 1


def build_parser() -> argparse.ArgumentParser:
    """Build the CLI parser."""

    parser = argparse.ArgumentParser(description="AgentPort CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_machine_parser = subparsers.add_parser("init-machine", help="Create machine-level agent-entry files")
    init_machine_parser.add_argument("--target", default=".", help="Target directory for machine context")
    init_machine_parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    init_machine_parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    init_machine_parser.set_defaults(func=cmd_init_machine)

    init_project_parser = subparsers.add_parser("init-project", help="Create project-level agent context files")
    init_project_parser.add_argument("--target", default=".", help="Target project directory")
    init_project_parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    init_project_parser.add_argument("--dry-run", action="store_true", help="Show actions without writing")
    init_project_parser.set_defaults(func=cmd_init_project)

    audit_parser = subparsers.add_parser("audit", help="Audit required files and likely secret leakage")
    audit_parser.add_argument("--target", default=".", help="Context directory to audit")
    audit_parser.add_argument("--mode", choices=["auto", "machine", "project"], default="auto")
    audit_parser.add_argument("--json", action="store_true", help="Emit JSON")
    audit_parser.set_defaults(func=cmd_audit)

    route_parser = subparsers.add_parser("route", help="Classify candidate context before storing it")
    source = route_parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Candidate context text")
    source.add_argument("--file", help="Path to a candidate context file")
    route_parser.add_argument("--format", choices=["json", "markdown"], default="json")
    route_parser.add_argument("--write", action="store_true", help="Write candidate to .agent-context/inbox")
    route_parser.add_argument("--root", default=".", help="Project root for --write")
    route_parser.set_defaults(func=cmd_route)

    return parser


def main() -> int:
    """CLI entrypoint."""

    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
