#!/usr/bin/python
import RPi.GPIO as GPIO
import time
def ReadTem():
	file=open("/sys/bus/w1/devices/28-0000024a8c0b/w1_slave")
	text=file.read()
	file.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature
