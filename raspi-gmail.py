#!/usr/bin/env python
 
import RPi.GPIO as GPIO, feedparser, time
 
DEBUG = 1
 
USERNAME = "verma.rahul" # just the part before the @ sign, add yours here
PASSWORD = "mraV121201"
 
NEWMAIL_OFFSET = 0 # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 10 # check mail every 10 seconds
 
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
 
while True:
 	count = 0;
	newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
 
	if DEBUG:
		print "You have", newmails, "new emails!"
 
	if newmails > NEWMAIL_OFFSET:
		GPIO.output(RED_LED, False)
		while count < 20:
			time.sleep(0.5)
			GPIO.output(GREEN_LED, True)
			time.sleep(0.5)
			GPIO.output(GREEN_LED, False)
			count = count + 1
	else:
		GPIO.output(GREEN_LED, False)
		while count < 20:
			time.sleep(0.5)
			GPIO.output(RED_LED, True)
			time.sleep(0.5)
			GPIO.output(RED_LED,False)
			count = count + 1
