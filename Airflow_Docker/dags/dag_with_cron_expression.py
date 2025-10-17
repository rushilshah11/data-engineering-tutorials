from airflow import DAG 
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'rushil',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id="dag_with_cron_expression_v4",
    description="This is our first DAG with cron expression",
    start_date=datetime(2025, 9, 1),
    schedule='0 3 * * Tue'
) as dag:
    
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )
    task2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5'
    )
    task3 = BashOperator(
        task_id='print_whoami',
        bash_command='whoami'
    )
    task1 >> task2 >> task3

