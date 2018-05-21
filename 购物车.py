#____author:Administrator
#date:     2018/2/16
product_list=[
    ('mac',  1000),
    ('book',  100),
    ('bike',  500),
    ('tesla',  2000),
    ('aaa',  10)
]
shopping_list=[]
saving=input('please input your money:')
if saving.isdigit():
    saving=int(saving)
    while True:
        # for i in product_list:
        #     print(product_list.index(i) + 1, i)
        # for i in enumerate(product_list):
        #     print(i)
        # for i in enumerate(product_list, 1):
        #     print(i)
        # for i, v in enumerate(product_list, 1):
        #     print(i, v)
        for i, v in enumerate(product_list, 1):
            print(i, '>>>>>', v)
        break
    for i in range(99):
        user_choice=input('选择要买什么。。。')
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice-1<len(product_list) and user_choice>=1:
                p_item=product_list[user_choice-1]
                if p_item[1]<=saving:           #买得起
                    shopping_list.append(p_item)
                    saving-=p_item[1]
                    print('Added %s into your shopping cart,your current balance is \033[36;1m%s\033[0m'%(p_item,saving))
                else:
                    print('\033[42;1m你的余额只剩[%s]啦。。。。\033[0m'%saving)
            else:
                print('product code [%s] is not exist...'%user_choice)
        elif user_choice=='q':                      #\033[31;1m%s\033[0m这个是给字体加颜色的，31红色，32绿色
            print('\033[41;1m------------shopping list-------------\033[0m')
            for i in shopping_list:
                print(i)
            print('你的余额为:%s'%(saving))
            exit()
        else:
            print('invalid option')
else:
    print('请输入数字。。。。。')









































