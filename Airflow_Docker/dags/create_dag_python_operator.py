from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'rushil',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def print_hello_world(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    name = first_name + " " + last_name

    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"Hello {name}, you are {age} years old.")

def getName(ti):
    ti.xcom_push(key='first_name', value='Rushil')
    ti.xcom_push(key='last_name', value='Shah')

def getAge(ti):
    ti.xcom_push(key='age', value=21)

with DAG(
    default_args=default_args,
    dag_id="our_first_dag_with_python_operator_v5",
    description="This is our first DAG with PythonOperator",
    start_date=datetime(2023, 1, 1, 2),
    schedule='@daily',
    catchup=False
) as dag:
    
    task1 = PythonOperator(
        task_id='greet',
        python_callable=print_hello_world,
    )

    task2 = PythonOperator(
        task_id='get_name',
        python_callable=getName
    )

    task3 = PythonOperator(
        task_id='get_age',
        python_callable=getAge
    )

    [task2, task3] >> task1
    