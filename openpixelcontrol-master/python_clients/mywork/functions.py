import time
import random
import opc
from colors import *

ADDRESS = '192.168.7.2:7890'

no_of_matrices = 4
leds = 100*no_of_matrices

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    print 'WARNING: could not connect to %s' % ADDRESS

def printme(my_pixels):
  if client.put_pixels(my_pixels, channel=0):
    print 'sent'
  else:
    print 'not connected'
  time.sleep(0.05)

def dislay_char(str,offset,my_pixels):
	for i in range(0,len(str)):
		method_name = str[i] # set by the command line options
		possibles = globals().copy()
		possibles.update(locals())
		method = possibles.get(method_name)
		if not method:
			raise Exception("Method %s not implemented" % method_name)
		color = color
		method(offset,my_pixels,color)
	return 

def A(offset,my_pixels,color):
  for i in range(1,5):
    temp = offset-10*i
    my_pixels[temp] = color
    my_pixels[(temp + 2)] = color
  my_pixels[(offset+1)] = color
  my_pixels[(offset-20+1)]= color
  printme(my_pixels)
  return 

def B(offset,my_pixels,color):
  for i in range(0,5):
  	temp = offset-10*i  
   	my_pixels[temp] = color
  # my_pixels[offset-40+2] = color
  my_pixels[(offset-40+1)] = color
  my_pixels[(offset+1)] = color
  my_pixels[(offset-30+2)] = color
  my_pixels[(offset-10+2)] = color
  my_pixels[(offset-20+1)] = color
  # my_pixels[offset+2] = color
  printme(my_pixels)
  return 

def C(offset,my_pixels,color):
  for i in range(0,5):
  	temp = offset-10*i
  	my_pixels[temp] = color
  my_pixels[offset-40+2] = color
  my_pixels[offset-40+1] = color
  my_pixels[offset+1] = color
  my_pixels[offset+2] = color
  printme(my_pixels)
  return 


def D(offset,my_pixels,color):
  for i in range(0,5):
    temp = offset- 10*i
    my_pixels[temp] = color
  my_pixels[offset-20+2] = color
  my_pixels[offset-10+2] = color
  my_pixels[offset-40+1] = color
  my_pixels[offset+1] = color
  my_pixels[offset-30+2] = color
  printme(my_pixels)
  return 


def E(offset,my_pixels,color):
  for i in range(0,5):
    temp = offset-10*i 
    my_pixels[temp] = color
  my_pixels[offset+1] = color
  my_pixels[offset+2] = color
  my_pixels[offset-20+1] = color
  my_pixels[offset-40+2] = color
  my_pixels[offset-40+1] = color
  printme(my_pixels)
  return 

def F(offset,my_pixels,color):
  for i in range(0,5):
    temp = offset-10*i
    my_pixels[temp] = color
  my_pixels[offset+2] = color
  my_pixels[offset+1] = color
  my_pixels[offset-20+1] = color
  printme(my_pixels)
  return 

def G(offset,my_pixels,color):
  for i in range(0,5):
    temp = offset-10*i
    my_pixels[temp] = color
  my_pixels[offset+2] = color
  my_pixels[offset+1] = color
  my_pixels[offset-20+1] = color
  my_pixels[offset-20+2] = color
  my_pixels[offset-40+1] = color
  my_pixels[offset-40+2] = color
  my_pixels[offset-30+2] = color
  printme(my_pixels)
  return 

def H(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-20+1]=color
    printme(my_pixels)
    return 

def I(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp+1] = color
    my_pixels[offset]=color
    my_pixels[offset+2]=color
    my_pixels[offset-40+2]=color
    my_pixels[offset-40]=color
    printme(my_pixels)
    return 


def J(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp+1] = color
    my_pixels[offset]=color
    my_pixels[offset+2]=color
    my_pixels[offset-20]=color
    my_pixels[offset-40]=color
    my_pixels[offset-30]=color
    printme(my_pixels)
    return 

