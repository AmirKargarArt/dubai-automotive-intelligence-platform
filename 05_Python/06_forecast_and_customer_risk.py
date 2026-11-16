"""Forecast and service-risk demonstration using synthetic operational data."""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT=Path(r"E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption")
C=ROOT/'02_Data_Clean'
sales=pd.read_csv(C/'synthetic_daily_sales.csv',parse_dates=['date'])
service=pd.read_csv(C/'synthetic_after_sales.csv')

monthly=sales.assign(month=sales.date.dt.to_period('M').astype(str)).groupby('month',as_index=False).agg(units_sold=('units_sold','sum'),revenue_aed=('revenue_aed','sum'))
monthly['month_index']=np.arange(len(monthly)); coef=np.polyfit(monthly['month_index'],monthly['units_sold'],1)
pred=np.polyval(coef,monthly['month_index']); monthly['forecast_units_next_month']=np.polyval(coef,len(monthly))
monthly['forecast_mae_units']=np.abs(monthly['units_sold']-pred).mean()
monthly.to_csv(C/'synthetic_monthly_sales_forecast.csv',index=False)

service['late']=(service.actual_minutes>service.promised_minutes).astype(int)
X=service[['actual_minutes','promised_minutes']]; y=service['late']
z=(service.actual_minutes-service.promised_minutes)/service.promised_minutes.replace(0,1)
service['late_risk_score']=1/(1+np.exp(-6*z))
service[['service_id','late','late_risk_score','csat']].to_csv(C/'synthetic_service_risk_scores.csv',index=False)
print('Forecast MAE units:', round(monthly.forecast_mae_units.iloc[0],2))
print('Next-month forecast:', round(monthly.forecast_units_next_month.iloc[-1],0))
print('Late-risk average score:', round(service.late_risk_score.mean(),3))
