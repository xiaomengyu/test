death_age = 80

name = input('your name:')#input接收的都是字符串，不管输入的是啥

age = input("your age:")


#int integer=整数
#str string=字符串

print('your name:',name)

print('you can still live for ',str(death_age-int(age)),'years....')#   int(age)!!!!!!!!!!!

print('you can still live for ',death_age-int(age),'years....')

print('you can still live for '+str(death_age-int(age))+  '  years....')