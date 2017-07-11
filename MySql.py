
#/usr/bin/python
import MySQLdb
import time
import os
import pdb
def MySqlWrite(data1,data2,data3):
	flag=1;
#	pdb.set_trace()
	db = MySQLdb.connect(host="60.205.185.77",port=3306,user='worker',passwd='302518',db='TemChk')
#	pdb.set_trace()
	cursor = db.cursor();
	sql1='INSERT INTO data_history(data1,data2,data3) VALUES ("%s","%s","%s")' % (data1,data2,data3);
#	pdb.set_trace()
	try:
		cursor.execute(sql1);
		db.commit();
	except:
		flag=0;
		db.rollback();
		print "connetion error!"
	db.close();
#	pdb.set_trace()
#	db2 = MySQLdb.connect(host="60.205.185.77",port=3306,user='worker',passwd='302518',db='TemChk')
#	pdb.set_trace()
#	cursor2 = db2.cursor()
#	current_time=time.ctime()
#	sql2='update data_realtime set data1="%s",set data2="%s",set data3="%s" where id = 1' % (data1,data2,data3)
#	sql2='update data_realtime set data1="%s",data2="%s",data3="%s" where id=1'% (data1,data2,data3)
#	pdb.set_trace()
#	try:
#		cursor2.execute(sql2);
#		db2.commit();
#	except:
#		pdb.set_trace()
#		flag=0;
#		db2.rollback();
#		print "connetion error!"
#	db2.close();
#	return flag;
