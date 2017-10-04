#!/usr/bin/env python
# coding: utf-8

import socket
import time

client='192.168.0.231'
PORT=6000
#ligne creation trame
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("Hello",(client,PORT))
