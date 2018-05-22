# Time    : 2018/3/19 17:35
# Author  : Jack
# File    : 购物车.py
# Software: PyCharm

product_list = [
    ('Mac',9000),
    ('kindle',800),
    ('tesla',30000),
    ('python book',110),
    ('bike',2000),
]
saving = input('please input your saving:')
shopping_car = []
if saving.isdigit():
    saving = int(saving)
    # for i in product_list:
    #     print(product_list.index(i)+1,i)
    # for i in enumerate(product_list,1):         #后面加一个逗号和一个一是参数
    #     print(i)
    while True:
        for i,v in enumerate(product_list,1):
            print(i,'>>>>>',v)
        choice = input('请选择购买的商品编号[退出：q]')
        if choice.isdigit():
            choice=int(choice)
            if choice>0 and choice<=len(product_list):
                p_item = product_list[choice-1]
                if p_item[1]<saving:
                    saving -= p_item[1]
                    shopping_car.append(p_item)
                else:
                    print('余额不足，还剩%s'%saving)


                print(p_item)
            else:
                print('商品编码不存在')

        elif choice=='q':
            print('------------------您已购买如下商品---------------')
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱'%saving)
            break
        else:
            print('invalid ')




























































