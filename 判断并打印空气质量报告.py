#____author:Administrator
#date:     2018/2/3
def main():
    PM = eval(input("What is today's PM2.5:"))    #eval()函数用来执行一个字符串表达式，并返回表达式的值。。。
    if PM > 75 :
        print("Unhealthy.Be careful!")
    if PM < 35:
        print("Good.Go running!")
main()




