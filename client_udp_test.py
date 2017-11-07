#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint
import time
##from threading import Thread
##
##class Clients:
##    def __init__(self, client='127.0.0.1', PORT=120000, ID=0):
##        self.client=client
##        self.PORT=PORT
##        self.ID=ID
##        self.Taille=Taille
##        self.GV=GV
##        self.SF=SF
##        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##
##    def send(self,trame):
##        self.sock.sendto(trame,(self.client,self.PORT))
##    def send_loop(self):
##        while (True):
##            self.ID+=1
##            self.Taille=randint(0,100)
##            self.GV=randint(0,100)
##            self.SF=randint(0,100)
##            
        






###client,PORT='192.168.0.231',6000
client,PORT="127.0.0.1",12000
ID=0


#générer des valeurs
while True:
    ID+=1
    Taille=randint(0,100)
    GV=randint(0,100)
    SF=randint(0,100)
    
#creation d'un trame
    trame=bytearray([ID,Taille,GV,SF])
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(trame,(client,PORT))
    print "Message envoyé:",trame[0],trame[1],trame[2],trame[3]
    
#afficher des infos sur l'écran
    print ""
    print "RESPONSE FROM SERVER"
    response, addr=sock.recvfrom(100)

    print "Trame de réponse:     ", response.encode("hex")
    print "ID:                               ",ord(response[0])
    print "Gite du bateau:           ",ord(response[3]),"°"
    print "Vitesse du vent:          ",ord(response[1]),"°"
    print "Direction du vent:       ",ord(response[2]),"nd"

##    lon=((float)(ord(response[4])<<24)+(ord(response[5])<<16)+(ord(response[6])<<8)+(ord(response[7])<<0))/1000000
##    lat=((float)(ord(response[8])<<24)+(ord(response[9])<<16)+(ord(response[10])<<8)+(ord(response[11])<<0))/1000000
    lon=((ord(response[4])<<24)+(ord(response[5])<<16)+(ord(response[6])<<8)+(ord(response[7])<<0))
    lat=((ord(response[8])<<24)+(ord(response[9])<<16)+(ord(response[10])<<8)+(ord(response[11])<<0))
    b4= ord(response[4])
    b8= ord(response[8])
    
    if b4>127:
        lon=(~lon)&0xFFFFFFFF
        lon=lon+1
        lon=lon*(-1)

    if b8>127:
        lat=(~lat)&0xFFFFFFFF
        lat=lat+1
        lat=lat*(-1) 
        
    print "Latitude:                     ",(float(lat))/1000000
        
    print "Longitude:                  ",(float(lon))/1000000,"\n"
  
    print "===========| END OF PACKET |==============\n"
    time.sleep(4)






