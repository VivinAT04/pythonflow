from concurrent.futures import ThreadPoolExecutor

from pythonflow.executor import Executor


class ParallelExecutor:

    @staticmethod
    def execute(tasks, dag_name):

        with ThreadPoolExecutor(
            max_workers=4
        ) as pool:

            futures = []

            for task in tasks:

                futures.append(
                    pool.submit(
                        Executor.run,
                        task
                    )
                )

            for future in futures:
                future.result()
