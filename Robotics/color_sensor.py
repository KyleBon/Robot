import RPI.GPIO as GPIO
import time



s2 = 19
s3 = 15
signal = 22
NUM_CYCLES = 10


def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(signal, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(s2, GPIO.OUT)
	GPIO.setup(s3, GPIO.OUT)
	print("\n")
	
	
	
	
	
def loop():
	temp = 1
	while(1):
	
		GPIO.output(s2, GPIO.low)
		GPIO.output(s3, GPIO.low)
		time.sleep(0.3)
		start = time.time()
		for impulse_count in range(NUM_CYCLES):
			GPIO.wait_for_edge(signal, GPIO.FALLING)
		duration = time.time() - start
		red = NUM_CYCLES / duration
		
		GPIO.output(s2, GPIO.LOW)
		GPIO.output(s3, GPIO.HIGH)
		time.sleep(0.3)
		start = time.time()
		for impulse_count in range(NUM_CYCLES:
			GPIO.wait_for_edge(signal, GPIO.FALLING)
		duration = time.time() - start
		blue = NUM_CYCLES / duration
		
		
		GPIO.output(s2, GPIO.HIGH)
		GPIO.output(s3, GPIO.HIGH)
		time.sleep(0.3)
		start = time.time()
		for impulse_count in range (NUM_CYCLES):
			GPIO.wait_for_edge(signal, GPIO.FALLING)
		duration = time.time() - start
		green = NUM_CYCLES / duration
		
		
		if green<7000 and blue<7000 and red<12000:
			print ("found the secret item!!!")
			temp=1
		elif red<12000 and blue<12000 and green<12000:
			print ("this item is green, the secret item is red")
			temp=1
		elif green<7000 and red<7000 and blue<12000:
			print ("this item is blue, the secret item is red")
		elif red<10000 and green<10000 and blue<10000 and temp == 1:
			print ("place the object.....")
			temp=0
			
			
			
def endgame():
	GPIO.cleanup()
	
if __name__ == '__main__':

	setup()
	
	try:
		loop()
	
	except KeyboardInterrupt:
		endgame()
		