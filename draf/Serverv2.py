from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
#CAMERA ----------------------------------------------------
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
 
urlcamera='http://192.168.43.222/'
cv2.namedWindow("Live transmission", cv2.WINDOW_AUTOSIZE)
prev=""
pres=""
#CAMERA ----------------------------------------------------
def sql(name):
    conx = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    cursor = conx.cursor()
    select = "select * from dboData where ID = " + name
    cus = cursor.execute(select)
    
    for row in cus:
        print(str(row))
        # print(*cursor.execute(select))  
    conx.close()
    
    return row

def insertsql():
    conx2 = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-E2PGTAG\SQLEXPRESS2019; Database=SQLDB; UID=dh; PWD=31052001')
    cursor2 = conx2.cursor()
    insert = "insert into * from Datagraph value "


server = Server()
url = "opc.tcp://localhost:4841"
server.set_endpoint(url)
name = "Servertest"

# server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

temp = param.add_variable(add_space, "Data", 0, ua.VariantType.String)
nameID = param.add_variable(add_space, "Name", 0, ua.VariantType.String)

temp.set_writable()
nameID.set_writable()
server.start()
print("Server started at {}".format(url))

# Khai bao bien khoi dau
nameget = "'BSOU3208'"
temppa = "0"

while True:
    
    # print(Data)
    
    #CAMERA----------------------------------------------------------------
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
            temp.set_value(temppa)
            name = nameID.get_value() 
            temppa = sql(nameget)
            prev=pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("Live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    #CAMERA----------------------------------------------------------------
    time.sleep(0)
cv2.destroyAllWindows()