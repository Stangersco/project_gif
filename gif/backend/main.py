from fastapi import FastAPI, File, UploadFile
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




