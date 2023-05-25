# LIBRARY IMPORT
from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes

# MODULE USER DEFINE
import SQL.Sql_res_connect as sqlres
import SQL.Sql_req_connect as sqlreq
from Varialble.Var_res_define import Stt,TufID,Origin,DeclareMass,RealMass,Error,Destination,Typep,DateSent,Datehandle,Status,getIf
from Varialble.Var_req_define import Sttsr,TufIDsr,Originsr,DeclareMasssr,RealMasssr,Errorsr,Destinationsr,Typepsr,DateSentsr,Datehandlesr,Statussr,getIfsr
import Camera_reader.Camera as Camera
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

CheckQR = ''
while True:
    Data_camera = Camera.Camera_read()
    temp = sqlres.sql(IDget)
    for x in range(len(temp)-1):
        temp[x] = str(temp[x])
    [varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus]=temp
    
    tempsr = sqlreq.sqlsr(IDgetsr)
    for x in range(len(tempsr)-1):
        tempsr[x] = str(tempsr[x]) 
    [varSTTsr,varIDsr,varOriginsr,varDeclareMasssr,varRealMasssr,varErrorsr,varDestinationsr,varTypesr,varDateSentsr,varDatehandlesr,varStatussr]=tempsr
    
    
    if CheckQR !=  Data_camera:
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
        checkcondition = Data_camera
    # Home condition 
    if vargetIf != 0 :
        IDget = str(vargetIf)
        
    # Search condition 
    if vargetIfsr != 0 :
        IDgetsr= str(vargetIfsr)

    # print(varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus)
    time.sleep(0.2)
    
Camera.cv2.destroyAllWindows()