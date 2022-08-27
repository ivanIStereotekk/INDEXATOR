
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi import FastAPI,Request


app = FastAPI(title="INDEXER APP", openapi_url="/openapi.json")



#Base path and templates

app.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")
HOME_DIR = Path.home()


# INDEXATOR
@app.get("/index", response_class=HTMLResponse)
async def indexer(request: Request):
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "home_dir":HOME_DIR})