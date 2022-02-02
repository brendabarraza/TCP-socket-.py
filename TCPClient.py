from email import message
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#YOUR_IP = complete datos
host = 'YOUR_IP'
host = socket.gethostbyname()

port =444

#YOUR_IP = complete datos
clientsocket.connect(('YOUR_IP', port))
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
