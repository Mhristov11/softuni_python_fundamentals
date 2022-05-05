# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# · "We have a perfect number!" - if the number is perfect.
# · "It's not so perfect." - if the number is NOT perfect.

def perfect_sum(number):
    total = 0
    for x in range(1, number):
        if number % x == 0:
            total += x
    if total == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())
perfect_sum(number)
