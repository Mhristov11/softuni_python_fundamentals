# Create a program that calculates how many loaves you can make with the budget you have.
# First, you will receive your budget. Then, you will receive the price for 1 kg flour
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1l milk is 25% more than the price
# for 1 kg flour. Notice that you need 0.250l milk for one bread, and the calculated price is for 1l.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# · For every bread that you make, you will receive 3 colored eggs.
# · For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored eggs
# for your bread. The count of eggs you will lose is calculated when you subtract 2 from your current
# count of loaves – ({current_bread_count} – 2)
# In the end, print the loaves of bread you made, the eggs you have gathered, and the money you have left,
# formatted to the 2nd decimal place

budget = float(input())
preice_per_kg_flour = float(input())
preice_per_pack_eggs = preice_per_kg_flour * 0.75
preice_per_liter_milk = preice_per_kg_flour * 1.25
price_for_one_bread = preice_per_kg_flour + preice_per_pack_eggs + preice_per_liter_milk / 4
number_of_breads = int(budget // price_for_one_bread)
money_left = budget - number_of_breads * price_for_one_bread
colored_eggs = 0
for current_bread_count in range(1, number_of_breads + 1):
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)
print(
    f"You made {number_of_breads:.0f} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.02f}BGN left.")
