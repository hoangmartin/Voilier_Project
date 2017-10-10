#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint

#server,PORT='192.168.0.231',6000
server,port="127.0.0.1",12000

print "Waiting connection..."
while True:
    ID=0
    ID+=1
    VVent=randint(0,100)
    DVent=randint(0,100)
    Gite=randint(0,100)

    Lon=getrandbits(0,1000000)
    b3=(Lon>>24)
    b2=(Lon>>16)&0xFF
    b1=(Lon>>8)&0xFF
    b0=(Lon>>0)&0xFF
    
    Lat=random.getrandbits(0,1000000)
    
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((server,port))
    
    data,addr=sock.recvfrom(1024)
    
#data  from client

    print "Connection established (: \n"
    print "Receive message:"
    print "ID:",ord(data[0])
    print "Longueur du datagram:",ord(data[1])
    print "GV:",ord(data[2])
    print "Safran",ord(data[3])
    print "===========END OF PACKET===========\n"

    
    
#résponse to client 
    trame_res=bytearray([ID,VVent,DVent,Gite,Lon,Lat])
    print "Envoi de la trame de réponse: ",str(trame_res).encode("hex")
    sock.sendto(trame_res, addr)    
    print ""
