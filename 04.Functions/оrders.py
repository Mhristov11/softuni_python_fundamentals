# Write a function that calculates the total price of an order and returns it.
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks",
# and a quantity of the product. The prices for a single piece of each product are:
# · coffee - 1.50
# · water - 1.00
# · coke - 1.40
# · snacks - 2.00
# Print the result formatted to the second decimal place.

def calculation(item, quantity):
    if item == "coffee":
        price = 1.5
    elif item == "water":
        price = 1
    elif item == "coke":
        price = 1.4
    elif item == "snacks":
        price = 2
    return (f"{(price * quantity):.02f}")


item = input()
quantity = int(input())
print(calculation(item, quantity))
