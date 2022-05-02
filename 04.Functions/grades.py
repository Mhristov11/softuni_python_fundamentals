#Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words.
#· 2.00 – 2.99 - "Fail"
#· 3.00 – 3.49 - "Poor"
#· 3.50 – 4.49 - "Good"
#· 4.50 – 5.49 - "Very Good"
#· 5.50 – 6.00 - "Excellent"

def grade_check(grade):
    if grade < 3:
        return "Fail"
    elif grade < 3.5:
        return "Poor"
    elif grade < 4.5:
        return "Good"
    elif grade < 5.5:
        return "Very Good"
    elif grade <= 6.0:
        return "Excellent"

grade = float(input())

print(grade_check(grade))

