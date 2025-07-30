CREATE SCHEMA IF NOT EXISTS energy;

-- Use the energy schema as default
SET search_path TO energy;

CREATE TABLE IF NOT EXISTS energy.energy_features (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMPTZ,

    -- Energy generation features
    generation_biomass NUMERIC,
    generation_fossil_brown_coal_lignite NUMERIC,
    generation_fossil_coal_derived_gas NUMERIC,
    generation_fossil_gas NUMERIC,
    generation_fossil_hard_coal NUMERIC,
    generation_fossil_oil NUMERIC,
    generation_fossil_oil_shale NUMERIC,
    generation_fossil_peat NUMERIC,
    generation_geothermal NUMERIC,
    generation_hydro_pumped_storage_consumption NUMERIC,
    generation_hydro_run_of_river_and_poundage NUMERIC,
    generation_hydro_water_reservoir NUMERIC,
    generation_marine NUMERIC,
    generation_nuclear NUMERIC,
    generation_other NUMERIC,
    generation_other_renewable NUMERIC,
    generation_solar NUMERIC,
    generation_waste NUMERIC,
    generation_wind_offshore NUMERIC,
    generation_wind_onshore NUMERIC,

    -- forecasts
    forecast_solar_day_ahead INTEGER,
    forecast_wind_onshore_day_ahead INTEGER,
    total_load_forecast INTEGER,
    total_load_actual NUMERIC,

    -- Prices
    price_day_ahead NUMERIC,
    price_actual NUMERIC,

    -- Weather and city features
    city_name TEXT,
    temp NUMERIC,
    temp_min NUMERIC,
    temp_max NUMERIC,
    pressure INTEGER,
    humidity INTEGER,
    wind_speed NUMERIC,
    wind_deg NUMERIC,
    rain_1h NUMERIC,
    rain_3h NUMERIC,
    snow_3h NUMERIC,
    clouds_all INTEGER,
    weather_id INTEGER,
    weather_main TEXT,
    weather_description TEXT,
    weather_icon TEXT,

    -- Time and date features
    hour INTEGER,
    wday INTEGER,
    month INTEGER,
    load_lag_1h NUMERIC,
    load_lag_24h NUMERIC,
    load_roll_24h NUMERIC,
    load_roll_7d NUMERIC
);
