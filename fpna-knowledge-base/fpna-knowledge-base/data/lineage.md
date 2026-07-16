# Data lineage

High-level flow from raw sources to reporting surfaces. Keep this current when
upstream tables or jobs change.

## Flow (fill in specifics)

1. Raw order and call events land in source schemas.
2. `acu_prod.rpt.order_fact` provides order-grain facts and revenue.
3. `acu_prod.rpt.v_calls` provides call volume used for footprint and
   attribution.
4. `home_prod.dashboards.mv_charter_enterprise` resolves channels and serves
   Charter/Spectrum reporting.
5. Dashboards and scorecards read from the materialized view.

## Notes

- Record any dual-write paths (for example ION/Concert) so downstream consumers
  know where duplication can enter. See [known-issues.md](known-issues.md).
