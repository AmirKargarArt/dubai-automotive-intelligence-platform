# Dubai Automotive Intelligence Platform — Cloud Migration Handoff

## 1. Project identity

- Project: Dubai Automotive Intelligence Platform — Sales, After-Sales & EV Adoption
- Owner: Amir Kargar
- Purpose: Build an evidence-based automotive intelligence platform for the UAE/Dubai market.
- Main business areas: sales, after-sales, EV adoption, used cars, fleet intelligence, customer voice, digital experience, and competitor benchmarking.
- Required languages: Persian (`fa-IR`), English (`en-US`), Arabic (`ar-AE`).
- Current local root: `E:\Data_Analysis\Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption`

## 2. Business objective

The platform should help automotive companies identify measurable opportunities in:

1. Sales growth and model mix.
2. Service capacity, cycle time, retention, and customer satisfaction.
3. EV readiness, charging access, EV education, and EV conversion.
4. Used-car trust, transparency, inspection, and warranty.
5. Fleet utilization and total cost of ownership.
6. Customer sentiment and recurring complaints.
7. Competitor positioning, digital experience, media messaging, and public market signals.

The analysis must present weaknesses as hypotheses or opportunities unless supported by verified internal data.

## 3. Project structure

```text
01_Data_Raw/                 Original and collected source data
02_Data_Clean/               Cleaned and analysis-ready CSV files
03_Excel/                   Business model and spreadsheet outputs
04_SQL/                     SQLite database, schema, seed data, KPI queries
05_Python/                  EDA, forecasting, risk, TCO, competitor notebooks
06_PowerBI/                 Power BI model and dashboard specifications
07_Dashboard/               Original dashboard
07_Dashboard_20Q/           20-question dashboard
07_Dashboard_Competitive/   Competitive intelligence dashboard
07_Dashboard_3Lang/         Latest three-language dashboard
08_AI_Insights/             Executive insights, recommendations, limitations
09_Documentation/           Roadmaps, dictionaries, source registry, handoff docs
10_Presentation/            English and Persian presentation decks
```

## 4. Important existing artifacts

### Data

- `02_Data_Clean/public_market_facts.csv`
- `02_Data_Clean/customer_reviews_public.csv`
- `02_Data_Clean/competitor_public_benchmark.csv`
- `02_Data_Clean/competitor_scorecard.csv`
- `02_Data_Clean/synthetic_daily_sales.csv`
- `02_Data_Clean/synthetic_after_sales.csv`
- `02_Data_Clean/synthetic_inventory.csv`
- `02_Data_Clean/synthetic_service_risk_scores.csv`
- `02_Data_Clean/tco_vehicle_comparison.csv`

Synthetic files must always be labelled as synthetic in Cloud dashboards and reports.

### SQL

- `04_SQL/01_create_schema.sql`
- `04_SQL/02_analysis_queries.sql`
- `04_SQL/04_kpi_queries.sql`
- `04_SQL/06_operational_kpi_queries.sql`
- `04_SQL/07_competitive_intelligence_queries.sql`
- `04_SQL/dubai_automotive.db`

### Python and notebooks

- `05_Python/Dubai_Automotive_20_Key_Questions_Analysis.ipynb`
- `05_Python/Competitive_Intelligence_Analysis.ipynb`
- `05_Python/06_forecast_and_customer_risk.py`
- `05_Python/07_tco_and_competitor_analysis.py`
- `05_Python/08_alert_rules.py`

### Dashboard

- Latest local dashboard: `07_Dashboard_3Lang/dist/index.html`
- Languages: Persian, English, Arabic.
- Current navigation: overview, sources/data quality, sales, after-sales, EV readiness, used cars, fleet, customer voice, competitors, opportunity priorities, recommendations, methodology.
- The current version is a static prototype. The next Cloud task is to connect it to real APIs or refreshed data files.

## 5. KPI contract

The shared KPI dictionary is:

`09_Documentation/kpi_dictionary_trilingual.csv`

It contains KPI ID, domain, English/Persian/Arabic labels, definition, formula, unit, source type, and priority.

Core KPIs include:

