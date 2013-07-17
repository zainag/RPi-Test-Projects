#!/usr/bin/env python
# Fan control mod for Raspberry Pi

import RPi.GPIO as GPIO, time,  os 

DEBUG = 1 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)
time.sleep(15)
GPIO.output(18, GPIO.LOW)
GPIO.cleanup()
