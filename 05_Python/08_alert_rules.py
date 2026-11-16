from pathlib import Path
import pandas as pd
ROOT=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption'); C=ROOT/'02_Data_Clean'
inv=pd.read_csv(C/'synthetic_inventory.csv'); service=pd.read_csv(C/'synthetic_after_sales.csv')
alerts=[]
for _,r in inv.iterrows():
    days=r.on_hand_units*30/max(r.monthly_demand,1)
    if days<20: alerts.append(['Inventory',r.branch,r.brand,'High','Inventory days below 20',round(days,1)])
for branch,r in service.groupby('branch'):
    ontime=(r.actual_minutes<=r.promised_minutes).mean()*100
    if ontime<75: alerts.append(['Service',branch,'All brands','Medium','On-time service below 75%',round(ontime,1)])
pd.DataFrame(alerts,columns=['alert_type','branch','brand','severity','rule','value']).to_csv(C/'operational_alerts.csv',index=False)
print('alerts:',len(alerts))
