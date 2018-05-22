#____author:Administrator
#date:     2018/2/3
# import  math
# def main():
#     print("This program find the real solutions to a quadratic\n")
#     a,b,c = eval(input("Please enter the coefficients (a,b,c): "))
#     delta = b*b - 4*a*c
#     if delta >= 0 :
#         discRoot = math.sqrt(delta)
#         root1 = (-b + discRoot) / (2 * a)
#         root2 = (-b - discRoot) / (2 * a)
#         print( '\n The solutions are :',root1,root2)
#     if delta < 0:
#         print('No way .....')
# main()

import  math
def main():
    print("This program find the real solutions to a quadratic\n")
    a,b,c = eval(input("Please enter the coefficients (a,b,c): "))
    delta = b*b - 4*a*c
    if a ==0 :
        x = -b / c
        print("\nThere is an solutions",x)
    elif delta < 0 :
        print("\nThe equation has no real roots !")
    elif delta == 0:
        x = -b / (2 * a)
        print("\nThere is a double root at :", x )
    else  :
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print( '\n The solutions are :',root1,root2)
main()










