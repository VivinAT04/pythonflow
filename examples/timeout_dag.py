import time

from pythonflow import task
from pythonflow import DAG


@task(timeout=3)
def slow_task():

    print("Sleeping...")

    time.sleep(10)


dag = DAG("timeout_dag")

dag.add_tasks(
    slow_task
)

dag.run()
