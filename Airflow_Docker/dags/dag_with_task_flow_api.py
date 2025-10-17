from airflow.decorators import task, dag
from datetime import datetime, timedelta

default_args = {
    'owner': 'rushil',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    default_args=default_args,
    dag_id="our_first_dag_with_task_flow_api_v2",
    description="This is our first DAG with Task Flow API",
    start_date=datetime(2023, 1, 1, 2),
    schedule='@daily',
    catchup=False
)
def hello_world_etl():
    
    @task(multiple_outputs=True)
    def getName():
        return {
            'first_name': 'Rushil',
            'last_name': 'Shah'
        }

    @task()
    def getAge():
        age = 21
        return age
    
    @task() 
    def greet(firstname, lastname, age):
        print(f"Hello {firstname} {lastname}, you are {age} years old.")

    name_dict = getName()
    age = getAge()
    greet(firstname=name_dict['first_name'], lastname=name_dict['last_name'], age=age)

greet_dag = hello_world_etl()