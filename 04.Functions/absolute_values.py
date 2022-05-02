# Write a program that receives a sequence of numbers, separated by a single space,
# and prints their absolute value as a list.

def absolute_value(numbers):
    numbers =numbers.split(" ")
    new_list = list()
    for n in numbers:
        current_number = abs(float(n))
        new_list.append(current_number)
    print(new_list)

numbers = input()
absolute_value(numbers)