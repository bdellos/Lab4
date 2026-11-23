---
name: analyze-episode
description: Analyze a recorded vacuum robot episode, meaning its sequence of states, actions, and rewards. Find loops, dead ends, and invalid moves, then summarize the episode.
---
Goal: analyze an episode that already exists in the repository. Report only. Do not edit files.

Steps:
1. Call search with pattern "episode" and path ".". Look for a file or test that holds a list of (state, action, reward) steps.
2. If no episode data is found, answer "no episode data found", list the files you searched, and stop. Do not invent an episode.
3. Call read_file on the file that holds the episode.
4. Loops: list every state that appears more than once.
5. Dead ends: list every step where the position did not change after an action (a blocked move).
6. Invalid moves: list every position outside the 4x4 grid (row or column below 0 or above 3) or on the X cell at (1, 1).

Final answer (inside <final>), using exactly these lines:
- Episode source: file and line numbers
- Steps: number of steps
- Loops: ... or "none"
- Dead ends: ... or "none"
- Invalid moves: ... or "none"
- Result: "episode valid", "loop detected", "dead end detected", or "invalid move detected"
