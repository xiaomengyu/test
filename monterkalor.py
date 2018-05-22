#____author:Administrator
#date:     2018/2/3
from random import  random
from math import  sqrt
from time import  clock
allhits = 2 ** 15
hits = 0
clock()                         #开始计时
for i in range(1, allhits):
    x,y = random(),random()
    dist = sqrt(x**2+y**2)                  #sqrt开方
    if dist <=1.0:
        hits +=1
pi = 4 * (hits / allhits)
print('PI的值是:%s'%pi)
print('程序运行 的时间是%-2.5ss'%clock())               #计时结束






