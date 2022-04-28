# On the first line, you will receive a number n. On the second line, you will receive a word.
# On the following n lines, you will be given some strings. You should add them to a list and print them.
# After that, you should filter out only the strings that include the given word and print that list too.

number = int(input())
search_word = input()
strings = list()
filtered = list()

for i in range(number):
    current_string = input()
    strings.append(current_string)
    if search_word in current_string:
        filtered.append(current_string)
print(strings)
print(filtered)
