#!/usr/bin/env python
# Example for RC timing reading for Raspberry Pi Must be used with GPIO 0.3.1a or later - earlier verions 
# are not fast enough!

import RPi.GPIO as GPIO, time, os 

DEBUG = 1 
GPIO.setmode(GPIO.BCM) 

GREEN_LED = 23
BLUE_LED = 24
RED_LED = 25

GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

def RCtime (RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	GPIO.setup(GREEN_LED, GPIO.OUT)
	GPIO.setup(BLUE_LED, GPIO.OUT)
	GPIO.setup(RED_LED, GPIO.OUT)

	time.sleep(.1)

	GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
		reading += 1
        return reading 

while True:
        reading = RCtime(18) # Read RC timing using pin #18
	print reading
	if reading < 250:
        	GPIO.output(BLUE_LED, False)
               	GPIO.output(RED_LED, False)
                GPIO.output(GREEN_LED, True)
      
        elif reading < 400:
              	GPIO.output(GREEN_LED, False)
             	GPIO.output(RED_LED, False)
            	GPIO.output(BLUE_LED, True)
        else:
              	GPIO.output(GREEN_LED, False)
         	GPIO.output(BLUE_LED, False)
              	GPIO.output(RED_LED, True)

