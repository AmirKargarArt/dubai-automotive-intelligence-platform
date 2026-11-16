# Detailed Execution Roadmap

## Project identity

- Project: Dubai Automotive Intelligence Platform
- Target company context: Al-Futtaim Automotive and its UAE automotive ecosystem
- Owner: Amir Kargar
- Career target: Data Analyst, BI Analyst, Automotive Intelligence Analyst
- Market: Dubai and UAE automotive sector
- Core tools: Excel, SQL, SQLite, Python, Jupyter, Power BI, HTML, JavaScript and API concepts

## Stage 00 — Idea definition

| Step | Task | Output | Tool | Status |
|---|---|---|---|---|
| 00.01 | Define portfolio goal | Automotive intelligence case study | Planning | Done |
| 00.02 | Define target market | Dubai and UAE | Planning | Done |
| 00.03 | Define target company | Al-Futtaim Automotive | Research | Done |
| 00.04 | Define business areas | Sales, after-sales, fleet, EV and used cars | Planning | Done |
| 00.05 | Define career narrative | End-to-end analytics project | README | Done |

## Stage 01 — Business problem framing

| Step | Question | Deliverable | Status |
|---|---|---|---|
| 01.01 | How can the company grow EV adoption? | EV analysis track | Done |
| 01.02 | Where can after-sales performance improve? | Customer experience track | Done |
| 01.03 | How should inventory and fleet be managed? | Operations track | Done |
| 01.04 | What can public data prove? | Source-traceable baseline | Done |
| 01.05 | What requires internal data? | Data-gap checklist | Done |

## Stage 02 — Company and ecosystem mapping

Mapped entities:

- Al-Futtaim Automotive
- Al-Futtaim Toyota
- Al-Futtaim Lexus
- Al-Futtaim BYD
- Al-Futtaim Volvo
- Al-Futtaim Automall
- Charge2MOOV
- Hertz UAE
- Al-Futtaim Vehicle Rentals
- Dubai RTA
- UAE Energy and EV policy bodies
- Toyota, Lexus, BYD, Volvo and Mercedes competitor context

## Stage 03 — Source discovery

| Source type | Data collected | Validation action | Status |
|---|---|---|---|
| Official company pages | Brands, services, fleet, charging and ecosystem | URL and collection date | Done |
| Official brand pages | Models, prices, hybrid and EV products | Product page cross-check | Done |
| UAE government | EV and Hybrid targets, charging policy | Government source registry | Done |
| Dubai RTA | Mobility and EV context | Official RTA page | Done |
| Third-party review pages | Aggregate service ratings | Rating plus review count | Done |
| Forums and Reddit | Qualitative customer hypotheses | Anecdotal label | Done |
| Kaggle and GitHub | Candidate external datasets | License and relevance review | Planned |

## Stage 04 — Data governance

- Create source registry
- Add URL, source type and collection date
- Separate official facts from interpretation
- Separate public data from synthetic data
- Label anecdotal reviews
- Record units and currencies
- Record assumptions and limitations
- Create data dictionary
- Create data collection plan
- Define refresh frequency

## Stage 05 — Raw data layer

Created or collected:

- Company profile
- UAE EV policy targets
- Vehicle catalog
- After-sales template
- Inventory template
- Customer template
- Public market facts
- Official site inventory
- Public customer reviews
- Review collection plan

## Stage 06 — Cleaning and transformation

- Standardize brand names
- Standardize powertrain labels
- Convert prices to AED
- Normalize dates
- Repair malformed review CSV quoting
- Separate indicator and value columns in policy data
- Validate row counts
- Create Power BI-ready extracts
- Create summary tables by brand and powertrain
- Generate data quality report

## Stage 07 — Excel layer

- Create master workbook
- Add raw data sheets
- Add clean data sheets
- Add policy target tables
- Add vehicle comparison
- Add source registry
- Add data dictionary
- Add operational templates
- Prepare workbook for stakeholder review

## Stage 08 — SQL layer

- Create database schema
- Create vehicle catalog tables
- Create policy tables
- Seed vehicle catalog
- Add KPI queries
- Add validation queries
- Add operational sales queries
- Add service queries
- Add inventory-days query
- Validate SQLite database

## Stage 09 — Python analysis layer

- Public-data EDA
- Policy target analysis
- Vehicle catalog cleaning
- Brand and powertrain comparison
- Price comparison
- Review analysis
- Synthetic data generation
- Monthly sales forecast
- Service delay risk score
- TCO analysis
- Competitor benchmark
- Operational alerts

## Stage 10 — Jupyter Notebook

Created notebook with 20 questions covering:

1. Brand model count
2. Powertrain mix
3. EV and Hybrid catalog share
4. Electrified price distribution
5. Lowest-priced electrified models
6. Price and powertrain relationship
7. UAE EV and Hybrid target path
8. Policy gap versus baseline
9. Charging infrastructure target
10. Ecosystem touchpoints
11. Service ratings
12. Review sample size
13. Negative review themes
14. Review source quality
15. Automall inspection opportunity
16. Hertz fleet scale
17. Commercial fleet opportunity
18. Model coverage versus policy target
19. Data gap prioritization
20. Recommended actions

## Stage 11 — Operational simulation

Synthetic files created for demonstration:

- Daily sales: 7,300 records
- After-sales service: 9,000 records
- Inventory: 20 records
- Monthly forecast output
- Service risk scores
- Operational alerts

## Stage 12 — Advanced analysis

- Five-year TCO comparison
- Energy cost assumption
- Service cost assumption
- Resale value assumption
- Competitor positioning
- Sales forecast MAE
- Service late-risk score
- Inventory days
- On-time service percentage
- CSAT
- Lead-to-sale conversion
- Gross margin

## Stage 13 — Power BI design

Report pages:

1. Executive Overview
2. Sales Funnel
3. Branch Performance
4. Inventory Optimization
5. After-Sales Control Tower
6. EV Adoption
7. Customer Voice
8. TCO and Competitors
9. Forecast and Alerts
10. Data Quality and Sources

## Stage 14 — Online dashboard

- Create separate hosted site
- Add 20-question navigation
- Add interactive charts
- Add Persian RTL layout
- Add Al-Futtaim Automotive identity
- Add Amir Kargar attribution
- Apply navy and cyan brand palette
- Publish private production URL
- Re-publish after branding corrections

## Stage 15 — Communication assets

- Executive summary
- Management recommendations
- Video script
- English PowerPoint
- Persian PowerPoint
- Trilingual Word document
- GitHub README
- Requirements file
- License
- Contributing guide

## Stage 16 — Final portfolio packaging

- Add screenshots
- Add dashboard URL
- Add notebook link
- Add data limitations
- Add source registry
- Add reproducibility steps
- Add short demo video
- Publish GitHub repository
- Add project to CV
- Add project to LinkedIn
- Prepare interview walkthrough

## Stage 17 — Production backlog

1. Replace synthetic data with authorized company data.
2. Connect CRM and dealer management system.
3. Add real branch-level reviews.
4. Add authentication to API.
5. Add scheduled data refresh.
6. Add monitoring and logging.
7. Validate TCO with finance data.
8. Run a 90-day pilot.
9. Measure recommendation impact.
