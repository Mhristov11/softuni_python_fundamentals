# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal poin

def factorial(number):
    f = 1
    for x in range(1, number + 1):
        f = f * x
    return f


num1 = int(input())
num2 = int(input())
result = factorial(num1) / factorial(num2)
print(f"{result:.02f}")
