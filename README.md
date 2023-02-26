# FG-UDP-controler
this is an UDP socket module of 飞参序列驱动的三维可视化试飞讲评系统。
## 环境
- Windows 11
- Flight gear 2022.3
- Python 3.9.7
- conda 4.12.0
- numpy 1.22.3
- pandas 1.3.4

## demo v0.1 使用说明：
0. 将config 目录下的fgudp.xml 放入 `` $FGROOT\data\Protocol\`` 目录下，其中``$FGROOT``是FlightGear的安装目录
1. 打开flightgear，在 设置 中输入以下字段
>--allow-nasal-from-sockets     
>--telnet=5555      
>--httpd=5500       
>--generic=socket,in,10,127.0.0.1,5701,udp,fgudp        
>--generic=socket,out,10,127.0.0.1,5700,udp,fgudp       
2. 在flightgear里点击 开始飞行
3. 启动 ``readcsv.py`` 程序，程序会读取simplydata2.csv保存的数据。
4. 当前版本可以连续的控制飞行高度了
## 已经完成的功能
1. 给定参数初始化
2. 可以较方便的更改参数（通过class FlightParameter类）
3. 现在可以通过csv文件读取飞行数据了（2022年5月3日）
4. 可以通过程序来连续的改变飞机的高度了。
## 尚待解决的问题：
1. aotustart的设置命令无效，需要去查找一下有没有这个东西
2. 改变飞机的姿势。
3. 改变飞机的路线。(目前可以通过传递经纬来改变)
4. 缓冲区溢出的问题。传递过多参数会导致缓冲区溢出，思路有 精简参数；压缩数据；增加缓冲区；分为多次发送。
## TODO：
1. 测试可用的参数，并整理出demo程序，可演示。
2. 尝试连续控制飞机轨迹
3. 尝试连续控制飞机姿态

## 尚待明确的参数：

``有关飞机姿势的参数``
``有关飞机路线的参数`` 
``其他参数`` 

