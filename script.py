from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
#from sqlalchemy import create_engine 

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
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


if 'data' in data:
    # Proceso de normalización y conversión a DataFrame
    df = pd.json_normalize(data['data'])

    # Filtrar las columnas necesarias
    columns_to_select = ['id', 'name', 'symbol', 'self_reported_market_cap','last_updated']
    df_filtered = df[columns_to_select]

    # Renombrar columnas para mayor claridad
    df_filtered.columns = ['id', 'name', 'symbol', 'market_cap', 'last_updated']

    # Mostrar el DataFrame resultante
    print(df_filtered.head())
else:
    print("No se encontraron datos en la respuesta de la API.")

#pd.set_option('display.max_columns', None)

#pd.json_normalize(data['data'])

# Normalizar los datos
#df_normalized = pd.json_normalize(data['data'])

# Guardar en un CSV
#df_normalized.to_csv('coinmarketcap_data.csv', index=False)

#Leer el CSV
#df = pd.read_csv('coinmarketcap_data.csv')

# Columnas 
#columns_to_select = ['id', 'name', 'symbol', 'self_reported_market_cap','last_updated']

#df_filtered = df[columns_to_select]

# Truncar las columnas a un tamaño máximo
#max_length = 256  # Ajusta según el tamaño de columna en Redshift
#for col in df.select_dtypes(include=['object']).columns:
#    df[col] = df[col].astype(str).str.slice(0, max_length)


# crear base de datos sql
#conn_string = 'postgresql://gianni_ev93_coderhouse:r9NYpl19Zl@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database'
#engine = create_engine(conn_string)

# Usar la conexión del motor para guardar el Dataframe en una base de datos
#with engine.connect() as conn:
#  df.to_sql('cryptocurrencies.gianni_ev93_coderhouse', conn, schema='gianni_ev93_coderhouse', if_exists='replace', index=False)

#print("Datos guardados exitosamente en la base de datos.")

