# Write a program to read an integer N and print all triples of the first N small Latin letters,
# ordered alphabetically:
n = int(input())

for x in range(0, n):
    for y in range(0, n):
        for z in range(0, n):
            print(f"{chr(97 + x)}{chr(97 + y)}{chr(97 + z)}")
