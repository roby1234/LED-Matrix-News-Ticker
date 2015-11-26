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

  def dislay_char(str,offset1,offset2,offset3,my_pixels):
  for i in range(0,len(str)):
    method_name = str[i] # set by the command line options
    if str[i]==' ':
      space(offset1,offset2,offset3,my_pixels)
      if (offset1+3)/10>offset1/10:
        offset1=offset1+93
      else:
        offset1=offset1+3
      if (offset2+3)/10>offset2/10:
        offset2=offset2+93
      else:
        offset2=offset2+3
      if (offset3+3)/10>offset3/10:
        offset3=offset3+93
      else:
        offset3=offset3+3
      continue
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
      raise Exception("Method %s not implemented" % method_name)
    else:
      method(offset1,offset2,offset3,my_pixels,color)
      if (offset1+3)/10>offset1/10:
        offset1=offset1+93
      else:
        offset1=offset1+3
      if (offset2+3)/10>offset2/10:
        offset2=offset2+93
      else:
        offset2=offset2+3
      if (offset3+3)/10>offset3/10:
        offset3=offset3+93
      else:
        offset3=offset3+3
      if offset1>=leds or offset2>=leds or offset3>=leds:
        break
  return 

#######################################################################################################################
def dislay_char_scroll(str,offset1,offset2,offset3,my_pixels):
  for i in range(len(str)-1,-1,-1):
    method_name = str[i] # set by the command line options
    if str[i]==' ':
      space(offset1,offset2,offset3,my_pixels)
      if (offset1-3)/10>offset1/10:
        offset1=offset1-93
      else:
        offset1=offset1-3
      if (offset2-3)/10>offset2/10:
        offset2=offset2-93
      else:
        offset2=offset2-3
      if (offset3-3)/10>offset3/10:
        offset3=offset3-93
      else:
        offset3=offset3-3
      continue
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    if not method:
      raise Exception("Method %s not implemented" % method_name)
    else:
      method(offset1,offset2,offset3,my_pixels,color)
      if (offset1-3)/10>offset1/10:
        offset1=offset1-93
      else:
        offset1=offset1-3
      if (offset2-3)/10<offset2/10:
        offset2=offset2-93
      else:
        offset2=offset2-3
      if (offset3-3)/10<offset3/10:
        offset3=offset3-93
      else:
        offset3=offset3-3
      if offset1<0 or offset2<0 or offset3<0:
        break
  return 
##########################################################################################################################3#
def scrolling(str,offset,my_pixels):

def A(offset1,offset2,offset3,my_pixels,color):
  if (offset1%100)!=69 or offset1!=69:
    for i in range(1,5):
      temp = offset1-10*i
      my_pixels[temp] = color
   if (offset2%100)!=69 or offset2!=69:
    for i in range(1,5):
      temp = offset3-10*i
      my_pixels[(temp)] = color
    
 
  
  my_pixels[(offset2)] = color
  my_pixels[(offset2-20)]= color
  printme(my_pixels)
  return 

