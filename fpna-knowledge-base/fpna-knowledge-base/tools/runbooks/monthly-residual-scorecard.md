# Runbook: Monthly Residual Scorecard

Steps to reproduce the monthly Charter/Spectrum residual scorecard.

## Inputs

- Source: `home_prod.dashboards.mv_charter_enterprise`
- Metrics: `cpa_total`, `residual_cpa`, `acl` (see `kpis/`)
- Accrual period: the reporting month

## Steps

1. Refresh or confirm the source materialized view is current.
2. Pull actuals at partner x channel x cohort_month grain.
3. Compute Total CPA, Residual CPA, and ACL using the canonical definitions.
4. Compare actuals to the contracted model. Above model is a gain, below is a
   miss.
5. Apply the channel taxonomy (OLA split, Transfer classification, Utility merge,
   PSG exclusion from metrics).
6. Validate against accrued figures (target alignment within about 1 percent).
7. Assemble the scorecard and talk track for the leadership audience.

## Checks before publishing

- Confirm the residual rate matches the active rate card.
- Confirm no double-counting from the traps in `data/known-issues.md`.
- Confirm never-activated orders are excluded (sentinel date).
