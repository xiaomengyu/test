# age_of_princal=56
# guess_age=int(input(">>:"))
# if guess_age==age_of_princal:
#      print("yes,you got it...")
#      print("yes,you got it...")
# else:
#  print('no,its wrong...')#tab!=四个space

# age_of_principal = 56   #princal是校长的意思
# for i in range(4):
#     guess_age = int(input(">>:"))
#     if guess_age == age_of_principal:
#          print("yes,you got it...")
#          break
#     elif guess_age<age_of_principal:
#          print('try heigher...')
#     elif guess_age>age_of_principal:
#         print('try smeller...')



# while True:
#     age_of_princal=56
#     guess_age=int(input(">>:"))
#     if guess_age==age_of_princal:
#         print("yes,you got it...")
#         print("yes,you got it...")
#     else:
#      print('no,its wrong...')



age_of_principal = 56   #princal是校长的意思
while True:
    guess_age = int(input(">>:"))
    if guess_age == age_of_principal:
         print("yes,you got it...")
         break
    elif guess_age<age_of_principal:
         print('try heigher...')
    elif guess_age>age_of_principal:
        print('try smeller...')
print('END')