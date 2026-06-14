import pandas as pd

scorecard = pd.read_csv(
    "../data/processed/fund_scorecard.csv"
)

def recommend_funds(risk_level):

    recommendations = (
        scorecard[scorecard["risk_grade"] == risk_level]
        .sort_values(by="sharpe_ratio_x", ascending=False)
        [["scheme_name", "risk_grade", "sharpe_ratio_x", "fund_score"]]
        .head(3)
    )

    return recommendations


risk = input("Enter Risk Level (Low/Moderate/High): ")

print("\nRecommended Funds")
print(recommend_funds(risk))