import time
from colors import *
import functions

no_of_matrices = 1
leds = 176*no_of_matrices
my_pixels = [(0,0,0)]*leds

count = 0
color = 0

def HBD(my_pixels):
  functions.H(90,my_pixels,LIGHTGREEN)
  functions.B(93,my_pixels,SKYBLUE)
  functions.D(96,my_pixels,YELLOW)
  functions.heart(42,my_pixels,RED)
  return

def misile(my_pixels):
  my_pixels[5] = RED
  my_pixels[15] = DARKMAGENTA
  functions.printme(my_pixels)
  time.sleep(.15)
  my_pixels[25] = PINK
  functions.printme(my_pixels)
  time.sleep(.15)
  my_pixels[35] = MAROON
  functions.printme(my_pixels)
  time.sleep(.15)
  my_pixels[44] = YELLOW
  my_pixels[45] = YELLOW
  my_pixels[46] = YELLOW
  my_pixels[53] = YELLOW
  my_pixels[57] = YELLOW
  my_pixels[42] = YELLOW
  my_pixels[48] = YELLOW
  functions.printme(my_pixels)
  time.sleep(.15)
  my_pixels[55] = DARKBLUE
  my_pixels[56] = DARKBLUE
  my_pixels[57] = DARKBLUE
  my_pixels[66] = DARKBLUE
  my_pixels[67] = DARKBLUE
  my_pixels[58] = DARKBLUE
  my_pixels[49] = DARKBLUE
  my_pixels[64] = DARKBLUE
  my_pixels[63] = DARKBLUE
  my_pixels[52] = DARKBLUE
  my_pixels[41] = DARKBLUE
  functions.printme(my_pixels)
  time.sleep(.15)  
  my_pixels[65] = LIGHTGREEN
  my_pixels[72] = LIGHTGREEN
  my_pixels[77] = LIGHTGREEN
  my_pixels[76] = LIGHTGREEN
  my_pixels[87] = LIGHTGREEN
  my_pixels[78] = LIGHTGREEN
  my_pixels[69] = LIGHTGREEN
  my_pixels[74] = LIGHTGREEN
  my_pixels[83] = LIGHTGREEN
  my_pixels[72] = LIGHTGREEN
  my_pixels[61] = LIGHTGREEN
  my_pixels[50] = LIGHTGREEN
  functions.printme(my_pixels)
  time.sleep(.15)
  my_pixels[75] = SILVER
  my_pixels[85] = SILVER
  my_pixels[75] = SILVER
  my_pixels[86] = SILVER
  my_pixels[97] = SILVER
  my_pixels[88] = SILVER
  my_pixels[79] = SILVER
  my_pixels[84] = SILVER
  my_pixels[93] = SILVER
  my_pixels[82] = SILVER
  my_pixels[71] = SILVER
  my_pixels[60] = SILVER
  functions.printme(my_pixels)
  time.sleep(.15)
  functions.clear(my_pixels)
  time.sleep(.15)
  return

def HBD_dynamic(my_pixels):
# alphabet H
  for i in range(4,-1,-1):
    temp = 10*i + 50
    my_pixels[temp] = LIGHTGREEN
    functions.printme(my_pixels)
  my_pixels[71] = LIGHTGREEN
  functions.printme(my_pixels)
  for i in range(4,-1,-1):
    temp = 10*i + 50
    my_pixels[temp + 2] = LIGHTGREEN
    functions.printme(my_pixels)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  functions.printme(my_pixels)
  time.sleep(1)

# alphabet B
  for i in range(0,5):
    temp = 10*i + 50
    my_pixels[temp + 3] = SKYBLUE
    functions.printme(my_pixels)
  my_pixels[94] = SKYBLUE
  functions.printme(my_pixels)
  my_pixels[85] = SKYBLUE
  functions.printme(my_pixels)
  my_pixels[74] = SKYBLUE
  functions.printme(my_pixels)
  my_pixels[65] = SKYBLUE
  functions.printme(my_pixels)
  my_pixels[54] = SKYBLUE
  functions.printme(my_pixels)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  functions.printme(my_pixels)
  time.sleep(1)

