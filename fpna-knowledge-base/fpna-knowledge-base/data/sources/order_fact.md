# Source: acu_prod.rpt.order_fact

Order-grain fact table and the primary source for order and revenue metrics.

## Grain

One row per order line item (confirm against the current definition).

## Key fields

- `gross_acu_revenue`: canonical revenue field, migrated from
  `rs_orderrevenuemap` and validated at about 0.27 percent delta across 5.5M
  orders.
- `lineitemstatuscode`: line item status. Watch for NULLs (see known issues).
- `customer_account_number`: 16-digit account id. Type carefully in Spark joins
  (see known issues).
- `external_order_id`: used as a fifth key type in tele-attribution.

## Refresh

Document the refresh cadence and upstream jobs here.

## Related

- Attribution and double-counting traps: [../known-issues.md](../known-issues.md)
- Lineage: [../lineage.md](../lineage.md)
