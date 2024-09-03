from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import logging
from dotenv import load_dotenv
from modules.toDatabase import toDatabase
from modules.getData import fetch_crypto_data

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    load_dotenv()

    # Extrar Data de la API desel modulo getdData
    try:
        data = fetch_crypto_data()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        logging.error(f"Error al obtener datos de la API: {e}")
        return

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


    # Enviar data a la base de datos Redshift utilizando el modulo toDatabase
    conn_string = 'postgresql://gianni_ev93_coderhouse:r9NYpl19Zl@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database'

    db = toDatabase()

    try:
        db.connect(conn_string, df)
    except Exception as e:
        logging.error(f"Error al conectar o enviar datos a la base de datos: {e}")

 


