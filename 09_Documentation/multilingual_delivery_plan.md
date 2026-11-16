# Multilingual Delivery Plan

Project owner: Amir Kargar

This project will be delivered in three synchronized versions:

- Persian (`fa-IR`): primary RTL presentation for local stakeholders.
- English (`en-US`): international portfolio and company-facing version.
- Arabic (`ar-AE`): UAE-market presentation for local automotive stakeholders.

## Synchronization rules

1. All three versions use the same source data, KPI definitions, filters, and calculation logic.
2. Only language, layout direction, labels, narrative text, and number/date formatting may differ.
3. Every insight must preserve its evidence, source URL, confidence level, and limitation across all languages.
4. Any change to a KPI must be made once in the data/model layer and then propagated to all versions.

## Delivery matrix

| Artifact | Persian | English | Arabic |
|---|---|---|---|
| Executive summary | Required | Required | Required |
| Excel business model | Required | Required | Required |
| SQL queries | Comments/labels | Comments/labels | Comments/labels |
| Python notebook | Narrative cells | Narrative cells | Narrative cells |
| Power BI specification | Required | Required | Required |
| Interactive dashboard | RTL | LTR | RTL |
| Presentation | Required | Required | Required |
| Source register | Required | Required | Required |

## First milestone

Before adding new analysis, create and validate one shared KPI dictionary and one shared source register. Then replicate the first dashboard page in all three languages and compare the outputs for numerical equality.

