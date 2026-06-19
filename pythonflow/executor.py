from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError


class Executor:

    @staticmethod
    def run(task):

        print(f"[RUNNING] {task.name}")

        with ThreadPoolExecutor(max_workers=1) as pool:

            future = pool.submit(
                task.func
            )

            try:
                future.result(
                    timeout=task.timeout
                )

                print(
                    f"[SUCCESS] {task.name}"
                )

                return True

            except TimeoutError:

                print(
                    f"[TIMEOUT] {task.name} exceeded {task.timeout}s"
                )

                return False
