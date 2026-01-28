# AI Guardrails for Claude Code

AI Guardrails is a **governance and memory system** for using Claude Code safely and scalably on real-world projects.

It is designed to solve a core failure mode of large language models in coding:
> *They stop searching too early, duplicate logic, and lose global context as projects grow.*

AI Guardrails fixes this by combining **explicit rules**, **external system memory**, **guided workflows**, and **mechanical enforcement**.

This repository is intended for **GitHub use** and can be adopted:
- by individuals
- by teams
- incrementally or fully
- with or without Claude Code plugins

---

## Why This Exists

Modern AI coding assistants are extremely capable, but they are not architects.

Common failure modes:
- First-match bias (grep → stop searching)
- Duplicate implementations instead of reuse
- Silent architectural drift
- Ever-increasing repo scans and token usage
- No durable memory across sessions

AI Guardrails introduces **structure and discipline** so AI remains helpful *without taking control away from humans*.

---

## Core Design Principles

1. **Architecture is semantic**
   - Only humans decide what is canonical.
   - AI assists, but does not invent structure.

2. **Memory must be external**
   - Repos cannot rely on AI context windows.
   - System understanding must live in files.

3. **Rules, memory, process, enforcement are separate**
   - Mixing them causes drift and confusion.

---

## Key Files & Their Roles

| File | Role | Changes When |
|----|----|----|
| `CLAUDE.md` | Rules / Constitution | Workflow or invariants change |
| `docs/PROJECT_GUIDE.md` | System map / External memory | Architecture, workflows, ownership change |
| `docs/CHANGELOG_AI.md` | Change history | Meaningful AI-assisted change completes |
| Skills | Process | Rare |
| Hooks | Enforcement | Rare |

---

## File Structure

### Plugin (user-level, reusable)

```text
~/.claude/plugins/ai-guardrails/
├── skills/
│   ├── bootstrap/        # Discover & map a repo once
│   │   └── SKILL.md
│   ├── start/            # Begin a guarded change
│   │   └── SKILL.md
│   └── end/              # Close a change + update memory
│       └── SKILL.md
├── hooks/
│   └── hooks.json        # Enforces documentation discipline
└── scripts/
    └── require_project_guide_update.py
```

### Per Project (checked into git)

```text
project-root/
├── CLAUDE.md
├── docs/
│   ├── PROJECT_GUIDE.md
│   └── CHANGELOG_AI.md   # optional but recommended
└── src/...
```

---

## Mental Model (Very Important)

> **CLAUDE.md = Law**  
> **PROJECT_GUIDE.md = Memory**  
> **Skills = Process**  
> **Hooks = Enforcement**

---

## Standard Workflow (Canonical)

### Phase 0 — New Project Setup

1. Create repo
2. Create `CLAUDE.md` (manual, intentional)

Example minimal `CLAUDE.md`:

```md
This project uses an external memory + canonical implementation workflow.

Before making any code changes:
- Read docs/PROJECT_GUIDE.md
- Identify the canonical implementation
- Prefer reuse over duplication

After making changes:
- Update docs/PROJECT_GUIDE.md if architecture or ownership changed

Generated artifacts must not be edited directly.
```

3. Start Claude Code with guardrails:

```bash
claude --plugin-dir ~/.claude/plugins/ai-guardrails
```

---

### Phase 1 — Bootstrap System Memory (Run Once)

```text
/ai-guardrails:bootstrap
```

This:
- Scans the repo efficiently
- Identifies workflows and ownership
- Distinguishes canonical sources vs generated artifacts
- Writes `docs/PROJECT_GUIDE.md`

⚠️ On curated repos, configure bootstrap to write to `PROJECT_GUIDE.generated.md` instead.

---

### Phase 2 — Making Any Change

#### 1. Start the change (mandatory)

```text
/ai-guardrails:start <goal>
```

Example:

```text
/ai-guardrails:start Change financial data source from web search to Google Sheet
```

This step:
- Forces behavioral restatement
- Identifies canonical ownership
- Prevents premature coding

#### 2. Approve the plan
Human confirms:
- Canonical location is correct
- No duplication is introduced

#### 3. Implement the change
Claude writes code.

Hooks may block further writes if:
- canonical behavior changed
- but PROJECT_GUIDE.md was not updated

#### 4. Close the change (mandatory)

```text
/ai-guardrails:end
```

This:
- Updates `docs/PROJECT_GUIDE.md` when needed
- Appends to `docs/CHANGELOG_AI.md`
- Finalizes the change

---

## What Counts as a Canonical Change?

A change is **canonical** if it alters any of the following:

- Source of truth (e.g., web → Google Sheet)
- Core workflow or pipeline
- Ownership boundaries
- Templates, generators, or shared abstractions
- User-facing global behavior (shortcuts, exports, formats)

If in doubt: treat it as canonical.

---

## How Enforcement Works (No Prompts, by Design)

There is **no Yes/No dialog**.

Instead:
- If code changes without guide updates → writes are blocked
- Updating `PROJECT_GUIDE.md` *is* the confirmation

You may override intentionally, but never silently.

---

## Manual Adoption (No Plugin)

You can still use the system without plugins:

1. Maintain `CLAUDE.md`
2. Maintain `docs/PROJECT_GUIDE.md`
3. Require canonical identification before coding
4. Require documentation after canonical changes

You lose enforcement, but keep structure.

---

## When NOT to Update Each File

- Do not update `CLAUDE.md` for feature changes
- Do not update `PROJECT_GUIDE.md` for trivial refactors
- Do not auto-write `CHANGELOG_AI.md` via hooks

Each file has a purpose.

---

## Who This Is For

- Engineers using Claude Code seriously
- Teams worried about AI-induced duplication
- Projects with generators, pipelines, or templates
- Anyone who wants AI help **without losing architectural control**

---

## License

MIT — use freely, copy aggressively, adapt to your workflow.
