#!/usr/bin/python
import RPi.GPIO as GPIO
import time
def ReadTem():
	file1=open("/sys/bus/w1/devices/28-0316b41664ff/w1_slave")
	file2=open("/sys/bus/w1/devices/28-04163431e4ff/w1_slave")
	file3=open("/sys/bus/w1/devices/28-0416c0048fff/w1_slave")
	text1=file1.read()
	text2=file2.read()
	text3=file3.read()
	file1.close()
	file2.close()
	file3.close()
	secondline1 = text1.split("\n")[1]
	temperaturedata1 = secondline1.split(" ")[9]
	temperature1 = float(temperaturedata1[2:])
	temperature1 = temperature1/1000
	secondline2 = text2.split("\n")[1]
	temperaturedata2 = secondline2.split(" ")[9]
	temperature2 = float(temperaturedata2[2:])
	temperature2 = temperature2/1000
	secondline3 = text3.split("\n")[1]
	temperaturedata3 = secondline3.split(" ")[9]
	temperature3 = float(temperaturedata3[2:])
	temperature3 = temperature3/1000
	tem=[str(temperature1),str(temperature2),str(temperature3)]
	return tem
