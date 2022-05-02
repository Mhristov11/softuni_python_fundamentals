# Create a function that receives three parameters, calculates a result depending on the given operator,
# and returns it. Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following: "multiply", "divide", "add", "subtract".

def calculations(a, b, command):
    if command == "multiply":
        result = a * b
    elif command == "divide":
        result = int(a / b)
    elif command == "add":
        result = a + b
    elif command == "subtract":
        result = a - b
    print(result)


command = input()
first_n = int(input())
second_n = int(input())

calculations(first_n, second_n, command)
