import RPi.GPIO as GPIO
import time
import sys
import tkinter as tk
from sensor import distance
import random

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT)
	GPIO.setup(11, GPIO.OUT)
	GPIO.setup(13, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	
def forward(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

def reverse(tf):
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)
	GPIO.cleanup()

def turn_left(tf):
	GPIO.output(7, True)
	GPIO.output(11, True)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

def turn_right(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()

def pivot_left(tf):
	GPIO.output(7, True)
	GPIO.output(11, False)
	GPIO.output(13, True)
	GPIO.output(15, False)
	time.sleep(tf)
	GPIO.cleanup()
	
def pivot_right(tf):
	GPIO.output(7, False)
	GPIO.output(11, True)
	GPIO.output(13, False)
	GPIO.output(15, True)
	time.sleep(tf)
	GPIO.cleanup()
	
def check_front():
	init()
	dist = distance()
	
	if dist < 15:
		print ('Too close',dist)
		init()
		reverse(2)
		dist = distance()
		if dist < 15:
			print ('Too close',dist)
			init()
			pivot_left(3)
			init()
			reverse(2)
			dist = distance()
			if dist < 15:
				print ('Too close, giving up',dist)
				sys.exit()
				
def autonomy():
	tf = 0.030
	x = random.randrange(0,4)
	
	if x == 0:
		for y in range(30):
			check_front()
			init()
			forward(tf)
	elif x == 1:
		for y in range(30):
			check_front()
			init()
			pivot_left(tf)
	elif x == 2:
		for y in range(30):
			check_front()
			init()
			turn_right(tf)
	elif x == 3:
		for y in range(30):
			check_front()
			init()
			turn_left(tf)
			
for z in range(10):
	autonomy()