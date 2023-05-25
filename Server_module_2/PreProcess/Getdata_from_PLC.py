from opcua import Server,ua, uamethod
import ctypes
from Rount.OPC_connect import param_getInfo
from Rount.OPC_connect import add_space
import time
U = param_getInfo.add_variable(add_space, "U", 0)
I = param_getInfo.add_variable(add_space, "I", 0)
Duty = param_getInfo.add_variable(add_space, "Duty", 0)
N = param_getInfo.add_variable(add_space, "N", 0)
Up = param_getInfo.add_variable(add_space, "Up", 0)
Down = param_getInfo.add_variable(add_space, "Down", 0)
U.set_writable()
I.set_writable()
Duty.set_writable()
N.set_writable()
Up.set_writable()
Down.set_writable()
def Preprocess():
    count = 0
    open('Data.txt', 'w').close()
    while (count<=10):
        files = open('Data.txt', 'a')
        U_get = U.get_value()
        I_get = I.get_value()
        Duty_get = Duty.get_value()
        N_get = N.get_value()
        Up_get = Up.get_value()
        Down_get = Down.get_value()
        # condition = (U_get!=U_old)or(Up_get!=Up_old)or(Down_get!=Down_old)or(N_get!=N_old)or(I_get!=I_old)or(Duty_get!=Duty_old)
        if(((Up_get!=0)or(Down_get!=0))and(N_get!=0)):
            files.write(str(U_get)+","+str(I_get)+","+str(N_get)+","+str(Duty_get)+","+str(Up_get)+","+str(Down_get)+","+"\n")
            U_old = U_get
            I_old = I_get
            N_old = N_get
            Duty_old = Duty_get
            Up_old = Up_get
            Down_old = Down_get
            count = count + 1
            time.sleep(0.2)
        files.close()  
    return 1