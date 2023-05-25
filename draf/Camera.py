import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import urllib.request
#cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

url='http://192.168.43.222/'
cv2.namedWindow("Live transmission", cv2.WINDOW_AUTOSIZE)
Data = ''
prev=""
pres=""
while True:
    img_resp=urllib.request.urlopen(url+'cam-hi.jpg')
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
            prev=pres
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
 
    cv2.imshow("Live transmission", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cv2.destroyAllWindows()