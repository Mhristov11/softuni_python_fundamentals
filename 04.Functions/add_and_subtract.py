# You will receive three integer numbers.
# Write functions named:
# · sum_numbers() that returns the sum of the first two integers
# · subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.

def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


def add_and_subtract(a, b, c):
    print(subtract(sum_numbers(a, b), c))


a, b, c = int(input()), int(input()), int(input())
add_and_subtract(a, b, c)
