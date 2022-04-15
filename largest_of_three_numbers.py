# import sys
#
# max_number=-sys.maxsize
#
# for x in range (3):
#     number=int(input())
#     if number > max_number:
#         max_number=number
#
# print(max_number)



n_one=int(input())
n_two=int(input())
n_three=int(input())

if n_one > n_two and n_one > n_three:
    print(n_one)
elif n_two > n_three and n_two > n_one:
    print(n_two)
else:
    print(n_three)