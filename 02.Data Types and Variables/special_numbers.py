# Write a program that reads an integer n. Then, for all numbers in the range [1, n],
# prints the number and if it is special or not (True / False).
# A number is special when the sum of its digits is 5, 7, or 11

number = int(input())

for x in range(1, number + 1):
    print(x, end=" ")
    print("->", end=" ")
    digit = x
    sum = 0
    while digit > 0:
        sum += (digit % 10)
        digit = int(digit / 10)
    if sum == 5 or sum == 7 or sum == 11:
        print("True")
    else:
        print("False")
