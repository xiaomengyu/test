#____author:Administrator
#date:     2018/2/25

list_1 = [1,5,92,3,54,7,5,5,5,5,5,5,2]
list_1 = set(list_1)
print(list_1,type(list_1))

#取交集
list1 = set([1,23,54,5,55,55,55,55,3])
list2 = set([1,5,5,5,55,5,555,3,4,89,77,23,3])
print(list1.intersection(list2))
print(list1 & list2)
#取并集
print(list1.union(list2))
print(list1 | list2)
#1中有而2中没有的
print(list1.difference(list2))
print(list1 - list2)
#判断是否子集
print(list1.issubset(list2))
#判断是否父集
print(list1.issuperset(list2))
#并集中去除交集
print(list1.symmetric_difference(list2))
print(list1 ^ list2)
#判断俩集合是否有交集，有则返回Flase,没有则返回True
print(list1.isdisjoint(list2))

list4 = set([1,2,3,4,5])
list4.add(999)
print(list4)
list4.update([1,5,99999,555])               #添加多个
print(list4)
list4.remove(1,)
print(list4)
print(1 in list4)
print(1 not in list4)
print(list4.pop())              #删除第一个值并返回
list4.discard(2,)
print(list4)                #删除这个指定的数字，并且只能是数字，如果集合不存在这个被指定的数字，不做任何事也不报错





