#____author:Administrator
#date:     2018/2/25

data = open('test',encoding='gbk').read()
print(data)
data = open('test',).read()
print(data)
data = open('test',encoding='utf-8').read()             #这里出错是windows的错
print(data)




