# You want to go to France by train, and the train ticket costs exactly 150$.
# You do not have enough money, so you decide to buy some items with your budget and
# then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Clothes-50 Shoes- 35 Accessories-20.5
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item,
# you have to reduce the budget with its price value. If you don't have enough money for it, you can't buy it.
# Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. Calculate
# if the budget after selling all the items is enough for buying the train ticket.

items = input().split("|")
budget = int(input())
total_prices = 0
condition = False
all_prices = []

for current_item in items:
    current_item = current_item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])
    condition = False
    if item_type == "Clothes":
        if item_price <= 50:
            condition = True
    if item_type == "Shoes":
        if item_price <= 35:
            condition = True
    if item_type == "Accessories":
        if item_price <= 20.5:
            condition = True

    if condition:
        if item_price <= budget:
            budget -= item_price
            total_prices += item_price
            new_item_price = item_price * 1.4
            all_prices.append(str(f"{new_item_price:.2f}"))

profit = (total_prices * 0.4)

print(" ".join(all_prices))
print(f"Profit: {profit:.2f}")
if (profit + total_prices + budget) >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
