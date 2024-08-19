DROP TABLE IF EXISTS gianni_ev93_coderhouse.coinmarketcap;

CREATE TABLE IF NOT EXISTS gianni_ev93_coderhouse.coinmarketcap(
    id INTEGER IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(250),
    symbol VARCHAR(64),
    marketcap int,
    price DECIMAL, 
	volume_24 DECIMAL     
);