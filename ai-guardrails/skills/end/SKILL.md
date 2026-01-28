---
name: end
description: Close the guarded change by updating PROJECT_GUIDE.md and recording the change
---

You are closing a guarded change.

1) Summarize what changed in 3-6 bullets.
2) Update `docs/PROJECT_GUIDE.md` with:
   - Canonical implementation location(s)
   - Rules that prevent duplication (e.g., “do not edit generated artifacts”)
   - Any new/changed entrypoints
3) Append a short entry to `docs/CHANGELOG_AI.md` (if it exists; otherwise create it).
4) Mark the change complete.

Do not make additional code changes unless required to update docs.

