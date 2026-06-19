from .task import TaskState
from .storage import Storage


class Executor:

    @staticmethod
    def execute(task, dag_name="default"):

        storage = Storage()
        attempts = 0

        while attempts <= task.retries:

            try:
                task.state = TaskState.RUNNING

                print(f"[RUNNING] {task.name}")

                storage.record_task_run(
                    dag_name,
                    task.name,
                    task.state,
                    attempts
                )

                task()

                task.state = TaskState.SUCCESS

                print(f"[SUCCESS] {task.name}")

                storage.record_task_run(
                    dag_name,
                    task.name,
                    task.state,
                    attempts
                )

                return

            except Exception as e:

                attempts += 1
                task.state = TaskState.FAILED

                print(f"[FAILED] {task.name}: {e}")

                storage.record_task_run(
                    dag_name,
                    task.name,
                    task.state,
                    attempts,
                    str(e)
                )

                if attempts <= task.retries:
                    print(
                        f"[RETRY {attempts}/{task.retries}] "
                        f"{task.name}"
                    )

        raise RuntimeError(
            f"{task.name} failed after retries"
        )
