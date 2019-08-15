
import requests
import  _thread
import  time
from sys import  path
import  sys

sys.path.insert(0,'/home/qiaocheng/PycharmProjects/news_recmd_cloud')

from  Getnews import Getnews


Getnews.mian_getnews()

#
# def recmd_start(threadName):
#     while(1):
#         url = 'http://106.15.234.244:7000/start_news_recmd'
#         requests.get(url)
#         print("sleep tonight")
#
#
#
#
#
#
#
# _thread.start_new_thread(recmd_start,('Thread-1',))
# url='http://106.15.234.244:7000/'
# #url='http://0.0.0.0:7000/'
# print("22222")
# time.sleep(3)
# r = requests.get(url)
# print("=====1"+str(r.content))
# time.sleep(3)
# r = requests.get(url)
# print("=====2"+str(r.content))
# time.sleep(3)
# r = requests.get(url)
# print("=====3"+str(r.content))
# time.sleep(3)
# r = requests.get(url)
