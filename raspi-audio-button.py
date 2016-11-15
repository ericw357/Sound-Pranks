#!/usr/bin/env python

import os
import subprocess
from time import sleep
import logging
import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

def rndmp3 ():
	randomfile = random.choice(os.listdir("/home/pi/mp3/cammode/"))
	file = ' /home/pi/mp3/cammode/'+ randomfile
#	subprocess.call(["/home/pi/Record.sh 10 &"], shell=True)
	subprocess.call(["mpg123 -q" + file + "&"], shell=True)
	logging.basicConfig(level=logging.INFO,
			filename='/var/www/html/index.html',
			format='%(asctime)s    %(message)s')
	logging.info(randomfile)
	f = open('/var/www/html/index.html','a')
	f.write('<a href=/'+randomfile +'>Listen</a><br>')
	f.close()


while True:
	if (GPIO.input(23) == True):
		sleep(3);
		rndmp3 ();
		sleep(60);
