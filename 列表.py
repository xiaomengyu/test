#____author:Administrator
#date:     2018/2/7
# a=[1,2,3,4,5,6,'hello']
# print(a[1:3])
# print(a)
# print(a[1:])
# print(a[1:99999])
# print(a[:-1])
# print(a[-1])
# print(a[::1])
# print(a[::2])
# print(a[::1])
# print(a[2:-1:2])
# print(a[-1::])
# print(a[-1:3:-2])


# a=[1,2,3,4,5,6,'hello']
# a.append('world')
# print(a)
# print(a.append('world'))
# a.insert(2,'world')
# print(a)
# print(a.insert(2,'world'))

# a=[1,2,3,4,5,6,'hello']
# a[1]=''
# print(a)
# a[1]=   '      '
# print(a)
# a[1]='    jack'
# print(a)
# a[1:4]=['a','g','o','r']
# print(a)
# a.remove('hello')
# print(a)
# a.remove(5)
# print(a)
# print(a.remove(5))
# a.remove(a[3])
# print(a)

# a=[1,2,3,4,5,6,'hello']
# a.pop(3)
# print(a)
# print(a.pop(3))                 #返回被删除的值,若是pop()里面的括号是空的，则删除列表的最后一个元素
# print(a)

# a=[1,2,3,4,5,6,'hello']
# del a[3]
# print(a)
# del a
# print(a)

# a=[1.5,53,6,6,6,6,6,6,6.0,6]
# t=a.count(6)
# print(t)
# print([1.5,53,6,6,6,6,6,6,6.0,6].count(6))

# a=[1,2,3,4]
# b=[7,8,9,]
# a.extend(b)
# print(a)
# print(b)

# a=[1,2,3,'hello',4,5,6,'hello','hello','hello']
# print(a.index('hello'))
# b=a[3+1:]
# print(b)
# print(b.index('hello'))
# finally_hello=3+1+3+1
# print('finally_hello:',finally_hello)

# a=[1,2,3,'hello',4,5,6,['hello','hello','hello']]
# print(a.index(['hello','hello','hello']))
# b=a.reverse()
# print(b)
# print(a.reverse())
# a.reverse()
# print(a)

# a=[5,6,9,1,99,55555,7,3,3,3,3,]
# b=a.sort()
# print(b)
# print(a.sort())
# a.sort()
# print(a)
# b=['s','g','y','u','a','b','l','x','.','0','A']
# b.sort()
# print(b)                        #按照ASCII码的顺序来排序


# a=[4,9,3,55,1,00,88,3]
# a.sort(reverse=True)
# print(a)
#
# a=[4,9,3,55,1,00,88,3]
# a.sort(reverse=False)
# print(a)
#
# a=[4,9,3,55,1,00,88,3]
# a.sort()
# print(a)


# a=[1,2,3,'hello',4,5,6,'hello','hello','hello']
# print(9 in a)
# print('hello ' in a )
# print('hello' in a)
# print(a.count(6))
# print(a.count(999))
# print(a.count('hello'))

# a=[1,2,3,'hello',4,5,6,'hello','hello','hello']
# a.clear()
# print(a)
# print(a.clear())

# a=[1,2,3,'hello',4,5,6,'hello','hello','hello']
# b=(a is list)
# print(b)
# print(type(a) is list)

# a=[1,9,5.6,555,[555,888]]
# b=a.copy()
# # print(a)
# # print(b)
# a[1]=456
# a[4][1]=123                     #copy只copy第一层的元素
# print(a)
# print(b)


# import copy
# a=[1,5,9,66,[122,555]]
# b=a
# a[1]=222
# print(a)
# print(b)
# # c=copy.copy(a)
# c=copy.deepcopy(a)
# a[1]=999999
# a[4][0]=5689
# print(a)
# print(c)

import copy
a=[555,889,'jkuku']
a[1]=56777
p1=a[:]                     #三种copy的方式
p2=copy.copy(a)
p3=list(a)
print(p1,p2,p3)



