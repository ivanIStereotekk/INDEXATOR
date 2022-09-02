
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette import status
from starlette.responses import Response
from starlette.templating import Jinja2Templates
from fastapi import FastAPI,Request



app = FastAPI(title="INDEXER APP", openapi_url="/openapi.json")


from pydantic import BaseModel


#Model
class PathToDirectory(BaseModel):
    path: str



#Base path and templates

app.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")
HOME_DIR = Path.home()


# INDEXATOR

@app.post("/json_path")
async def path_to_dir(path: PathToDirectory):
    path = Path()
    if path:
        return {'dataset':path.iterdir()}
    else:
        return {'response':"No data here"}

#Web_Interface
@app.get("/index", response_class=HTMLResponse)
async def indexer(request: Request):
    desktop = HOME_DIR/"Desktop"
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "home_dir":HOME_DIR,"_list": desktop.iterdir()})

#get_by_url
@app.get("/{folder}",)
async def list_files(folder:str):
    new_path = HOME_DIR/f"{folder}"
    print(new_path)
    return {"List of files - ":new_path.iterdir(),"You wanted a list a ":new_path}

#get in javascript -  XMLhttpRequest
@app.post("/path")
async def get_from_directory(path: str):
    my_path = Path(path)
    try:
        return {"dataset": my_path.iterdir()}
    except Exception:
        return {"Empty":"Empty list of nothing !"}

