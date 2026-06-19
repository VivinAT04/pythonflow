import time
import runpy
from datetime import datetime

from croniter import croniter


def run_cron(
    cron_expression,
    dag_file
):
    base_time = datetime.now()

    iterator = croniter(
        cron_expression,
        base_time
    )

    next_run = iterator.get_next(datetime)

    print(
        f"Cron scheduler started for {dag_file}"
    )

    print(
        f"Next run at: {next_run}"
    )

    while True:

        now = datetime.now()

        if now >= next_run:

            print("\n--- Executing scheduled DAG ---")

            runpy.run_path(
                dag_file,
                run_name="__main__"
            )

            next_run = iterator.get_next(datetime)

            print(
                f"Next run at: {next_run}"
            )

        time.sleep(1)


if __name__ == "__main__":
    run_cron(
        cron_expression="*/1 * * * *",
        dag_file="examples/simple_dag.py"
    )
