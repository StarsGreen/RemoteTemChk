#/usr/bin/python
import MySQLdb
import time
import os
import pdb
def MySqlWrite(TemData):
	flag=1;
	pdb.set_trace()
	db = MySQLdb.connect(host="60.205.185.77",port=3306,user='worker',passwd='302518',db='TemChk')
	pdb.set_trace()
	cursor = db.cursor();
	sql='INSERT INTO TemData(data,time) VALUES("%s","%s")' % (TemData,time.ctime());
	pdb.set_trace()
	try:
		cursor.execute(sql);
		db.commit();
	except:
		flag=0;
		db.rollback();
		print "connetion error!"
	db.close();
	return flag;
