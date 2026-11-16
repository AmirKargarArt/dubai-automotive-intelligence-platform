-- Seed data generated from vehicle_catalog.csv
-- NULL indicates that the public source did not publish the field.
INSERT INTO dim_brand (brand_key, brand_name, distributor, source_id) VALUES
(1, 'BYD', 'Al-Futtaim Automotive', 'SRC008'),
(2, 'Volvo', 'Al-Futtaim Automotive', 'SRC011'),
(3, 'Toyota', 'Al-Futtaim Automotive', 'SRC012'),
(4, 'Lexus', 'Al-Futtaim Automotive', 'SRC014');

INSERT INTO dim_model (model_key, brand_key, model_name, vehicle_type, powertrain) VALUES
(1, 1, 'ATTO 3', 'SUV', 'BEV'),
(2, 1, 'ATTO 3', 'SUV', 'BEV'),
(3, 1, 'SEAL 7 DM-i', 'Sedan', 'PHEV'),
(4, 1, 'HAN', 'Sedan', 'BEV'),
(5, 2, 'EX30', 'SUV', 'BEV'),
(6, 3, 'Corolla Hybrid', 'Sedan', 'HEV'),
(7, 3, 'Camry Hybrid', 'Sedan', 'HEV'),
(8, 3, 'Land Cruiser Hybrid', 'SUV', 'HEV'),
(9, 3, 'RAV4 Hybrid', 'SUV', 'HEV'),
(10, 3, 'Corolla', 'Sedan', 'ICE'),
(11, 4, 'ES500e', 'Sedan', 'BEV'),
(12, 4, 'RZ500e', 'SUV', 'BEV'),
(13, 4, 'UX300h', 'SUV', 'HEV'),
(14, 4, 'NX350h', 'SUV', 'HEV'),
(15, 3, 'bZ4X Touring', 'SUV', 'BEV');
