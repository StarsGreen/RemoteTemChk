#!/usr/bin/python
import os
import sys
import time
import WriteTem
import ReadTem
import MySql
import pdb

if __name__ == '__main__':
	while 1:
		tem=ReadTem.ReadTem()
#		print tem[0],tem[1],tem[2]
#		pdb.set_trace()
		if MySql.MySqlWrite(tem[0],tem[1],tem[2])!=1:
			pdb.set_trace()
			print "write data to server error!"
		WriteTem.WriteTem(tem[0],tem[1],tem[2])
		time.sleep(1000)		
			 		
