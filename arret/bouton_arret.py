#!/bin/python3

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def fermeture(channel):
	os.system("/usr/local/bin/lcd_setup arret")
	os.system("sudo shutdown -h now") 

GPIO.add_event_detect(4, GPIO.FALLING, callback = fermeture, bouncetime = 2000)

while 1:
	time.sleep(1)

