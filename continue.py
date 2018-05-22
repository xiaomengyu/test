#____author:Administrator
#date:     2018/2/3


# for i in range(1,11):
#     if i%2==0:
#         continue
#     print(i)


exit_flag=False
for i in range(9):
    if i>5:
        continue
    print(i)
    for o in range(9):
        if o==5:
            # exit_flag = False
            exit_flag = True
            break
        print('layer:',o)
    if exit_flag:
        break



















