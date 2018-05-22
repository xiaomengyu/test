#____author:Administrator
#date:     2018/2/25

f = open('test',)                                                #tell 告诉需要打印的位置
print(f.tell())
print(f.read())
print(f.tell())

f = open('test')
print(f.tell())
print(f.readline())                                             #这表明一个中文字符占据俩的单元
print(f.tell())

f = open('test')
print(f.tell())
print(f.read(1))
print(f.tell())

#seek 回到什么地方

f.seek(190)                               #括号里的参数控制需要从哪里开始打印
print(f.readlines())

f.seek(10)                               #括号里的参数控制需要从哪里开始打印
print(f.readline())

print(f.encoding)                       #cp936就是gbk2312



