# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only
# distinct digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.

year = int(input())
happy_year = False

while not happy_year:
    year += 1
    str_year = str(year)
    set_year = set(str_year)
    if len(str_year) == len(set_year):
        print(str_year)
        happy_year = True
