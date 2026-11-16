# Cloud Continuation Prompt

You are taking over the Dubai Automotive Intelligence Platform created by Amir Kargar.

Your job is to continue the project without changing the business definitions or losing traceability.

## Context

This is a UAE/Dubai automotive intelligence platform covering sales, after-sales, EV adoption, used cars, fleet intelligence, customer voice, digital experience, and competitor benchmarking.

The project must have three synchronized interfaces:

- Persian (`fa-IR`, RTL)
- English (`en-US`, LTR)
- Arabic (`ar-AE`, RTL)

The main project handoff file is:

`09_Documentation/CLOUD_MIGRATION_HANDOFF.md`

Read it completely before modifying the project.

## First actions

1. Inspect the complete repository structure.
2. Read `README.md`, `requirements.txt`, `09_Documentation/CLOUD_MIGRATION_HANDOFF.md`, `09_Documentation/kpi_dictionary_trilingual.csv`, and `09_Documentation/source_registry.csv`.
3. Check Git status and preserve existing user work.
4. Verify all CSV files are UTF-8 with BOM or are loaded explicitly as UTF-8.
5. Validate notebook JSON and SQL syntax.
6. Do not delete or overwrite existing dashboards before creating a backup.

## Required implementation

Build a staging data pipeline with these layers:

```text
raw -> clean -> analytics -> serving -> dashboard
```

Add these metadata fields wherever appropriate:

- `source_id`
- `collected_at`
- `data_version`
- `is_synthetic`
- `language_neutral_kpi_id`

Use the KPI definitions in `kpi_dictionary_trilingual.csv` as the single source of truth. Do not invent a different formula for the Persian or Arabic dashboard.

## Dashboard requirements

Extend `07_Dashboard_3Lang/dist/index.html` or migrate it carefully to a modern framework. Preserve:

- Amir Kargar attribution.
- Persian, English, and Arabic language selector.
- RTL/LTR switching.
- Executive overview.
- Sales and market analysis.
- After-sales performance.
- EV readiness.
- Used-car opportunity.
- Fleet intelligence.
- Customer voice.
- Competitor benchmark.
- Opportunity prioritization.
- Recommendations.
- Sources and methodology.

Every insight card must contain:

1. What happened?
2. Why does it matter?
3. What action is recommended?
4. What data is needed to validate it?

## Quality and trust requirements

- Never present a hypothesis as a verified company weakness.
- Clearly label public, internal, estimated, and synthetic data.
- Add source links near public claims.
- Show data freshness and last refresh time.
- Show a confidence level for each insight.
- Show known limitations.
- Keep secrets in the Cloud secret manager, never in source files.

## Validation checklist

Run and report:

- Row counts before and after cleaning.
- Missing-value counts.
- Duplicate counts.
- Invalid date and numeric values.
- KPI reconciliation between SQL, Python, Excel, and dashboard.
- Equal numeric results across Persian, English, and Arabic.
- Browser checks for RTL, LTR, mobile, and desktop layouts.
- Build and deployment status.

## Deliverables to return

At the end, return:

1. Cloud staging URL.
2. Production URL only after validation.
3. Git commit hash.
4. Data pipeline description.
5. List of new or modified files.
6. Data-quality results.
7. Dashboard screenshots or preview link.
8. Remaining limitations.
9. Exact instructions for the next person.

Do not claim completion if the pipeline, dashboard, or deployment was not actually tested.

