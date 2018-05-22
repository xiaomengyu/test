# for x in range(4):
#     a=int(input("请输入第一个数字a:"))
#     b=int(input('请输入第二个数字b:'))
#     c=int(input('请输入第三个数字c:'))
#     if a>=b>=c or a>=c>=b:
#         print("最大值为a.....")
#     elif b>=a>=c or b>=c>=a:
#         print("最大值为b.....")
#     elif c>=a>=b or c>=b>=a:
#         print("最大值为c....")
#     else:
#         print('输入有误。。。。')



for i in range(4):
    num1=int(input("请输入第一个数字a:"))
    num2=int(input('请输入第二个数字b:'))
    num3=int(input('请输入第三个数字c:'))
    if num1>=num2:
        if num1>num3:
            print( 'The max num is num1')
        else:
            print('The max num is num3')
    else:
        if num2>=num1:
            if num2>=num3:
                print('The max num is num2')
            else:
                print('The max num is num3')





