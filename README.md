# Vacuum Robot Lab — Strategy 1: Write / Persistent Memory Architecture

This repository adapts **slide 21's three-layer persistent memory architecture** to a small Python demonstration that can be run with a free GitHub Copilot account. The goal is to show how project knowledge can be written to files, kept separate by purpose, and loaded again when needed.

> **Tooling honesty:** `CLAUDE.md` and `@...` imports are Claude Code conventions. GitHub Copilot does not automatically treat those files as Claude Code memory. In this repository, `.github/copilot-instructions.md` is the Copilot-specific instruction file, and `src/context_loader.py` explicitly demonstrates loading the three context layers. When using Copilot Chat, ask it to open/read the relevant files and verify its References when available.

## The three layers from slide 21

| Slide 21 layer | Repository example | Purpose in this demo |
|---|---|---|
| **Project memory** (`./CLAUDE.md`) | `CLAUDE.md` and `memory/project/CLAUDE.md` | Shared project facts, architecture, coding rules, and boundaries. The root `CLAUDE.md` is a Claude Code example; the nested Markdown file is also loaded explicitly by the Python demo. |
| **User memory** (`~/.claude/CLAUDE.md`) | `memory/user/CLAUDE.md` | Example reusable developer preferences. This is a repository-local **simulation** of user memory, not a claim that Copilot automatically reads a home-directory Claude file. Replace the example preferences with your own if appropriate. |
| **Dynamic imports** (`@context.md`) | `memory/dynamic/context.md` | Task-specific facts loaded only when requested. `python -m src.demo --dynamic` demonstrates this on-demand layer. |

## Project structure

```text
context-engineering-vacuum-lab/
├── .github/
│   └── copilot-instructions.md  # Instructions for GitHub Copilot Chat
├── CLAUDE.md                    # Claude Code-style project memory example
├── memory/
│   ├── project/CLAUDE.md        # Shared project context and rules
│   ├── user/CLAUDE.md           # Example user preferences (simulation)
│   └── dynamic/context.md       # Task-specific grid context, loaded on demand
├── src/
│   ├── context_loader.py        # Explicitly loads the context layers
│   ├── environment.py           # Stores the supplied grid and start position
│   └── demo.py                  # Prints the loaded layers and environment
├── tests/
│   └── test_context_loader.py   # Checks default vs. dynamic loading
```

## Run it

Use Python 3.10+; the demo uses only the Python standard library. From the repository root:

```bash
python -m src.demo
python -m src.demo --dynamic
python -m unittest discover -s tests -v
```

- The default demo loads project and example user context.
- The `--dynamic` option also loads `memory/dynamic/context.md`.
- Tests check that dynamic context is opt-in and that the expected context sources are present.

## Vacuum environment boundary

The sample 4×4 grid is represented in `src/environment.py` as supplied assignment data. This context-engineering demonstration does **not** define transition function `T`, reward function `R`, or Q-learning behavior. Do not infer meanings for grid values unless the assignment handout explicitly defines them. Q-learning is planned for a later stage.

## Demonstrating with GitHub Copilot Free in VS Code

1. Open the **inner** `context-engineering-vacuum-lab` folder as the VS Code workspace.
2. Sign in to GitHub Copilot Free and open Copilot Chat.
3. Open `.github/copilot-instructions.md` and ask: `Read .github/copilot-instructions.md and memory/project/CLAUDE.md. Summarize the project goal, file layout, and limitations. Do not modify files.`
4. Then ask: `Read memory/user/CLAUDE.md and explain which preferences are examples rather than automatically loaded Copilot settings.`
5. For the dynamic layer, ask: `Read memory/dynamic/context.md and summarize only the grid facts. Do not infer transition or reward rules.`
6. In the terminal, run the three commands in the Run it section to show the explicit loader and tests.

Copilot may not automatically read every Markdown file just because it exists. For a clear and reproducible demonstration, explicitly ask it to read the files, and use the Python loader to demonstrate exactly which layers are included in each run.

## Strategy 4: Isolation through sub-agents

This repository defines three specialized coding assistants:

| Agent | Responsibility |
|---|---|
| environment-specialist | Analyze grid facts and environment requirements |
| rl-specialist | Plan the future Q-learning component |
| reviewer | Check relevant files for correctness and consistency |

Definitions are stored in .claude/agents/.
Delegation instructions are stored in the root CLAUDE.md.

The main assistant assigns focused tasks and supplies relevant
requirements and file references. Each specialist returns a
concise report for the main assistant to evaluate and integrate.

This demonstrates context isolation: specialists focus on their
assigned task rather than receiving every project detail and
the full conversation history.

The specialists are currently configured for read-only analysis.
Q-learning implementation is deferred.

### Example request

"Use environment-specialist to check the stored grid and starting
position against the assignment. Then use reviewer to assess
those findings. Report inconsistencies and unresolved questions
without editing files or implementing Q-learning."

### Configuration versus execution

These files define the intended sub-agent behavior.
They do not independently launch AI models.

The Python context-loading demo demonstrates reading persistent
context files; it does not execute these sub-agents.

Actual delegation requires a coding assistant that supports
the configuration. Do not claim that a sub-agent ran unless
it was actually invoked.