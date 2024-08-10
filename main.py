from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
#from modules import DataConn
from sqlalchemy import create_engine 
import requests
import logging
from dotenv import load_dotenv



# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b822fdc7-3991-4228-aa43-84651085916c',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



if 'data' in data:
    # Proceso de normalización y conversión a DataFrame
    df = pd.json_normalize(data['data'])

    # Filtrar las columnas necesarias
    columns_to_select = ['id', 'name', 'symbol', 'self_reported_market_cap', 'quote.USD.price', 'quote.USD.volume_24h']

    df_filtered = df[columns_to_select]

    # Renombrar columnas para mayor claridad
    df_filtered.columns = ['id', 'name', 'symbol', 'market_cap', 'price', 'volume_24']
    df = df_filtered.head(2000)

    # Mostrar el DataFrame resultante
    num_rows = len(df_filtered)
    num_rows2 = len(df)
    print(f'La Api me extrae un total de filas de:', num_rows)
    print(df.head())
else:
    print("No se encontraron datos en la respuesta de la API.")


#crear base de datos sql
conn_string = 'postgresql://gianni_ev93_coderhouse:r9NYpl19Zl@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database'
engine = create_engine(conn_string)

# Usar la conexión del motor para guardar el Dataframe en una base de datos
with engine.connect() as conn:
  df.to_sql('coinmarketcap', conn, schema='gianni_ev93_coderhouse', if_exists='replace', index=False)

  print("Datos guardados exitosamente en la base de datos.")
  print(f'Se han registrado en la base de datos un total de filas de:',num_rows2)

