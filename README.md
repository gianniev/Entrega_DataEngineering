# Segunda entrega Coderhouse

Ahora desde el main.py se importan los modulos getData y toDatabase.
- getData extrae los datos de la API de coinmarketcap.
- toDatabase los envia a la base de datos Redshift


- En el main.py tengo el código hecho con Python y Json para extraer datos de la API de Coinmarketcap.
- Extraigo datos de criptomonedas, las manipulo, renombro columnas y lo transformo en un DataFrame.
- Luego se envía a la base de datos REDSHIFT con SQL Alchemy para comprobarlo a travéz del DBevaer.


# Segunda entrega Coderhouse

Ahora desde el main.py se importan los modulos getData y toDatabase.
- getData extrae los datos de la API de coinmarketcap.
- toDatabase los envia a la base de datos Redshift

# Version de pandas
pip install pandas==2.1.4

# Chequear versión
python -c "import pandas as pd; print(pd.__version__)"


# Entrega 03 de Setiembre, Pre entrega numero 3. Clase 10
- Agregado docker-compose.yaml
- Agregado dags, falta meterlo en una carpeta
- Falta poner el main.py dentro del def main():
- He logrado avanzar en ciertos aspectos pero no he podido concretar correctamente la visualización del dag en Airflow y tampoco visualizar las tablas/schemas con dbeaver. Espero tener una segunda oportunidad para completar la entrega nuevamente ya que no he podido completarla. Algo en el pipeline estoy fallando
