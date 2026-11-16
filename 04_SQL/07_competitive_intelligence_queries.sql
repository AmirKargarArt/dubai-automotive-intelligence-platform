-- Competitive Intelligence queries
SELECT company, total_score, ev_readiness, after_sales, fleet_mobility
FROM competitor_scorecard ORDER BY total_score DESC;

SELECT company, segment, brand_count, showroom_count, service_center_count,
       ev_relevance, used_car_capability, fleet_capability, digital_capability
FROM competitor_public_benchmark ORDER BY ev_relevance DESC, total_score DESC;

SELECT company, total_score - (SELECT AVG(total_score) FROM competitor_scorecard) AS score_vs_average
FROM competitor_scorecard ORDER BY score_vs_average DESC;
