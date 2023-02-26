from queue import Queue
import time
import threading
import fgmodule.fgenv as fgenv  # flight gear 通信模块
import testlist as fpara
import pandas as pd
import numpy as np

Qframe = Queue(200)
filename = "./simpledata.csv"
df = pd.read_csv(filename)
cols_5data = df[['aileron', 'elevator', 'rudder', 'throttle0', 'throttle1', 'alt-ft']]


def sendframe():
    print("发送了一个初始化帧")

    while (True):
        if Qframe.empty():
            if t2.is_alive():
                print("读取未完成")
            else:
                print("读取已完成")
                return
            # TODO：
            # 等待另一个发送线程的结束。
        else:
            frame = Qframe.get()
            # 返回并删除头部元素
            print("send frame is " + frame)
            # TODO:找到发送函数
            # myfgenv.step(frame)实际上是一个训练的函数
            myfgenv.step(frame)
            # 从缓冲区读取一个帧，并且发送到fg
            print("延时控制，睡眠0.1s")
            # 延时控制
            time.sleep(0.1)


## 载入数据

# read_fightrange
def read_fight_range():
    csv_data = pd.read_csv("./simpledata.csv")
    cols_5data = csv_data[['aileron', 'elevator', 'rudder', 'throttle0', 'throttle1', 'alt-ft']]
    print(cols_5data)
    for i in range(cols_5data.shape[0]):
        data_array = np.array(cols_5data.loc[i])
        data_list = data_array.tolist()
        f1 = ""
        for i in data_list:
            f1 += str(i) + ","
        f1.strip(',')
        f1 += "\n"
        if not Qframe.full():
            Qframe.put(f1)
            print("已经插入1frame")
            print(f1)
        else:
            while True:
                print("Qframe is full ,waiting!")
                time.sleep(0.1)
                if not Qframe.full():
                    Qframe.put(f1)
                else:
                    break


print("client begin!")

## 初始化flightgear通信端口
# TODO:这个放在线程之前合适，还是应该放到后面?可能放到后面会更快点。
space_num = 6
myfgenv = fgenv.fgstart(space_num)
state = myfgenv.replay()

t1 = threading.Thread(target=sendframe)
t2 = threading.Thread(target=read_fight_range)

# 读取文件
# 开始自动飞行
t2.start()
t1.start()
