# Write a program that receives a number and creates the following pattern.
# The number represents the largest count of stars on one row.

number = int(input())

for x in range(number + 1):
    print(x * "*")
for x in range(number - 1, 0, -1):
    print(x * "*")
