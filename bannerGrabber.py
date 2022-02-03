import socket

def banner(ip, port)
    s = socket.socket()
    s.connect((ip, int(port)))
    print(str(s.recv(1024)).strip('b'))

def main():
    ip = input("please enter the ip: ")
    port = str(input("please enter the port: "))
    banner(ip, port)

main()
