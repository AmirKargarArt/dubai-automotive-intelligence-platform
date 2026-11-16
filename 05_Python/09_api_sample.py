"""Optional API sample. Run with: uvicorn 09_api_sample:app --reload"""
from pathlib import Path
import pandas as pd
try:
    from fastapi import FastAPI
except ImportError:
    FastAPI=None
ROOT=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption'); C=ROOT/'02_Data_Clean'
if FastAPI:
    app=FastAPI(title='Dubai Automotive Intelligence API')
    @app.get('/health')
    def health(): return {'status':'ok','owner':'Amir Kargar'}
    @app.get('/sales/summary')
    def sales_summary(): return pd.read_csv(C/'synthetic_daily_sales.csv').groupby('brand',as_index=False).agg(units_sold=('units_sold','sum'),revenue_aed=('revenue_aed','sum')).to_dict('records')
else:
    app=None
