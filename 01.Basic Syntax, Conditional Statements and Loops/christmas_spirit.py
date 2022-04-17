# It is time to get in a Christmas mood. You need to decorate the house in time for the big event,
# but you have limited days to do so.
# You will receive an allowed quantity for one type of decoration and days left until Christmas day
# to decorate the house.
# There are 4 types of decorations, and each piece costs a price
# · Ornament Set – 2$ per piece
# · Tree Skirt – 5$ per piece
# · Tree Garlands – 3$ per piece
# · Tree Lights – 15$ per piece
# Every second day you buy an Ornament Set quantity of times and increase your Christmas spirit by 5.
# Every third day you buy Tree Skirts and Tree Garlands (both quantity of times) and increase your spirit by 13.
# Every fifth day you buy Tree Lights and increase your Christmas spirit by 17. If you have bought Tree Skirts and
# Tree Garlands on the same day, you additionally increase your spirit by 30.
# Every tenth day you lose 20 points of the spirit because your cat ruins all tree decorations, and you should
# rebuild the tree and buy one piece of tree skirt, garlands, and lights. That is why you are forced to increase
# the allowed quantity with 2 at the beginning of every eleventh day.
# Also, if the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, and you lose
# an additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.

quantity = int(input())
days_left = int(input())
total_cost = 0
christmas_spirit = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15

for days in range(1, days_left + 1):
    if days % 11 == 0:
        quantity += 2
    if days % 2 == 0:
        total_cost += quantity * ornament_set_price
        christmas_spirit += 5
    if days % 3 == 0:
        total_cost += (tree_skirt_price * quantity) + (tree_garlands_price * quantity)
        christmas_spirit += 13
    if days % 5 == 0:
        total_cost += tree_lights_price * quantity
        christmas_spirit += 17
    if days % 3 == 0 and days % 5 == 0:
        christmas_spirit += 30
    if days % 10 == 0:
        total_cost += tree_skirt_price + tree_garlands_price + tree_lights_price
        christmas_spirit -= 20

    if days == days_left and days % 10 == 0:
        christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
