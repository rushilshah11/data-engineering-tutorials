from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'rushil',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="our_first_dag_version_5",
    default_args=default_args,
    description="This is our first DAG",
    start_date=datetime(2023, 1, 1, 2),
    schedule='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "Hello World, This is our first task"'
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo "I\'m the second task, and I will run after the first task"',
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo "I\'m the third task, and I will run after first task but at the same time as second task"',
    )

    # Take dependency method 1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # Take dependency method 2
    # task1 >> task2
    # task1 >> task3

    # Take dependency method 3
    task1 >> [task2, task3]

