from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request

 # Config Server
server = Server()
url = "opc.tcp://localhost:4841"
server.set_endpoint(url)
name = "Servertest"

#Config Camera
font = cv2.FONT_HERSHEY_PLAIN
 
urlCa='http://192.168.1.133/'
cv2.namedWindow("Live transmission", cv2.WINDOW_AUTOSIZE)
prev=""
pres=""

server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

temp = param.add_variable(add_space, "Temperature", 0, ua.VariantType.String)
nameID = param.add_variable(add_space, "Name", 0)
dataget = param.add_variable(add_space, "Dataget", 0)

temp.set_writable()
nameID.set_writable()
dataget.set_writable()
server.start()
print("Server started at {}".format(url))

# Khai bao bien khoi dau
name = 2
oldname = 0
temperature = "0"
Data = "ss"
while True:

    img_resp=urllib.request.urlopen(urlCa+'cam-hi.jpg')
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)
 
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        pres = obj.data
        if prev == pres:
            pass
        else:
            print("Type:",obj.type)
            print("Data: ",obj.data)
            Data = obj.data
            prev=pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("Live transmission", frame)
    
    temp.set_value(temperature)
    name = nameID.get_value()
    temperature = str(Data)
    time.sleep(0.1)
    print(temperature)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()