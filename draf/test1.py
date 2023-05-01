from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
import socket
hostname = socket.gethostname()
server_ip_address = socket.gethostbyname(hostname)
server_port = 502
print(server_ip_address)

store = ModbusSlaveContext(zero_mode = True)
context = ModbusServerContext(slaves = store, single=True)
print("[+]Info : Server Started on IP : {I} and PORT : {P}".format(I=server_ip_address,P=server_port))
StartTcpServer(address=(server_ip_address,server_port))
