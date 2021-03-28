import socket
import os
import subprocess

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def options(command):
    # file and directory listing
    msg = "Command output:\n"
    msg += subprocess.check_output(command, shell=True, universal_newlines=True)
    print(msg)
    return msg

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            msg = data.decode()
            output = options(msg)
            if(msg == "exit"):
                break  
            conn.sendall(str.encode(output))

