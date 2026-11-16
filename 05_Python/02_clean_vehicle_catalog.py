from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
raw=ROOT/"01_Data_Raw/vehicle_catalog.csv"
out=ROOT/"02_Data_Clean"
df=pd.read_csv(raw, na_values=["NA",""])
for c in ["range_km_wltp","battery_kwh","max_power_kw","price_aed"]: df[c]=pd.to_numeric(df[c], errors="coerce")
df["is_electrified"]=df["powertrain"].isin(["BEV","HEV","PHEV"])
df["price_per_range_km"]=df["price_aed"]/df["range_km_wltp"]
df.to_csv(out/"vehicle_catalog_clean.csv",index=False)
df.groupby(["brand","powertrain"],dropna=False).size().reset_index(name="model_count").to_csv(out/"vehicle_catalog_summary.csv",index=False)
print(df.groupby(["brand","powertrain"],dropna=False).size())
