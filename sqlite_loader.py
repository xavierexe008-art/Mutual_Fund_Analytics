import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
perf = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
txn = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

# Load master dataset
fund = pd.read_csv("data/raw/01_fund_master.csv")

# Save to SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database created successfully!")