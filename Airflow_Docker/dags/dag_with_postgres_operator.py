from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    'owner': 'rushil',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}



with DAG(
    dag_id='postgres_example_dag_v3',
    default_args=default_args,
    start_date=datetime(2025, 10, 1),
    schedule="0 0 * * *",
) as dag:
    task1 = SQLExecuteQueryOperator(
        task_id='create_table',
        conn_id='postgres_localhost',
        sql="""
            CREATE TABLE IF NOT EXISTS dag_runs (
                dt date,
                dag_id character varying(250),
                primary key (dt, dag_id)
            )
        """
    )

    task2 = SQLExecuteQueryOperator(
        task_id='insert_dag_run',
        conn_id='postgres_localhost',
        sql="""
            INSERT INTO dag_runs (dt, dag_id) VALUES ('{{ ds }}', '{{ dag.dag_id }}')
            ON CONFLICT (dt, dag_id) DO NOTHING
        """
    )

    task3 = SQLExecuteQueryOperator(
        task_id='delete_data_from_table_dag_run',
        conn_id='postgres_localhost',
        sql="""
            DELETE FROM dag_runs WHERE dt = '{{ ds }}' AND dag_id = '{{ dag.dag_id }}'
        """
    )

    task1 >> task3 >> task2