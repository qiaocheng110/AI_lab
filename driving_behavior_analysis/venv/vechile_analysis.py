import  random
from math import ceil
import  numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm
import matplotlib
import  pandas as pd
#from docutils.nodes import legend
import pymysql
import os
import json

cwd_ch = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd_ch)
print('cwd_ch',cwd_ch)



speed_list=[]
Angle_list=[]
Aspeed_list=[]
Aangle_list=[]
speed_propation=[]
Angle_propation=[]
Aspeed_propation=[]
Aangle_propation=[]
max_speed=0
max_Angle=0
min_speed=0
min_Angle=0
step_size_60=5
def read_data():
    with open("data/data.csv") as f:
        for line in f:
            line = line.rstrip()
            speed_list.append(float(line.split(',')[0]))
            Angle_list.append(float(line.split(',')[1]))
    temp_speed=speed_list[0]
    temp_angle=Angle_list[0]
    for speed in speed_list[1:]:
        Aspeed_list.append(speed-temp_speed)
        temp_speed=speed
    for angle in Angle_list[1:]:
        Aangle_list.append(angle-temp_angle)
        temp_angle=angle
    global max_speed
    global max_Angle
    global min_speed
    global min_Angle
    max_speed=max(speed_list)
    max_Angle=max(Angle_list)
    min_speed=min(speed_list)
    min_Angle=min(Angle_list)




def draw_speed_bar():
    speed_array=np.array(sorted(speed_list))
    if(max_speed<60):
        speed_propation.append((speed_array<2.5).sum()/speed_array.size)
        speed_propation.append(((2.5<=speed_array) & (speed_array<7.5)).sum()/speed_array.size)
        speed_propation.append(((7.5<=speed_array) & (speed_array<12.5)).sum()/speed_array.size)
        speed_propation.append(((12.5<=speed_array) & (speed_array<17.5)).sum()/speed_array.size)
        speed_propation.append(((17.5<=speed_array) & (speed_array<22.5)).sum()/speed_array.size)
        speed_propation.append(((22.5<=speed_array) & (speed_array<27.5)).sum()/speed_array.size)
        speed_propation.append(((27.5<=speed_array) & (speed_array<32.5)).sum()/speed_array.size)
        speed_propation.append(((32.5<=speed_array) & (speed_array<37.5)).sum()/speed_array.size)
        speed_propation.append(((37.5<=speed_array) & (speed_array<42.5)).sum()/speed_array.size)
        speed_propation.append(((42.5<=speed_array) & (speed_array<47.5)).sum()/speed_array.size)
        speed_propation.append(((47.5<=speed_array) & (speed_array<52.5)).sum()/speed_array.size)
        speed_propation.append(((52.5<=speed_array) & (speed_array<57.5)).sum()/speed_array.size)
        speed_propation.append(((57.5<=speed_array) & (speed_array<62.5)).sum()/speed_array.size)
        x_pos=np.arange(0,61,5)
    elif(60<=max_speed<120):
        speed_propation.append((speed_array<5).sum()/speed_array.size)
        speed_propation.append(((5<=speed_array) & (speed_array<15)).sum()/speed_array.size)
        speed_propation.append(((15<=speed_array) & (speed_array<25)).sum()/speed_array.size)
        speed_propation.append(((25<=speed_array) & (speed_array<35)).sum()/speed_array.size)
        speed_propation.append(((35<=speed_array) & (speed_array<45)).sum()/speed_array.size)
        speed_propation.append(((45<=speed_array) & (speed_array<55)).sum()/speed_array.size)
        speed_propation.append(((55<=speed_array) & (speed_array<65)).sum()/speed_array.size)
        speed_propation.append(((65<=speed_array) & (speed_array<75)).sum()/speed_array.size)
        speed_propation.append(((75<=speed_array) & (speed_array<85)).sum()/speed_array.size)
        speed_propation.append(((85<=speed_array) & (speed_array<95)).sum()/speed_array.size)
        speed_propation.append(((95<=speed_array) & (speed_array<105)).sum()/speed_array.size)
        speed_propation.append(((105<=speed_array) & (speed_array<115)).sum()/speed_array.size)
        speed_propation.append(((115<=speed_array) & (speed_array<125)).sum()/speed_array.size)
        x_pos=np.arange(0,121,10)
    elif(max_speed>120):
        speed_propation.append((speed_array < 5).sum() / speed_array.size)
        speed_propation.append(((5 <= speed_array) & (speed_array < 15)).sum() / speed_array.size)
        speed_propation.append(((15 <= speed_array) & (speed_array < 25)).sum() / speed_array.size)
        speed_propation.append(((25 <= speed_array) & (speed_array < 35)).sum() / speed_array.size)
        speed_propation.append(((35 <= speed_array) & (speed_array < 45)).sum() / speed_array.size)
        speed_propation.append(((45 <= speed_array) & (speed_array < 55)).sum() / speed_array.size)
        speed_propation.append(((55 <= speed_array) & (speed_array < 65)).sum() / speed_array.size)
        speed_propation.append(((65 <= speed_array) & (speed_array < 75)).sum() / speed_array.size)
        speed_propation.append(((75 <= speed_array) & (speed_array < 85)).sum() / speed_array.size)
        speed_propation.append(((85 <= speed_array) & (speed_array < 95)).sum() / speed_array.size)
        speed_propation.append(((95 <= speed_array) & (speed_array < 105)).sum() / speed_array.size)
        speed_propation.append(((105 <= speed_array) & (speed_array < 115)).sum() / speed_array.size)
        speed_propation.append(((115 <= speed_array) & (speed_array < 125)).sum() / speed_array.size)
        speed_propation.append(((125 <= speed_array) & (speed_array < 140)).sum() / speed_array.size)
        speed_propation.append((140 <= speed_array).sum() / speed_array.size)
        x_pos = np.arange(0, 141, 10)
    cmap1=cm.ScalarMappable(col.Normalize(min(speed_propation),max(speed_propation),cm.hot))
    print(x_pos.size)
    print(len(speed_propation))
    plt.bar(x_pos,np.array(speed_propation),align='center',width=2.5,alpha=0.5,color=cmap1.to_rgba(np.array(speed_propation)))
    plt.xlabel("Vehicle Speed [km/h]")
    plt.ylabel("Proportion")
    plt.savefig('./pic/draw_speed_bar.png')
    plt.close()
   # plt.show()

