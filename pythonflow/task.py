class Task:

    def __init__(
        self,
        func,
        retries=0,
        timeout=None
    ):
        self.func = func
        self.name = func.__name__

        self.retries = retries
        self.timeout = timeout

        self.upstream = []
        self.downstream = []

    def __rshift__(self, other):
        self.downstream.append(other)
        other.upstream.append(self)
        return other


def task(func=None, retries=0, timeout=None):

    if func is not None and callable(func):
        return Task(
            func,
            retries=retries,
            timeout=timeout
        )

    def decorator(f):
        return Task(
            f,
            retries=retries,
            timeout=timeout
        )

    return decorator
