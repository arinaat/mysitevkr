import base64
import json
import sys
from io import BytesIO

sys.path.append(r'C:\...\mysitevkr')
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from main import style_transfer
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

@app.get("/proba", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("tool1.html", {"request": request})

@app.post("/proba")
def form(request: Request, uploaded_file1: UploadFile, uploaded_file2: UploadFile):
    content_image = uploaded_file1.file.read()
    style_image = uploaded_file2.file.read()
    img2 = style_transfer(content_image, style_image)
    a = base64.b64encode((img2.file.read()).encode("utf-8"))  # bytes
    data = {a}
    return JSONResponse(data)
    # return Response(content=content_image, media_type="image/png")


if __name__ == '__api__':
    uvicorn.run(app, port=8080)