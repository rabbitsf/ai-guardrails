---
name: bootstrap
description: Generate an AI-optimized docs/PROJECT_GUIDE.md system map (exact standard structure)
---

You are bootstrapping the repository’s **AI-optimized system map**.

Your ONLY output is to create or overwrite: `docs/PROJECT_GUIDE.md`
Do NOT implement features or refactor code.

## Goal
Produce a concise, high-signal PROJECT_GUIDE that:
- avoids full-repo rescans
- encodes workflows and canonical ownership
- prevents duplication (especially generator vs artifact mistakes)

## Required output structure (MUST MATCH EXACTLY)
Write `docs/PROJECT_GUIDE.md` using this exact section layout and headings:

1) Project overview
   - What this project does
   - What this project does NOT do

2) High-level architecture
   - Canonical source layer (where permanent changes must be made)
   - Artifact / output layer (generated files)
   - A clear “Rule: do not edit artifacts directly” statement

3) End-to-end workflows (behavior-first)
   - At least 2 workflows if possible (A/B). If only 1 exists, include 1 and mark the second as TBD.

4) Canonical implementations (Single Source of Truth)
   - Include at least ONE canonical behavior subsection (4.1, 4.2, etc.)
   - If you cannot confidently identify canonical implementations, write placeholders with “TBD” and list where you searched.
   - Every subsection MUST include:
     - User-facing behavior
     - Canonical implementation (paths)
     - Generated artifacts (patterns)
     - Operational rule (regen vs edit)

5) Generated artifacts vs canonical sources
   - Two lists: artifacts vs sources

6) Duplication hotspots (AI warnings)
   - Bullet list of areas likely to be duplicated

7) Safe change playbook
   - A short numbered checklist

## Discovery process (keep token usage low)
1) Read `README.md` if present; extract only essentials.
2) List top-level directories/files.
3) Identify likely “entrypoints”:
   - scripts, CLIs, agent skills, pipelines, build tools, or main apps
4) Identify generated artifacts by looking for:
   - build/output directories
   - repeated patterns like *_report.*, *_analysis.*, dist/, build/, out/, artifacts/
5) Identify canonical sources by looking for:
   - templates, generators, shared libraries, core modules
6) If the repo appears to depend on external generators (e.g. files under `~/.claude/skills/`):
   - explicitly record that as canonical source layer
   - treat generated files inside this repo as artifacts

## Style constraints
- Keep the file <= ~200 lines
- Prefer short bullets over paragraphs
- Use concrete file paths/patterns when known
- If uncertain, say “TBD” rather than guessing

## Final step
After writing `docs/PROJECT_GUIDE.md`, output a brief confirmation message:
- “Bootstrapped docs/PROJECT_GUIDE.md”
- One bullet list of what was confidently identified vs TBD

