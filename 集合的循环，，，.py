#____author:Administrator
#date:     2018/2/25

# f = open('test1',)
# print(f.readlines())
#
#
# f = open('test')
# for line in f.readlines():
#     print(line.strip())                         #strip这个是去掉空格和换行
#
# f = open('test')
# for line in f.readlines():
#     print(line)

#不打印第十行
f =open('test')
# for index,line in enumerate(f.readlines()):                     #readlines是把集合里的玩意儿变成一个列表，所以可以按照列表进行操作
#     if index == 9:
#         print('-----------')
#         continue
#     print(line.strip())                 #readline只适合读取小文件，因为需要把集合中的元素转换成列表，如果有20个G的文件要读取，内存就炸了
count = 0
for i in f:                                             #这个就是一行一行的读取，用完就释放掉
    if count ==9:
        print('---------------------')
        count += 1
        continue
    print(i.strip())
    count += 1







