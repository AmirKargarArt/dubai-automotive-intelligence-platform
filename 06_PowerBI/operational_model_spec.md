# Power BI Operational Model

## Fact tables

- `synthetic_daily_sales`: date, branch, brand, powertrain, leads, test_drives, units_sold, revenue_aed, gross_profit_aed.
- `synthetic_after_sales`: service_id, date, branch, brand, service_type, promised_minutes, actual_minutes, csat, resolution_status.
- `synthetic_inventory`: branch, brand, powertrain, on_hand_units, monthly_demand, lead_time_days.

## Measures

```DAX
Lead Conversion % = DIVIDE(SUM(Sales[units_sold]), SUM(Sales[leads]))
Test Drive Conversion % = DIVIDE(SUM(Sales[units_sold]), SUM(Sales[test_drives]))
Gross Margin % = DIVIDE(SUM(Sales[gross_profit_aed]), SUM(Sales[revenue_aed]))
On-Time Service % = DIVIDE(CALCULATE(COUNTROWS(Service), Service[actual_minutes] <= Service[promised_minutes]), COUNTROWS(Service))
Average CSAT = AVERAGE(Service[csat])
Inventory Days = DIVIDE(SUM(Inventory[on_hand_units]) * 30, SUM(Inventory[monthly_demand]))
EV Sales Share = DIVIDE(CALCULATE(SUM(Sales[units_sold]), Sales[powertrain] = "BEV"), SUM(Sales[units_sold]))
```

## Recommended report pages

1. Executive Overview
2. Sales Funnel and Profitability
3. Branch and Inventory
4. After-Sales Control Tower
5. EV Adoption and Charging
6. Customer Reviews and Quality
