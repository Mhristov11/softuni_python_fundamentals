# You have initial energy 100 and initial coins 100. You will be given a string representing the working day events.
# Each event is separated with '|' (vertical bar): "event1|event2| … eventN"
# Each event contains an event name or an ingredient and a number, separated by a dash ("{event/ingredient}-{number}")
# •	If the event is "rest":
# o	You gain energy (the number in the second part). Note: your energy cannot exceed your initial energy (100).
# Print: "You gained {gained_energy} energy.".
# o	After that, print your current energy: "Current energy: {current_energy}.".
# •	If the event is "order":
# o	You've earned some coins (the number in the second part).
# o	Each time you get an order, your energy decreases by 30 points.
# 	If you have the energy to complete the order, print: "You earned {earned} coins.".
# 	Otherwise, skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case, you have an ingredient you should buy.
# The second part of the event contains the coins you should spend.
# o	If you have enough money, you should buy the ingredient and print:
# "You bought {ingredient}."
# o	Otherwise, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the following 3 lines:
# "Day completed!"
# "Coins: {coins}"
# "Energy: {energy}"

events = input().split("|")
total_energy = 100
total_coins = 100

closed = False

for comand in events:
    current_event = comand.split("-")
    event = current_event[0]
    number = int(current_event[1])

    if event == "rest":
        if (number + total_energy) <= 100:
            total_energy += number
        else:
            number = 0
        print(f"You gained {number} energy.")
        print(f"Current energy: {total_energy}.")
    elif event == "order":
        if total_energy - 30 >= 0:
            total_energy -= 30
            total_coins += number
            print(f"You earned {number} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins - number >= 0:
            total_coins -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            closed = True
            break
if not closed:
    print(f"Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
