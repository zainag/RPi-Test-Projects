#!/usr/bin/env python
# Fan control mod for Raspberry Pi

import RPi.GPIO as GPIO, time, datetime, subprocess, os 

DEBUG = 1 
GPIO.setmode(GPIO.BCM)

# Respective ports on the GPIO header 
FAST = 18
SLOW = 25

# Default settings for fan control
MAX_TEMP = 50
MIN_TEMP = 40
POLL_TIME = 5
 
GPIO.setup(FAST, GPIO.OUT)
GPIO.setup(SLOW, GPIO.OUT)

def get_temperature():
    # Returns the temperature in degrees C
	try:
  		s = subprocess.check_output(["vcgencmd","measure_temp"])
  		return float(s.split("=")[1][:-3])
	except:
		# Something went wrong keep the fan on high
		return MAX_TEMP+1
		
try:
	while True:
		current_temp = get_temperature()
		print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - current temp is ' + str(current_temp)
		
		if	current_temp > MAX_TEMP:
			print 'Setting fan speed to HIGH'
			GPIO.output(SLOW, GPIO.LOW)
			GPIO.output(FAST, GPIO.HIGH)
			POLL_TIME = 5

		elif (current_temp <= MAX_TEMP) and (current_temp > MIN_TEMP):
			print 'Setting fan speed to LOW'
			GPIO.output(FAST, GPIO.LOW)
			GPIO.output(SLOW, GPIO.HIGH)
			POLL_TIME = 10
		else:
			print 'Turn the fan off!'
			GPIO.output(SLOW, GPIO.LOW)
			GPIO.output(FAST, GPIO.LOW)
			POLL_TIME = 15

		time.sleep(POLL_TIME)
		
except KeyboardInterrupt:
	print'\nCtrl-C pressed, exiting now!'
finally:
	GPIO.cleanup()
