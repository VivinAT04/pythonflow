from pythonflow import task, DAG
import time


@task
def extract():
    print("Extracting...")
    time.sleep(2)


@task
def clean():
    print("Cleaning...")
    time.sleep(5)


@task
def validate():
    print("Validating...")
    time.sleep(5)


@task
def report():
    print("Generating report...")


extract >> clean
extract >> validate

clean >> report
validate >> report

dag = DAG("parallel_dag")

dag.add_tasks(
    extract,
    clean,
    validate,
    report
)

dag.run()
