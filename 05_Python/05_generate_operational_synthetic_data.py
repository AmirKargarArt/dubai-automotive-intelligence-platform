"""Generate clearly-labelled synthetic operational data for portfolio demonstration."""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(r"E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption")
OUT = ROOT / "02_Data_Clean"
rng = np.random.default_rng(42)
dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")
branches = ["Dubai Festival City", "Sheikh Zayed Road", "Al Quoz", "Abu Dhabi Airport Road", "Sharjah"]
brands = ["Toyota", "Lexus", "BYD", "Volvo"]
power = {"Toyota":"Hybrid", "Lexus":"Hybrid", "BYD":"BEV", "Volvo":"BEV"}

rows=[]
for d in dates:
    for b in branches:
        for brand in brands:
            leads=int(rng.poisson(7 if brand in ["Toyota","BYD"] else 4))
            tests=int(min(leads, rng.binomial(leads, .36)))
            sales=int(min(tests, rng.binomial(tests, .24)))
            price={"Toyota":125000,"Lexus":280000,"BYD":160000,"Volvo":240000}[brand]
            rows.append([d.date(),b,brand,power[brand],leads,tests,sales,price,sales*price,sales*price*rng.uniform(.08,.14)])
sales=pd.DataFrame(rows,columns=["date","branch","brand","powertrain","leads","test_drives","units_sold","avg_price_aed","revenue_aed","gross_profit_aed"])
sales.to_csv(OUT/"synthetic_daily_sales.csv",index=False)

service=[]
for i in range(9000):
    opened=pd.Timestamp("2025-01-01")+pd.Timedelta(days=int(rng.integers(0,365)))
    promised=int(rng.normal(150,35)); actual=max(20,int(rng.normal(promised,45)))
    csat=round(np.clip(rng.normal(4.1 if actual<=promised else 3.1,.65),1,5),1)
    service.append([f"S{i+1:05d}",opened.date(),rng.choice(branches),rng.choice(brands),rng.choice(["Maintenance","Repair","Warranty","Recall"],p=[.48,.28,.16,.08]),promised,actual,csat,rng.choice(["Resolved","Escalated"],p=[.91,.09])])
service=pd.DataFrame(service,columns=["service_id","opened_date","branch","brand","service_type","promised_minutes","actual_minutes","csat","resolution_status"])
service.to_csv(OUT/"synthetic_after_sales.csv",index=False)

inventory=[]
for b in branches:
    for brand in brands:
        for powertrain in [power[brand]]:
            inventory.append([b,brand,powertrain,int(rng.integers(5,45)),int(rng.integers(3,25)),int(rng.integers(7,32))])
pd.DataFrame(inventory,columns=["branch","brand","powertrain","on_hand_units","monthly_demand","lead_time_days"]).to_csv(OUT/"synthetic_inventory.csv",index=False)

print("Generated synthetic_daily_sales.csv", len(sales))
print("Generated synthetic_after_sales.csv", len(service))
print("Generated synthetic_inventory.csv", len(inventory))
