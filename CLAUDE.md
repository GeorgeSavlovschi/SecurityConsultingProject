# Security Consulting Project - Claude Context

## 0. Claude usage

### 0.1 Workflow Orchestration

**Plan Mode Default**
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

**Subagent Strategy**
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

**Self-Improvement Loop**
- After ANY correction from the user: update tasks/lessons.md with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

**Verification Before Done**
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

**Demand Elegance (Balanced)**
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

**Autonomous Bug Fixing**
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests - then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

---

### 0.2 Task Management

1. **Plan First**: Write plan to plan/todo/<new_task_name>.md with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to plan/todo/<new_task_name>.md
6. **Capture Lessons**: Update tasks/lessons.md after corrections

---

### 0.3 Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

---

### 0.4 Code Navigation

  - Always prefer Serena MCP tools (find_symbol, get_symbols_overview, search_for_pattern) over reading entire files
  - Always save the logs to a file in the folder \logs\ that you then search with serena, do not ingest full logs and waste tokens
  - Use symbolic tools to understand structure first, only read file sections when needed
  - Use find_symbol with include_body=true for targeted reads instead of ingesting whole files

## 1. Infrastructure Overview

- No infrastructure available yet, ask before building, or before assumptions about infrastructure.

---

## 6. Development Guidelines

### 6.1 Package Management (uv)
- Add dependency: `uv add package`
- Add dev dependency: `uv add --dev package` (keeps tools like ruff/pytest out of production Docker images)
- Run tools: `uv run <tool>`
- Sync environment: `uv sync`
- Update lockfile: `uv lock`
- Always use `uv sync` or `uv add`, NEVER use `uv pip install`

### 6.2 Code Quality
- Type hints required for all code
- All functions must have docstrings
- Functions must be focused and small
- Follow existing patterns exactly
- Line length: 88 chars maximum

### 6.3 Testing (pytest)
- No testing yet


### 6.4 Code Style
- PEP 8 naming (snake_case for functions/variables)
- Class names in PascalCase
- Constants in UPPER_SNAKE_CASE
- Document with docstrings
- Use f-strings for formatting

### 6.5 Git Management
- All Git operations are done manually via git_push.py
- When ready to commit/push, stop and ask user to run it

### 6.6 Development Philosophy
- Readability: Make code easy to understand
- Performance: Consider performance without sacrificing readability
- Maintainability: Write code that is easy to update
- Testability: Ensure code is testable
- Reusability: Create reusable components and functions
- Less Code = Less Debt: Minimize code footprint

### 6.7 Coding Best Practices
- Early Returns: Use to avoid nested conditions
- Descriptive Names: Use clear variable/function names (prefix handlers with "handle")
- Constants Over Functions: Use constants where possible
- DRY Code: Do not repeat yourself
- Functional Style: Prefer functional, immutable approaches when not verbose
- TODO Comments: Mark issues in existing code with "TODO:" prefix
- Error Handling: Use specific exceptions, avoid bare excepts
- No helpers: Ask user if you should implement helpers only when absolutely necessary

---

## 7. Documentation guidelines
- Always follow formatting structure available in files from the \plan\ folder
- Always update the `Last updated:` timestamp at the top of the file when making changes
- For diagrams:
  - create all labels using quoted strings: `V2["..."]`
  - never use `\n` but use HTML breaks: `<br/>`
  - used parentheses in text directly for comments, example: `(old, removed)`

---

## 8. System Architecture
- No architecture yet, ask before building, or before assumptions about architecture.

---

## 9. Python Tools

### 9.1 git_push.py Workflow
- Included in git_push.py workflow:
  - Code formatting & linting (Ruff)
  - Type checking (Pyright)
  - CI failure resolution
  - Testing (Pytest)

### 9.2 Pyright
- Mode: basic
- Python: 3.11
- Reports missing imports and unused variables
- Common fixes:
  - Add None checks for Optional types
  - Narrow string types with isinstance

---

## 10. Database Interactions
- No database interactions yet, ask before building, or before assumptions about database interactions.

---

## 11. Custom Skills

Located in `skills/` directory. Invoke via `/skill-name`:

| Skill | Trigger | Purpose |
|-------|---------|---------|
| `doc-coauthoring` | Writing docs, proposals, specs, RFCs | Structured 3-stage workflow: Context Gathering → Refinement & Structure → Reader Testing |
| `mcp-builder` | Building MCP servers for LLM integrations | Guide for creating MCP servers (Python FastMCP or Node/TS SDK) with research, planning, implementation, and eval phases |
| `skill-creator` | Creating, editing, or benchmarking skills | Create new skills, run evals, optimize descriptions, iterate with variance analysis |

---

## 12. Pending Tasks

None currently.

