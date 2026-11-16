CREATE TABLE dim_date (date_key INT PRIMARY KEY, full_date DATE NOT NULL, year INT NOT NULL, month INT NOT NULL, quarter INT NOT NULL);
CREATE TABLE dim_brand (brand_key INT PRIMARY KEY, brand_name VARCHAR(100) NOT NULL, distributor VARCHAR(150), source_id VARCHAR(20));
CREATE TABLE dim_model (model_key INT PRIMARY KEY, brand_key INT NOT NULL, model_name VARCHAR(150) NOT NULL, vehicle_type VARCHAR(50), powertrain VARCHAR(20), FOREIGN KEY (brand_key) REFERENCES dim_brand(brand_key));
CREATE TABLE dim_location (location_key INT PRIMARY KEY, emirate VARCHAR(50), area VARCHAR(100), latitude DECIMAL(9,6), longitude DECIMAL(9,6));
CREATE TABLE fact_sales (sale_id BIGINT PRIMARY KEY, date_key INT, brand_key INT, model_key INT, location_key INT, units_sold INT, revenue_aed DECIMAL(18,2), discount_aed DECIMAL(18,2), customer_type VARCHAR(30), source_id VARCHAR(20));
CREATE TABLE fact_service (service_id BIGINT PRIMARY KEY, date_key INT, brand_key INT, model_key INT, location_key INT, service_type VARCHAR(80), service_revenue_aed DECIMAL(18,2), parts_revenue_aed DECIMAL(18,2), turnaround_hours DECIMAL(10,2), source_id VARCHAR(20));
CREATE TABLE fact_ev_market (record_id BIGINT PRIMARY KEY, year INT, geography VARCHAR(80), indicator VARCHAR(100), value DECIMAL(18,4), unit VARCHAR(30), source_id VARCHAR(20));

CREATE TABLE vehicle_catalog (catalog_id VARCHAR(20) PRIMARY KEY, brand_key INT, model_name VARCHAR(150), vehicle_type VARCHAR(50), powertrain VARCHAR(20), trim VARCHAR(100), range_km_wltp DECIMAL(10,2), battery_kwh DECIMAL(10,2), max_power_kw DECIMAL(10,2), price_aed DECIMAL(18,2), market VARCHAR(50), status VARCHAR(50), source_id VARCHAR(20));

CREATE TABLE dim_customer (customer_key INT PRIMARY KEY, customer_type VARCHAR(30), emirate VARCHAR(50), source_id VARCHAR(20));
CREATE TABLE fact_inventory (inventory_id BIGINT PRIMARY KEY, snapshot_date DATE, location_key INT, brand_key INT, model_key INT, units_on_hand INT, days_in_inventory DECIMAL(10,2), unit_cost_aed DECIMAL(18,2), source_id VARCHAR(20));
