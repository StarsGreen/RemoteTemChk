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
		print time.ctime()
		tem=ReadTem.ReadTem()
#		print tem[0],tem[1],tem[2]
#		pdb.set_trace()
		MySql.MySqlWrite(tem[0],tem[1],tem[2])
#			pdb.set_trace()
#			print "write data to server error!"
		WriteTem.WriteTem(tem[0],tem[1],tem[2])
#		time.sleep(0.5)	
#		pdb.set_trace()	
		print time.ctime()
#		pdb.set_trace()	
	 		
