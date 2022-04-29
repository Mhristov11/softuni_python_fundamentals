# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive
# the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
#	Find the gifts with this name in your collection, if any, and change their values to "None".
# •	"Required {gift} {index}"
#	If the index is valid, replace the gift on the given index with the given gift.
# •	"JustInCase {gift}"
#	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space

gifts = input().split(" ")
len_list = len(gifts)
command = input()

while command != "No Money":
    new_command = command.split(" ")
    if new_command[0] == "OutOfStock":
        if new_command[1] in gifts:
            item = new_command[1]
            while (new_command[1] in gifts):
                gift_index = gifts.index(new_command[1])
                gifts[gift_index] = "None"

    elif new_command[0] == "Required":
        gift_index = int(new_command[2])
        if 0 <= gift_index < len_list:
            gifts[gift_index] = (f"{new_command[1]}")

    elif new_command[0] == "JustInCase":
        gifts.pop()
        gifts.append(new_command[1])

    command = input()

for _ in (gifts):
    if "None" in gifts:
        gifts.remove("None")

print(" ".join(gifts))