def K(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
    my_pixels[offset+2]=color
    my_pixels[offset-10+1]=color
    my_pixels[offset-30+1]=color
    my_pixels[offset-40+2]=color
    printme(my_pixels)
    return 

def L(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
    my_pixels[offset-40+1]=color
    my_pixels[offset-40+2]=color
    printme(my_pixels)
    return 


def M(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-10+1]=color
    my_pixels[offset+1]=color
    printme(my_pixels)
    return 

def N(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-10+1]=color
    printme(my_pixels)
    return 

def O(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset+1]=color
    my_pixels[offset-40+1]=color
    printme(my_pixels)
    return 

def P(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
    my_pixels[offset-10+2] = color
    my_pixels[offset+1] = color
    my_pixels[offset+2] = color
    my_pixels[offset-20+1] = color
    my_pixels[offset-20+2] = color
    printme(my_pixels)
    return 

def Q(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset+1]=color
    my_pixels[offset-40+1]=color
    my_pixels[offset-20+1]=color
    printme(my_pixels)
    return 

def R(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
    my_pixels[offset-10+2] = color
    my_pixels[offset+1] = color
    my_pixels[offset-20+1] = color
    my_pixels[offset-30+2] = color
    my_pixels[offset-40+2] = color
    printme(my_pixels)
    return 

def S(offset,my_pixels,color):
    for i in range(2,-1,-1):
    	my_pixels[offset + i] = color
  	my_pixels[offset - 10] = color
  	my_pixels[offset - 20] = color
  	my_pixels[offset - 19] = color
  	my_pixels[offset - 18] = color
  	my_pixels[offset - 28] = color
  	my_pixels[offset - 38] = color
  	my_pixels[offset - 39] = color
  	my_pixels[offset - 40] = color
  	printme(my_pixels)
    return 

def T(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp+1] = color
    my_pixels[offset]=color
    my_pixels[offset+2]=color
    printme(my_pixels)
    return 

def U(offset,my_pixels,color):
    for i in range(0,5):
        temp = offset-10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-40+1]=color
    printme(my_pixels)
    return 

def V(offset,my_pixels,color):
    for i in range(0,4):
        temp =offset-10*i 
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-40+1]=color
    printme(my_pixels)
    return 


def W(offset,my_pixels,color):
    for i in range(0,5):
        temp =offset - 10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-40+1]=color
    my_pixels[offset-30+1]=color
    printme(my_pixels)
    return 

def X(offset,my_pixels,color):
    for i in range(0,5):
        temp =offset - 10*i
        my_pixels[temp] = color
        my_pixels[temp + 2] = color
    my_pixels[offset-20] = BLACK
    my_pixels[offset+2-20] = BLACK
    my_pixels[offset-20+1]=color
    printme(my_pixels)
    return 


def Y(offset,my_pixels,color):
    for i in range(2,5):
        temp = offset-10*i
        my_pixels[temp+1] = color
    my_pixels[offset]=color
    my_pixels[offset+2]=color
    my_pixels[offset-10+1]=color
    printme(my_pixels)
    return 

def Z(offset,my_pixels,color):
    my_pixels[offset]=color
    my_pixels[offset+1]=color
    my_pixels[offset+2]=color
    my_pixels[offset-20+1]=color
    my_pixels[offset-40]=color
    my_pixels[offset-40+1]=color
    my_pixels[offset-40+2]=color
    printme(my_pixels)
    return 

def heart(offset,my_pixels,color):#offset = 42
  my_pixels[offset-38] = color
  my_pixels[offset-29] = color
  my_pixels[offset-10] = color
  my_pixels[offset-20] = color
  my_pixels[offset+1] = color
  my_pixels[offset-8] = color
  my_pixels[offset+3] = color
  my_pixels[offset-6] = color
  my_pixels[offset-16] = color
  my_pixels[offset-27] = color
  return

def clear(my_pixels):
  for i in range(0,leds):
    my_pixels[i] = (0, 0, 0)
  printme(my_pixels)
  time.sleep(1)  


def clear_moving(my_pixels):
  for i in range(0,leds):
    my_pixels[i] = (0, 0, 0)
  printme(my_pixels)
  time.sleep(.15)  

def spiral(my_pixels , k , l , m , n , count):
  while True:
    for j in range(l,n,1):
      my_pixels[l*10 + j] = LIGHTSEAGREEN
      printme(my_pixels)
      count = count + 1
    if count > 99:
      break
    k = k+1
    for i in range(k,m,1):
      my_pixels[i*10 + m-1] = LIGHTSEAGREEN
      count = count + 1
      printme(my_pixels)
    if count > 99:
      break
    n = n-1
    for j in range(n-1 , l-1 , -1):
      my_pixels[n*10 + j] = LIGHTSEAGREEN
      count = count + 1
      printme(my_pixels)
    if count > 99:
      break
    m = m-1
    for i in range(m-1 , k-1 , -1):
      my_pixels[i*10 + l] = LIGHTSEAGREEN
      count = count + 1
      printme(my_pixels)
    if count > 99:
      break
    l = l + 1
  printme(my_pixels)
  return