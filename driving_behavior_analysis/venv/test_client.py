#导入必要的模块
import numpy as np
import matplotlib.pyplot as plt
import  requests
import  json
import  time
import base64
pic_list=["draw_accelerated_bar","draw_angle_bar","draw_angular_bar","draw_speed_bar"]

def start_analysis_func():
    url='http://106.15.234.244:7000/start_vechile_analysis'
    results=requests.get(url)
    results.encoding='utf-8'
    content=results.text
    print(content)

def get_analysis_bar():
    url='http://106.15.234.244:7000/get_analysis_bar'
    results=requests.get(url)
    data=json.loads(results.text)
    for pic in pic_list:
        base64_data=data[pic]
        byte_data=base64.b64decode(base64_data)
        file=open("./pic/%s_n.png" %(pic),'wb')
        file.write(byte_data)
        file.close()
    print(data['content'])

def get_analysis_data():
    url='http://106.15.234.244:7000/get_analysis_data'
    results=requests.get(url)
    data=json.loads(results.text)
    for property in data:
        print(data[property])

def recmd_start():
    print("1111")
    url = 'http://106.15.234.244:7000/start_news_recmd'
    #url = 'http://0.0.0.0:7000/start_news_recmd'
    r = requests.get(url)
    print(r.content)


#recmd_start()
n=10
while(n!=0):
    n=n-1
    time.sleep(0.5)
    start_analysis_func()
    get_analysis_bar()
    get_analysis_data()
#
# if __name__ == '__main__':
#     start_analysis_func()
#     get_analysis_bar()
#     get_analysis_data()



# while(1):
#     time.sleep(1)
# n=10
# start=time.clock()
# while(n!=0):
#     n=n-1
#     time.sleep(0.1)
#     get_analysis_data()
# print(time.clock()-start)
    # get_analysis_bar()
    # get_analysis_data()

#产生测试数据
# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# ax1 = fig.add_subplot(111)
# #设置标题
# ax1.set_title('Scatter Plot')
# #设置X轴标签
# plt.xlabel('X')
# #设置Y轴标签
# plt.ylabel('Y')
# #画散点图
# ax1.scatter(x,y,c = 'r',marker = 'o')
# #设置图标
# plt.legend('x1')
# #显示所画的图
# plt.show()
