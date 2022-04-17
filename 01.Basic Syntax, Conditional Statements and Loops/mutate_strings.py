# You will be given two strings. Transform the first string into the second one, letter by letter.
# Print only the unique strings.
# Note: the strings will have the same lengths


first_word = input()
second_word = input()

for x in range(len(first_word)):
    if first_word[x] != second_word[x]:
        replacement = second_word[x]
        new_word = first_word[0:x] + replacement + first_word[x + 1:]
        first_word = new_word
        print(first_word)
