from fastapi import FastAPI, File, UploadFile
from app import gif_creat

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    with open(file.filename, 'r') as f:
        return f.read()


@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile]):
    directory = []
    for i in files:
        directory.append(i.filename)

    gif_name = gif_creat(directory)
    return gif_name

'''
@app.get("/file/download")
def download_file():
    return FileResponse(path='data.json', filename='list.json')
'''


