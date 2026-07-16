# Known data issues and guardrails

These are documented traps in the data. Treat them as guardrails when writing
queries or interpreting metrics. Each entry states the symptom, the cause, and
the fix or mitigation.

## Twilio leg-level fan-out inflates order metrics

- **Symptom:** core order metrics inflated, notably for T-Mobile and AT&T.
- **Cause:** leg-level fan-out in the `twilio_map` CTE produces multiple rows per
  order.
- **Mitigation:** de-duplicate to order grain before aggregating. Confirm the
  join does not multiply rows.

## ION / Concert dual-write duplication in order_fact

- **Symptom:** duplicated orders.
- **Cause:** dual-write of the same order through ION and Concert paths.
- **Mitigation:** apply the documented de-duplication key before counting.

## Sentinel date 1901-01-01 for never-activated orders

- **Symptom:** actives counts too high.
- **Cause:** `1901-01-01` is used as a placeholder activation date for orders
  that never activated.
- **Fix:** exclude the sentinel date from active-order logic. Never treat it as a
  real activation.

## NULL lineitemstatuscode dropped by NOT IN filter

- **Symptom:** revenue gap (observed for T-Mobile).
- **Cause:** `NOT IN` filters silently drop rows where `lineitemstatuscode` is
  NULL.
- **Fix:** handle NULLs explicitly (for example `... OR lineitemstatuscode IS
  NULL`) or use a NULL-safe filter.

## Rate card key rename breaks activation-rate joins

- **Symptom:** activation-rate joins fail from April 2026 onward.
- **Cause:** rate card key renamed from `T-Mobile IG` to `T-Mobile Integrated`.
- **Fix:** map both keys, or standardize on the new key across the join.

## BIGINT vs STRING mismatch on customer_account_number

- **Symptom:** precision loss on 16-digit account numbers in Spark joins.
- **Cause:** BIGINT / STRING type mismatch on `customer_account_number`.
- **Fix:** cast both sides to STRING before joining on the account number.

## Genesys telephony migration: call SID moved columns

- **Symptom:** orders fail channel attribution after the migration.
- **Cause:** Twilio call SIDs moved to a separate `twilio_call_id` column.
- **Fix:** dual-join approach that coalesces raw fields individually with the
  native call_id preferred, then re-derives helper fields from the coalesced
  values.

## Vivint fuzzy-match phantom payments

- **Symptom:** phantom paid matches appear before the payment file arrives.
- **Cause:** fuzzy-match fallbacks (Levenshtein-1, first-initial) create matches
  that are not real payments.
- **Fix:** require deterministic matching (leadID echo) for payment attribution.
  Do not rely on fuzzy fallbacks for paid status.
