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
    select = "select * from dboData where ID = " + IDss
    cus = cursor.execute(select)
    print(cus(0))
    for row in cus:
        print(str(row)) 
    conx.close() 
    return row

def sqlsr():
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
url = "opc.tcp://localhost:4841"
server.set_endpoint(url)
name = "Serverwrite"

add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

Datasent = param.add_variable(add_space, "Datasent", 0)
getIf = param.add_variable(add_space, "IDfromClient", 0)

Datasent.set_writable()
getIf.set_writable()

server.start()
print("Server started at {}".format(url))

# Khai bao bien khoi dau
Senddata = "(300.0, 'UNKNOWN', 'UNKNOWN', 0.0, '0', '0', 'UNKNOWN', 'UNKNOWN', datetime.date(1111, 1, 1), datetime.date(1111, 1, 1), 'UNKNOWN')"
vargetIf = "VGTF6745"
IDget = "UNKNOWN"


while True:

    temp = sql()

    #Xu ly chuoi
    
        
    a = 1
    if a == 1 :
        Datasent.set_value(Senddata)
        vargetIf = getIf.get_value()
        a = 0
    if vargetIf != 0 :
        IDget = str(vargetIf)

    time.sleep(1)