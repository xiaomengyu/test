# Time    : 2018/3/19 20:32
# Author  : Jack
# File    : 字典.py
# Software: PyCharm

dic = {'name':'Alex','age':35,'hobby':'girl','is_handsome':True}            #字典两大特点:无序以及键唯一
print(dic)
print(dic['name'])

# dic = {[1,5,9]:'Alex','age':35,'hobby':'girl','is_handsome':True}
# #unhashable,因为列表以及字典都是可变类型，整型，字符串和元组才是不可变类型，key必须为不可变类型


dic1 = {'name':'Alex'}
dic1['age']=11
print(dic1)
dic1['name']=11
print(dic1)
dic1.setdefault('age',33)               #这个玩意儿是添加一个值，若是前面字典里面有则忽略
print(dic1)
dic1.setdefault('e',33)
print(dic1)





















