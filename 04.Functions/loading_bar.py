# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without
# remainder (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending
# on the number you have received in the input. Print the result on the console. For more clarification,
# see the examples below.

def loading_bar(number):
    n = int(number / 10)
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percent_number = n * "%"
        points_nummber = (10 - n) * "."
        print(f"{number}% [{percent_number}{points_nummber}]")
        print("Still loading...")


percents = int(input())
loading_bar(percents)
