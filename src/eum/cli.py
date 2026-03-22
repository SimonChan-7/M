"""Project CLI placeholder for the unified pipeline chain."""

from __future__ import annotations

PIPELINE_STEPS = ("parse", "mine", "extract", "validate", "normalize", "aggregate", "evaluate")


def main() -> None:
    """Placeholder CLI entrypoint."""
    print("TODO: implement unified CLI", " -> ".join(PIPELINE_STEPS))


if __name__ == "__main__":
    main()
