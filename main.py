from fastapi import FastAPI
import uvicorn
#from Tree_code import Filedownload
from fastapi.responses import FileResponse
from fastapi import Header, status
from fastapi import APIRouter
from Tree_code import Db_connect
import cx_Oracle
import os
import re

conn = ""
cursor = ""
app = FastAPI()

#https://apidch.dev.nextgen.local/FILEDOWNLOADER/30248326-CDDCPE1AAZOR00006-ORIG-AAZOR
@app.get("/FILEDOWNLOADER/{File_id_info}", status_code=status.HTTP_201_CREATED)
def verify_item(File_id_info: str):
    splitline = File_id_info.split("-")
    Fileid = str(splitline[0])
    Filename = str(splitline[1])
    Filetype = str(splitline[2])
    Clientname = str(splitline[3])
    
    # Verify received data field Function --- currently not using pydantic class
    #validateData(Fileid,Filename,Filetype,Clientname)

    # call function to search file from fileinfo1_Arch_path
    returnfile = getFileFromArchive(Fileid,Filename,Filetype,Clientname)
       
    if str(returnfile)  == '0':
        
        return {
            "Error" : "File Not Found",
            "Filename" : Filename,
            "File ID" : Fileid
        }
    
    else:
               
        return FileResponse(returnfile, media_type='application/octet-stream',filename=Filename)
        
    #return returnfile
    #else:
     #   print("Incorrect file path")
    
    



def validateData(id,name,type,client): # WILL DO THIS CHANGES IN UPCOMING DAYS
    print(str(id))
    print(str(name))
    print(str(type))
    print(str(client))



def getFileFromArchive(id,name,type,client):
    
    try:
        con = db_connection()
        cursor = con.cursor()
        
        select_qry = """select nvl((select archived_path from fileinfo1_arch_path where fileid = :fi and file_type = :ft ),'NOT_FOUND') from dual""" # need to check this
        cursor.execute(select_qry, {"fi": id,"ft": type}) # in oracle pass dic in mysql and other pass tuple
        temp = cursor.fetchone()
        file_path = temp[0]
        if os.path.exists(file_path):
            return file_path
        else:
            print("File not found")
            print(file_path)
            return 0

        

    except cx_Oracle.DatabaseError as e:
        print("Problem connecting to Oracle", e)
        return {
            "status": "Failed to find request id "
        }


#def sendFile(returnfile):
 #   print(returnfile)
    #return FileResponse(returnfile, media_type='application/octet-stream',status_code=200)
    #return FileResponse("CDGBRCNAREDU63896.gz", media_type='application/octet-stream')
    #return FileResponse("deer.jpg", media_type='application/octet-stream')

def db_connection():
    db_arr = Db_connect.dbconfig()
    var1 = db_arr[0] #username
    var2 = db_arr[1] #password
    var3 = db_arr[2] #host
    var4 = db_arr[3] #port
    var5 = db_arr[4] #servicename
    print(var1,var2,var3,var4,var5)
    connection_line = var1 +'/'+ var2 +'@'+ var3 +'/'+var5
    print(db_arr)
    try:
        conn = cx_Oracle.connect(connection_line)
        return (conn)
    except cx_Oracle.DatabaseError as e:
        print("Problem connecting to Oracle", e)

def createcursor(conn):
    if conn:
        return conn.cursor()


def closeconnection(conn):
    if conn:
        conn.close()

def closecursor(cursor):
    if cursor:
        cursor.close()

uvicorn.run(app, port=8080,host = '0.0.0.0')

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
