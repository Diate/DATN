from opcua import Server,ua, uamethod
import ctypes
from Rount.OPC_connect import param
from Rount.OPC_connect import add_space

Sttsr = param.add_variable(add_space, "STTsr", 0)
TufIDsr = param.add_variable(add_space, "IDsr", 0)
Originsr = param.add_variable(add_space, "Originsr", 0)
DeclareMasssr = param.add_variable(add_space, "DeclareMasssr", 0)
RealMasssr = param.add_variable(add_space, "RealMasssr", 0)
Errorsr = param.add_variable(add_space, "Errorsr", 0)
Destinationsr = param.add_variable(add_space, "Destinationsr", 0)
Typepsr = param.add_variable(add_space, "Typesr", 0)
DateSentsr = param.add_variable(add_space, "DateSentsr", 0)
Datehandlesr = param.add_variable(add_space, "Datehandlesr", 0)
Statussr = param.add_variable(add_space, "Statussr", 0)
getIfsr = param.add_variable(add_space, "IDfromClientsr", 0)

Sttsr.set_writable()
TufIDsr.set_writable()
Originsr.set_writable()
DeclareMasssr.set_writable()
RealMasssr.set_writable()
Errorsr.set_writable()
Destinationsr.set_writable()
Typepsr.set_writable()
DateSentsr.set_writable()
Datehandlesr.set_writable()
Statussr.set_writable()
getIfsr.set_writable()

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
