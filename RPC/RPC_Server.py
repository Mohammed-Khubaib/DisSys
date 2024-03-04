from xmlrpc.server import SimpleXMLRPCServer

def welcome_msg():
  return 'Welcome to the Hello world RPC program \nyou can get the addition of two numbers here'

def add(num1,num2):
  return num1+num2

server = SimpleXMLRPCServer(("localhost",8050)) 
server.register_function(add,'add')
server.register_function(welcome_msg,'welcome_msg')
server.serve_forever()