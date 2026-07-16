---
id: cpa_total
name: Total CPA
domain: charter_spectrum
formula: total_commission / active_units
grain: partner x channel x cohort_month
source: home_prod.dashboards.mv_charter_enterprise
owner: james.burke
favorable_direction: up
status: approved
last_reviewed: 2026-07-01
aliases: [Commission Per Active, Total Commission Per Active]
related_kpis: [residual_cpa, acl]
dashboards: []
---

## Definition

Commission Per Active: the total commission paid by the partner (Spectrum) to RV
per activated unit sold. Total CPA combines the upfront and residual components.

## Interpretation

Higher is favorable for RV. Compare actuals against the contracted model:
actuals above model are a gain, actuals below model are a miss. The same
convention applies to Upfront CPA and Residual CPA.

## Calculation notes

- Population is activated units. Orders never activated (see the sentinel-date
  trap in `data/known-issues.md`) must not count as active.
- Platinum Service Group (PSG) is excluded from the metric but retained in
  connect counts.
- Allconnect Utility and Allconnect Utility Call Transfer are merged into a
  single channel for reporting.

## Caveats

- Confirm the channel taxonomy before slicing (Offline Affiliates splits into OLA
  ex P50/Mazama/PSG, P50, and Mazama; Connect Platform orders classify as
  Transfer).
- See `data/known-issues.md` for attribution and double-counting traps that
  affect the denominator.

## Reference query

```sql
-- Illustrative. Adjust to the current model and rate card.
SELECT
    partner,
    channel,
    cohort_month,
    SUM(total_commission) / NULLIF(SUM(active_units), 0) AS cpa_total
FROM home_prod.dashboards.mv_charter_enterprise
GROUP BY partner, channel, cohort_month;
```
