
from pathlib import Path

from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from fastapi import FastAPI,Request,Form


app = FastAPI(title="INDEXER APP", openapi_url="/openapi.json")

# from fastapi.middleware.cors import CORSMiddleware
#
#
# origins = [
#
#     "*",
#
#
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["127.0.0.1:8000/path",'http://localhost:8080','127.0.0.1'],
#     allow_credentials=False,
# )


#Base path and templates

app.mount("/static", StaticFiles(directory="static"), name="static")
TEMPLATES = Jinja2Templates(directory="templates")
HOME_DIR = Path.home()


# INDEXATOR
@app.get("/index", response_class=HTMLResponse)
async def indexer(request: Request):
    desktop = HOME_DIR/"Desktop"
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "home_dir":HOME_DIR,"_list": desktop.iterdir()})

@app.get("/{folder}",)
async def list_files(folder:str):
    new_path = HOME_DIR/f"{folder}"
    print(new_path)
    return {"List of files - ":new_path.iterdir(),"You wanted a list a ":new_path}

@app.post("/path")
@app.get("/path")
async def get_from_directory(path: str):
    my_path = Path(path)
    try:
        return {"Dataset": my_path.iterdir()}
    except Exception:
        return {"Empty":"Empty list of nothing !"}

