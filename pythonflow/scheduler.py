import time
import runpy


def run_every(interval_seconds, dag_file):

    print(
        f"Scheduler started. "
        f"Running {dag_file} every "
        f"{interval_seconds} seconds."
    )

    while True:

        print("\n--- Executing DAG ---")

        runpy.run_path(
            dag_file,
            run_name="__main__"
        )

        print(
            f"Sleeping for "
            f"{interval_seconds} seconds..."
        )

        time.sleep(interval_seconds)


if __name__ == "__main__":

    run_every(
        interval_seconds=30,
        dag_file="examples/simple_dag.py"
    )
