from time import time
import keyboard

def inputBeat(key, frame):
	milli = frame * 1000
	start = int(time() * 1000)
	end = start + milli
	#print("Press: \'" + key + "\'")
	p = False
	while(start <= end):
		ans = keyboard.is_pressed(' ')
		if(start >= end):
			return False
		if(ans and start <= end):
			ans = False
			#print("Pressed")
			return True

		start = int(time() * 1000)
	return False