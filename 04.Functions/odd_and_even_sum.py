# You will receive a single number. You should write a function that returns the sum of all even and all odd digits
# in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

def new_sum(nums):
    sum_evens = 0
    sum_odds = 0
    for n in nums:
        if n % 2 == 0:
            sum_evens += n
        else:
            sum_odds += n

    print(f"Odd sum = {sum_odds}, Even sum = {sum_evens}")


nums = map(int, list(input()))
new_sum(nums)
