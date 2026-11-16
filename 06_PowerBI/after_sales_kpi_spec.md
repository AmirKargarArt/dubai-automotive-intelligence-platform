# After-sales KPI definitions
- Service Revenue = SUM(total_service_revenue_aed)
- Average Turnaround Hours = AVG(turnaround_hours)
- Customer Satisfaction = AVG(customer_satisfaction_score)
- Warranty Share = COUNTIF(warranty_flag, TRUE) / COUNT(service_id)
- Repeat Service Rate = customers with service_visits > 1 / active customers
- Parts Mix = SUM(parts_revenue_aed) / SUM(total_service_revenue_aed)
- Inventory Days = AVG(days_in_inventory)

Data policy: these files are templates only until validated operational data is available.