angle_step_size=10
def draw_angle_bar():
    Angle_array=np.array(sorted(Angle_list))
    high_boundary=(max_Angle//angle_step_size)*angle_step_size+angle_step_size
    low_boundary=(min_Angle//angle_step_size)*angle_step_size-angle_step_size
    x_pos_temp=np.arange(low_boundary,high_boundary+1,angle_step_size)
    x_pos=[]
    for pos in x_pos_temp[0:-1]:
        Angle_propation.append(((pos<=Angle_array) & (Angle_array<pos+angle_step_size)).sum()/Angle_array.size)
        x_pos.append(pos+angle_step_size/2)
    cmap1=cm.ScalarMappable(col.Normalize(min(Angle_propation),max(Angle_propation),cm.hot))
    plt.bar(x_pos,Angle_propation,align='center',width=6.5,alpha=0.5,color=cmap1.to_rgba(Angle_propation))
    plt.xlabel("Wheel Angle [deg]")
    plt.ylabel("Proportion")
    plt.savefig('./pic/draw_angle_bar.png')
    plt.close()
   # plt.show()

#加速度
aspeed_size=1
def draw_accelerated_bar():
    Aspeed_array=np.array(sorted(Aspeed_list))
    Aspeed_mini=Aspeed_array[(-10<=Aspeed_array)&(Aspeed_array<=10)] #合理范围内的数据列表
    max_aspeed=max(Aspeed_mini)
    min_aspeed=min(Aspeed_mini)
    high_boundary=(max_aspeed//aspeed_size)*aspeed_size+aspeed_size
    low_boundary=(min_aspeed//aspeed_size)*aspeed_size-aspeed_size
    x_pos_temp=np.arange(low_boundary,high_boundary+1,aspeed_size)
    x_pos=[]
    for pos in x_pos_temp[0:-1]:
        Aspeed_propation.append(((pos<=Aspeed_mini)&(Aspeed_mini<pos+aspeed_size)).sum()/Aspeed_array.size)
        x_pos.append(pos+aspeed_size/2)
    Aspeed_propation.insert(0,(Aspeed_array<-10).sum()/Aspeed_array.size)
    Aspeed_propation.append((Aspeed_array>10).sum()/Aspeed_array.size)
    x_pos.insert(0,-11)
    x_pos.append(11)
    cmap1 = cm.ScalarMappable(col.Normalize(min(Aspeed_propation), max(Aspeed_propation), cm.hot))
    plt.bar(x_pos, Aspeed_propation, align='center', width=0.8, alpha=0.5, color=cmap1.to_rgba(Aspeed_propation))
    plt.xlabel("Accelerated Speed [m/s2]")
    plt.ylabel("Proportion")
    plt.text(x_pos[0],Aspeed_propation[0]+0.01,str('<-10'),ha='center')
    plt.text(x_pos[-1],Aspeed_propation[-1]+0.01,str('>10'),ha='center')
    plt.savefig('./pic/draw_accelerated_bar.png')
    plt.close()
   # plt.show()


angle_size=4

def draw_angular_bar():
    Aangle_array=np.array(sorted(Aangle_list))
    Aangle_mini=Aangle_array[(-100<=Aangle_array)&(Aangle_array<=100)] #合理范围内的数据列表
    max_aangle=max(Aangle_mini)
    min_aangle=min(Aangle_mini)
    high_boundary=(max_aangle//angle_size)*angle_size+angle_size
    low_boundary=(min_aangle//angle_size)*angle_size-angle_size
    x_pos_temp = np.arange(low_boundary, high_boundary + 1, angle_size)
    x_pos = []
    for pos in x_pos_temp:
        Aangle_propation.append(((pos<=Aangle_mini)&(Aangle_mini<pos+angle_size)).sum()/Aangle_array.size)
        x_pos.append(pos+angle_size/2)
    Aangle_propation.insert(0, (Aangle_array < -100).sum() / Aangle_array.size)
    Aangle_propation.append((Aangle_array > 100).sum() / Aangle_array.size)
    x_pos.insert(0,-100-angle_size)
    x_pos.append(100+angle_size)
    cmap1 = cm.ScalarMappable(col.Normalize(min(Aangle_propation), max(Aangle_propation), cm.hot))
    plt.bar(x_pos, Aangle_propation, align='center', width=2.5, alpha=0.5, color=cmap1.to_rgba(Aangle_propation))
    plt.xlabel("Angular Acceleration [deg/s]")
    plt.ylabel("Proportion")
    plt.text(x_pos[0],Aangle_propation[0]+0.01,str('<-110'),ha='center')
    plt.text(x_pos[-1],Aangle_propation[-1]+0.01,str('>110'),ha='center')
    plt.savefig('./pic/draw_angular_bar.png')
    plt.close()
    #plt.show()


'''
驾驶行为KPI计算
'''
distance=30#行驶距离(km)
#平均车速
def average_speed():
    avg_speed=sum(speed_list)/len(speed_list)
    print("=====平均车速======",avg_speed)
    return  avg_speed

#超速比例
def overspeed():
    num=(np.array(speed_list)>120).sum()
    overspeed_per=num/len(speed_list)
    print("=====超速指标=======",overspeed_per)
    return overspeed_per

#超速次数
def eval_vspeed_times():
    # a=[10,20,30,40,50,60,80,123,123,124,121,122,145,87,68,67,123,125,125,12,9,8,6,12,123,12,1,1]
    count=0
    flag=False
    # speed_list=a
    for speed in speed_list:
        if(speed>120 ):
            if(flag==False):
                count=count+1
                flag=True
                continue
            else:
                continue
        flag=False
    overspeed_freq=count/distance*1000#overspeed times  in 1000km
    print("====超速次数===",overspeed_freq)
    return  overspeed_freq

#急刹车次数<-10km/h
def fun_brake():
    count=0
    flag=False
    for accelerate in Aspeed_list:
        if(accelerate<-10):
            if(flag==False):
                count=count+1
                flag=True
                continue
            else:
                continue
        flag=False
    brake_freq=count/distance*1000
    print("====急刹车次数===",brake_freq)
    return brake_freq


#急加速次数>10km/h
def fun_accelerate():
    count=0
    temp=0
    flag=False
    for accelerate in Aspeed_list:
        if(accelerate>10):
            temp = temp + 1
            if(flag==False):
                count=count+1
                flag=True
                continue
            else:
                continue
        flag=False
    accelerate_freq=count/distance*1000
    print("====急加速====",accelerate_freq)
    return accelerate_freq


#怠速比例
def idle():
    count=(np.array(speed_list)==0).sum()
    idle_per=count/len(speed_list)
    print("====怠速比例===",idle_per)
    return  idle_per

#急转弯
def sharp_turn():
    count=0
    temp=0
    flag=False
    for angular in Aangle_list:
        if(angular>100 or angular<-100):
            temp = temp + 1
            if(flag==False):
                count=count+1
                flag=True
                continue
            else:
                continue
        flag=False
    accelerate_freq=count/distance*1000
    print("====急转弯====",accelerate_freq)
    return accelerate_freq


def start_analysis():
    dictObj={}
    read_data()
    draw_speed_bar()
    draw_angle_bar()
    draw_accelerated_bar()
    draw_angular_bar()
    speed_propation.clear()
    Angle_propation.clear()
    Aspeed_propation.clear()
    Aangle_propation.clear()
    dictObj['average_speed']=average_speed()
    dictObj['overspeed']=overspeed()
    dictObj['eval_vspeed_times']=eval_vspeed_times()
    dictObj['fun_brake']=fun_brake()
    dictObj['fun_accelerate']=fun_accelerate()
    dictObj['sharp_turn']=sharp_turn()
    dictObj['idle']=idle()
    jsobj=json.dumps(dictObj)
    speed_list.clear()
    Angle_list.clear()
    Aspeed_list.clear()
    Aangle_list.clear()
    fileObject=open('./analysis_data/analysis_data.json','w')
    fileObject.write(jsobj)
    fileObject.close()
    return "finish the main"
# main()
# if __name__ == '__main__':
#     read_data()
#     draw_speed_bar()
#     draw_angle_bar()
#     draw_accelerated_bar()
#     draw_angular_bar()
#     average_speed()
#     overspeed()
#     eval_vspeed_times()
#     fun_brake()
#     fun_accelerate()
#     sharp_turn()
#     idle()