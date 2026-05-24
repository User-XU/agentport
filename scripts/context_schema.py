"""Shared constants for AgentPort scripts."""

from __future__ import annotations

import re
from pathlib import Path


PROJECT_REQUIRED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "HERMES.md",
    ".agent-context/rules/project-rules.md",
    ".agent-context/memory/PROJECT_MEMORY.md",
    ".agent-context/logs/LOG.md",
    ".agent-context/private/README.md",
)

MACHINE_REQUIRED_FILES = (
    "agent-entry/instructions/agent-rules.md",
    "agent-entry/instructions/memory-evolution-policy.md",
    "agent-entry/instructions/project-init-policy.md",
    "agent-entry/memories/MEMORY.md",
    "agent-entry/memories/collaboration.md",
    "agent-entry/memories/safety-boundaries.md",
    "agent-entry/memories/runtime-defaults.md",
    "agent-entry/init/new-machine-agent-init.md",
)

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".env",
    ".py",
    ".js",
    ".ts",
    ".sh",
}

SENSITIVE_PATTERNS = (
    ("openai_key", re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}")),
    (
        "assigned_secret",
        re.compile(
            r"(?i)(api[_-]?key|secret|password|auth[_-]?token|access[_-]?token)"
            r"\s*[:=]\s*['\"]?[^\s'\"]{8,}"
        ),
    ),
    (
        "private_key",
        re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----"),
    ),
)


def project_root() -> Path:
    """Return repository root based on this script location."""

    return Path(__file__).resolve().parents[1]


def template_root(name: str) -> Path:
    """Return a template directory by name."""

    return project_root() / "templates" / name


def agent_entry_root() -> Path:
    """Return the canonical machine-level agent-entry source."""

    return project_root() / "agent-entry"


def should_skip_dir(path: Path) -> bool:
    """Return whether a directory should be skipped during recursive scans."""

    return path.name in EXCLUDED_DIRS


def is_text_candidate(path: Path) -> bool:
    """Return whether the path should be scanned as text."""

    return path.suffix in TEXT_SUFFIXES or path.name in {"AGENTS.md", "CLAUDE.md", "HERMES.md"}
