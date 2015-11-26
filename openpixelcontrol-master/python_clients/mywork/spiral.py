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
GREEN = (0x00,0x80,0x00)
my_pixels = [(0,0,0)]*100
count = 0
color = 0

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
  while True:
    for j in range(l,n,1):
      my_pixels[l*10 + j] = GREEN
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.1)
      count = count + 1
    if count > 99:
      break
    k = k+1
    for i in range(k,m,1):
      my_pixels[i*10 + m-1] = GREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.1)      
    if count > 99:
      break
    n = n-1
    for j in range(n-1 , l-1 , -1):
      my_pixels[n*10 + j] = GREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.1)      
    if count > 99:
      break
    m = m-1
    for i in range(m-1 , k-1 , -1):
      my_pixels[i*10 + l] = GREEN
      count = count + 1
      if client.put_pixels(my_pixels, channel=0):
        print 'sent'
      else:
        print 'not connected'
      time.sleep(0.1)
    if count > 99:
      break
    l = l + 1
  if client.put_pixels(my_pixels, channel=0):
    print 'sent'
  else:
    print 'not connected'  
  time.sleep(1)
