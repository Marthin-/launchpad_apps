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


def main():

	lp = launchpad.Launchpad();
	if lp.Open():
		print("Launchpad Mk1/S/Mini")
	# create an instance

        lp.LedAllOn()
        t.delay(1000)
        lp.Reset()

        lp.ButtonFlush()

        totalInput = 0
    
        status = [0, 0, False]

        mode = 'green'

        while True:
            if lp.ButtonChanged() is True:
                status = lp.ButtonStateXY()
                print(status)
                if status[0] == 8 and status[1] == 8 and status[2] is False:
                    break
                elif status[0] == 8 and status[1] == 7:
                    mode = 'red'
                    lp.LedCtrlXY(status[0], status[1], 3, 0)
                    lp.LedCtrlXY(8, 6, 0, 0)
                    lp.LedCtrlXY(8, 5, 0, 0)
                elif status[0] == 8 and status[1] == 6:
                    mode = 'orange' 
                    lp.LedCtrlXY(status[0], status[1], 3, 3)
                    lp.LedCtrlXY(8, 5, 0, 0)
                    lp.LedCtrlXY(8, 7, 0, 0)
                elif status[0] == 8 and status[1] == 5:
                    mode = 'green' 
                    lp.LedCtrlXY(status[0], status[1], 0, 3)
                    lp.LedCtrlXY(8, 6, 0, 0)
                    lp.LedCtrlXY(8, 7, 0, 0)
                else:
                    if mode == 'green':
                        colors = [0,3]
                    elif mode == 'red':
                        colors = [3,0]
                    else:
                        colors = [3,3]
                    if status[2] is True:
                        lp.LedCtrlXY(status[0], status[1], colors[0], colors[1])

        lp.LedCtrlString( 'exit', 3, 3, -1, 50 )
        t.delay(1000)
	lp.Reset() # turn all LEDs off
	lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

	
if __name__ == '__main__':
	main()
