# Power BI Model Specification
## Pages
1. Executive Overview
2. Sales by Brand and Model
3. After-Sales Performance
4. EV Adoption and Policy Targets
5. Dubai Location Analysis
6. Forecast and Scenarios
## Core Measures
- Total Units = SUM(fact_sales[units_sold])
- Revenue AED = SUM(fact_sales[revenue_aed])
- Average Price = DIVIDE([Revenue AED],[Total Units])
- EV Share = DIVIDE(CALCULATE([Total Units],dim_model[powertrain]="BEV"),[Total Units])
- Service Revenue AED = SUM(fact_service[service_revenue_aed])
## Data quality checks
- No missing brand or model keys
- No negative units or revenue
- Every KPI has source_id lineage
- Separate official facts from assumptions
