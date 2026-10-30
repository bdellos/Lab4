"""Load persistent context from Markdown files in a predictable order."""

from pathlib import Path
from typing import Final

ROOT: Final[Path] = Path(__file__).resolve().parents[1]
PROJECT_MEMORY: Final[Path] = ROOT / "memory" / "project" / "CLAUDE.md"
USER_MEMORY: Final[Path] = ROOT / "memory" / "user" / "CLAUDE.md"
DYNAMIC_CONTEXT: Final[Path] = ROOT / "memory" / "dynamic" / "context.md"


def read_context_file(path: Path) -> str:
    """Read one context file, raising a useful error if it is missing."""
    if not path.is_file():
        raise FileNotFoundError(f"Required context file not found: {path}")
    return path.read_text(encoding="utf-8").strip()


def load_context(include_dynamic: bool = False) -> list[tuple[str, str]]:
    """Return labelled context sources; dynamic context is opt-in."""
    sources = [
        ("Project memory", read_context_file(PROJECT_MEMORY)),
        ("User memory", read_context_file(USER_MEMORY)),
    ]
    if include_dynamic:
        sources.append(("Dynamic task context", read_context_file(DYNAMIC_CONTEXT)))
    return sources
