from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
import shutil

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

pd.set_option('display.max_columns', None)

pd.json_normalize(data['data'])

# Normalizar los datos
df_normalized = pd.json_normalize(data['data'])

# Guardar en un CSV
df_normalized.to_csv('coinmarketcap_data.csv', index=False)

#Leer el CSV
df = pd.read_csv('coinmarketcap_data.csv')

# Normalizar los datos
df_normalized = pd.json_normalize(data['data'])

# Ruta del archivo CSV (en el directorio actual)
csv_file_path = 'coinmarketcap_data.csv'

# Guardar el DataFrame en un archivo CSV
df_normalized.to_csv(csv_file_path, index=False)

# Verificar si el archivo se ha guardado correctamente
if os.path.exists(csv_file_path):
    print(f"Archivo CSV guardado exitosamente en {csv_file_path}.")
else:
    print("El archivo no se ha guardado correctamente.")
