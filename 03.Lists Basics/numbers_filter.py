#On the first line, you will receive a single number n. On the following n lines,
# you will receive integers. After that, you will be given one of the following commands:
#· even
#· odd
#· negative
#· positive
#Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

#first way
n=int(input())
all_numbers=list()

for x in range (n):
    current_number=int(input())
    all_numbers.append(current_number)

filtered=list()
command=input()

for x in all_numbers:
    if command=="even":
        if x % 2 ==0:
            filtered.append(x)
    if command=="odd":
        if x % 2 !=0:
            filtered.append(x)
    if command=="negative":
        if x < 0:
            filtered.append(x)
    if command=="positive":
        if x >=0:
            filtered.append(x)

print(filtered)


#second way
n=int(input())

odd=list()
even=list()
negative=list()
positive=list()

for x in range (n):
    current_number=int(input())
    if current_number % 2 ==0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number < 0 :
        negative.append(current_number)
    else:
        positive.append(current_number)

command=input()
print(eval(command))