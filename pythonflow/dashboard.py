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
