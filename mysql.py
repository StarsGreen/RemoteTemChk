#/usr/bin/python
import MySQLdb
import time
import os
def MySQLWrite(TemData):
	flag=1;
	db = MySQLdb.connect("60.205.185.77:3306","worker","302518","TemData");
	cursor = db.cursor();
	sql="INSERT INTO TemData(tem_data,sub_time) VALUES(%s,%s)" %(TemData,time.time());
	try:
		cursor.execute(sql);
		db.commit();
	except:
		flag=0;
		db.rollback();
		print "connetion error!"
	db.close();
	return flag;
