# FP&A Knowledge Base

A centralized, version-controlled, AI-readable knowledge base for the FP&A team.
It documents financial methodology, KPI definitions, data sources, and query
tools so that both people and AI agents can answer questions consistently and
correctly.

## What lives here (and what does not)

This repository holds definitions, methodology, documentation, and query logic.
It does not hold actual financial figures, forecasts, or any PII. Those stay in
the governed data platform and are referenced here by table and metric ID.
Keeping live numbers out is deliberate: it removes an access-control and
staleness burden, and it is not what makes the base useful to an agent.

## How to navigate

- `index.md` is the master table of contents (stable IDs to file paths).
- `glossary.md` gives one-line definitions with links to full entries.
- `kpis/` holds one metric per file, each with a YAML frontmatter contract.
- `data/` documents source tables, lineage, and known data traps.
- `tools/` holds reusable query templates and operational runbooks.
- `AGENTS.md` orients AI coding agents working inside the repo.

## Contributing

Every change goes through a pull request. New or changed KPI definitions require
sign-off from the metric owner (see `.github/CODEOWNERS`). A CI check validates
KPI frontmatter and internal links on every PR. See the pull request template
for the definition of done.

## Metric status

Each KPI carries a `status` of `draft`, `approved`, or `deprecated`. When
pointing an AI coworker at this base, restrict it to `approved` content unless
you are deliberately exploring drafts.
