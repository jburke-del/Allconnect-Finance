---
id: residual_cpa
name: Residual CPA
domain: charter_spectrum
formula: acl * mrr_5yr * residual_rate
grain: partner x channel x cohort_month
source: home_prod.dashboards.mv_charter_enterprise
owner: james.burke
favorable_direction: up
status: approved
last_reviewed: 2026-07-01
aliases: [Residual Commission Per Active]
related_kpis: [cpa_total, acl]
dashboards: []
---

## Definition

Residual CPA: the residual (ongoing) portion of commission per active, modeled as
ACL times the five-year MRR times the residual rate.

## Interpretation

Higher is favorable for RV. As with Total CPA, actuals above the contracted model
are a gain and below are a miss.

## Calculation notes

- Formula: `Residual CPA = ACL x 5yr MRR x residual_rate`.
- The residual rate reflects the Y2 payment scheme. Confirm the current rate
  against the active rate card before publishing (this template uses the Y2 rate
  of 11 percent as a starting point).
- Y1 MRR is anchored to the newest cohort, then stepped by the annual price
  multipliers. Keep the multiplier set aligned with the current rate card.

## Caveats

- Y1 to Y2 payment scheme transitions change the applicable rate. Do not mix
  schemes within a single cohort comparison.
- ACL feeds directly into this metric, so any survival-curve change flows
  through. See [acl.md](acl.md).

## Reference query

```sql
-- Illustrative. Residual CPA = ACL x 5yr MRR x residual rate.
```
