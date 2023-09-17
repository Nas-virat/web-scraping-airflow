from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator


default_args = {
    'owner': 'Napas',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id = 'test_dag',
    default_args = default_args,
    description = 'test dag',
    start_date = datetime(2023,9,16,2),
    schedule_interval = '@daily',
) as dag:
    
    task_1 = BashOperator(
        task_id = 'task_1',
        bash_command = 'echo "Hello World!"',
    )

    task_1
