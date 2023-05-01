from opcua import Server,ua, uamethod
from random import randint
import pyodbc
import time
import ctypes

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
    temp.set_value(temppa)
    name = nameID.get_value() 
    temppa = sql(nameget)
    time.sleep(2)