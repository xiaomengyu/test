num=0
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)
else:
    print('else......')


num=0
while num<10:
    num+=1
    if num%2==0:
        break
    print(num)
else:
    print('else......')
