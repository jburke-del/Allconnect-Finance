---
id: metric_id                 # snake_case, unique, matches index.md
name: Human Readable Name
domain: charter_spectrum       # business area this metric belongs to
formula: numerator / denominator
grain: partner x channel x cohort_month
source: schema.table           # canonical source table(s)
owner: firstname.lastname      # accountable metric owner (see CODEOWNERS)
favorable_direction: up        # up | down | neutral
status: draft                  # draft | approved | deprecated
last_reviewed: 2026-07-01      # ISO date, updated at each review
aliases: []                    # optional: other names people use
related_kpis: []               # optional: list of related metric ids
dashboards: []                 # optional: links to canonical dashboards
---

## Definition

One clear paragraph. State exactly what the metric measures and, if the name is
ambiguous, what it does not measure.

## Interpretation

How to read it. State the favorable direction in words and what a move means for
the business.

## Calculation notes

Precise calculation logic: filters, exclusions, weighting, time windows, and any
edge cases. Be explicit about the population (who is in, who is out).

## Caveats

Known gotchas, exclusions, and comparisons (for example, actuals vs contracted
model). Link to `data/known-issues.md` entries where relevant.

## Reference query

```sql
-- Canonical query that computes this metric.
```
