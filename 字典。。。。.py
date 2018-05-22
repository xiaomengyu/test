#____author:Administrator
#date:     2018/2/24

# info={
#     '1':'dssff',
#     '2':'fdghh',
#     '3':'fjkjkjk',
#     '4':'hjfjhdhjd'
# }                                       #字典是无序的
# print(info)
# print(info['2'])
# info['2']='我爱小梦玉'
# print(info)
# info['544545']='我爱'
# print(info)
# del info['2']
# print(info)
# info.pop('1')
# print(info)
# info.popitem()                  #这个是随机删除
# print(info)

info={
     '1':'dssff',
     '2':'fdghh',
     '3':'fjkjkjk',
     '4':'hjfjhdhjd'
 }
print(info.get('1'))
print(info.get('6'))                #这个是判断有没有这个值
print('20 ' in info)
print('2' in info)
print(info.values())
print(info.keys())
info.setdefault('1',{'www.baidu.com':[1,2,3]})              #能娶到这个值就返回这个值，没有的话就创建一个新的
print(info)
info.setdefault('88888',{'www.baidu.com':[1,2,3]})
print(info)
