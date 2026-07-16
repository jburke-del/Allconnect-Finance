# Source: home_prod.dashboards.mv_charter_enterprise

Materialized view underpinning Charter/Spectrum enterprise reporting. Owned end
to end by the FP&A analytics owner.

## Purpose

Provides the order and channel-resolved base for Charter/Spectrum CPA, survival,
and residual reporting.

## Channel resolution

- Offline Affiliates splits into OLA ex P50/Mazama/PSG, P50, and Mazama.
- Connect Platform orders classify as Transfer.
- Allconnect Utility and Allconnect Utility Call Transfer merge into one channel.
- PSG is excluded from metrics but retained in connect counts.

## Refresh

Document the refresh cadence and dependencies here.

## Related

- Known issues: [../known-issues.md](../known-issues.md)
- Lineage: [../lineage.md](../lineage.md)
