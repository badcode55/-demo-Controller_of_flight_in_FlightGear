# 试飞讲评系统Teaching and evaluation  tools system for aviation experiments

此项目为飞参序列驱动的三维可视化试飞讲评系统对外演示版本，不涉及核心代码。

公开的代码仅包括一段对FlightGear控制的演示。

## 环境说明

- Windows 11
- [Flight gear](https://www.flightgear.org/) 2022.3
- [Python](https://www.python.org/downloads/) 3.9.7
- [conda](https://www.anaconda.com/) 4.12.0
- numpy 1.22.3
- pandas 1.3.4

## 使用说明

0. 将本项目config 目录下的`fgudp.xml` 放入 ` $FGROOT\data\Protocol\` 目录下，

   [^$FGROOT]: 比如，你的FlightGear软件安装在C:\FlightGear\ ,那么$FGROOT就是指C:\FlightGear

   

1. 打开flightgear软件，在`设置`中输入以下字段(仅设置一次即可)

```shell
--allow-nasal-from-sockets
--telnet=5555
--httpd=5500
--generic=socket,in,10,127.0.0.1,5701,udp,fgudp
--generic=socket,out,10,127.0.0.1,5700,udp,fgudp
```

2. 在flightgear里点击`开始飞行`
3. 通过任意编译器（比如 vscode）运行`readcsv.py` 程序，程序会读取`simplydata2.csv`测试文件的数据。

*若想再次使用，打开FlightGear软件后，重复上述第2-3步*

## 演示版本已经完成的功能

1. 对给定参数初始化
2. 选取了一组通用的飞机控制参数，可以控制飞机的轨迹和姿态。
3. 通过缓冲机制并发读取文件和传递飞行参数。
4. 采用插值算法等优化技术，提高了飞参序列的平滑过渡，提高了系统的性能和稳定性。

## 实际效果

（待补充）

## 参考项目

[FGAutopilot](https://github.com/lingjiameng/FGAutopilot)

## 完整版本效果

注意：以下程序截图基于本像项目进一步开发的，并非本项目全部具备。由于涉及知识产权和保密规定，不予公开源代码，敬请谅解！



![总体界面展示](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\总体界面展示.png)

[^图1]: 总体界面展示



![飞机航线轨迹显示4.3.1](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\飞机航线轨迹显示4.3.1.jpg)

[^图2]: 飞机轨迹地图展示



![3可视化仪表展示](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\3可视化仪表展示.jpg)

[^图3]: 仪表盘展示（这个还不完善。。。还是草稿状态）

![飞机视角①4.1.1](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\飞机视角①4.1.1.jpg)

[^图4]: 飞机视角展示：舱内视角



![飞机视角②4.1.2](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\飞机视角②4.1.2.jpg)

[^图5]: 飞机视角展示：侧面



![飞机视角③4.1.3](D:\横向项目\遥测数据管理\电子试讲系统\github展示demo版本\SAU-Teaching_and_evaluation_tools_system_for_aviation_experiments\README.assets\飞机视角③4.1.3.jpg)

[^图6]: 飞机视角展示：某一旋转角度



