import time
from roboclaw import Roboclaw

#Windows comport name
rc = Roboclaw("COM11",115200)
#Linux comport name
#rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
address = 0x80

while(1):
	rc.ForwardM1(address,32)	#1/4 power forward
	rc.BackwardM2(address,32)	
	time.sleep(2)