#!/usr/bin/env python3.6
from concurrent.futures import ThreadPoolExecutor
import  concurrent
import requests
import os
import  time
DEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "download")
BASE_URL = "http://flupy.org/data/flags"
CC_LIST = ("CN", "US", "JP", "EG")

if not os.path.exists(DEST_DIR):
    os.mkdir(DEST_DIR)


def get_img(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    response = requests.get(url)
    return response.content

def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)

def download_one(cc):
    img = get_img(cc)
    save_img(img, cc.lower() + ".gif")
    return cc

def download_many(cc_list):
    with ThreadPoolExecutor(max_workers=5) as exector:
        future_list = []
        for cc in cc_list:
    # 使用submit提交执行的函数到线程池中，并返回futer对象（非阻塞）
            future = exector.submit(download_one, cc)
            future_list.append(future)
            print(cc, future)

        result = []
    # as_completed方法传入一个Future迭代器，然后在Future对象运行结束之后yield Future
        for future in concurrent.futures.as_completed(future_list):
    # 通过result()方法获取结果
            res = future.result()
            print(res, future)
            result.append(res)
    return len(result)


if __name__ == "__main__":
    while(1):
        time.sleep(0.1)
        download_many(CC_LIST)