
import time
import random
import opc
# import colors

ADDRESS = '192.168.7.2:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print 'connected to %s' % ADDRESS
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print 'WARNING: could not connect to %s' % ADDRESS

# Send pixels forever
red = (20,0,0)
green = (0,20,0)
blue = (0,0,20)
my_pixels = [(0,0,0)]*200
count = 0
color = 0
while True:
    # for i in range(0,100): 
    #     my_pixels[i] = (0, 0, 0)
    if color >=0 and color <= 199 :
        my_pixels[count] = red
    elif color >= 200 and color <= 399 :
        my_pixels[count] = green
    elif color >= 400 and color <= 599 :
        my_pixels[count] = blue
    color = (color + 1)%600
    count = (count + 1)%200
    # random.shuffle(my_pixels)S
    if client.put_pixels(my_pixels, channel=0):
      print 'color = ' + str(color)
    else:
      print 'not connected'
    time.sleep(0.01)

