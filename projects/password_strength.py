# CB 1st Password Strength Checker

import time

password_score = 0
length = False
upper = False
lower = False
digit = False
special = False

print("Password strength checker")


while True:
    user_password = input("Enter password: ")
    if len(user_password) >= 8:
        password_score += 1
        length = True
    else:
        pass

    for i in user_password:
        if i.isupper():
            password_score += 1
            upper = True
            break
        else:
            break

    for i in user_password:
        if i.islower():
            password_score += 1
            lower = True
            break
        else:
            break

    for i in user_password:
        if i.isdigit():
            password_score += 1
            digit = True
            break
        else:
            break
    
    for i in user_password:
        if i.isdigit() == False and i.islower == False and i.isupper == False:
            password_score += 1
            special == True
            break
        else:
            break

    # checking if there is a special character in the code

    break

print("Checking password strength...")
while True:
    time.sleep(1)
    if length == True: 
        print("Length Check: PASSED")
    else:
        print("Length Check: FAILED")
        print("Tip: Make sure your password is at least 8 characters long.")
    print("...")
    time.sleep(1)
    if upper == True: 
        print("Uppercase Check: PASSED")
    else:
        print("Uppercase Check: FAILED")
        print("Tip: Have a variety of upper and lowercase letters in your password.")
    print("...")
    time.sleep(1)
    if lower == True: 
        print("Lowercase Check: PASSED")
    else:
        print("Lowercase Check: FAILED")
        print("Tip: Have a variety of upper and lowercase letters in your password.")
    print("...")
    time.sleep(1)
    if digit == True: 
        print("Digit Check: PASSED")
    else:
        print("Digit Check: FAILED")
        print("Tip: Make sure to have numbers in your password.")
    time.sleep(1)
    if special == True:
        print("Special Character Check: PASSED")
    else:
        print("Special Character Check: FAILED")
        print("Tip: Having special characters is good practice for your passwords.")
    
    break

print("Password Strength: ")
if password_score <= 2:
    print(f"Score: {password_score}/5")
    print("Rating: Weak")
elif password_score == 3:
    print("Score: 3/5")
    print("Rating: Moderate")
elif password_score == 4:
    print("Score: 4/5")
    print("Rating: Strong")
elif password_score == 5:
    print("Score: 5/5")
    print("Rating: Very Strong")
    print("Good job!")