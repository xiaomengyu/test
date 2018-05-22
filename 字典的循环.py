#____author:Administrator
#date:     2018/2/25
a={
    '1':'jksdjksdkj',
    '2':'jkdjkdjkskj',
    '3':'kldslksdlksd',
    '4':'jkjkdfjkdf'
}
for i in a:                     #这个比下面的更高效，下面的需要先把字典转换成列表，浪费
    print(i,a[i])
for k,v in a.items():
    print(k,v)


