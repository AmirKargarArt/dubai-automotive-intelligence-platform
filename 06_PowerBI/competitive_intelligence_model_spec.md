# Competitive Intelligence Power BI Model

## Tables

- `competitor_public_benchmark`: company, segment, brand and network facts, capability indicators and source metadata.
- `competitor_scorecard`: normalized 1–5 benchmark scores for footprint, portfolio, EV, after-sales, used cars, fleet and digital experience.
- `source_registry`: source traceability and collection dates.

## Pages

1. Competitive Executive Overview
2. Market Footprint
3. Brand and Portfolio Comparison
4. EV Readiness Index
5. After-Sales Benchmark
6. Used Cars and Fleet Mobility
7. Digital Experience
8. SWOT and Opportunity Gaps

## Measures

```DAX
Average Competitor Score = AVERAGE(Scorecard[total_score])
EV Readiness Rank = RANKX(ALL(Scorecard[company]), MAX(Scorecard[ev_readiness]),, DESC)
Score vs Average = MAX(Scorecard[total_score]) - [Average Competitor Score]
Capability Coverage = DIVIDE(COUNTROWS(FILTER(Benchmark, Benchmark[ev_relevance] >= 4)), COUNTROWS(Benchmark))
```

Scores are structured portfolio benchmarks, not audited market share. Keep the source status visible in the report.