def B(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
  	temp = offset1-10*i  
   	my_pixels[temp] = color
  # my_pixels[offset-40+2] = color
  my_pixels[(offset2-40)] = color
  my_pixels[(offset2)] = color
  my_pixels[(offset3-30)] = color
  my_pixels[(offset3-10)] = color
  my_pixels[(offset2-20)] = color
  # my_pixels[offset+2] = color
  printme(my_pixels)
  return 

def C(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
  	temp = offset1-10*i
  	my_pixels[temp] = color
  my_pixels[offset3-40] = color
  my_pixels[offset2-40] = color
  my_pixels[offset2] = color
  my_pixels[offset3] = color
  printme(my_pixels)
  return 


def D(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
    temp = offset1- 10*i
    my_pixels[temp] = color
  my_pixels[offset3-20] = color
  my_pixels[offset3-10] = color
  my_pixels[offset2-40] = color
  my_pixels[offset2] = color
  my_pixels[offset3-30] = color
  printme(my_pixels)
  return 


def E(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
    temp = offset1-10*i 
    my_pixels[temp] = color
  my_pixels[offset2] = color
  my_pixels[offset3] = color
  my_pixels[offset2-20] = color
  my_pixels[offset3-40] = color
  my_pixels[offset2-40] = color
  printme(my_pixels)
  return 

def F(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
    temp = offset1-10*i
    my_pixels[temp] = color
  my_pixels[offset3] = color
  my_pixels[offset2] = color
  my_pixels[offset2-20] = color
  printme(my_pixels)
  return 

def G(offset1,offset2,offset3,my_pixels,color):
  for i in range(0,5):
    temp = offset1-10*i
    my_pixels[temp] = color
  my_pixels[offset3] = color
  my_pixels[offset2] = color
  my_pixels[offset2-20] = color
  my_pixels[offset3-20] = color
  my_pixels[offset2-40] = color
  my_pixels[offset3-40] = color
  my_pixels[offset3-30] = color
  printme(my_pixels)
  return 

def H(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-20]=color
    printme(my_pixels)
    return 

def I(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset2-10*i
        my_pixels[temp] = color
    my_pixels[offset1]=color
    my_pixels[offset3]=color
    my_pixels[offset3-40]=color
    my_pixels[offset1-40]=color
    printme(my_pixels)
    return 


def J(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset1-10*i
        my_pixels[temp+1] = color
    my_pixels[offset]=color
    my_pixels[offset+2]=color
    my_pixels[offset-20]=color
    my_pixels[offset-40]=color
    my_pixels[offset-30]=color
    printme(my_pixels)
    return 

def K(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset1-10*i
        my_pixels[temp] = color
    my_pixels[offset3]=color
    my_pixels[offset2-10]=color
    my_pixels[offset2-30]=color
    my_pixels[offset3-40]=color
    printme(my_pixels)
    return 

def L(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset1-10*i
        my_pixels[temp] = color
    my_pixels[offset2-40]=color
    my_pixels[offset3-40]=color
    printme(my_pixels)
    return 


def M(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-10]=color
    my_pixels[offset2]=color
    printme(my_pixels)
    return 

def N(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-10]=color
    printme(my_pixels)
    return 

def O(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2]=color
    my_pixels[offset2-40]=color
    printme(my_pixels)
    return 

def P(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset1-10*i
        my_pixels[temp] = color
    my_pixels[offset3-10] = color
    my_pixels[offset2] = color
    my_pixels[offset3] = color
    my_pixels[offset2-20] = color
    my_pixels[offset3-20] = color
    printme(my_pixels)
    return 

def Q(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2]=color
    my_pixels[offset2-40]=color
    my_pixels[offset2-20]=color
    printme(my_pixels)
    return 

def R(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset1-10*i
        my_pixels[temp] = color
    my_pixels[offset3-10] = color
    my_pixels[offset2] = color
    my_pixels[offset2-20] = color
    my_pixels[offset3-30] = color
    my_pixels[offset3-40] = color
    printme(my_pixels)
    return 

def S(offset1,offset2,offset3,my_pixels,color):
    for i in range(2,-1,-1):
    	my_pixels[offset1 + i] = color
  	my_pixels[offset1 - 10] = color
  	my_pixels[offset1 - 20] = color
  	my_pixels[offset2 - 20] = color
  	my_pixels[offset3 - 20] = color
  	my_pixels[offset3 - 30] = color
  	my_pixels[offset3 - 40] = color
  	my_pixels[offset2 - 40] = color
  	my_pixels[offset1 - 40] = color
  	printme(my_pixels)
    return 

def T(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp = offset2-10*i
        my_pixels[temp] = color
    my_pixels[offset1]=color
    my_pixels[offset3]=color
    printme(my_pixels)
    return 

def U(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 = offset1-10*i
        temp2 = offset3-10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-40]=color
    printme(my_pixels)
    return 

def V(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,4):
        temp1 =offset1-10*i 
        temp2 =offset3-10*i 
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-40]=color
    printme(my_pixels)
    return 


def W(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 =offset1 - 10*i
        temp2 =offset3 - 10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset2-40]=color
    my_pixels[offset2-30]=color
    printme(my_pixels)
    return 

def X(offset1,offset2,offset3,my_pixels,color):
    for i in range(0,5):
        temp1 =offset1 - 10*i
        temp2 =offset3 - 10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
    my_pixels[offset1-20] = BLACK
    my_pixels[offset3-20] = BLACK
    my_pixels[offset2-20]=color
    printme(my_pixels)
    return 


def Y(offset1,offset2,offset3,my_pixels,color):
    for i in range(2,5):
        temp = offset2-10*i
        my_pixels[temp] = color
    my_pixels[offset1]=color
    my_pixels[offset3]=color
    my_pixels[offset2-10]=color
    printme(my_pixels)
    return 

def Z(offset1,offset2,offset3,my_pixels,color):
    my_pixels[offset1]=color
    my_pixels[offset2]=color
    my_pixels[offset3]=color
    my_pixels[offset2-20]=color
    my_pixels[offset1-40]=color
    my_pixels[offset2-40]=color
    my_pixels[offset3-40]=color
    printme(my_pixels)
    return 


def space(offset1,offset2,offset3,my_pixels):
  color = BLACK
  for i in range(0,5):
        temp1 =offset1 - 10*i
        temp2 =offset2 - 10*i
        temp3 =offset3 - 10*i
        my_pixels[temp1] = color
        my_pixels[temp2] = color
        my_pixels[temp3] = color
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