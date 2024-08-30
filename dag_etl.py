import os 
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/dags')  # Ensure the DAG can import main.py

from main import main

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'cryptocurrencies_etl',
    default_args=default_args,
    description='Extract, Transform and Load crypto data daily',
    schedule_interval="@daily",
    catchup=False,
) as dag:

    #Task 1
    run_main_script = PythonOperator(
        task_id = "run_main_script",
        python_callable=main, # Call main function from the main
    )

    # Task Dependencies
    run_main_script
