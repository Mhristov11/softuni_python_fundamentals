# Write a program that receives two numbers (factor and count).
# It should create a list with a length of the given count that contains only integer numbers,
# which are multiples of the given factor. The numbers should be only positive,
# and they should be arranged in ascending order, starting from the value of the factor.

first_number = int(input())
second_number = int(input())

new_list = list()
for num in range(1, second_number + 1):
    new_list.append(num * first_number)
print(new_list)
