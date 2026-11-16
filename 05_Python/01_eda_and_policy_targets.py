"""Dubai Automotive Intelligence Platform - starter EDA and forecasting pipeline."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
raw = ROOT / "01_Data_Raw"
out = ROOT / "02_Data_Clean"
out.mkdir(exist_ok=True)
ev = pd.read_csv(raw / "uae_ev_policy_targets.csv")
ev.to_csv(out / "uae_ev_policy_targets_clean.csv", index=False)
summary = ev.groupby(["indicator","unit"], as_index=False)["value"].agg(["min","max","mean"]).reset_index()
summary.to_csv(out / "ev_policy_summary.csv", index=False)
print(summary)
plt.figure(figsize=(8,4))
policy = ev[ev["indicator"] == "EV_and_hybrid_share"]
plt.plot(policy["year"], policy["value"], marker="o", color="#0653B6")
plt.title("UAE EV and Hybrid Share Policy Targets")
plt.xlabel("Year")
plt.ylabel("Share (%)")
plt.grid(alpha=.25)
plt.tight_layout()
plt.savefig(out / "uae_ev_policy_targets.png", dpi=160)
print("Pipeline complete. Public policy data only; no proprietary sales data inferred.")
