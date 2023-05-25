from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from opcua import Server
from opcua import ua
from random import randint
import time


server = Server()
url = "opc.tcp://localhost:4845"
server.set_endpoint(url)

name = "Rocket_Systems_OPCUA_Simulation_Server"
add_space = server.register_namespace(name)
server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")

U = param.add_variable(add_space, "U", 0)
I = param.add_variable(add_space, "I", 0)
Duty = param.add_variable(add_space, "Duty", 0)
N = param.add_variable(add_space, "N", 0)
Up = param.add_variable(add_space, "Up", 0)
Down = param.add_variable(add_space, "Down", 0)
U.set_writable()
I.set_writable()
Duty.set_writable()
N.set_writable()
Up.set_writable()
Down.set_writable()
plt.ylim(0, 270)
server.start()
print("Server started at {}".format(url))
Conditionold = 0
# files = open('Data1.txt', 'a')
# files.close()   
Mass = 670
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
while True:
    files = open('Data2.txt', 'a')
    U_get = U.get_value()
    I_get = I.get_value()
    Duty_get = Duty.get_value()
    N_get = N.get_value()
    Up_get = Up.get_value()
    Down_get = Down.get_value()
    condition = (U_get!=U_old)or(Up_get!=Up_old)or(Down_get!=Down_old)or(N_get!=N_old)or(I_get!=I_old)or(Duty_get!=Duty_old)
    if(((Up_get!=0)or(Down_get!=0))and(N_get!=0)):
        # print("Setpoint: ", Setpointget," || Data: ", Dataget)
        # now = datetime.now()
        # now2 = now.timestamp()
        files.write(str(U_get)+","+str(I_get)+","+str(N_get)+","+str(Duty_get)+","+str(Up_get)+","+str(Down_get)+","+str(Mass)+"\n")
        # plt.scatter(now2, Setpointget,s=4,color='r', label='Setpoint')
        # plt.scatter(now2, Dataget,s=4,color='g', label='Setpoint')
        # plt.pause(0.05)
        U_old = U_get
        I_old = I_get
        N_old = N_get
        Duty_old = Duty_get
        Up_old = Up_get
        Down_old = Down_get
        time.sleep(0.5)
    files.close()    








