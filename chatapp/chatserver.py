#chatserver.py
import socket
import sys
import time


new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080


new_socket.bind((host_name,port))
print("Binding Successfull.....")
print("This is your IP Address",s_ip)


name = input("Enter your Nick Name: ")
new_socket.listen(1)

conn,add = new_socket.accept() 

print("Recieved Connection from ",add[0])
print("Connection Establish. Connected from:",add[0])

client = (conn.recv(1024)).decode()
print(client+" has connected.")
conn.send(name.encode())


while True:
	msg = input("Me: ")
	conn.send(msg.encode())
	msg = conn.recv(1024)
	msg = msg.decode()
	print(client," : ",msg)