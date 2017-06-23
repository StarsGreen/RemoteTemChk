#!/usr/bin/python
import os
import sys
import time
import WriteTem
import ReadTem
import MySql

if __name__ == '__main__':
	while 1:
		if MySql.MySqlWrite(30)!=1:
			print "write data to server error!"
		WriteTem.WriteTem(30)
		
			 		
