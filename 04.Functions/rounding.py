# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list

def rounding(new_list):
    final_list = list()
    for n in new_list:
        current_number = round(float(n))
        final_list.append(current_number)
    return final_list


new_list = input().split(" ")

print(rounding(new_list))
