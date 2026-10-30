# Copilot Instructions — Vacuum Robot Lab

## Project purpose
This repository demonstrates Strategy 1: Write / Persistent Memory Architecture for the vacuum robot lab.

## Architecture
- Python 3.10+; standard library only.
- `src/context_loader.py` loads Markdown context files.
- `src/environment.py` stores the sample grid as assignment data.
- `src/demo.py` demonstrates default and optional dynamic context loading.
- `memory/project/CLAUDE.md` contains the shared project context and rules.
- `memory/user/CLAUDE.md` contains example developer workflow preferences.
- `memory/dynamic/context.md` contains task-specific grid facts.

## Important constraints
- Do not invent transition rules, reward functions, or Q-learning behavior. The assignment says Q-learning comes later and the supplied description does not define those rules.
- Treat the grid values as assignment data only unless the assignment defines their meaning.
- Keep changes small and explain which files are changed.
- Use descriptive names and type hints for public functions.
- Do not place passwords, API keys, or private credentials in repository files.

## Validation
- Demo: `python -m src.demo`
- Optional dynamic context demo: `python -m src.demo --dynamic`
- Tests: `python -m unittest discover -s tests -v`

When asked about task-specific grid facts, read `memory/dynamic/context.md` rather than guessing.
