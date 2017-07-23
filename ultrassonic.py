from HCSR-04 import hcsr
import time
import pigpio

pi = pigpio.pi()
ultrassonic = hcsr(pi, 20, 21) 		#__init__(self, pi, trig, echo):

while True:
	distance = ultrassonic.get_distance(pi)
	distance = round(distance, 2)
	print distance

	time.sleep(1)
