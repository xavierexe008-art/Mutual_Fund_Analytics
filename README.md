# Mutual Fund Analytics Dashboard

## Project Overview

This project was developed as part of the Bluestock Data Analyst Internship Capstone Project.

The objective of the project is to analyze mutual fund performance, investor behavior, SIP trends, and risk metrics using Python, SQLite, and Power BI. The project includes an ETL pipeline, exploratory data analysis, performance analytics, advanced risk analytics, and an interactive Power BI dashboard.

---

## Objectives

* Analyze mutual fund industry trends
* Evaluate fund performance using risk-adjusted metrics
* Study investor transaction behavior
* Monitor SIP and market trends
* Build an interactive dashboard for decision-making

---

## Tech Stack

* Python
* Pandas
* NumPy
* SQLite
* Jupyter Notebook
* Power BI
* Git & GitHub

---

## Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── dashboard/
│   └── bluestock_mf_dashboard.pbix
│
├── reports/
│   ├── rolling_sharpe_chart.png
│   ├── var_cvar_report.csv
│   ├── sip_continuity_report.csv
│   └── hhi_concentration_report.csv
│
└── README.md
```

---

## ETL Pipeline

1. Data Ingestion
2. Data Cleaning
3. Missing Value Handling
4. Feature Engineering
5. Data Transformation
6. SQLite Database Creation

---

## Exploratory Data Analysis

Performed analysis on:

* Mutual Fund Categories
* Investor Demographics
* Transaction Trends
* State-wise Investments
* SIP Behaviour

---

## Performance Analytics

Implemented:

* Daily Returns
* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Fund Scorecard

---

## Advanced Analytics

Implemented:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Fund Recommendation System
* Sector HHI Concentration Analysis

---

## Dashboard Pages

### Industry Overview

* AUM Analysis
* Industry Trends
* Fund House Comparison

### Fund Performance

* Risk vs Return Analysis
* Fund Rankings
* Benchmark Comparison

### Investor Analytics

* State-wise Investments
* Age Group Analysis
* Transaction Distribution

### SIP & Market Trends

* SIP Growth Trends
* Category Inflows
* Benchmark Market Performance

---

## Key Findings

* SIP inflows showed steady growth during the analysis period.
* Significant differences were observed in fund risk-adjusted performance.
* Investor behaviour varies across age groups and locations.
* Rolling Sharpe analysis highlighted differences in fund stability.
* SIP continuity analysis identified at-risk investors.

---

## Author

Pritam

Bluestock Data Analyst Internship Capstone Project
