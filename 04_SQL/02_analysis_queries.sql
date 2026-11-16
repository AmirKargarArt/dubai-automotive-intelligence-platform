-- Dubai Automotive Intelligence Platform analytical queries
SELECT b.brand_name, SUM(f.units_sold) AS units_sold, SUM(f.revenue_aed) AS revenue_aed FROM fact_sales f JOIN dim_brand b ON f.brand_key=b.brand_key GROUP BY b.brand_name ORDER BY revenue_aed DESC;
SELECT p.powertrain, SUM(f.units_sold) AS units_sold, AVG(f.revenue_aed/NULLIF(f.units_sold,0)) AS avg_value_per_unit FROM fact_sales f JOIN dim_model p ON f.model_key=p.model_key GROUP BY p.powertrain;
SELECT l.emirate, COUNT(DISTINCT f.sale_id) AS transactions, SUM(f.revenue_aed) AS revenue_aed FROM fact_sales f JOIN dim_location l ON f.location_key=l.location_key GROUP BY l.emirate ORDER BY revenue_aed DESC;
SELECT service_type, AVG(turnaround_hours) AS avg_turnaround_hours, SUM(service_revenue_aed) AS service_revenue_aed FROM fact_service GROUP BY service_type ORDER BY service_revenue_aed DESC;
