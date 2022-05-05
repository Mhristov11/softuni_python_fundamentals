# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.

def smallest_num(n1, n2, n3):
    list = [n1, n2, n3]
    print(min(list))


n1 = int(input())
n2 = int(input())
n3 = int(input())

smallest_num(n1, n2, n3)
