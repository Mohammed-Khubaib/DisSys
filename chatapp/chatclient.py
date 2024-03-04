#chatclient.py
import socket
import sys
import time


socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print("This is your IP Address: ",ip)
server_host = input("Enter your friends IP Address: ")
name = input("Enter your Nick Name :")

socket_server.connect((server_host,sport))


socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()



print(server_name," has Joined....")
while True:
	msg = (socket_server.recv(1024)).decode()
	print(server_name + " : ",msg)
	msg = input("Me : ")
	socket_server.send(msg.encode())
