import runpy

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pythonflow.storage import Storage

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/")
def dashboard(request: Request):
    storage = Storage()
    rows = storage.get_history()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "rows": rows,
            "graph_path": "/static/dag_graph.png"
        }
    )


@app.get("/api/runs")
def get_runs():
    storage = Storage()
    rows = storage.get_history()

    return {
        "runs": [
            {
                "dag_name": row[0],
                "task_name": row[1],
                "state": row[2],
                "attempt": row[3],
                "error": row[4],
                "created_at": row[5]
            }
            for row in rows
        ]
    }


@app.get("/api/runs/latest")
def get_latest_run():
    storage = Storage()
    rows = storage.get_history()

    if not rows:
        return {
            "latest": None
        }

    row = rows[0]

    return {
        "latest": {
            "dag_name": row[0],
            "task_name": row[1],
            "state": row[2],
            "attempt": row[3],
            "error": row[4],
            "created_at": row[5]
        }
    }


@app.post("/api/run-dag")
def run_dag():
    runpy.run_path(
        "examples/parallel_dag.py",
        run_name="__main__"
    )

    return {
        "message": "DAG executed successfully",
        "dag_file": "examples/parallel_dag.py"
    }
