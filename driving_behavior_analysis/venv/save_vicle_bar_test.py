# -*- coding: utf-8 -*-
import pymysql
import  os
import time
def now_to_date(format_string="%Y-%m-%d %H:%M:%S"):
    time_stamp=int(time.time())
    time_array=time.localtime(time_stamp)
    str_date=time.strftime(format_string,time_array)
    return str_date

def save_vichle_bar():
    date_time=now_to_date()
    pic_list = []
    try:
        files = os.listdir('./pic')
        for file in files:
            f = open('./pic/%s' % (file))
            #f = open('./pic/%s' % (file),encoding='utf-8')
            file = file.split('.')[0]
            data = f.read()
            f.close()
            pic_list.append(data)
    except IOError as e:
        print("Error %d: %s" %(e.args[0],e.args[1]))
        sys.exit(1)



    try:
        db=pymysql.connect(host="rm-uf6s62dsd72ecgx15ro.mysql.rds.aliyuncs.com",user="tsp_ar",passwd="root=0514tsp",db="tsp_ar",port=3306)
        cursor = db.cursor()
        #cursor.execute("INSERT INTO vicle_analysis_pic (time) VALUES ('%s')" %(date_time))

        #cursor.execute("INSERT INTO vicle_analysis_pic (time,'accelerate_bar','angle_bar','angular_bar','speed_bar') VALUES ('%s','%s','%s','%s','%s')" %(date_time,pymysql.Binary(pic_list[0]),pymysql.Binary(pic_list[1]),pymysql.Binary(pic_list[2]),pymysql.Binary(pic_list[3])))
       # cursor.execute("INSERT INTO vicle_analysis_pic (time) VALUES ('%s')" %(date_time))
        #cursor.execute("INSERT INTO vicle_analysis_pic SET speed_bar='%s'" %(pic_list[0]))
        sql="INSERT INTO vicle_analysis_pic (speed_bar) VALUES  (%s)"
        # cursor.execute("INSERT INTO vicle_analysis_pic SET time='%s'" %date_time)
        cursor.execute(sql,pic_list[0])
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print("connect the db failure",e)
        sys.exit(1)


save_vichle_bar() 