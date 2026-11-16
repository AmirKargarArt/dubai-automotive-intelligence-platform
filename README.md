# Dubai Automotive Intelligence Platform

## Portfolio case study — Amir Kargar

A source-traceable business intelligence platform for a Dubai automotive distributor such as Al-Futtaim Automotive. It connects Excel, SQL, Python, Power BI-ready data and an online dashboard to answer one business question:

> Should the company prioritize EV growth, after-sales service quality, fleet operations or conventional vehicle volume?

## Deliverables

- `01_Data_Raw/`: public source extracts and input templates.
- `02_Data_Clean/`: cleaned catalog, policy, reviews, public facts and labelled synthetic operational data.
- `03_Excel/`: Excel master workbook.
- `04_SQL/`: schema, KPI queries, validation and operational queries.
- `05_Python/`: EDA, cleaning, 20-question notebook, synthetic data generator and forecast/risk demonstration.
- `06_PowerBI/`: model, KPI and import specifications.
- `07_Dashboard_20Q/`: separate published interactive dashboard.
- `08_AI_Insights/`: executive summary, management recommendations, model notes and data quality.
- `09_Documentation/`: source registry, data dictionary, site inventory and review collection plan.

## Online dashboard

[Open the Al-Futtaim Automotive 20-question dashboard](https://dubai-auto-20q-intelligence.masoudkargar.chatgpt.site)

## Technical stack

`Excel → SQL/SQLite → Python/NumPy/Pandas → Power BI → Online Dashboard`

## Operational demonstration

Files beginning with `synthetic_` are clearly labelled demonstration data. They model daily sales, leads, test drives, revenue, gross profit, service orders, CSAT, on-time service and inventory days. They must be replaced by authorized company exports before real decisions.

## Key KPIs

Sales conversion, average selling price, revenue, gross profit, inventory days, service on-time rate, average repair time, CSAT, complaint resolution time, EV adoption and charger utilization.

## Reproducibility

1. Run `python 05_Python/05_generate_operational_synthetic_data.py`.
2. Run `python 05_Python/06_forecast_and_customer_risk.py`.
3. Run `python 05_Python/04_full_pipeline.py` for the public-data pipeline.
4. Open `05_Python/Dubai_Automotive_20_Key_Questions_Analysis.ipynb`.
5. Import `02_Data_Clean/powerbi_*.csv` and synthetic KPI files into Power BI.
6. Open the online dashboard above.

## Data governance and limitations

Public product, policy and review data are source-traceable. User reviews are third-party or anecdotal and are used for hypothesis generation. Operational files are synthetic, not company data. The project does not claim private sales, margin or service performance.

## Presentation

Use `08_AI_Insights/video_script.md` for a two-to-three-minute portfolio walkthrough.

**Amir Kargar — Data Analysis**
