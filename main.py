from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/deer")
def deer():
    return FileResponse("deer.jpg", media_type='application/octet-stream')


@app.get("/csv")
def csv():
    return FileResponse("UK.csv", media_type='application/octet-stream')

@app.get("/binary")
def binary():
    return FileResponse("CDISLNOGBRVF08966.GO", media_type='application/octet-stream')






#def config():
    #pass
    #api.include_router(home.router)
#   api.include_router(segmentation_main.router)


#if __name__ == '__main__':
#    config()

uvicorn.run(app, port=8080,host = '0.0.0.0')

