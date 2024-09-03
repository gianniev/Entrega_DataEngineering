import os 
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from modules.crypto_data import run_pipeline

#sys.path.append('/opt/airflow/dags')  # Ensure the DAG can import main.py

 

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'cryptocurrencies_etl',
    default_args=default_args,
    description='Extract, Transform and Load crypto data daily',
    schedule_interval="@daily",
    catchup=False,
    tags=['crypto'],  # Adding tags for better organization
) as dag:

    
    # Task 1
    run_pipeline_task = PythonOperator(
        task_id='run_pipeline_task',
        python_callable=run_pipeline,  
    )

    # Define Task Dependencies
    run_pipeline_task
