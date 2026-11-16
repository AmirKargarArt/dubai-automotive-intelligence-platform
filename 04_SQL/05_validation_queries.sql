SELECT COUNT(*) AS vehicle_rows FROM vehicle_catalog;
SELECT powertrain, COUNT(*) AS model_count FROM vehicle_catalog GROUP BY powertrain ORDER BY model_count DESC;
SELECT brand, COUNT(*) AS model_count, SUM(CASE WHEN is_electrified=1 THEN 1 ELSE 0 END) AS electrified_models FROM vehicle_catalog GROUP BY brand ORDER BY model_count DESC;
SELECT year, indicator, value FROM ev_policy_targets WHERE year=2050;