- Total Deliveries
- Year-over-Year Growth
- Market Share
- Model Mix
- Lead Conversion Rate
- Service Retention Rate
- Average Service Cycle Time
- First-Time Fix Rate
- Customer Satisfaction
- Service Complaint Rate
- EV Share
- EV Readiness Index
- Charging Coverage
- EV Test Drive Conversion
- Used Car Trust Score
- Fleet Utilization
- Fleet Cost per Kilometer
- Digital Conversion Rate
- Positive Sentiment Rate
- Competitive Digital Score

The Cloud implementation must preserve these definitions and must not silently change formulas between languages.

## 6. Three-language rules

1. Persian is RTL and uses `fa-IR`.
2. Arabic is RTL and uses `ar-AE`.
3. English is LTR and uses `en-US`.
4. KPI values must be numerically identical in all three versions.
5. Only labels, explanatory text, date/number formatting, and direction may change.
6. Use a translation dictionary rather than hard-coding inconsistent labels.
7. Store language-independent KPI IDs in the data layer.

Shared glossary:

`09_Documentation/multilingual_glossary_excel.csv`

## 7. Source and evidence policy

Source registry:

`09_Documentation/source_registry.csv`

Every public claim should include:

- Source URL
- Source type
- Publication date
- Access date
- Extracted metric or claim
- Reliability score
- Limitation

Use official company, government, investor, market, and reputable media sources first. Public reviews are directional signals, not a complete representation of all customers.

## 8. Recommended Cloud architecture

### Development

- Git repository for source control.
- Python 3.11 or newer.
- `requirements.txt` for reproducible dependencies.
- `.env.example` for configuration names only.
- No API keys, tokens, passwords, or personal credentials in Git.

### Data layer

- Object storage for raw and cleaned CSV/Parquet files.
- PostgreSQL or cloud warehouse for curated tables.
- Separate `raw`, `clean`, `analytics`, and `serving` schemas.
- Add `source_id`, `collected_at`, `is_synthetic`, and `data_version` to serving tables.

### Processing layer

- Scheduled ingestion job.
- Python cleaning and KPI pipeline.
- SQL transformation layer.
- Data quality job before dashboard refresh.
- Log every run, row count, error, and data version.

### Dashboard layer

- Deploy `07_Dashboard_3Lang` as a static web app or migrate to React/Next.js.
- Add API endpoints for KPI summaries, trends, competitor scores, and sources.
- Add language selector and RTL/LTR handling.
- Add date, company, brand, region, powertrain, and source-quality filters.

### Optional services

- Power BI connected to a curated warehouse view.
- GitHub Actions for validation and deployment.
- Cloud scheduler for daily/weekly data refresh.
- Secrets manager for API keys.

## 9. Cloud migration sequence

1. Create private Git repository.
2. Upload project excluding secrets, temporary files, caches, and local credentials.
3. Add `.env.example` and environment documentation.
4. Run dependency installation.
5. Validate CSV encoding and schema.
6. Load clean data into a staging database.
7. Run SQL schema and KPI queries.
8. Run Python notebooks/scripts in a reproducible environment.
9. Execute data-quality checks.
10. Expose serving views or API endpoints.
11. Connect the dashboard to serving data.
12. Test all three languages and RTL/LTR layouts.
13. Deploy a private staging version.
14. Review with sample business users.
15. Publish production only after validation.

## 10. Release gates

Do not mark the project production-ready until:

- All three languages show equal KPI values.
- All public claims have traceable sources.
- Synthetic data is clearly labelled.
- Data-quality checks pass.
- Dashboard values match SQL outputs.
- Notebook outputs match dashboard extracts.
- No secrets are committed.
- The executive summary includes limitations and validation requirements.

## 11. Known limitations

- Some operational data is synthetic or template-based.
- Public competitor data is not a substitute for internal CRM, DMS, finance, or service data.
- Public reviews are biased toward customers who choose to post.
- Market-share coverage may differ by source and period.
- Recommendations are hypotheses until validated with company data.

## 12. Immediate next task

Create a Cloud staging environment, load the clean data, run the KPI contract, and connect the three-language dashboard to a read-only serving layer. Preserve the current local prototype as a fallback.

