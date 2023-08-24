from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from app import gif_creat


app = FastAPI()


@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile]):

    directory = []

    for i in files:
        directory.append(i.filename)

    gif_name = gif_creat(directory)

    return gif_name


@app.post('/login/{a}')
async def login(a):
    return


@app.get("/status")
async def get_status():
    return



"""
@app.get("/file/download")
def download_file():
    return FileResponse(path='gif_save/gif_19_08_2023_14_49_03.gif', filename='list.json')
"""


