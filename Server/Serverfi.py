from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes


def sql():
    conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    IDss = str(IDget)
    IDss = "'" + IDss + "'"
    cursor = conx.cursor()
    select = "select * from dboData where ID = " + IDss
    cus = cursor.execute(select)
    for row in cus:
        print(str(row)) 
    conx.close() 
    return row

def sqlsr():
    conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    IDss = str(IDgetsr)
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

# Set variable for Hometab

Stt = param.add_variable(add_space, "STT", 0)
TufID = param.add_variable(add_space, "ID", 0)
Origin = param.add_variable(add_space, "Origin", 0)
DeclareMass = param.add_variable(add_space, "DeclareMass", 0)
RealMass = param.add_variable(add_space, "RealMass", 0)
Error = param.add_variable(add_space, "Error", 0)
Destination = param.add_variable(add_space, "Destination", 0)
Typep = param.add_variable(add_space, "Type", 0)
DateSent = param.add_variable(add_space, "DateSent", 0)
Datehandle = param.add_variable(add_space, "Datehandle", 0)
Status = param.add_variable(add_space, "Status", 0)
getIf = param.add_variable(add_space, "IDfromClient", 0)

# Set variable for Search
Sttsr = param.add_variable(add_space, "STTsr", 0)
TufIDsr = param.add_variable(add_space, "IDsr", 0)
Originsr = param.add_variable(add_space, "Originsr", 0)
DeclareMasssr = param.add_variable(add_space, "DeclareMasssr", 0)
RealMasssr = param.add_variable(add_space, "RealMasssr", 0)
Errorsr = param.add_variable(add_space, "Errorsr", 0)
Destinationsr = param.add_variable(add_space, "Destinationsr", 0)
Typepsr = param.add_variable(add_space, "Typesr", 0)
DateSentsr = param.add_variable(add_space, "DateSentsr", 0)
Datehandlesr = param.add_variable(add_space, "Datehandlesr", 0)
Statussr = param.add_variable(add_space, "Statussr", 0)
getIfsr = param.add_variable(add_space, "IDfromClientsr", 0)

# Set variable for Qr

# Config Variable  
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
# ----------------------------------
Sttsr.set_writable()
TufIDsr.set_writable()
Originsr.set_writable()
DeclareMasssr.set_writable()
RealMasssr.set_writable()
Errorsr.set_writable()
Destinationsr.set_writable()
Typepsr.set_writable()
DateSentsr.set_writable()
Datehandlesr.set_writable()
Statussr.set_writable()
getIfsr.set_writable()
# ----------------------------------

server.start()
print("Server started at {}".format(url))

# Var define Infinity
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

IDgetsr = "UNKNOWNS"
oldIDsr = "None"
varSTTsr = 0
varIDsr = "Unknown"
varOriginsr = "Unknown"
varDeclareMasssr = 0
varRealMasssr = 0
varErrorsr = 0
varDestinationsr = "Unknown"
varTypesr = "Unknown"
varDateSentsr = "**/**/****"
varDatehandlesr = "**/**/****"
varStatussr = "Unknown"
vargetIfsr = "BSOU3208"


while True:

    temp = sql()
    for x in range(len(temp)-1):
        temp[x] = str(temp[x])
    [varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus]=temp
    
    tempsr = sqlsr()
    for x in range(len(tempsr)-1):
        tempsr[x] = str(tempsr[x]) 
    [varSTTsr,varIDsr,varOriginsr,varDeclareMasssr,varRealMasssr,varErrorsr,varDestinationsr,varTypesr,varDateSentsr,varDatehandlesr,varStatussr]=tempsr
    
    a = 1
    if a == 1 :
        # Hometab send-get data
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
        
        # Searchtab send-get data
        Sttsr.set_value(varSTTsr)
        TufIDsr.set_value(varIDsr)
        Originsr.set_value(varOriginsr)
        DeclareMasssr.set_value(varDeclareMasssr)
        RealMasssr.set_value(varRealMasssr)
        Errorsr.set_value(varErrorsr)
        Destinationsr.set_value(varDestinationsr)
        Typepsr.set_value(varTypesr)
        DateSentsr.set_value(varDateSentsr)
        Datehandlesr.set_value(varDatehandlesr)
        Statussr.set_value(varStatussr)
        vargetIfsr = getIfsr.get_value()
        a = 0
    # Home condition 
    if vargetIf != 0 :
        IDget = str(vargetIf)
        
    # Search condition 
    if vargetIfsr != 0 :
        IDgetsr= str(vargetIfsr)

    # print(varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus)
    time.sleep(1)