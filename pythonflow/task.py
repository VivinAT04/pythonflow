class TaskState:
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Task:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

        self.upstream = []
        self.downstream = []

        self.state = TaskState.PENDING
        self.retries = 3

    def __call__(self):
        return self.func()

    def __rshift__(self, other):
        self.downstream.append(other)
        other.upstream.append(self)
        return other


def task(func):
    return Task(func)
