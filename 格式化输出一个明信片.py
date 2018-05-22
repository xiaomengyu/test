#____author:Administrator
#date:     2018/2/2





# name=input('Name:')
# age=input('Age:')
# job=input('Job:')
# salary=input('Salary:')
# if salary.isdigit():        #长得像不像数字，比如220d,'222'
#     salary=int(salary)
#     msg='''
#     ------------info of %s--------------
#     Name:    %s
#     Age :    %s
#     Job ：   %s
#     Salary:  %s
#     You will be retired in %d years
#     --------------end-----------------
#     '''%(name,name,age,job,salary,65-int(age))
#     print(msg)
# else:
#     print('工资输入有误，请重新输入:')



# name=input('Name:')
# age=int(input('Age:'))
# job=input('Job:')
# salary=input('Salary:')
# if salary.isdigit():        #长得像不像数字，比如220d,'222'
#     salary=int(salary)
# else:
#     # print('工资输入有误，请重新输入:')
#     # exit()
#     exit('工资输入有误，请重新输入:')
#
# msg='''
# ------------info of {_name}--------------
# Name:    {_name}
# Age :    {_age}
# Job ：   {_job}
# Salary:  {_salary}
# You will be retired in {_d} years
# --------------end-----------------
# '''.format(_name=name,_age=age,_job=job,_salary=salary,_d=65-age)               #注意input这个函数只能是输出的str类型的变量
# print(msg)



name=input('Name:')
age=int(input('Age:'))
job=input('Job:')
salary=input('Salary:')
if salary.isdigit():        #长得像不像数字，比如220d,'222'
    salary=int(salary)
else:
    # print('工资输入有误，请重新输入:')
    # exit()
    exit('工资输入有误，请重新输入:')

msg='''
------------info of {0}--------------
Name:    {0}
Age :    {1}
Job ：   {2}
Salary:  {3}
You will be retired in {4} years
--------------end-----------------
'''.format(name,age,job,salary,65-age)               #注意input这个函数只能是输出的str类型的变量
print(msg)