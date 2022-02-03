import socket

s = socket.socket()

ip = input("plese enter the ip: ")
port = str(input("plese enter the port: "))

s.connect((ip, int(port)))

print(s.recv(1024))
