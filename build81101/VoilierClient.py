#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint
import time
 

class VoilierClient:

    
    def __init__(self):
        self.IPser=""
        self.port=0
        self.ID=0
        self.SF=0
        self.GV=0
        self.taille=0
        self.gite=0
        self.latitude=0
        self.longitude=0
        self.vitVent=0
        self.orientVent=0

    def initCom(self, IPser,port):
        self.IPser=IPser
        self.port=port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print "Connecting to "+ str(self.IPser)+  " on port "+str(self.port)
        print ""
        self.sock.connect((self.IPser,self.port))
        
        
    def txrx(self):
        self.ID+=1
        self.taille=randint(0,100)
        # self.GV=randint(0,100)
        # self.SF=randint(0,100)
            
        self.trame=bytearray([self.ID,self.taille,self.GV,self.SF])
        self.sock.send(self.trame)

        print "Message envoyé     :",self.trame[0],self.trame[1],self.trame[2],self.trame[3]
            
        response, addr=self.sock.recvfrom(13)

        lon=((ord(response[4])<<24)+(ord(response[5])<<16)+(ord(response[6])<<8)+(ord(response[7])<<0))
        lat=((ord(response[8])<<24)+(ord(response[9])<<16)+(ord(response[10])<<8)+(ord(response[11])<<0))
        b4= ord(response[4])
        b8= ord(response[8])
        self.gite= ord(response[3])
        self.vitVent=ord(response[1])
        self.orientVent=ord(response[2])

        if b4>127:
            lon=(~lon)&0xFFFFFFFF
            lon=lon+1
            lon=lon*(-1)

        self.longitude=float(lon)/1000000

        if b8>127:
            lat=(~lat)&0xFFFFFFFF
            lat=lat+1
            lat=lat*(-1) 
            
        self.latitude=float(lat)/1000000      

    


# cliMartin=VoilierClient()
# cliMartin.initCom("127.0.0.1",12000)
# cliMartin.txrx()

# print "Vitesse du vent    :",cliMartin.vitVent
# print "Orientation du vent:",cliMartin.orientVent 
# print "Latitude           :",cliMartin.latitude 
# print "Longitude          :",cliMartin.longitude