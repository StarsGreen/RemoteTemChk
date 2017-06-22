#!/usr/bin/python
#-*- coding: UTF-8 -*-
import codecs
import sys
import os
import time
def WriteTem(data):
	fo=open("datafile",'a')
	fo.write(data+time.time())
	fo.close()
	
