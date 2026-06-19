from pythonflow import task, DAG


def test_dag_executes_tasks_in_order():
    result = []

    @task
    def first():
        result.append("first")

    @task
    def second():
        result.append("second")

    first >> second

    dag = DAG("test_dag")
    dag.add_tasks(first, second)
    dag.run()

    assert result == ["first", "second"]
