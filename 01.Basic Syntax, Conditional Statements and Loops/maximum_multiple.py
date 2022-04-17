# On the first line, you will be given a positive number, which will serve as a divisor. On the second line,
# you will receive a positive number that will be the boundary. You should find the largest integer N, that is:
# · divisible by the given divisor
# · less than or equal to the given bound
# · greater than 0

n1 = int(input())
n2 = int(input())
magic_n = 0
for x in range(n1, n2 + 1):
    if x % n1 == 0:
        magic_number = x
print(magic_number)
