import time
from colors import *
import functions

no_of_matrices = 4
leds = 100*no_of_matrices
my_pixels = [(0,0,0)]*leds

count = 0
color = 0

def HBD(my_pixels):
  functions.H(94,my_pixels,RED)
  functions.E(97,my_pixels,LIGHTGREEN)
  functions.L(190,my_pixels,RED)
  functions.L(193,my_pixels,LIGHTGREEN)
  functions.O(196,my_pixels,RED)
  functions.Y(291,my_pixels,RED)
  functions.O(294,my_pixels,LIGHTGREEN)
  functions.D(297,my_pixels,RED)
  functions.E(390,my_pixels,LIGHTGREEN)
  functions.R(393,my_pixels,RED)
  functions.H(47,my_pixels,PINK)
  functions.O(140,my_pixels,YELLOW)
  functions.W(143,my_pixels,SKYBLUE)
  functions.A(147,my_pixels,PINK)
  functions.R(240,my_pixels,YELLOW)
  functions.E(243,my_pixels,SKYBLUE)
  functions.Y(247,my_pixels,PINK)
  functions.O(340,my_pixels,YELLOW)
  functions.U(343,my_pixels,SKYBLUE)
  return

functions.clear(my_pixels)
functions.printme(my_pixels)
while True:
  HBD(my_pixels)
  functions.printme(my_pixels)