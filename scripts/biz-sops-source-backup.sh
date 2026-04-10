#!/usr/bin/env bash
set -euo pipefail

PATH="/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/usr/local/bin"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEFAULT_SOURCE_REPO="$(cd "$SCRIPT_DIR/.." && pwd)"

CODEX_HOME="${CODEX_HOME:-/Users/gillettes/.codex}"
SOURCE_REPO="${BIZ_SOPS_SOURCE_REPO:-$DEFAULT_SOURCE_REPO}"
REMOTE_NAME="${BIZ_SOPS_REMOTE:-origin}"
BRANCH_NAME="${BIZ_SOPS_BRANCH:-main}"
DELETE_GUARD_MAX="${BIZ_SOPS_DELETE_GUARD_MAX:-5}"
LOCK_ID="${BIZ_SOPS_BACKUP_ID:-$(printf '%s' "$SOURCE_REPO" | shasum -a 256 | awk '{print substr($1,1,12)}')}"
LOCK_DIR="$CODEX_HOME/tmp/biz-sops-source-backup-$LOCK_ID.lock"

log() {
  printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S')" "$*"
}

fail() {
  log "ERROR: $1" >&2
  exit "${2:-1}"
}

cleanup_lock() {
  rm -f "$LOCK_DIR/pid" >/dev/null 2>&1 || true
  rmdir "$LOCK_DIR" >/dev/null 2>&1 || true
}

ensure_clean_git_state() {
  local repo_path="$1"
  local repo_label="$2"

  [[ -d "$repo_path/.git" ]] || fail "$repo_label repo not found at $repo_path."

  local current_branch
  current_branch="$(git -C "$repo_path" rev-parse --abbrev-ref HEAD)"
  [[ "$current_branch" == "$BRANCH_NAME" ]] || fail "$repo_label repo must be on '$BRANCH_NAME' (current: $current_branch)."

  if git -C "$repo_path" diff --name-only --diff-filter=U | grep -q .; then
    fail "$repo_label repo has merge conflicts. Resolve them before automatic backup can continue."
  fi
}

mkdir -p "$CODEX_HOME/log" "$CODEX_HOME/tmp"

case "$DELETE_GUARD_MAX" in
  ''|*[!0-9]*)
    fail "BIZ_SOPS_DELETE_GUARD_MAX must be a non-negative integer. Current value: '$DELETE_GUARD_MAX'."
    ;;
esac

if ! mkdir "$LOCK_DIR" 2>/dev/null; then
  if [[ -f "$LOCK_DIR/pid" ]]; then
    lock_pid="$(cat "$LOCK_DIR/pid" 2>/dev/null || true)"
    if [[ -n "$lock_pid" ]] && kill -0 "$lock_pid" 2>/dev/null; then
      fail "Backup already running with PID $lock_pid." 2
    fi
  fi

  cleanup_lock

  if ! mkdir "$LOCK_DIR" 2>/dev/null; then
    fail "Unable to acquire backup lock at $LOCK_DIR." 3
  fi
fi

printf '%s\n' "$$" > "$LOCK_DIR/pid"
trap cleanup_lock EXIT

ensure_clean_git_state "$SOURCE_REPO" "Source"

log "Fetching $REMOTE_NAME/$BRANCH_NAME for source repo."
git -C "$SOURCE_REPO" fetch "$REMOTE_NAME" "$BRANCH_NAME"

status_before="$(git -C "$SOURCE_REPO" status --porcelain)"
if [[ -z "$status_before" ]]; then
  if git -C "$SOURCE_REPO" rev-parse --verify "$REMOTE_NAME/$BRANCH_NAME" >/dev/null 2>&1; then
    if ! git -C "$SOURCE_REPO" merge-base --is-ancestor "$REMOTE_NAME/$BRANCH_NAME" HEAD || \
       ! git -C "$SOURCE_REPO" merge-base --is-ancestor HEAD "$REMOTE_NAME/$BRANCH_NAME"; then
      log "Source repo is clean but not in sync. Rebasing onto $REMOTE_NAME/$BRANCH_NAME."
      git -C "$SOURCE_REPO" pull --rebase "$REMOTE_NAME" "$BRANCH_NAME"
      log "Pushing clean fast-forward state from source repo."
      git -C "$SOURCE_REPO" push "$REMOTE_NAME" "$BRANCH_NAME"
    else
      log "No local changes to back up from source repo."
    fi
  else
    log "Remote branch $REMOTE_NAME/$BRANCH_NAME not found. Nothing to sync from source repo."
    exit 0
  fi

  log "Source backup check completed successfully."
  exit 0
fi

log "Staging source repo changes."
git -C "$SOURCE_REPO" add -A

if git -C "$SOURCE_REPO" diff --cached --quiet; then
  log "Nothing staged after add; exiting."
  exit 0
fi

deleted_count="$(git -C "$SOURCE_REPO" diff --cached --name-only --diff-filter=D | wc -l | tr -d ' ')"
if (( deleted_count > DELETE_GUARD_MAX )); then
  fail "Deletion guard tripped: $deleted_count tracked file deletions exceed limit $DELETE_GUARD_MAX. Review changes in $SOURCE_REPO before backup continues. Recovery: git restore --staged --worktree <path> for uncommitted deletions, or git revert <sha> after a commit."
fi

commit_message="vault backup: $(date '+%Y-%m-%d %H:%M:%S')"
log "Creating source backup commit: $commit_message"
git -C "$SOURCE_REPO" commit -m "$commit_message"

log "Rebasing latest source commit onto $REMOTE_NAME/$BRANCH_NAME."
if ! git -C "$SOURCE_REPO" pull --rebase "$REMOTE_NAME" "$BRANCH_NAME"; then
  git -C "$SOURCE_REPO" rebase --abort >/dev/null 2>&1 || true
  fail "Rebase failed while syncing the source repo. Manual intervention required."
fi

log "Pushing source backup to GitHub."
git -C "$SOURCE_REPO" push "$REMOTE_NAME" "$BRANCH_NAME"

log "Source backup completed successfully."
