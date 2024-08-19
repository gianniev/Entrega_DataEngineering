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

class toDatabase:
    def connect(self, conn_string, df ):
        self.conn_string = conn_string
        engine = create_engine(self.conn_string)

        with engine.connect() as conn:
            df.to_sql('coinmarketcap', conn, schema='gianni_ev93_coderhouse', if_exists='replace', index=False)

            num_rows2 = len(df)
            print("Datos guardados exitosamente en la base de datos.")
            print(f'Se han registrado en la base de datos un total de filas de:',num_rows2)


    #crear base de datos sql
    #conn_string = 'postgresql://gianni_ev93_coderhouse:r9NYpl19Zl@data-engineer-cluster.cyhh5bfevlmn.us-east-1.redshift.amazonaws.com:5439/data-engineer-database'
    #engine = create_engine(conn_string)

    # Usar la conexión del motor para gua rdar el Dataframe en una base de datos
   # with engine.connect() as conn:
    #df.to_sql('coinmarketcap', conn, schema='gianni_ev93_coderhouse', if_exists='replace', index=False)

    #print("Datos guardados exitosamente en la base de datos.")
    #print(f'Se han registrado en la base de datos un total de filas de:',num_rows2)