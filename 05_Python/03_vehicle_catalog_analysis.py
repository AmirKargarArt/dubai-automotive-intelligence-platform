from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"02_Data_Clean/vehicle_catalog_clean.csv")
df["price_aed"]=pd.to_numeric(df["price_aed"],errors="coerce")
df["range_km_wltp"]=pd.to_numeric(df["range_km_wltp"],errors="coerce")
df["price_per_range_km"]=df["price_aed"]/df["range_km_wltp"]
summary=df.groupby(["brand","powertrain"],dropna=False).agg(model_count=("model","count"),avg_price_aed=("price_aed","mean"),avg_range_km=("range_km_wltp","mean")).reset_index()
summary.to_csv(ROOT/"02_Data_Clean/brand_powertrain_summary.csv",index=False)
priced=df.dropna(subset=["price_aed"]).sort_values("price_aed")
priced[["brand","model","powertrain","price_aed","range_km_wltp","price_per_range_km"]].to_csv(ROOT/"02_Data_Clean/priced_vehicle_comparison.csv",index=False)
plt.figure(figsize=(9,5))
summary.groupby("powertrain",dropna=False)["model_count"].sum().plot(kind="bar",color=["#0653B6","#16845B","#D1495B","#8CC8FF"])
plt.title("Dubai Automotive Catalog by Powertrain")
plt.xlabel("Powertrain")
plt.ylabel("Model count")
plt.tight_layout()
plt.savefig(ROOT/"02_Data_Clean/catalog_powertrain_mix.png",dpi=160)
print(summary.to_string(index=False))
