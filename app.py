#!/usr/bin/env python
#
# basic launchpad programming
# press any button to light its LED 
# press stop to change color to green
# press trk on to change to orange
# press to solo to change to red
# 
# press arm to exit

import sys

try:
	import launchpad_py as launchpad
except ImportError:
	try:
		import launchpad
	except ImportError:
		sys.exit("error loading launchpad.py")

import random
from pygame import time as t

########
####
# callback(launchpad, [X,Y,true/false])
def callback(lp, status):
    print(status)
    if status[0] == 8 and status[2] == False:
        if status[1] == 1:
            return 'draw'
        elif status[1] == 2:
            return 'dice'
        elif status[1] == 8:
            return 'exit'
        else:
            return 'none'

########
####
# dice (launchpad)
def dice(lp):
    lp.LedCtrlString(str(random.randint(1,20)),0,3,-1,50)
    return

########
####
# draw
def draw(lp,status):
    print("draw mode")
    mode = 'green'
    while True:
        if lp.ButtonChanged() is True:
            status = lp.ButtonStateXY()
            if status[0] == 8 and status[1] == 8 and status[2] is False:
                break
            elif status[0] == 8 and status[1] == 4:
                mode = 'eraser'
                lp.LedCtrlXY(status[0], status[1], 1, 1)
                lp.LedCtrlXY(8, 7, 0, 0)
                lp.LedCtrlXY(8, 6, 0, 0)
                lp.LedCtrlXY(8, 5, 0, 0)
            elif status[0] == 8 and status[1] == 7:
                mode = 'red'
                lp.LedCtrlXY(status[0], status[1], 3, 0)
                lp.LedCtrlXY(8, 6, 0, 0)
                lp.LedCtrlXY(8, 4, 0, 0)
                lp.LedCtrlXY(8, 5, 0, 0)
            elif status[0] == 8 and status[1] == 6:
                mode = 'orange' 
                lp.LedCtrlXY(status[0], status[1], 3, 3)
                lp.LedCtrlXY(8, 5, 0, 0)
                lp.LedCtrlXY(8, 4, 0, 0)
                lp.LedCtrlXY(8, 7, 0, 0)
            elif status[0] == 8 and status[1] == 5:
                mode = 'green' 
                lp.LedCtrlXY(status[0], status[1], 0, 3)
                lp.LedCtrlXY(8, 6, 0, 0)
                lp.LedCtrlXY(8, 4, 0, 0)
                lp.LedCtrlXY(8, 7, 0, 0)
            else:
                if mode == 'green':
                    colors = [0,3]
                elif mode == 'red':
                    colors = [3,0]
                elif mode == 'eraser':
                    colors = [0,0]
                else:
                    colors = [3,3]
                if status[2] is True:
                    lp.LedCtrlXY(status[0], status[1], colors[0], colors[1])
    return
##########################
######################
###### MAIN #######
######################
##########################

def main():

### CONNECT ###
	lp = launchpad.Launchpad();
	if lp.Open():
		print("Launchpad Mk1/S/Mini")
        else:
            return
        lp.Reset()
        lp.ButtonFlush()
###############

### INIT ###
        while True:
            if lp.ButtonChanged() is True:
                status=lp.ButtonStateXY()
                output = callback(lp,status)
                if output == 'exit':
                    break
                elif output == 'dice':
                    dice(lp)
                elif output == 'draw':
                    draw(lp,status)

        t.delay(100)
	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()
