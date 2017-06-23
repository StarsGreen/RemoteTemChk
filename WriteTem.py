#!/usr/bin/python
import sys
import os
import time
import pdb
def WriteTem():
	data=30
	pdb.set_trace()
	fo = open("datafile",'a')
#	fo.write("sdfsfdsf")
	fo.write(str(data)+'		'+time.ctime()+'\n')
	fo.close()
	
