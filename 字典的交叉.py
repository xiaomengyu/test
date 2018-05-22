#____author:Administrator
#date:     2018/2/25
a={
    '1':'jksdjksdkj',
    '2':'jkdjkdjkskj',
    '3':'kldslksdlksd',
    '4':'jkjkdfjkdf'
}
b={
    '1':',fdkdkkd',
    'fdlld':'jkdfjkdkj',
    'fdjkjkfdjk':'fdjkdjkfd'
}
print(a.items())
a.update(b)          #这个的作用是，把b中的数据与a交叉的部分更新到a中，没有交叉的部分加入到a中
print(a)

# c=dict.fromkeys([7,8,9],[444,{'name':'zt'},'gffgfgfg'])
# print(c)
# c[8][1]['name']=45445                   #这个跟copy一样，全改了，因为共用了同一个内存地址
# print(c)





