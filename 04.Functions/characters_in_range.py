# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.

def characters(char1, char2):
    first_number = ord(char1)
    second_number = ord(char2)
    list = []
    for x in range(first_number + 1, second_number):
        current_letter = chr(x)
        list.append(current_letter)

    print(" ".join(list))


char1 = input()
char2 = input()
characters(char1, char2)
