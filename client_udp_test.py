#!/usr/bin/env python
# coding: utf-8

import socket
from random import randint
import time

#client,PORT='192.168.0.231',6000
client,PORT="127.0.0.1",12000
ID=0


#générer des valeurs
while True:
    ID+=1
    Taille=randint(0,100)
    GV=randint(0,100)
    SF=randint(0,100)
    
#creation d'un trmae
    trame=bytearray([ID,Taille,GV,SF])
    sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(trame,(client,PORT))
    print "Message envoyé:",trame[0],trame[1],trame[2],trame[3]
    
#afficher des infos sur l'écran
    print ""
    print "Réponse du serveur"
    response, addr=sock.recvfrom(100)

    print "Trame de réponse:     ", response.encode("hex")
    print "ID:                               ",ord(response[0])
    print "Gite du bateau:           ",ord(response[3])
    print "Vitesse du vent:          ",ord(response[1])
    print "Direction du vent:       ",ord(response[2])
    print "Latitude:                     ",(ord(response[4])<<24)+(ord(response[5])<<16)+(ord(response[6])<<8)+(ord(response[7])<<0)
    print "Longitude:                  ",(ord(response[8])<<24)+(ord(response[9])<<16)+(ord(response[10])<<8)+(ord(response[11])<<0),"\n"
  
    print "===========| END OF PACKET |=============="
    time.sleep(2)












