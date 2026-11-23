---
name: validate-environment
description: Validate the vacuum robot grid environment. Check the grid size, start position, X cell, boundaries, and terminal states against the expected facts and context files, and report any mismatch.
---
Goal: check that the grid stored in code matches the expected facts. Report only. Do not edit files.

Expected facts (zero-based (row, column) coordinates):
- 4 rows and 4 columns
- "start" at (0, 0)
- "X" at (1, 1)
- -1 at (3, 1)
- 10 at (3, 3)
- every other cell is 0

Rules:
- Do not assume X is the start position.
- Do not assume what X, -1 or 10 mean (wall, penalty, goal). Report them only as cell values.

Steps:
1. Call read_file on src/environment.py. Find the grid (GRID) and the start position (START_POSITION or START).
2. Check the grid has 4 rows of 4 cells, and that every cell matches the expected facts.
3. Check the start position points to the cell that holds "start". If it points anywhere else, report it as a problem.
4. Call read_file on memory/dynamic/context.md if it exists. Note every sentence that disagrees with the expected facts.
5. Boundaries: a position is in bounds only if row and column are both between 0 and 3. List the in-bounds neighbors of the start cell.
6. Terminal states: check whether any file you read defines which cells end an episode. If none does, write "terminal states not defined". Do not guess.

Final answer (inside <final>), using exactly these lines:
- Files checked: ...
- Matches: ...
- Problems: one per line as "file: what it says vs. expected", or "none"
- Boundaries: ...
- Terminal states: ...
- Result: "environment valid" if there are no problems, otherwise "environment has problems"
