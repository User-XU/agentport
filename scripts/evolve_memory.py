#!/usr/bin/env python3
"""Classify candidate context before making it durable memory."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

from context_schema import SENSITIVE_PATTERNS


RULE_WORDS = ("must", "always", "never", "rule", "policy", "必须", "总是", "永远", "不要", "规则", "约束")
PROJECT_WORDS = ("project", "repo", "repository", "directory", "path", "test", "README", "SCHEMA", "项目", "仓库", "目录", "验证")
PREFERENCE_WORDS = ("prefer", "preference", "collaboration", "style", "我喜欢", "偏好", "协作", "风格")
KNOWLEDGE_WORDS = ("research", "source", "paper", "article", "concept", "comparison", "知识", "研究", "论文", "文章", "对比")


@dataclass
class Route:
    bucket: str
    confidence: str
    reason: str
    safe_to_sync: bool


def contains_sensitive(text: str) -> bool:
    """Return whether text looks sensitive."""

    return any(pattern.search(text) for _, pattern in SENSITIVE_PATTERNS)


def has_any(text: str, words: tuple[str, ...]) -> bool:
    """Case-insensitive keyword test."""

    lowered = text.lower()
    return any(word.lower() in lowered for word in words)


def classify_text(text: str) -> Route:
    """Classify candidate context into a recommended durable bucket."""

    compact = re.sub(r"\s+", " ", text).strip()
    if not compact:
        return Route("discard", "high", "empty candidate", False)
    if contains_sensitive(compact):
        return Route("private_state", "high", "candidate appears to contain a secret or credential", False)
    if has_any(compact, RULE_WORDS) and has_any(compact, PROJECT_WORDS):
        return Route("project_rules", "medium", "candidate looks like a project-specific behavior rule", True)
    if has_any(compact, RULE_WORDS):
        return Route("public_rules", "medium", "candidate looks like a reusable behavior rule", True)
    if has_any(compact, PROJECT_WORDS):
        return Route("project_memory", "medium", "candidate looks project-specific", True)
    if has_any(compact, KNOWLEDGE_WORDS):
        return Route("knowledge", "medium", "candidate looks like reusable formal knowledge", True)
    if has_any(compact, PREFERENCE_WORDS):
        return Route("public_memory", "medium", "candidate looks like a stable collaboration preference", True)
    return Route("review", "low", "candidate needs human review before durable storage", True)


def write_candidate(root: Path, text: str, route: Route) -> Path:
    """Write candidate to a review inbox for later human confirmation."""

    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    out_dir = root / ".agent-context" / "inbox"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{stamp}-{route.bucket}.md"
    path.write_text(
        "\n".join(
            [
                "---",
                f"bucket: {route.bucket}",
                f"confidence: {route.confidence}",
                f"safe_to_sync: {str(route.safe_to_sync).lower()}",
                "---",
                "",
                text.strip(),
                "",
            ]
        ),
        encoding="utf-8",
    )
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Candidate context text")
    source.add_argument("--file", help="Path to a candidate context file")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    parser.add_argument("--write", action="store_true", help="Write candidate to .agent-context/inbox")
    parser.add_argument("--root", default=".", help="Project root for --write")
    args = parser.parse_args()

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


if __name__ == "__main__":
    raise SystemExit(main())

