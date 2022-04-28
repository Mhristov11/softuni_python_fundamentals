# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

# first way
nums = input().split(" ")
new_list = []

for x in (nums):
    if int(x) > 0:
        new_list.append(-int(x))
    else:
        new_list.append(abs(int(x)))
print(new_list)

# second way
nums = [- num if num > 0 else abs(num) for num in list(map(int, input().split(" ")))]
print(nums)
