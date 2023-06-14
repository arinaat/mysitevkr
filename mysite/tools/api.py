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
app = FastAPI()



templates = Jinja2Templates(directory="templates")



@app.get("/proba", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("tool1.html", {"request": request})


@app.post("/proba", response_class=HTMLResponse)
def form(request: Request, uploaded_file1: UploadFile = File(...), uploaded_file2: UploadFile = File(...)):
    # print('encode')
    # print(uploaded_file1.file.read())
    # print('decode')
    # print(base64.b64decode(uploaded_file1.file.read()))
    a = uploaded_file1.filename
    b = uploaded_file2.filename
    print(a)
    # b = uploaded_file2.file.read().decode("iso-8859-1").encode("utf-8")
    # a = (base64.b64decode(uploaded_file1.file.read())).decode('utf-8')
    # b = (base64.b64decode(uploaded_file2.file.read())).decode('utf-8')
    # a = uploaded_file1.file.read().decode('base64')
    # b = uploaded_file2.file.read().decode('base64')
    img = style_transfer(a, b)

    return Response(content=img, media_type="image/png")


if __name__ == '__api__':
    uvicorn.run(app, port=8080)