import time
from colors import *
import func_new

no_of_matrices = 4
leds = 100*no_of_matrices
out = leds - 21
my_pixels = [(0,0,0)]*leds

count = 0
color = 0

func_new.clear(my_pixels)
func_new.printme(my_pixels)
while True:
  with open('news.txt') as f:
    for a in f:
      func_new.scrolling(a,out-2, out-1 ,out,my_pixels)
