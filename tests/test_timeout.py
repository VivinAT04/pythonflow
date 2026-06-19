from pythonflow import task


def test_timeout_property():

    @task(timeout=5)
    def sample():
        pass

    assert sample.timeout == 5
