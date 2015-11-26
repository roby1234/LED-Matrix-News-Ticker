import time
from colors import *
import functions



my_pixels = [(0,0,0)]*100
count = 0
color = 0

def HBD(offset,my_pixels):
  functions.A((90+offset),my_pixels,LIGHTGREEN)
  # if (90 + offset + 3) <= 99 :
  functions.B((90+offset+3),my_pixels,SKYBLUE)
  # if (90 + offset + 6) <= 99 :
  #   functions.D((offset+6),my_pixels,YELLOW)
    # for i in range(0,5):
    #   temp = 10*i + 50 - mov
    #   index = temp%100 
    #   my_pixels[index] = LIGHTGREEN
    #   index = (temp + 2)%100 
    #   my_pixels[index] = LIGHTGREEN
    #   index = (temp + 3)%100 
    #   my_pixels[index] = SKYBLUE
    #   index = (temp + 6)%100 
    #   my_pixels[index] = YELLOW
    # for i in range(1,4):
    #   index = (10*i + 55 - mov)%100 
    #   my_pixels[index] = SKYBLUE
    #   index = (10*i + 58 - mov)%100 
    #   my_pixels[index] = YELLOW
    
    # index = (71 - mov)%100 
    # my_pixels[index] = LIGHTGREEN
    # index = (54 - mov)%100 
    # my_pixels[index] = SKYBLUE
    # index = (74 - mov)%100 
    # my_pixels[index] = SKYBLUE
    # index = (94 - mov)%100 
    # my_pixels[index] = SKYBLUE
    # index = (57 - mov)%100 
    # my_pixels[index] = YELLOW
    # index = (97 - mov)%100 
    # my_pixels[index] = YELLOW
  return





sav = 0
offset = 10
while True:
  offset = (offset-1)
  if offset == -1 :
    offset = 9
  functions.clear_moving(my_pixels)   
  HBD(offset,my_pixels)
  time.sleep(.1)
  functions.printme(my_pixels)
  time.sleep(.05)


