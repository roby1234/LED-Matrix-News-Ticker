#!/usr/bin/env python

import time
import random
import opc
import colors

ADDRESS = '192.168.7.2:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    print 'WARNING: could not connect to %s' % ADDRESS

RED   = (0xFF,0x00,0x00)
LIGHTSEAGREEN = (0x20,0xB2,0xAA)
SKYBLUE   = (0x87,0xCE,0xEB)
LIGHTGREEN  = (0x90,0xEE,0x90)
YELLOW    = (0xFF,0xFF,0x00)
my_pixels = [(0,0,0)]*200
count = 0
color = 0

def HBD(my_pixels):
    for i in range(0,5):
      temp = 10*i + 50 - mov
      index = temp%200 
      my_pixels[index] = LIGHTGREEN
      index = (temp + 2)%200 
      my_pixels[index] = LIGHTGREEN
      index = (temp + 3)%200 
      my_pixels[index] = SKYBLUE
      index = (temp + 6)%200 
      my_pixels[index] = YELLOW
    for i in range(1,4):
      index = (10*i + 55 - mov)%200 
      my_pixels[index] = SKYBLUE
      index = (10*i + 58 - mov)%200 
      my_pixels[index] = YELLOW
    
    index = (71 - mov)%200 
    my_pixels[index] = LIGHTGREEN
    index = (54 - mov)%200 
    my_pixels[index] = SKYBLUE
    index = (74 - mov)%200 
    my_pixels[index] = SKYBLUE
    index = (94 - mov)%200 
    my_pixels[index] = SKYBLUE
    index = (57 - mov)%200 
    my_pixels[index] = YELLOW
    index = (97 - mov)%200 
    my_pixels[index] = YELLOW
    return




while True:
  sav = 0
  mov = 0
  while True:
    mov = (mov + 1)%200	
    sav = sav + 1
    if sav > 200: break
    for i in range(0,200):
    	my_pixels[i] = (0, 0, 0)
    if client.put_pixels(my_pixels, channel=0):
      print 'sent'
    else:
      print 'not connected'
    time.sleep(.1)    
    HBD(my_pixels)
    time.sleep(.1)
    if client.put_pixels(my_pixels, channel=0):
      print 'sent'
    else:
      print 'not connected'
    time.sleep(.1)


