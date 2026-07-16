---
id: acl
name: Average Customer Life
domain: charter_spectrum
formula: sum(survival_probability) over months 1..60
grain: partner x channel x cohort_month
source: home_prod.dashboards.mv_charter_enterprise
owner: james.burke
favorable_direction: up
status: approved
last_reviewed: 2026-07-01
aliases: [ACL]
related_kpis: [residual_cpa, cpa_total]
dashboards: []
---

## Definition

Average Customer Life: expected customer lifetime in months, computed as the area
under the pooled survival curve summed over 60 months.

## Interpretation

Higher ACL means customers persist longer, which raises residual value. Favorable
direction is up.

## Calculation notes

- Survival is pooled and weighted by M0 units (units at payment number zero) at
  each payment number.
- The model curve is extended past the observed data cutoff before summing.
- ACL is summed over 60 months.

## Caveats

- Pooling choice matters: unit-weighted pooling differs from a simple average of
  cohort curves. Keep the weighting consistent with the contracted model.

## Reference query

```sql
-- Illustrative pooled survival, unit-weighted at each payment number.
-- Replace with the canonical model logic.
```
