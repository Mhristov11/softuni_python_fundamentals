# As a gladiator, Peter needs to repair his broken equipment when he loses a fight.
# His equipment consists of a helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired.
# You will receive the price of each item in his equipment.
# Calculate his expenses for the year for renewing his equipment.
# As output, you must print Peter`s total expenses for new equipment

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_amount = 0
shield_repair_times = 0
for x in range(1, lost_fights_count + 1):
    if x % 2 == 0:
        total_amount += helmet_price
    if x % 3 == 0:
        total_amount += sword_price
    if x % 2 == 0 and x % 3 == 0:
        total_amount += shield_price
        shield_repair_times += 1
        if shield_repair_times % 2 == 0:
            total_amount += armor_price

print(f"Gladiator expenses: {total_amount:.02f} aureus")
