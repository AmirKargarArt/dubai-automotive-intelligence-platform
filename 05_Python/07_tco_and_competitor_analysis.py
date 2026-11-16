from pathlib import Path
import pandas as pd

ROOT=Path(r'E:/Data_Analysis/Dubai Automotive Intelligence Platform Sales, After-Sales & EV Adoption'); OUT=ROOT/'02_Data_Clean'
cars=pd.DataFrame([
['Toyota Corolla Hybrid','Toyota','Hybrid',89900,6.2,4500,42000],['Toyota RAV4 Hybrid','Toyota','Hybrid',114900,5.8,5200,50000],['BYD ATTO 3','BYD','BEV',149900,0,1800,62000],['Lexus UX300h','Lexus','Hybrid',172000,5.5,7000,48000],['Volvo EX30','Volvo','BEV',189900,0,2200,65000]],columns=['model','brand','powertrain','price_aed','fuel_l_per_100km','annual_service_aed','resale_value_aed'])
fuel_price=2.9; annual_km=20000; years=5
cars['energy_cost_5y_aed']=cars.fuel_l_per_100km.fillna(0)/100*annual_km*years*fuel_price
cars['service_cost_5y_aed']=cars.annual_service_aed*years
cars['tco_5y_aed']=cars.price_aed+cars.energy_cost_5y_aed+cars.service_cost_5y_aed-cars.resale_value_aed
cars.to_csv(OUT/'tco_vehicle_comparison.csv',index=False)

competitors=pd.DataFrame([
['Toyota','Mass market / Hybrid','High','High','Medium','Al-Futtaim Toyota / official UAE'],['BYD','EV / PHEV','High','Growing','High','Al-Futtaim BYD / official UAE'],['Lexus','Premium / Hybrid / EV','Medium','High','High','Al-Futtaim Lexus / official UAE'],['Volvo','Premium EV','Medium','Medium','High','Volvo UAE / official UAE'],['Mercedes-Benz','Premium / EV','High','High','High','Gargash / official UAE']],columns=['brand','positioning','portfolio_breadth','after_sales_signal','electrification_relevance','source_context'])
competitors.to_csv(OUT/'competitor_benchmark.csv',index=False)
print(cars[['model','tco_5y_aed']]); print(competitors)
