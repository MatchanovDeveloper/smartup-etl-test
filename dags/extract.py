from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
# from products import products_etl

with DAG(
    dag_id="products_etl_pipeline",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False,
) as dag:

    run_script_p = BashOperator(
        task_id="products",
        bash_command="""
            cd /opt/airflow/dags/pipelines
            python products.py
        """,
    )

    run_script_c = BashOperator(
        task_id="customers",
        bash_command="""
            cd /opt/airflow/dags/pipelines
            python customers.py
        """,
    )

    run_script_o = BashOperator(
        task_id="orders",
        bash_command="""
            cd /opt/airflow/dags/pipelines
            python orders.py
        """,
    )

    run_script_p >> run_script_c >> run_script_o
