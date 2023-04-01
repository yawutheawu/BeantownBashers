from time import time
import keyboard
from pyglet.window import key as k

def inputBeat(key, frame):
	milli = frame * 1000
	start = int(time() * 1000)
	end = start + milli
	print("Press: \'" + key + "\'")
	while(start <= end):
		ans = keyboard.is_pressed(key)
		if(start >= end):
			return False
		if(ans):
			ans = False
			return True

		start = int(time() * 1000)
	return False


'''
good = inputBeat("w", 5)
if(good):
	print("Input on time")
else:
	print("Incorrect or out of time")
'''