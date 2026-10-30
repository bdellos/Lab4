# Project Memory — Vacuum Robot Lab

## Project context
- This is a classroom lab about a vacuum robot in a 4×4 grid.
- The current task is to demonstrate context-engineering Strategy 1: Write / Persistent Memory Architecture.
- The current lab description says transition and reward functions are not provided as expected; Q-learning is a later task, not part of this demonstration.
- The sample grid shown in the handout is represented in `src/environment.py`.

## Architecture
- Python 3.10+.
- Standard library only for this demo.
- `src/context_loader.py` reads persistent context files.
- `src/environment.py` stores the example grid and starting location.
- `src/demo.py` prints the context sources and a compact environment summary.
- Unit tests are in `tests/`.

## Coding standards
- Use descriptive names.
- Add explicit type hints to public functions.
- Keep context content in Markdown files rather than hard-coding it into the demo.
- Do not invent transition rules, rewards, or Q-learning behavior that the handout has not defined.

## Validation
- Run `python -m unittest discover -s tests -v`.
- Run `python -m src.demo`.
