from airflow import DAG
from datetime import datetime
from pokemon import dataExtraction
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "Arthur Silva",
    "start_date": datetime(2025, 3, 17),
}

dag = DAG(
    "dataExtraction",
    default_args=default_args,
    schedule_interval="0 10 * * *", # https://crontab.guru/
    max_active_runs=1,
)

start_pipeline = DummyOperator(
    task_id="start_pipeline",
    dag=dag
)

data_extraction = PythonOperator(
    task_id='dataExtraction',
    python_callable=dataExtraction,
    dag=dag
)

done_pipeline = DummyOperator(
    task_id="done_pipeline",
    dag=dag
)

start_pipeline >> data_extraction >> done_pipeline