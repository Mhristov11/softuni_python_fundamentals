# Write a program that receives three whole numbers and prints the largest one.

import sys

max_number = -sys.maxsize

for x in range(3):
    number = int(input())
    if number > max_number:
        max_number = number

print(max_number)
