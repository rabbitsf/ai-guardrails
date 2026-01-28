#!/usr/bin/env python3
import subprocess
import sys

GUIDE = "docs/PROJECT_GUIDE.md"

# Treat these as "docs changes" that satisfy the requirement
DOC_OK_PREFIXES = ("docs/",)
DOC_OK_FILES = {GUIDE, "docs/CHANGELOG_AI.md"}

def run(cmd):
    return subprocess.check_output(cmd, stderr=subprocess.DEVNULL).decode("utf-8").strip()

def is_git_repo():
    try:
        out = run(["git", "rev-parse", "--is-inside-work-tree"])
        return out.lower() == "true"
    except Exception:
        return False

def changed_files():
    # staged + unstaged
    out = run(["git", "diff", "--name-only"])
    out2 = run(["git", "diff", "--name-only", "--staged"])
    files = set([f for f in (out + "\n" + out2).split("\n") if f.strip()])
    return files

def is_doc_file(path: str) -> bool:
    return path in DOC_OK_FILES or any(path.startswith(p) for p in DOC_OK_PREFIXES)

def block(msg: str):
    print(msg)
    # Claude Code hook convention: exit 2 blocks the tool call
    sys.exit(2)

def main():
    if not is_git_repo():
        # If no git repo, we can't reliably enforce. Don't block, but warn.
        print("⚠️ Guardrails: Not a git repo; cannot enforce PROJECT_GUIDE update requirement.")
        sys.exit(0)

    files = changed_files()
    if not files:
        sys.exit(0)

    guide_changed = GUIDE in files

    # “Non-doc changes” means anything outside docs/
    non_doc_changes = [f for f in files if not is_doc_file(f)]

    if non_doc_changes and not guide_changed:
        block(
            "❌ Guardrails: You have non-doc changes but docs/PROJECT_GUIDE.md is not updated.\n"
            "Update Section 4 (Canonical implementations) to reflect the change, then retry.\n"
            f"Non-doc changes detected (sample): {non_doc_changes[:5]}"
        )

    sys.exit(0)

if __name__ == "__main__":
    main()

