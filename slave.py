# Command list --> 
#view_cwd - will show all files in the directory where the files are running



import os
import socket

s = socket.socket()
port = 9999
host = input("Please enter Address ")
s.connect((host,port))
print()
print("Connected Successfully")


# Connections k aage ka maal

while 1:
    command = s.recv(1024)
    command = command.decode()
    if command=="view_cmd":
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())
        print("command has been executed")


