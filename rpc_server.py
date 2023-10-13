from xmlrpc.server import SimpleXMLRPCServer

def add(num1, num2):
    return num1 + num2

def findLen(s):
    return len(s)

server = SimpleXMLRPCServer(("localhost",5050))
server.register_function(add)
server.register_function(findLen)
server.serve_forever()
