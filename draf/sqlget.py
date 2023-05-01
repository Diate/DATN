from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes

def sql():
    conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    IDss =str(IDget)
    IDss = "'" + IDss + "'"
    cursor = conx.cursor()
    select = "select * from dboData where ID = " + IDss + " AND Status = 'Done'"
    cus = cursor.execute(select)
    
    for row in cus:
        print(str(row)) 
    conx.close()

    return row


server = Server()
url = "opc.tcp://localhost:4842"
server.set_endpoint(url)
name = "Serversearch"

add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")


Stt = param.add_variable(add_space, "STTsr", 0)
TufID = param.add_variable(add_space, "IDsr", 0)
Origin = param.add_variable(add_space, "Originsr", 0)
DeclareMass = param.add_variable(add_space, "DeclareMasssr", 0)
RealMass = param.add_variable(add_space, "RealMasssr", 0)
Error = param.add_variable(add_space, "Errorsr", 0)
Destination = param.add_variable(add_space, "Destinationsr", 0)
Typep = param.add_variable(add_space, "Typesr", 0)
DateSent = param.add_variable(add_space, "DateSentsr", 0)
Datehandle = param.add_variable(add_space, "Datehandlesr", 0)
Status = param.add_variable(add_space, "Statussr", 0)
getIf = param.add_variable(add_space, "IDfromClientsr", 0)


Stt.set_writable()
TufID.set_writable()
Origin.set_writable()
DeclareMass.set_writable()
RealMass.set_writable()
Error.set_writable()
Destination.set_writable()
Typep.set_writable()
DateSent.set_writable()
Datehandle.set_writable()
Status.set_writable()
getIf.set_writable()

server.start()
print("Server started at {}".format(url))

# Khai bao bien khoi dau
IDget = "UNKNOWN"
oldID = "None"
varSTT = 0
varID = "Unknown"
varOrigin = "Unknown"
varDeclareMass = 0
varRealMass = 0
varError = 0
varDestination = "Unknown"
varType = "Unknown"
varDateSent = "**/**/****"
varDatehandle = "**/**/****"
varStatus = "Unknown"
vargetIf = "BSOU3208"


while True:

    temp = sql()
    
    for x in range(len(temp)-1):
        temp[x] = str(temp[x])
    #Xu ly chuoi
    
    [varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus]=temp
    
    a = 1
    if a ==1 :
        Stt.set_value(varSTT)
        TufID.set_value(varID)
        Origin.set_value(varOrigin)
        DeclareMass.set_value(varDeclareMass)
        RealMass.set_value(varRealMass)
        Error.set_value(varError)
        Destination.set_value(varDestination)
        Typep.set_value(varType)
        DateSent.set_value(varDateSent)
        Datehandle.set_value(varDatehandle)
        Status.set_value(varStatus)
        vargetIf = getIf.get_value()
        a = 0
        
    if vargetIf != 0 :
        IDget = str(vargetIf)

    # print(varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus)
    time.sleep(1)