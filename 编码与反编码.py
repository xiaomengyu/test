#____author:Administrator
#date:     2018/2/21

msg='我爱小梦玉'
print(msg)
print(msg.encode('utf-8'))                 #下面的b表示这是个byte类型，加了utf-8表示在不同的操作系统下统一标准
print(msg.encode())                         #encode函数自动在后面补全encode='utf-8'
print(msg.encode(encoding='utf-8'))
print(msg.encode(encoding='utf-8').decode(encoding='utf-8'))

