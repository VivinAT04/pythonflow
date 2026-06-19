from .executor import Executor


class DAG:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_tasks(self, *tasks):
        self.tasks.extend(tasks)

    def run(self):

        executed = set()

        while len(executed) < len(self.tasks):

            for task in self.tasks:

                if task in executed:
                    continue

                ready = all(
                    parent in executed
                    for parent in task.upstream
                )

                if ready:

                    Executor.execute(task)

                    executed.add(task)
