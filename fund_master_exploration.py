import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Columns:")
print(df.columns)

print("\nFund Houses:")
if "fund_house" in df.columns:
    print(df["fund_house"].unique())

print("\nCategories:")
if "category" in df.columns:
    print(df["category"].unique())

print("\nSub Categories:")
if "subcategory" in df.columns:
    print(df["subcategory"].unique())