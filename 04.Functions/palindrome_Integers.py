# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def palindrome(numbers):
    str_list = map(str, numbers.split(", "))
    for x in str_list:
        if x[::-1] == x:
            print("True")
        else:
            print("False")


numbers = input()
palindrome(numbers)
