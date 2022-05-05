# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order

result = sorted(list(map(int, input().split(" "))))

print(result)
