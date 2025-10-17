from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'rushil',
    'retry': 5,
    'retry_delay': timedelta(minutes=5),
}

def get_sklearn():
    import sklearn
    print("scikit-learn version:", sklearn.__version__)

with DAG(
    dag_id='my_dag', 
    default_args=default_args, 
    schedule='@daily',
    start_date=datetime(2025, 10, 1),
) as dag:
    get_sklearn_task = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )
    get_sklearn_task