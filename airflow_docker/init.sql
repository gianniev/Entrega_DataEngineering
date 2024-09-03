-- Ensure schema exists
CREATE SCHEMA IF NOT EXISTS gianni_ev93_coderhouse;

-- Create table in the specified schema
CREATE TABLE IF NOT EXISTS gianni_ev93_coderhouse.coinmarketcap (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(250),
    symbol VARCHAR(64),
    marketcap INT,
    price DECIMAL, 
    volume_24 DECIMAL
);
