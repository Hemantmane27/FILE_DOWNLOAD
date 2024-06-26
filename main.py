from fastapi import FastAPI
import uvicorn
from Tree_code import Filedownload

app = FastAPI()

def config():
    app.include_router(Filedownload.router)
    

if __name__ == '__main__':
    config()

uvicorn.run(app, port=8081,host = '0.0.0.0')

#---------------------------- Ignore below part -------------------------------
#@app.get("/")
#def index():
 #   return {"Hello": "World"}

#@app.get("/deer")
#def deer():
  #  return FileResponse("deer.jpg", media_type='application/octet-stream')


#@app.get("/csv")
#def csv():
 #   return FileResponse("UK.csv", media_type='application/octet-stream')

##@app.get("/binary")
##def binary():
  #  return FileResponse("CDISLNOGBRVF08966.GO", media_type='application/octet-stream')
