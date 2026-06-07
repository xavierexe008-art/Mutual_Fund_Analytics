import pandas as pd

files = {
    "AUM": "data/raw/03_aum_by_fund_house.csv",
    "SIP": "data/raw/04_monthly_sip_inflows.csv",
    "Category": "data/raw/05_category_inflows.csv",
    "Folio": "data/raw/06_industry_folio_count.csv",
    "Holdings": "data/raw/09_portfolio_holdings.csv"
}

for name, path in files.items():
    df = pd.read_csv(path)
    print("\n" + name)
    print(df.columns.tolist())