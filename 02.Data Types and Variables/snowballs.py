# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# · The weight of the snowball (integer).
# · The time needed for the snowball to get to its target (integer).
# · The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# You need to print the highest calculated snowball's value

n = int(input())
best_calculation = 0
for x in range(n):
    weight = int(input())
    time = int(input())
    quality = int(input())
    calculation = (weight / time) ** quality
    if calculation > best_calculation:
        best_calculation = calculation
        for_print = f"{weight} : {time} = {best_calculation:.0f} ({quality})"
print(for_print)
