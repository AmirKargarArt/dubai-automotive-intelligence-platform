# Power BI Import Manifest
Import these files from `02_Data_Clean`:
- `powerbi_vehicle_catalog.csv`
- `powerbi_ev_policy.csv`
- `powerbi_brand_powertrain_summary.csv`

Recommended relationships:
- Vehicle Catalog[brand] -> Brand dimension
- Vehicle Catalog[powertrain] -> Powertrain dimension
- EV Policy[year] -> Date dimension

Refresh note: public product specifications and policy targets only.
