# Write a function that checks if a given password is valid. Password validations are:
# · It should be 6 - 10 (inclusive) characters long
# · It should consist only of letters and digits
# · It should have at least 2 digits

def pass_check(new_password):
    number_of_chr = False
    letters_and_digits_check = False
    number_count = True
    counter = 0
    if len(new_password) < 6 or 10 < len(new_password):
        print("Password must be between 6 and 10 characters")
        number_of_chr = True
    password_parts = list(new_password)
    for chr in password_parts:
        if chr in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz":
            letters_and_digits_check = True
        elif chr in "123456789":
            letters_and_digits_check = True
            counter += 1
        else:
            letters_and_digits_check = False
        if not letters_and_digits_check:
            print("Password must consist only of letters and digits")
            break
    if counter < 2:
        number_count = False
        print("Password must have at least 2 digits")

    if number_count and letters_and_digits_check and not number_of_chr:
        print("Password is valid")


new_password = input()
pass_check(new_password)
