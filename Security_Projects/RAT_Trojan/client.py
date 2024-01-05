import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(True):
        msg = input("Your command: ")
        if msg != "":   # handling empty inputs which would interrupt the connection.
            s.sendall(str.encode(msg))
            if(msg == "exit"):
                break
            data = s.recv(2048)
            if data:
                print('Received:\n', data.decode())
            else:
                continue
        else:
            print("Please enter a command... \n")