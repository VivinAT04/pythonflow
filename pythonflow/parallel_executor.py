from concurrent.futures import ThreadPoolExecutor

from pythonflow.executor import Executor


class ParallelExecutor:

    @staticmethod
    def execute(tasks, dag_name):

        with ThreadPoolExecutor(
            max_workers=len(tasks)
        ) as pool:

            futures = [
                pool.submit(
                    Executor.run,
                    task
                )
                for task in tasks
            ]

            for future in futures:
                future.result()
