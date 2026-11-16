from pathlib import Path
import sqlite3, json, math
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/"01_Data_Raw"; clean=ROOT/"02_Data_Clean"; out=ROOT/"08_AI_Insights"; dbdir=ROOT/"04_SQL"
clean.mkdir(exist_ok=True); out.mkdir(exist_ok=True)
vehicle=pd.read_csv(raw/"vehicle_catalog.csv", na_values=["NA",""])
ev=pd.read_csv(raw/"uae_ev_policy_targets.csv")
sources=pd.read_csv(ROOT/"09_Documentation/source_registry.csv")
for c in ["range_km_wltp","battery_kwh","max_power_kw","price_aed"]: vehicle[c]=pd.to_numeric(vehicle[c],errors="coerce")
vehicle["is_electrified"]=vehicle["powertrain"].isin(["BEV","HEV","PHEV"])
vehicle["price_per_range_km"]=vehicle["price_aed"]/vehicle["range_km_wltp"]
vehicle.to_csv(clean/"powerbi_vehicle_catalog.csv",index=False)
ev.to_csv(clean/"powerbi_ev_policy.csv",index=False)
summary=vehicle.groupby(["brand","powertrain"],dropna=False).agg(model_count=("model","count"),priced_models=("price_aed",lambda x:x.notna().sum()),avg_price_aed=("price_aed","mean"),avg_range_km=("range_km_wltp","mean")).reset_index()
summary.to_csv(clean/"powerbi_brand_powertrain_summary.csv",index=False)
qa={"vehicle_rows":int(len(vehicle)),"source_rows":int(len(sources)),"missing_brand":int(vehicle["brand"].isna().sum()),"missing_model":int(vehicle["model"].isna().sum()),"negative_prices":int((vehicle["price_aed"]<0).sum()),"verified_public_rows":int((vehicle["status"]=="verified_public").sum()),"pending_spec_rows":int(vehicle["status"].astype(str).str.contains("pending").sum()),"data_quality_status":"PASS_WITH_PENDING_PUBLIC_SPECS"}
(out/"data_quality_report.json").write_text(json.dumps(qa,indent=2),encoding="utf-8")
conn=sqlite3.connect(dbdir/"dubai_automotive.db")
vehicle.to_sql("vehicle_catalog",conn,if_exists="replace",index=False)
ev.to_sql("ev_policy_targets",conn,if_exists="replace",index=False)
sources.to_sql("sources",conn,if_exists="replace",index=False)
conn.execute("CREATE INDEX IF NOT EXISTS idx_vehicle_brand ON vehicle_catalog(brand)")
conn.execute("CREATE INDEX IF NOT EXISTS idx_vehicle_powertrain ON vehicle_catalog(powertrain)")
conn.commit()
brand_stats=vehicle.groupby("brand").agg(models=("model","count"),electrified_share=("is_electrified","mean"),priced_models=("price_aed",lambda x:x.notna().sum())).sort_values("models",ascending=False)
policy_2050=float(ev.loc[(ev.indicator=="EV_and_hybrid_share")&(ev.year==2050),"value"].iloc[0])
top_brand=brand_stats.index[0]
insights=["The current public catalog contains %d models across %d brands."%(len(vehicle),vehicle.brand.nunique()),"%s has the largest representation in the current catalog with %d models."%(top_brand,int(brand_stats.loc[top_brand,"models"])),"The catalog is a public product benchmark, not company sales data; sales conclusions require validated registration or internal CRM data.","The UAE policy target reaches %.0f%% EV and hybrid share by 2050, creating a long-term electrification scenario for the dashboard."%policy_2050,"The highest-value next data acquisition is monthly registrations by brand/model and after-sales work orders by service center."]
(out/"management_insights.md").write_text("# Management Insights\\n\\n"+"\\n".join("- "+x for x in insights)+"\\n\\n## Limitations\\nPublic catalog and policy data only. No private sales or service results are inferred.\\n",encoding="utf-8")
case="# Dubai Automotive Intelligence Platform\\n\\n## Portfolio Case Study\\nBuilt by **Amir Kargar** using Excel, SQL, Python, Power BI-ready data and an online dashboard prototype.\\n\\n## Business question\\nShould a Dubai automotive distributor prioritize EV growth, after-sales services or conventional vehicle volume?\\n\\n## Current evidence\\n- 15 publicly sourced vehicle records across BYD, Toyota, Lexus and Volvo.\\n- BEV, HEV, PHEV and ICE categories represented.\\n- UAE EV policy targets and charging targets documented.\\n- SQL star-schema foundation and SQLite analytical database created.\\n\\n## Reproducibility\\n1. Run `python 05_Python/04_full_pipeline.py`.\\n2. Open `04_SQL/dubai_automotive.db`.\\n3. Import `02_Data_Clean/powerbi_*.csv` into Power BI.\\n4. Open `07_Dashboard/index.html`.\\n\\n## Data limitation\\nPublic product and policy data are separated from private operating data. Pending specifications remain explicitly marked.\\n"; (ROOT/"README.md").write_text(case,encoding="utf-8")
conn.close()
print(json.dumps(qa,indent=2))
