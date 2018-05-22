#____author:Administrator
#date:     2018/2/25

f = open('test','r')               #这个是文件句柄,这个r可要可不要，因为默认的都是加r的
print(f.read())

f = open('test',)
data = f.read()
print(data)

f = open('test',)               #这个可以看出这个pycharm自带的中文编码格式
print(f)

data1 = f.read()
data2 = f.read()
print(data1,data2)                      #这里data2没有打印出来，因为data2是从data1读完结束时开始读的
                                        #程序从上到下依次执行，所以data2读到了data1的尾部，无解。。。。。
                                        #文件读一次就完了。。。。




