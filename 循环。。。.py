#____author:Administrator
#date:     2018/2/2



# for x in range(3):
#     print(x)
#
#
# for i in range(2,4) :
#     print(i)

# for i in range(1,101):
#     if  i%2==0:
#         print('loop:',i)

# for i in range(1,101,2):
#     print('loop:',i)######(1,101)相当于从1开始，终止于100，==[1,100],后面的2等价于步长，相当于2-1的间隔

# for i in range(1,101,1):
#     print('loop:',i)


# _user='zt'
# _password='abc123'
# passed_authentication=True    #此语句判断要不要执行最后的一条print,是一个flag,标志位
#
# for i in range(3):
#     user=input('Username:')
#     password=input('Password:')
#     if user==_user and password==_password:
#         print('Welcome  %s login....' %user)
#         passed_authentication=False
#         break
#     else:
#         print('Invalid username or password!')
# # if  passed_authentication==True:
# if passed_authentication:
#     print('请自重。。。。')


# _user='zt'
# _password='abc123'
# for i in range(3):
#     user=input('Username:')
#     password=input('Password:')
#     if user==_user and password==_password:
#         print('Welcome  %s login....' %user)
#         break
#     else:
#         print('Invalid username or password!')
# else:
#     print('请自重。。。。')



# _user='zt'
# _password='abc123'
# counter=0
# while counter<3:
#     user=input('Username:')
#     password=input('Password:')
#     if user==_user and password==_password:
#         print('Welcome  %s login....' %user)
#         break
#     else:
#         print('Invalid username or password!')
#     counter += 1
# else:
#     print('请自重。。。。')



_user='zt'
_password='abc123'
counter=0
while counter<3:
    user=input('Username:')
    password=input('Password:')
    if user==_user and password==_password:
        print('Welcome  %s login....' %user)
        break
    else:
        print('Invalid username or password!')
    counter += 1
    if counter==3:
        keep_going_choice = input('还想玩么？【y/n】')
        if keep_going_choice == 'y':
            counter = 0
else:
    print('请自重。。。。')











