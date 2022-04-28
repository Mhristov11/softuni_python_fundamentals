# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
# · One with all the positives (including 0) numbers
# · One with all the negatives numbers

n = int(input())
list_positive = []
list_negative = []
count_positives = 0
sum_negatives = 0

for x in range(n):
    number = int(input())
    if number < 0:
        list_negative.append(number)
        sum_negatives += number
    else:
        list_positive.append(number)
        count_positives += 1

print(list_positive)
print(list_negative)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_negatives}")
