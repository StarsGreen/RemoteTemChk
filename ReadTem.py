import RPi.GPIO as GPIO
import time
import json
def ReadTem():
        file=open("/sys/bus/w1/devices/28-0000024a8c0b/w1_slave")
        #read temprature
        text=file.read()
        #close file
        file.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return temperature
