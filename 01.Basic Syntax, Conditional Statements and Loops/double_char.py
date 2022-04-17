# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.
comand = input()

for x in range(len(comand)):
    print(comand[x] * 2, end="")
