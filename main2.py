from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from modules import APIConnector
from sqlalchemy import create_engine 
import requests
import logging
from dotenv import load_dotenv

def main():
    # URL base para CoinMarketCap y API Key
    base_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    api_key = 'b822fdc7-3991-4228-aa43-84651085916c'
    
    # Parámetros predeterminados para la solicitud
    default_params = {
        'start': '1',
        'limit': '5000',
        'convert': 'USD'
    }

    # Crear una instancia de APIConnector
    api_connector = APIConnector(base_url, api_key, default_params)

    # Obtener los datos
    data = api_connector.get_data()

    if data:
        # Aquí puedes manipular el dataframe `df_filtered` basado en los datos obtenidos
        print("Datos obtenidos:", data)
    else:
        print("No se pudieron obtener los datos.")

if __name__ == "__main__":
    main()
