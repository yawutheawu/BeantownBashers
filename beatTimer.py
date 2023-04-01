#Derek 4/1/23 Beat Timer
from time import time

def inputBeat(key, frame):
	milli = frame * 1000
	start = int(time() * 1000)
	end = start + milli
	print(start)
	print(end)
	while(start <= end):
		ans = str(input("Type \'" + key + "\'"))
		if(ans == key and start <= end):
			return True
		start = int(time() * 1000)
	return False



good = inputBeat("w", 5)
if(good):
	print("Input on time")
else:
	print("Incorrect or out of time")
