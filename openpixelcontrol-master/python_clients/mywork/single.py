import time
from colors import *
import functions

no_of_matrices = 4
leds = 100*no_of_matrices
my_pixels = [(0,0,0)]*leds

functions.clear(my_pixels)

while True:
    count = 0
    while count <= leds:
        print str(count) 
        if count != 0:
            my_pixels[count-1] = BLACK
        if count == leds:
            break
        my_pixels[count] = TEAL
        functions.printme(my_pixels)
        count = count + 1
        time.sleep(.0001)
