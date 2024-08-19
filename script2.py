from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from sqlalchemy import create_engine 

# Define la conexión a la base de datos
conn_string = 'postgresql://gianni_ev93_coderhouse:r9NYpl19Zl@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database'
engine = create_engine(conn_string)

# Consulta SQL para leer datos de la tabla
query = 'SELECT * FROM gianni_ev93_coderhouse.coinmarketcap'

# Leer datos desde la base de datos a un DataFrame
df = pd.read_sql_query(query, con=engine)

# Mostrar las primeras filas del DataFrame
print(df.head())
