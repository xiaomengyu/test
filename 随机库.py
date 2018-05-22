#____author:Administrator
#date:     2018/2/3
# for i in range(5):
#     from  random import *
#     print(random())     #此为取一个0到1的随机数字

# from  random import *
# print(uniform(1,10))    #在1到10之间随机生成一个小数
# print(randint(1,10))    #生成一个整数
# for i in range(33):
#     print(randrange(0,11,2))       #此为从0到10之间随机取一个跨度为2的数字
# ra=[0,1,2,3,4,5,6,7,8,9,10,11,'hello']
# for i in range(22):
    # print(choice(ra))             #在列表中随机选择一个数字或者啥玩意

# for i in range(29):
#     shuffle(ra)
#     print(ra)           #此处print中不能加shuffle(ra),用处是随机改变列表的顺序
# for i in range(9):
#     print(sample(ra,4))        #随机在ra中选取四个元素


from  random import *
seed (10)
print(uniform(1,10))
print(uniform(1,10))
seed(9)
print(uniform(1,10))
print(uniform(1,10))
seed(10)
print(uniform(1,10))
print(uniform(1,10))
seed(9)
print(uniform(1,10))
print(uniform(1,10))
seed(99999)
print(uniform(1,10))
print(uniform(1,10))


