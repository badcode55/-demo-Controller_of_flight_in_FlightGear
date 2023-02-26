
import time
import fgmodule.fgenv as fgenv  # flight gear 通信模块
import testlist as fpara


fptest=fpara.FlightParameter()
replayframe=fptest.getValueStr()

print("client begin!")

## 初始化flightgear通信端口
space_num=6
myfgenv = fgenv.fgstart(space_num)


## 开始自动飞行

state = myfgenv.replay(replayframe)
# 复位飞机至飞行起点
##这里有很大的问题，我设置的参数，最后总是坠机


for i in range(1000):
    next_state, reward, done, _ = myfgenv.step(replayframe)
    #人工加入延时,限制收发频率。此处并不好，待修改
    time.sleep(0.1)
'''
epoch = 1000
for i in range(epoch):
#state = myfgenv.replay() #
    while True:
    #下面这行代码是危险的，会不断的重置飞机的高度
        action=fptest.getKey()


    #action = (aileron, elevator, rudder, throttle0, altitude_ft)
    #PID.pid 返回值：
    #  control = str(aileron)+","+str(elevator)+","+str(rudder) + \
    #     ","+str(throttle0)+","+str(throttle1)+"\n"  # type: str
    
    # 格式化控制量为规定格式的控制帧
        action_frame=fptest.getValueStr()
    #action_frame = "%f,%f,%f,%f,%f\n" % action

    # FG执行控制帧给定的相应动作，返回下一个状态的观察值
        next_state, reward, done, _ = myfgenv.step(action_frame)

        if done:# 如果坠机，结束循环
            break

        state = next_state #更新状态为观察到的新的状态

    ##人工加入延时,限制收发频率。此处并不好，待修改
        time.sleep(0.1)

'''