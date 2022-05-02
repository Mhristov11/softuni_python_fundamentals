# You will receive 2 lines of input. On the first line, you will receive a single string of integers,
# separated by a comma and a space ", ". On the second line, you will receive a count of beggars.
# Your job is to print a list with the sum of what each beggar brings home, assuming they all take regular turns,
# from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5],
# the second one collects [2, 4]. The same list with 3 beggars would produce a better outcome for
# the second beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list
# is not necessarily a multiple of n. The list length could be even shorter - i.e.,
# the last beggars will take nothing (0)

numbers = list(map(int, input().split(", ")))
number_of_beggars = int(input())
sum_for_beggars = [0] * number_of_beggars
for current_beggar in range(number_of_beggars):
    for current_sum in range(current_beggar, len(numbers), number_of_beggars):
        sum_for_beggars[current_beggar] += numbers[current_sum]
print(sum_for_beggars)