# alphabet D
  for i in range(0,5):
    temp = 10*i + 50
    my_pixels[temp + 6] = YELLOW
    functions.printme(my_pixels)
  my_pixels[97] = YELLOW
  functions.printme(my_pixels)
  for i in range(3,0,-1):
    my_pixels[10*i + 58] = YELLOW
    functions.printme(my_pixels)
  my_pixels[57] = YELLOW
  functions.printme(my_pixels)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  functions.printme(my_pixels)
  time.sleep(1)

  my_pixels[4] = RED
  functions.printme(my_pixels)   
  my_pixels[13] = RED
  functions.printme(my_pixels)
  my_pixels[22] = RED
  functions.printme(my_pixels)
  my_pixels[32] = RED
  functions.printme(my_pixels)
  my_pixels[43] = RED
  functions.printme(my_pixels)
  my_pixels[34] = RED
  functions.printme(my_pixels)
  my_pixels[45] = RED
  functions.printme(my_pixels)
  my_pixels[36] = RED
  functions.printme(my_pixels)
  my_pixels[26] = RED
  functions.printme(my_pixels)
  my_pixels[15] = RED
  functions.printme(my_pixels)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  functions.printme(my_pixels)
  time.sleep(1) 

# alphabet S
  offset_s = 40
  for i in range(2,-1,-1):
    my_pixels[offset_s + i] = CHOCOLATE
    functions.printme(my_pixels)
  my_pixels[offset_s - 10] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 20] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 19] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 18] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 28] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 38] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 39] = CHOCOLATE
  functions.printme(my_pixels)
  my_pixels[offset_s - 40] = CHOCOLATE
  functions.printme(my_pixels)
  functions.printme(my_pixels)
  # for i in range(0,100):
  #   my_pixels[i] = (0, 0, 0)
  # functions.printme(my_pixels)
  time.sleep(1)
  
# alphabet A
  offset_a = 43
  for i in range(4,0,-1):
    my_pixels[offset_a -10*i] = PURPLE
    functions.printme(my_pixels)
  my_pixels[offset_a + 1] = PURPLE
  functions.printme(my_pixels)
  for i in range(1,5):
    my_pixels[offset_a -10*i + 2] = PURPLE
    functions.printme(my_pixels)
  my_pixels[offset_a - 19] = PURPLE
  functions.printme(my_pixels)
  functions.printme(my_pixels)  
  # for i in range(0,100):
  #   my_pixels[i] = (0, 0, 0)
  # functions.printme(my_pixels)
  time.sleep(1)
 
# alphabet V
  offset_v = 46
  for i in range(0,4):
    my_pixels[offset_v - 10*i] = ORANGE
    functions.printme(my_pixels)
  my_pixels[offset_v - 39] = ORANGE
  functions.printme(my_pixels)
  for i in range(3,-1,-1):
    my_pixels[offset_v + 2 - 10*i] = ORANGE
    functions.printme(my_pixels)
  functions.printme(my_pixels)
  # for i in range(0,100):
  #   my_pixels[i] = (0, 0, 0)
  # functions.printme(my_pixels)
  time.sleep(1)

# alphabet I
  offset_i = 49
  for i in range(0,5):
    my_pixels[offset_i - 10*i] = LIGHTSEAGREEN
    functions.printme(my_pixels)
  functions.printme(my_pixels)
  for i in range(0,100):
    my_pixels[i] = (0, 0, 0)
  functions.printme(my_pixels)
  time.sleep(1)  

  return

while True:
  m = 10
  n = 10
  i=0
  j=0
  k=0
  l=0
  count = 0
  functions.clear(my_pixels)
  functions.printme(my_pixels)
  functions.spiral(my_pixels , k , l , m , n , count)
  functions.clear(my_pixels)
  sav = 0
  HBD_dynamic(my_pixels)
  while True:
    sav = sav + 1
    if sav > 3: break
    HBD(my_pixels)
    functions.printme(my_pixels)
    functions.printme(my_pixels)
    time.sleep(1.8)
    functions.clear(my_pixels)
    misile(my_pixels)
    functions.printme(my_pixels)
    time.sleep(.5)
