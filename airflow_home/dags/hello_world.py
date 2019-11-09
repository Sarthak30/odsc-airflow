from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def hello():
    print "Hello World"

dag = DAG('hello_world', description='Simple tutorial for DAG', schedule_interval='0 12 * * *',
        start_date=datetime(2019, 11, 8), catchup=False)

dummy_operator = DummyOperator(task_id="dummy", retries=3, dag=dag)

hello_operator = PythonOperator(task_id="hello_operator", python_callable=hello, dag=dag)

dummy_operator >> hello_operator
