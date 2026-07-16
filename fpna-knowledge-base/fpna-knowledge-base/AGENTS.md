# AGENTS.md

Guidance for AI coding agents (Claude Code, Cursor, Copilot, Codex, and others)
working inside this repository. Humans should start with `README.md`.

## What this repository is

A knowledge base for the FP&A team: financial methodology, KPI definitions,
data-source documentation, and query tools. It is documentation and logic only.
It contains no live financial figures and no PII.

## Hard constraints

- Never add actual financial figures, forecasts, customer data, or PII to this
  repo. Reference the governed source table and metric ID instead.
- Never invent a KPI. If a metric is not defined in `kpis/`, say so and propose a
  new entry using `kpis/_template.md` rather than assuming a formula.
- Treat only KPIs with `status: approved` as authoritative. Flag `draft` and
  `deprecated` explicitly when you use them.
- When you write a query, honor the documented traps in `data/known-issues.md`.
  These are guardrails, not trivia.

## Conventions

- One concept per file. Keep files small and focused.
- KPI files carry a YAML frontmatter contract. Every required key must be
  present: id, name, domain, formula, grain, source, owner, favorable_direction,
  status, last_reviewed.
- Prose in Markdown. Runnable logic as real `.sql` or `.py` files under `tools/`.
- Cite the source table for any metric or figure.
- Do not use em dashes in drafted content. Use commas, colons, parentheses, or
  restructured sentences instead.

## What to read before touching each area

| Task | Read first |
| --- | --- |
| Define or edit a metric | `kpis/_template.md`, then the target file in `kpis/` |
| Write a query | `data/sources/`, then `data/known-issues.md` |
| Understand data flow | `data/lineage.md` |
| Reproduce a report | the relevant runbook in `tools/runbooks/` |

## Validation

`scripts/validate_kb.py` checks KPI frontmatter and internal links. Run it before
opening a PR with `python scripts/validate_kb.py`. CI runs it automatically.
