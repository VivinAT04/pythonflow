from .parallel_executor import ParallelExecutor


class DAG:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_tasks(self, *tasks):
        self.tasks.extend(tasks)

    def run(self):

        executed = set()

        while len(executed) < len(self.tasks):

            ready_tasks = []

            for task in self.tasks:

                if task in executed:
                    continue

                ready = all(
                    parent in executed
                    for parent in task.upstream
                )

                if ready:
                    ready_tasks.append(task)

            if not ready_tasks:
                raise RuntimeError(
                    "No executable tasks found. "
                    "Possible DAG cycle."
                )

            ParallelExecutor.execute(
                ready_tasks,
                self.name
            )

            for task in ready_tasks:
                executed.add(task)
