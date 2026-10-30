"""Demonstrate Strategy 1: persistent context plus optional dynamic context."""

import argparse

from src.context_loader import load_context
from src.environment import START_POSITION, format_grid


def main() -> None:
    parser = argparse.ArgumentParser(description="Demonstrate persistent context loading.")
    parser.add_argument(
        "--dynamic",
        action="store_true",
        help="also load the task-specific dynamic context file",
    )
    args = parser.parse_args()

    print("=== Vacuum Robot Context Engineering Demo ===")
    print("Strategy: 1 — Write / Persistent Memory Architecture")
    print(f"Dynamic context requested: {'yes' if args.dynamic else 'no'}")
    print(f"Robot start position (row, column; zero-based): {START_POSITION}")
    print("\nSample grid (displayed as assignment data, not a learned model):")
    print(format_grid())

    sources = load_context(include_dynamic=args.dynamic)
    print("\n=== Context sources loaded ===")
    for label, content in sources:
        print(f"\n--- {label} ---")
        print(content)

    print("\n=== Takeaway ===")
    print("Stable project/user context persists in files; task-specific context is loaded on demand.")


if __name__ == "__main__":
    main()
