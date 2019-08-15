import  numpy as np
import  pandas as pd
import json
file=open("data.txt",'r')
datas=file.readlines()
car_list=list()
temp = {}
fileObject=open('transfer.txt','w')
fileObject.truncate() #clear the txt
def seperate_channel(channels):
    print(channels)
    temp_list=list()
    for  channel in channels:
        if(channel['id']==1 or channel['id']==3 or channel['id']==4 or channel['id']==15):
            temp_list.append(channel)
    return temp_list


for data in datas:
    data=json.loads(data)
    temp["tboxinfo"]=data["tboxinfo"]
    temp['channels']=seperate_channel(data["channels"])
    jsonobject=json.dumps(temp)
    fileObject.write(jsonobject)
    fileObject.write('\n')
    car_list.append(temp)
    temp.clear()

fileObject.close()
print('data transfer has been finished')

#  print(data)
#while line:
#     print(line)
#     line=file.readline()
#     s1=json.loads(line)

