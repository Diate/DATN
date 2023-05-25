# LIBRARY IMPORT
from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes
#--------LIB CAMERA IMPORT----------
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
#-------LID CAMERA END IMPORT-------
#-------LID XLDL BEGIN IMPORT-------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import keras
#-------LID XLDL END IMPORT---------

#CAMERA INIT BEGIN----------------------------------------------------
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
urlcamera='http://192.168.43.222/'
cv2.namedWindow("Live transmission", cv2.WINDOW_AUTOSIZE)
prev=""
pres=""
#CAMERA INIT END----------------------------------------------------

# MODULE USER DEFINE BEGIN -----------------------------------------
import SQL.Sql_res_connect as sqlres
import SQL.Sql_req_connect as sqlreq
from Varialble.Var_res_define import Stt,TufID,Origin,DeclareMass,RealMass,Error,Destination,Typep,DateSent,Datehandle,Status,getIf
from Varialble.Var_req_define import Sttsr,TufIDsr,Originsr,DeclareMasssr,RealMasssr,Errorsr,Destinationsr,Typepsr,DateSentsr,Datehandlesr,Statussr,getIfsr
from PreProcess.Getdata_from_PLC import I,U,Duty,N,Up,Down
import PreProcess.Getdata_from_PLC as fn
# MODULE USER DEFINE END -----------------------------------------

# Var define Infinity BEGIN ----------------------------------------
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
count = 0
#INFINITY DEFINE DATA_get_BEGIN------------------------------------------
U_old = 0
I_old = 0
N_old = 0
Duty_old = 0
Up_old = 0
Down_old = 0
U_get = 0
I_get = 0
Duty_get = 0
N_get = 0
Up_get = 0
Down_get = 0
#INFINITY DEFINE DATA_get_END------------------------------------------

# Var define Infinity END ----------------------------------------


while True:
    #CAMERA BEGIN----------------------------------------------------------------
    img_resp=urllib.request.urlopen(urlcamera+'cam-hi.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
    #_, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres=obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            Data = str(obj.data).split('\'')[1]
            print("Data: ",Data)

            # SERVER ORIGIN BEGIN---------------------
            
            # SQL READER BEGIN -----------------------------------------------------
            # Move Data from QR_Camera to ID get 
            IDget = Data
            
            temp = sqlres.sql(IDget)
            for x in range(len(temp)-1):
                temp[x] = str(temp[x])
            [varSTT,varID,varOrigin,varDeclareMass,varRealMass,varError,varDestination,varType,varDateSent,varDatehandle,varStatus]=temp

            # flag = fn.Preprocess()
            # df = pd.read_csv("Datamerge.csv",sep=";")
            # SQL READER END-----------------------------------------------------

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
            # vargetIf = getIf.get_value()    

            # time.sleep(0.2)
    
            # SERVER ORIGIN END---------------------
            
            prev=pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("Live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    #CAMERA END----------------------------------------------------------------
                
    tempsr = sqlreq.sqlsr(IDgetsr)
    for x in range(len(tempsr)-1):
        tempsr[x] = str(tempsr[x]) 
    [varSTTsr,varIDsr,varOriginsr,varDeclareMasssr,varRealMasssr,varErrorsr,varDestinationsr,varTypesr,varDateSentsr,varDatehandlesr,varStatussr]=tempsr
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

    # if vargetIf != 0 :
        # IDget = str(vargetIf)
        
    # Search condition 
    if vargetIfsr != 0 :
        IDgetsr= str(vargetIfsr)
    time.sleep(0.2)
    
cv2.destroyAllWindows()