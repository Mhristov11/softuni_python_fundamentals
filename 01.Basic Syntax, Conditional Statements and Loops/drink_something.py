# Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky.
# Create a program that receives an age and prints what they drink.

ages = int(input())

if ages <= 14:
    type_of_drink = "toddy"
elif ages <= 18:
    type_of_drink = "coke"
elif ages <= 21:
    type_of_drink = "beer"
else:
    type_of_drink = "whisky"

print(f"drink {type_of_drink}")
