from pythonflow import task, DAG


counter = 0


@task
def extract():
    print("Extracting data")


@task(retries=3)
def clean():

    global counter

    counter += 1

    if counter < 2:
        raise Exception("Temporary failure")

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
