# Vacuum Robot Lab — Claude Code Project Memory Example

@memory/project/CLAUDE.md

## Context-loading policy
- The project memory above contains stable project facts and rules.
- Do not load `memory/dynamic/context.md` unless task-specific grid details are needed or the dynamic-context demonstration is requested.
- When task-specific grid details are needed, read `memory/dynamic/context.md` and identify it as task-specific context.
- Do not invent transition rules, reward functions, or Q-learning behavior that the assignment has not defined.

## Validation commands
- Run the demo: `python -m src.demo`
- Demonstrate explicit dynamic context in the Python loader: `python -m src.demo --dynamic`
- Run tests: `python -m unittest discover -s tests -v`

Note: This file demonstrates Claude Code-style project memory syntax. GitHub Copilot uses `.github/copilot-instructions.md`; the Python loader explicitly reads the repository's memory files for a tool-independent demonstration.

## Strategy 4: Context isolation through sub-agents

The main assistant coordinates work and integrates specialist
findings. Sub-agent definitions are in .claude/agents/.

### Delegation rules

- Use environment-specialist for grid consistency, environment
  requirements, and proposed environment interfaces.
- Use rl-specialist for future Q-learning requirements,
  model-free learning concepts, and learner interfaces.
- Use reviewer for independent checks of relevant documentation,
  agent definitions, or code.

### Task handoff

For each delegated task, provide:

1. A focused objective.
2. The relevant confirmed requirements.
3. The specific files needed.
4. The expected output.
5. Any unresolved assumptions or constraints.

Do not paste the entire conversation or every context file into
each task. Specialists should receive the information relevant
to their assigned responsibility.

Project-wide instructions may already be available through the
coding assistant. Keep those instructions short and place
specialized detail in files read only when needed.

### Integration

- Request analysis and recommendations during this preparation
  stage; Q-learning implementation remains deferred.
- Review specialist findings before incorporating them.
- Resolve conflicting recommendations against confirmed
  assignment requirements.
- Preserve unanswered questions instead of silently inventing rules.
- Report which specialists were actually used and summarize
  their findings.
- If sub-agent execution is unavailable, explain that limitation.
  Do not describe an ordinary file read as an executed sub-agent.

### Example delegation

Ask environment-specialist to compare src/environment.py with
the supplied grid and report coordinate inconsistencies and
unspecified environment behavior.

Provide only the grid requirements, relevant environment files,
and the requested report format.

Then ask reviewer to check the findings against those same
requirements before making corrections.