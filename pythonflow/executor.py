from .task import TaskState


class Executor:

    @staticmethod
    def execute(task):

        attempts = 0

        while attempts <= task.retries:

            try:
                task.state = TaskState.RUNNING

                print(f"[RUNNING] {task.name}")

                task()

                task.state = TaskState.SUCCESS

                print(f"[SUCCESS] {task.name}")

                return

            except Exception as e:

                attempts += 1

                task.state = TaskState.FAILED

                print(f"[FAILED] {task.name}: {e}")

                if attempts <= task.retries:
                    print(
                        f"[RETRY {attempts}/{task.retries}] "
                        f"{task.name}"
                    )

        raise RuntimeError(
            f"{task.name} failed after retries"
        )
