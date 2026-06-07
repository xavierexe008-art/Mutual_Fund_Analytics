# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | INTEGER | Unique fund identifier |
| scheme_name | TEXT | Fund scheme name |
| fund_house | TEXT | AMC name |
| category | TEXT | Equity/Debt etc |

## fact_nav

| Column | Type | Description |
|----------|---------|-------------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|---------|-------------|
| investor_id | INTEGER | Investor identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Amount invested |

## fact_performance

| Column | Type | Description |
|----------|---------|-------------|
| return_1yr_pct | REAL | 1 year return |
| return_3yr_pct | REAL | 3 year return |
| return_5yr_pct | REAL | 5 year return |
| expense_ratio_pct | REAL | Expense ratio |