import RPi.GPIO as GPIO
import time

def distance():
	GPIO.setmode(GPIO.BOARD)
	
	GPIO_trigger = 12
	GPIO_echo = 18
	
	GPIO.setup(GPIO_trigger, GPIO.OUT)
	GPIO.setup(GPIO_echo, GPIO.IN)
	
	GPIO.output(GPIO_trigger, True)
	
	time.sleep(0.00001)
	GPIO.output(GPIO_trigger, False)
	
	StartTime = time.time()
	StopTime = time.time()
	
	while GPIO.input(GPIO_echo) == 0:
			StartTime = time.time()
			
	while GPIO.input(GPIO_echo) == 1:
			StopTime = time.time()
			
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2
	
	return distance
	
if __name__ == '__main__':
		try:
			while True:
					dist = distance()
					# print ("measure distance = %.1f cm" % dist)
					time.sleep(1)
					
		except KeyboardInterrupt:
			   # print ("measurement stopped by user...")
			   GPIO.cleanup()