-- KPI queries for first Power BI/SQL review
SELECT powertrain, COUNT(*) AS model_count FROM dim_model GROUP BY powertrain ORDER BY model_count DESC;
SELECT b.brand_name, COUNT(m.model_key) AS model_count FROM dim_brand b LEFT JOIN dim_model m ON b.brand_key=m.brand_key GROUP BY b.brand_name ORDER BY model_count DESC;
SELECT powertrain, AVG(CASE WHEN range_km_wltp IS NOT NULL THEN range_km_wltp END) AS avg_range_km FROM vehicle_catalog_clean GROUP BY powertrain;
