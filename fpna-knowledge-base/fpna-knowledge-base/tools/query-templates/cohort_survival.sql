-- Cohort survival template (illustrative).
-- Pooled survival weighted by M0 units at each payment number.
-- Replace table and column names with the canonical model logic before use.

WITH cohort_base AS (
    SELECT
        cohort_month,
        payment_number,
        SUM(active_units) AS active_units,
        SUM(m0_units)     AS m0_units
    FROM home_prod.dashboards.mv_charter_enterprise
    GROUP BY cohort_month, payment_number
),

pooled AS (
    SELECT
        payment_number,
        SUM(active_units) / NULLIF(SUM(m0_units), 0) AS survival_probability
    FROM cohort_base
    GROUP BY payment_number
)

SELECT
    payment_number,
    survival_probability
FROM pooled
WHERE payment_number BETWEEN 1 AND 60
ORDER BY payment_number;
