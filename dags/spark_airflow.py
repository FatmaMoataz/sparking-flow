import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

dag = DAG(
    dag_id = "sparkingflow",
    default_args = {
        "owner" : "Fatma Moataz",
        "start_date" : airflow.utils.dates.days_ago(1)
    },
    schedule_interval = "@daily"
)

start = PythonOperator(
    task_id = "start",
    python_callable = lambda: print("Starting the DAG"),
    dag = dag
    )

python_job = SparkSubmitOperator(
    task_id = "python_job",
    application = "jobs/python/wordcountjob.py",
    conn_id = "spark-conn",
    dag = dag
)

end = PythonOperator(
    task_id = "end",
    python_callable = lambda: print("Ending the DAG"),
    dag = dag
    )

start >> python_job >> end