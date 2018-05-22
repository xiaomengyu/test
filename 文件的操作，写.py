#____author:Administrator
#date:     2018/2/25

# f = open('test',)
# f.write('我爱小梦玉')                    #错误示例

f = open('test1','w')                   #注意w写的操作要换个文件名，因为w写的操作是创建一个新的文件，会把原来的文件覆盖掉，小心
f.write('hhhh,\n')
f.write('我爱北京天安门')
f.close()                       #这个是关闭程序的，可加可不加




