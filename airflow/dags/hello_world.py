from datetime import datetime, timedelta
from textwrap import dedent

from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 1, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
dag = DAG(
    'example',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=None,
    tags=['example'],
)

def print_function():
    print("The Function Ran!")

run_etl = PythonOperator(
    task_id='whole_example_etl',
    python_callable=print_function,
    dag=dag,
)
run_etl
