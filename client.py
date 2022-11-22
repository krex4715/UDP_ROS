

import socket

client = '192.168.50.96'

port = 2001


clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.sendto('Hello!!!'.encode(), (client, port))