from socket import *
from math import pi
import socket
import time
import datetime
import random
import string

serverPort = 9000
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Serveri eshte ne linje...")
while True:
    message, clientAddress = serverSocket.recvfrom(128)
    print("Mesazhi i pranuar: " + message.decode("ASCII"))
    mesazhi = message.decode("ASCII").split(' ')
