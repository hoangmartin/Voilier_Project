#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint
import time
from threading import Thread


class SocketError(Exception):
    pass 

class VoilierClients:

    
    def __init__(self):
        self.IPser=""
        self.port=0
        self.ID=0
        self.SF=0
        self.GV=0
        self.Taille=0
        self.gite=0
        self.Latitude=0
        self.Longitude=0

    def initCom(self, IP,PORT):
        self.IPser=IP
        self.port=PORT
        try:
            self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        except socket.error,msg:
            raise SocketError,"Error in Socket Object Creation!!"
        try:
            print "Connecting to "+ str(self.IPser)+  " on port "+str(self.port)
            self.sock.connect((self.IPser,self.port))
        except socket.error,msg:
            raise SocketError,"Connection refused to "+str(self.IPser)+ "on port "+str(self.port)


        
    def TxRx(self):        
        while (True):
            self.ID+=1
            self.Taille=randint(0,100)
            self.GV=randint(0,100)
            self.SF=randint(0,100)
            
            self.trame=bytearray([self.ID,self.Taille,self.GV,self.SF])
            self.sock.sendto(self.trame,(self.IPser,self.port))

            print "Message envoyé:",self.trame[0],self.trame[1],self.trame[2],self.trame[3]
            
            self.response, self.addr=self.sock.recvfrom(1024)
            print ""
            print "RESPONSE FROM SERVER"
            print "Trame de réponse:     ", self.response.encode("hex")
            print "ID:                               ",ord(self.response[0])
            print "Gite du bateau:           ",ord(self.response[3]),"°"
            print "Vitesse du vent:          ",ord(self.response[1]),"°"
            print "Direction du vent:       ",ord(self.response[2]),"nd"
            self.lon=((ord(self.response[4])<<24)+(ord(self.response[5])<<16)+(ord(self.response[6])<<8)+(ord(self.response[7])<<0))
            self.lat=((ord(self.response[8])<<24)+(ord(self.response[9])<<16)+(ord(self.response[10])<<8)+(ord(self.response[11])<<0))
            self.b4= ord(self.response[4])
            self.b8= ord(self.response[8])
        
            if self.b4>127:
                self.lon=(~self.lon)&0xFFFFFFFF
                self.lon=self.lon+1
                self.lon=self.lon*(-1)

            if self.b8>127:
                self.lat=(~self.lat)&0xFFFFFFFF
                self.lat=self.lat+1
                self.lat=self.lat*(-1) 
            
            print "Latitude:                     ",(float(self.lat))/1000000
            
            print "Longitude:                  ",(float(self.lon))/1000000,"\n"
            
            
            print "===========| END OF PACKET |==============\n"       
            time.sleep(4)        


CliMartin=VoilierClients()
CliMartin.initCom("127.0.0.1",12000)
CliMartin.TxRx()



