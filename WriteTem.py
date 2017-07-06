#!/usr/bin/python
import sys
import os
import time
import pdb
def WriteTem(data1,data2,data3):
#	pdb.set_trace()
	fo = open("datafile",'a')
#	fo.write("sdfsfdsf")
	fo.write(str(data1)+'	'+str(data2)+'	'+str(data3)+'	'+time.ctime()+'\n')
	fo.close()
	
