#!/usr/bin/env python
# coding: utf-8

import socket
 
server="127.0.0.1"
PORT=5000

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((server,PORT))

while True:
    data,addr=sock.recvfrom(5) #ligne decodage de la trame
    print data
    data.close()
