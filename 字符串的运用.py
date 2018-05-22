#____author:Administrator
#date:     2018/2/22

name='my name\t is {name} and i am {years} old'
print(name.count('a'))
print(name.capitalize())
print(name.center(55,'+'))                  #一共55个字符，不够的用+补上
print(name.encode(encoding='utf-8'))
print(name.endswith('zt'))              #判断这个字符串是否是以zt结尾的
print(name.expandtabs(tabsize=33))      #这个是用来给加入的什么键量化一个大小。。。。。。
print(name[name.find('name'):11])
print(name[name.find('name'):])
print(name.format(name='zt',years=22))
print(name.format_map({'name':'zt','years':22}))
print(name.isalnum())
print('zb456'.isalnum())            #这个函数只能在字符串里包含字母和阿拉伯数字，包含其他的任何玩意都为False
print(name.isalpha())               #判断是否为纯英文字符
print('5555'.isdecimal())         #判断是否为十进制的数字
print('55'.isdigit())               #判断是否为整数
print('jajk阿德恒大cajk'.isidentifier())        #判断是否为一个合法的变量名
print('daa'.islower())          #判断是否为小写
print('33'.isnumeric())
print('33.33'.isnumeric())      #判断是否为数字，除了数字以外的任何夹杂在其中不合法
print(' '.isspace())            #是否为空格
print('My Name Is '.istitle())  #判断句子中是否都为首字母开头的玩意儿
print('klkalk'.isprintable())   #tty file ,drive file 等文件类型的玩意儿都属于不可打印的
print('JKKJFJK'.isupper())      #判断是否都为大写
print(''.join(['2','555','5454','gghhg']))
print('***'.join(['2','555','5454','gghhg']))
print('+'.join(['2','555','5454','gghhg']))
print(name.ljust(50,'+'))
print(name.rjust(55,'-'))
print('HJJK'.lower())
print('kjjjf'.upper())
print('\n我爱小梦玉'.lstrip())
print('测试')
print('我爱小梦玉\n'.rstrip())               #这个的作用是去掉空格
print('测试')
print('\n我爱小梦玉\n'.strip())
print('测试')
#这个很有意思，用来加密或破解
p = str.maketrans('abcdefghijk','0123456789+')               #前面的变量必须和后面的一一对应
print('woaixiaomengyu'.translate(p))
print('-----')                  #最后就把这个字符串里的字母一一加密成了这个玩意。。。。
print('alex li'.replace('l','L'))
print('alex li'.replace('l','L',1))#这个的用处就是把前面的玩意换成后面的玩意，加个数字控制变换的个数
print('alex li'.rfind('l'))         #和find 一样，不过是最右边的那个
print('alex lil'.rfind('l'))
print('我爱 小 梦玉 gg'.split())             #将一个字符串按照空格分割成一个元素
print('我爱 小 梦玉 gg'.split('小'))          #后面的可以将什么换成将要分割的标志
print('1+2+3+4+5+6+7+8+9'.split('+'))
print('1+2+\n3+4'.splitlines())             #这个是将换行了的分割成元素
print('1+2+3+4'.splitlines())
print('jhhjahhgg'.startswith('jhh'))
print('Alex LI'.swapcase())
print('dhsjhs jksdkj  55 hdhjah'.title())           #把这个变成标题，自动把第一个字母大写
print('Alex LI'.zfill(55))






















