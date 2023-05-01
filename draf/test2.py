from pymodbus.constants import Endian
from pymobus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadBuilder
import socket
import time

hostname = socket.gethostname()
server_ip_address = socket.gethostbyname(hostname)
server_port = 502

client = ModbusTcpClient(server_ip_address,server_port)

print("[+]Info : Connection : "+ str(client.connect()))

for i in range(0,10):
    print("[+]Info : Writing Value : {V} On Register : {R}".format(V=i,R=i))
    client.write_registers(i,i)
    