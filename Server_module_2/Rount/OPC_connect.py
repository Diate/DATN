from opcua import Server,ua, uamethod
import ctypes

server = Server()
url = "opc.tcp://localhost:4842"
server.set_endpoint(url)
name = "Serversearch"

add_space = server.register_namespace(name)

node = server.get_objects_node()
param = node.add_object(add_space, "Parameters")
param_getInfo = node.add_object(add_space, "Parameters_getInfo")

server.start()
print("Server started at {}".format(url))

