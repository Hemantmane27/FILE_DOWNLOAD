from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from fastapi import Header, status
from fastapi import APIRouter
from Tree_code import Db_connect
import cx_Oracle

conn = ""
cursor = ""



app = FastAPI()
router = APIRouter()
#https://apidch.dev.nextgen.local/FILEDOWNLOADER/30248326-CDDCPE1AAZOR00006-ORIG-AAZOR
@router.get("/FILEDOWNLOADER/{File_id_info}", status_code=status.HTTP_201_CREATED)
def verify_item(File_id_info: str):
    splitline = File_id_info.split("-")
    Fileid = str(splitline[0])
    Filename = str(splitline[1])
    Filetype = str(splitline[2])
    Clientname = str(splitline[3])
    print("HEMANT ")
    # Verify received data field Function --- currently not using pydantic class
    validateData(Fileid,Filename,Filetype,Clientname)

    # call function to search file from fileinfo1_Arch_path
    returnfile = getFileFromArchive(Fileid,Filename,Filetype,Clientname)
    print(str(returnfile))
    # call function to send response as file 
    #sendFile(returnfile)
    # Create data set to support above program

    # find out how it will capture response for file not found



    return {"Message": "Item found", "Item": File_id_info,"ID": Fileid,"Name": Filename,"Type": Filetype,"Client": Clientname}

app.include_router(router)

def validateData(id,name,type,client):
    print(str(id))
    print(str(name))
    print(str(type))
    print(str(client))

def getFileFromArchive(id,name,type,client):
    print("Fileinfo1_arch_path")
    try:
        con = db_connection()
        cursor = con.cursor()
        select_qry = """select "12" from dual""" # need to check this
        cursor.execute(select_qry) # in oracle pass dic in mysql and other pass tuple
        temp = cursor.fetchone() # list
        request_id = temp[0]
        print("REQUEST ID")
        print(request_id)
        return request_id
    except cx_Oracle.DatabaseError as e:
        print("Problem connecting to Oracle", e)
        return {
            "status": "Failed to find request id"
        }


def sendFile(returnfile):
    print("response code")


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

