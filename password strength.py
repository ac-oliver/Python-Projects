symbols = '!@#$%^&*()<>?:{}|_+,./;'

print("A strong password is at least 9 characters long, contains one uppercase letter, one lowercase letter, and a "
      "number")

while True:
    user_pass = input("Enter your password to test its strength: ")

    test_upper = any(item.isupper() for item in user_pass)
    test_lower = any(item.islower() for item in user_pass)
    test_number = any(item.isnumeric() for item in user_pass)
    test_length = len(user_pass) >= 9
    test_special = any(i in symbols for i in user_pass)

    print()
    print("Here's a breakdown of your password: ")
    print()

    if test_upper:
        upper_accept = "Upper case letter present."
        print(upper_accept)
    else:
        upper_reject = "Upper case letter absent."
        print(upper_reject)

    if test_lower:
        lower_accept = "Lower case letter present"
        print(lower_accept)
    else:
        lower_reject = "Lower case letter is absent."
        print(lower_reject)

    if test_number:
        number_present = "Number present."
        print(number_present)
    else:
        number_absent = "Number absent."
        print(number_absent)

    if test_length:
        length_present = "Password is long enough."
        print(length_present)
    else:
        length_absent = "Password is too short."
        print(length_absent)

    if test_special:
        special_present = "Special character is present." + "\n"
        print(special_present)
    else:
        special_absent = "Special character is absent." + "\n"
        print(special_absent)

    if test_upper and test_lower and test_number and test_length and test_special:
        print("That's a strong password. Good job.") + "\n"
    else:
        print("Your password is lacking. See above for what you're missing.")