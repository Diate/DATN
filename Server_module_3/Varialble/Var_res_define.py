from opcua import Server,ua, uamethod
import ctypes
from Rount.OPC_connect import param_res
from Rount.OPC_connect import add_space

Stt = param_res.add_variable(add_space, "STT", 0)
TufID = param_res.add_variable(add_space, "ID", 0)
Origin = param_res.add_variable(add_space, "Origin", 0)
DeclareMass = param_res.add_variable(add_space, "DeclareMass", 0)
RealMass = param_res.add_variable(add_space, "RealMass", 0)
Error = param_res.add_variable(add_space, "Error", 0)
Destination = param_res.add_variable(add_space, "Destination", 0)
Typep = param_res.add_variable(add_space, "Type", 0)
DateSent = param_res.add_variable(add_space, "DateSent", 0)
Datehandle = param_res.add_variable(add_space, "Datehandle", 0)
Status = param_res.add_variable(add_space, "Status", 0)
getIf = param_res.add_variable(add_space, "IDfromClient", 0)

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