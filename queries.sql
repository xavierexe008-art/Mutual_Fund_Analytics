-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average 1 year return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- Funds with low expense ratio
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top categories
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- Total transactions
SELECT COUNT(*)
FROM fact_transactions;

-- Average transaction amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- SIP transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- Redemption transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- Top states by investment
SELECT state, SUM(amount_inr)
FROM fact_transactions
GROUP BY state;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;