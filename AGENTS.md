# RealEstateScrapeFactory - Codex Context

## 0. Codex usage
### 0.1 Code Navigation

  - Always use the appropriate installed MCP for the task: prefer Serena MCP tools (find_symbol, get_symbols_overview, search_for_pattern) over reading entire files, use Context7 MCP for official library/framework docs, Playwright MCP for browser/UI verification flows, and Sentry MCP for error/issue investigation and production debugging context  - Always save the logs to a file in the folder \logs\ that you then search with serena, do not ingest full logs and waste tokens
  - Use symbolic tools to understand structure first, only read file sections when needed
  - Use find_symbol with include_body=true for targeted reads instead of ingesting whole files

## 1. Infrastructure Overview

### 1.1 Server1 (192.168.2.250)
- Role: Main server - Jenkins, PostgreSQL, Redis, RabbitMQ, Docker Registry, k3s
- SSH: Port 56969, key+password auth (key-only from server2)
- Services:
  - PostgreSQL: 5432
  - Redis: 6379
  - RabbitMQ: 5672 (AMQP), 15672 (Management)
  - Docker Registry: 5000
  - Jenkins: 8180
  - k3s API: 6443

### 1.2 Server2 (192.168.2.251)
- Role: Worker node - Celery workers only
- SSH: Port 56969, key+password auth
- Firewall: Ports 56969 (SSH), 6443 (k3s API)
- k3s: Standalone cluster, pulls images from server1 registry

## 2. Celery Workers
- Server1: 1 worker pod
- Server2: 8 worker pods (500m CPU, 1536Mi RAM each)
- Broker: RabbitMQ amqp://192.168.2.250:5672
- Backend: Redis redis://192.168.2.250:6379/0

## 3. Kubernetes Deployments

| Deployment | Server | Jenkinsfile |
|------------|--------|-------------|
| worker | server1 | Jenkinsfile_worker1 |
| worker2 | server2 | Jenkinsfile_worker2 |
| beat | server1 | Jenkinsfile_beat |
| discord-bot | server1 | Jenkinsfile_discord_bot |

## 4. Key Files
- k8s/secrets.yaml
- k8s/worker-deployment.yaml
- k8s/worker2-deployment.yaml
- docker/base.dockerfile
  - Base Docker image with Python, system dependencies, and uv package manager
  - Other dockerfiles inherit from this base image
- docker/worker.dockerfile
- Kubeconfig server2: /var/lib/jenkins/.kube/config-server2

## 5. Workflow
- Edit files via VSCode SSH to server1 workspace
- Push via git_push.py
  - Custom Python script for git operations with automated linting and testing
  - Always run manually by user, unless asked
- Deploy via Jenkins, manually by user
- Do NOT run kubectl apply directly

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
- Run all tests: `uv run pytest`
- Run specific file: `uv run pytest tests/test_file.py`
- Run specific test: `uv run pytest tests/test_file.py::test_name`
- Verbose output: `uv run pytest -v`
- Test directory: `tests/`

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
- Simplicity: Write simple, straightforward code
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
- Minimal Changes: Only modify code related to the task at hand
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

### 8.1 Core Components

| File | Purpose |
|------|---------|
| celery_app.py | Celery application instance and task auto-discovery |
| celeryconfig.py | Celery configuration (queues, schedules, worker settings) |
| db_handler.py | Database operations (PostgreSQL) |
| db_connector.py | Database connection management |
| scraper.py | Main scraping logic |
| utils.py | Shared utilities (Redis, cookies, driver helpers) |

### 8.2 Task Modules (tasks/)

| File | Purpose |
|------|---------|
| scraper_tasks.py | Scraping Celery tasks |
| cookie_tasks.py | Cookie refresh tasks |
| data_refinement_tasks.py | Data processing and refinement |
| misc_tasks.py | Queue management, cleanup, backups |

### 8.3 Utility Modules

| File | Purpose |
|------|---------|
| test_floors.py | Floor calculation logic for Vietnamese listings |
| test_gemini.py | Gemini API wrapper for AI processing |
| get_floors.py | Floor extraction from listing descriptions |
| refine.py | Data refinement logic |

### 8.4 Debug Scripts

| File | Purpose |
|------|---------|
| tester_bds.py | Manual testing for batdongsan.com |
| tester_cht.py | Manual testing for chotot.com |

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
- Always test assumptions beforehand by running raw SQL queries in pgAdmin or psql shell
- Before adding new tables or columns:
  - Run SQL queries to check if expected column or similar already exists
  - Verify the criteria matches intended targets
- Before updating or deleting rows:
  - Run SELECT query with same criteria first
  - Review which rows will be affected
- Double-check existing database schema and relationships before applying any changes

---

## 11. Pending Tasks

None currently.
