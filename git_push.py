"""Commit and push helper for SecurityConsultingProject.

Reads credentials from `.env` and pushes to:
https://github.com/GeorgeSavlovschi/SecurityConsultingProject
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

ENV_FILE = Path(".env")
TARGET_REPO = "https://github.com/GeorgeSavlovschi/SecurityConsultingProject.git"
DEFAULT_BRANCH = "main"
DEFAULT_COMMIT_MESSAGE = "chore: update SecurityConsultingProject files"


def run(
    command: list[str],
    *,
    check: bool = True,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    """Run a subprocess command."""
    return subprocess.run(
        command,
        check=check,
        text=True,
        capture_output=capture_output,
    )


def ensure_safe_directory() -> None:
    """Allow git operations in this working directory in sandboxed environments."""
    run(
        [
            "git",
            "config",
            "--global",
            "--add",
            "safe.directory",
            str(Path.cwd()),
        ],
        check=False,
    )


def load_dotenv(path: Path) -> None:
    """Load simple KEY=VALUE pairs from .env."""
    if not path.exists():
        print(f"Missing required file: {path}")
        sys.exit(1)

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]
        os.environ.setdefault(key, value)


def in_git_repo() -> bool:
    """Return True if the current directory is already a git repository."""
    result = run(["git", "rev-parse", "--is-inside-work-tree"], check=False)
    return result.returncode == 0


def ensure_git_repo(branch: str) -> None:
    """Initialize repository if needed and switch to target branch."""
    if not in_git_repo():
        print("Initializing new git repository...")
        run(["git", "init"])
    run(["git", "checkout", "-B", branch])


def ensure_identity(username: str) -> None:
    """Set git identity if not already configured for this repository."""
    current_name = run(
        ["git", "config", "--get", "user.name"],
        check=False,
        capture_output=True,
    ).stdout.strip()
    current_email = run(
        ["git", "config", "--get", "user.email"],
        check=False,
        capture_output=True,
    ).stdout.strip()

    if not current_name:
        run(["git", "config", "user.name", username])
    if not current_email:
        fallback_email = f"{username}@users.noreply.github.com"
        run(["git", "config", "user.email", fallback_email])


def set_origin(remote_url: str) -> None:
    """Create or update origin remote."""
    has_origin = run(
        ["git", "remote", "get-url", "origin"],
        check=False,
        capture_output=True,
    ).returncode == 0

    if has_origin:
        run(["git", "remote", "set-url", "origin", remote_url])
    else:
        run(["git", "remote", "add", "origin", remote_url])


def build_authenticated_url(repo_url: str, username: str, token: str) -> str:
    """Build HTTPS URL with URL-encoded credentials."""
    if not repo_url.startswith("https://"):
        print("Only HTTPS repo URLs are supported by this helper.")
        sys.exit(1)
    safe_user = quote(username, safe="")
    safe_token = quote(token, safe="")
    return repo_url.replace("https://", f"https://{safe_user}:{safe_token}@", 1)


def commit_all(commit_message: str) -> None:
    """Stage and commit all changes if any exist."""
    run(["git", "add", "-A"])
    has_changes = bool(
        run(["git", "status", "--porcelain"], capture_output=True).stdout.strip()
    )
    if not has_changes:
        print("No changes to commit.")
        return
    run(["git", "commit", "-m", commit_message])


def try_rebase_from_origin(branch: str) -> None:
    """Rebase on remote branch when it exists."""
    remote_exists = run(
        ["git", "ls-remote", "--heads", "origin", branch],
        check=False,
        capture_output=True,
    )
    if remote_exists.returncode != 0 or not remote_exists.stdout.strip():
        return
    run(["git", "pull", "--rebase", "origin", branch, "--allow-unrelated-histories"])


def main() -> None:
    ensure_safe_directory()
    load_dotenv(ENV_FILE)

    username = os.environ.get("GIT_USERNAME", "").strip()
    token = os.environ.get("GIT_TOKEN", "").strip()
    commit_message = os.environ.get("GIT_COMMIT_MESSAGE", DEFAULT_COMMIT_MESSAGE).strip()

    if not username or not token:
        print("Missing GIT_USERNAME or GIT_TOKEN in .env")
        sys.exit(1)

    ensure_git_repo(DEFAULT_BRANCH)
    ensure_identity(username)

    authenticated_url = build_authenticated_url(TARGET_REPO, username, token)
    set_origin(authenticated_url)

    try:
        commit_all(commit_message)
        try_rebase_from_origin(DEFAULT_BRANCH)
        run(["git", "push", "-u", "origin", DEFAULT_BRANCH])
    finally:
        # Keep local git config free of embedded credentials.
        set_origin(TARGET_REPO)

    print(f"Pushed to {TARGET_REPO} ({DEFAULT_BRANCH})")


if __name__ == "__main__":
    main()
