"""Assignment environment data only; no transition/reward model is assumed."""

from typing import Final

GRID: Final[list[list[int | str]]] = [
    ["start", 0, 0, 0],
    [0, "X", 0, 0],
    [0, 0, 0, 0],
    [0, -1, 0, 10],
]

START_POSITION: Final[tuple[int, int]] = (1, 1)


def format_grid() -> str:
    """Return the sample grid as aligned text."""
    cell_width = max(len(str(cell)) for row in GRID for cell in row)
    return "\n".join(" ".join(f"{str(cell):>{cell_width}}" for cell in row) for row in GRID)
