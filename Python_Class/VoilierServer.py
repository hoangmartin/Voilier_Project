#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint

class VoilierServer:
##    def __init__(self, server='127.0.0.1',port=12000):
##        self.server=server
##        self.port=port
##        self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
##
##    def envoyer(self, ):
##
##




##
#server,PORT='192.168.0.231',6000
server,port="127.0.0.1",12000
ID=0

print "Waiting connection..."

while True:

    # ici , on déclare des éléments de la trame | tout en aléatoire, ID incrément
    ID+=1
    VVent=randint(0,100)
    DVent=randint(0,100)
    Gite=randint(0,100)

    
    sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind((server,port))

#data  from client
    data,addr=sock.recvfrom(1024)
    print "Connection established (: \n"
    print "MESSAGE SENDING"
    
#definie Longtitude - Latitude

    Long= 5517822
    b3=(Long>>24)&0xFF
    b2=(Long>>16)&0xFF #décale 16bits et garder les 4 derniers bits en utilisant "&"
    b1=(Long>>8)&0xFF
    b0=Long&0xFF
    
        
    Lati=-1651925
    b7=(Lati>>24)&0xFF
    b6=(Lati>>16)&0xFF
    b5=(Lati>>8)&0xFF
    b4=Lati&0xFF
    
#réponse to client
    
    trame_res=bytearray([ID,VVent,DVent,Gite,b3,b2,b1,b0,b7,b6,b5,b4])
    print "Envoi de la trame de réponse:",str(trame_res).encode("hex")
    sock.sendto(trame_res, addr)    
    print ""
    print "ID:                            ",ord(data[0])
    print "Longueur:                ",ord(data[1])
    print "GV:                          ",ord(data[2])
    print "Safran:                    ",ord(data[3])
    print ""
    
# afficher Longtitude - Latitude

    print "Latitude:                  ", ((float)(Lati))/1000000
    print "Valeur Hexa de b2: ",hex(b6)
    print "Valeur Hexa de b1: ",hex(b5)
    print "Valeur Hexa de b0: ",hex(b4)

    print ""
    print "Longtitude:              ", ((float)(Long))/1000000
    print "Valeur Hexa de b2: ",hex(b2)
    print "Valeur Hexa de b1: ",hex(b1)
    print "Valeur Hexa de b0: ",hex(b0), "\n"
    print "===========| END OF PACKET |============\n"
