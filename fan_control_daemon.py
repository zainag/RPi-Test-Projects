#!/usr/bin/env python
# Fan control mod for Raspberry Pi

import RPi.GPIO as GPIO, time, datetime, subprocess, os, logging

from daemon import runner

DEBUG = 1 
GPIO.setmode(GPIO.BCM)

# Respective ports on the GPIO header 
FAST = 18
SLOW = 25

# Default settings for fan control
MAX_TEMP = 50
MIN_TEMP = 40
POLL_TIME = 5

def get_temperature():
    # Returns the temperature in degrees C
	try:
  		s = subprocess.check_output(["vcgencmd","measure_temp"])
  		return float(s.split("=")[1][:-3])
	except:
		# Something went wrong keep the fan on high
		return MAX_TEMP+1

class App():
   
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/var/run/fandaemon/fandaemon.pid'
		self.pidfile_timeout = 5
           
	def run(self):
		GPIO.setup(FAST, GPIO.OUT)
		GPIO.setup(SLOW, GPIO.OUT)
		try:
			while True:
				current_temp = get_temperature()
				logstr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - current temp is ' + str(current_temp)
				logger.info(logstr);
				
				if	current_temp > MAX_TEMP:
					logger.info('Setting fan speed to HIGH')
					GPIO.output(SLOW, GPIO.LOW)
					GPIO.output(FAST, GPIO.HIGH)
					POLL_TIME = 5

				elif (current_temp <= MAX_TEMP) and (current_temp > MIN_TEMP):
					logger.info('Setting fan speed to LOW')
					GPIO.output(FAST, GPIO.LOW)
					GPIO.output(SLOW, GPIO.HIGH)
					POLL_TIME = 10
				else:
					logger.info('Turn the fan off!')
					GPIO.output(SLOW, GPIO.LOW)
					GPIO.output(FAST, GPIO.LOW)
					POLL_TIME = 15

				time.sleep(POLL_TIME)
				
		except:
			logger.error('Exiting now!')
		finally:
			GPIO.cleanup()

app = App()
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("/var/log/fandaemon/fandaemon.log")
handler.setFormatter(formatter)
logger.addHandler(handler)

daemon_runner = runner.DaemonRunner(app)
#This ensures that the logger file handle does not get closed during daemonization
daemon_runner.daemon_context.files_preserve=[handler.stream]
daemon_runner.do_action()
		

