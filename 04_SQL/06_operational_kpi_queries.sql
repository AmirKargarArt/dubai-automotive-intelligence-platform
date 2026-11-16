-- Portfolio demonstration queries over clearly-labelled synthetic operational data.
-- Load CSVs into the SQL database before running.
SELECT brand, SUM(units_sold) AS units_sold, ROUND(SUM(revenue_aed),0) AS revenue_aed,
       ROUND(SUM(gross_profit_aed),0) AS gross_profit_aed
FROM synthetic_daily_sales GROUP BY brand ORDER BY revenue_aed DESC;

SELECT branch, ROUND(AVG(CASE WHEN actual_minutes<=promised_minutes THEN 1.0 ELSE 0 END)*100,1) AS on_time_pct,
       ROUND(AVG(csat),2) AS avg_csat, COUNT(*) AS service_orders
FROM synthetic_after_sales GROUP BY branch ORDER BY avg_csat DESC;

SELECT branch, brand, on_hand_units, monthly_demand,
       ROUND(on_hand_units*30.0/NULLIF(monthly_demand,0),1) AS inventory_days
FROM synthetic_inventory ORDER BY inventory_days ASC;
