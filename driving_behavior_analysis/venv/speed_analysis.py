import  json
import  numpy as np
import matplotlib
import matplotlib.pyplot as plt


fileobject=open("transfer.txt",'r')
datas=fileobject.readlines()
speed_array=[]
speed_average_array=[]




def speed_plot():
    x=np.arange(len(speed_average_array))
    plt.scatter(x,speed_average_array)
    plt.xlabel('')
    plt.ylabel('')
    plt.show()
    print("s")




for data in datas:
    data=json.loads(data)
    channels=data['channels']
    channel=channels[1]
    speed_list=channel['data']
    speed_array=[speed_data['vehSpeed'] for speed_data in speed_list]
    print(speed_array)
    print('/n')
    speed_average_array.append(np.mean(speed_array)/10.0)
    speed_array.clear()

speed_plot()
print(speed_average_array)



