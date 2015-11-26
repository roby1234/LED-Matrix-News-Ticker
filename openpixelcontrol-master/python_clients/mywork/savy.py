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
my_pixels = [(0,0,0)]*100
count = 0
color = 0

def HBD(my_pixels):
    for i in range(0,5):
      temp = 10*i + 50
      my_pixels[temp] = LIGHTGREEN
      my_pixels[temp + 2] = LIGHTGREEN
      my_pixels[temp + 3] = SKYBLUE
      my_pixels[temp + 6] = YELLOW
    for i in range(1,4):
      my_pixels[10*i + 55] = SKYBLUE
      my_pixels[10*i + 58] = YELLOW
    my_pixels[71] = LIGHTGREEN
    my_pixels[54] = SKYBLUE
    my_pixels[74] = SKYBLUE
    my_pixels[94] = SKYBLUE
    my_pixels[57] = YELLOW
    my_pixels[97] = YELLOW
    my_pixels[32] = RED
    my_pixels[22] = RED
    my_pixels[43] = RED
    my_pixels[13] = RED
    my_pixels[34] = RED
    my_pixels[4] = RED
    my_pixels[45] = RED
    my_pixels[15] = RED
    my_pixels[36] = RED
    my_pixels[26] = RED
    return


def spiral(my_pixels , k , l , m , n , count):
  while True:
    for j in range(l,n,1):
      my_pixels[l*10 + j] = LIGHTSEAGREEN
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.05)
      count = count + 1
    if count > 99:
      break
    k = k+1
    for i in range(k,m,1):
      my_pixels[i*10 + m-1] = LIGHTSEAGREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.05)      
    if count > 99:
      break
    n = n-1
    for j in range(n-1 , l-1 , -1):
      my_pixels[n*10 + j] = LIGHTSEAGREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.05)      
    if count > 99:
      break
    m = m-1
    for i in range(m-1 , k-1 , -1):
      my_pixels[i*10 + l] = LIGHTSEAGREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.05)
    if count > 99:
      break
    l = l + 1
  if client.put_pixels(my_pixels, channel=0):
    print 'sent'
  else:
    print 'not connected'  
  time.sleep(.5)
  return



while True:
  m = 10
  n = 10
  i=0
  j=0
  k=0
  l=0
  count = 0
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  time.sleep(.5)
  spiral(my_pixels , k , l , m , n , count)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  time.sleep(.5)
  sav = 0
  while True:
    sav = sav + 1
    if sav > 200: break
    for i in range(0,100):
    	my_pixels[i] = (0, 0, 0)
    time.sleep(.5)    
    HBD(my_pixels)
    if client.put_pixels(my_pixels, channel=0):
      print 'sent'
    else:
      print 'not connected'
    time.sleep(.5)


