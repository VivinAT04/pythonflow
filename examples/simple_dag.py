from pythonflow import task, DAG


@task
def extract():
    print("Extracting data")


@task
def clean():
    print("Cleaning data")


@task
def report():
    print("Generating report")


extract >> clean >> report

dag = DAG("sample")

dag.add_tasks(
    extract,
    clean,
    report
)

dag.run()
