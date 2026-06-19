from pythonflow import task


def test_task_decorator_sets_name():
    @task
    def sample_task():
        return "ok"

    assert sample_task.name == "sample_task"


def test_task_dependency_chain():
    @task
    def first():
        pass

    @task
    def second():
        pass

    first >> second

    assert second in first.downstream
    assert first in second.upstream
