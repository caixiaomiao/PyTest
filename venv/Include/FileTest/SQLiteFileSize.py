# encoding=utf-8

import os
from os.path import join, getsize
import re
import array
import matplotlib.pyplot as plt
from pylab import *                                 #支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']


#获取所有文件
def getdirs(dir):
    files= os.listdir(dir)
    return files

files=getdirs(r'F:\sqliteTest')
print(files.__len__())
x = []
y = []
for name in files:
    if re.match("\w*\.db$",name) is not None:
        #获取文件名称中的文件数量
        datanum1file=name[5:7]
        x.append(datanum1file)
        #print(datanum1file)

        #获取文件大小
        filename=os.path.join(r'F:\sqliteTest', name)
        filesize=os.path.getsize(filename)/float(1024*1024)
        y.append(filesize)
        #print(filesize)

#开始绘图
#fig = plt.figure()1

#names = ['5', '10', '15', '20', '25']
#x = range(len(names))
#y = [0.855, 0.84, 0.835, 0.815, 0.81]

plt.plot(x, y, marker='*', mec='r', mfc='y',label=u'文件保存数量与文件大小曲线图')
#plt.plot(x, y1, marker='*', ms=10,label=u'y=x^3曲线图')
plt.legend()  # 让图例生效
#plt.xticks(x)
plt.margins(0)
#plt.subplots_adjust(left=10, bottom=10, right=11, top=11,wspace=1, hspace=2)
plt.xlabel(u"数据量(千条)") #X轴标签
plt.ylabel(u"文件大小(MB)") #Y轴标签
plt.title("num-size") #标题

plt.show()