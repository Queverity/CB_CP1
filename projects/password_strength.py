# CB 1st Password Strength Checker

# import time library
import time

password_score = 0

# These variables will be used when telling the user if their password passed certain checks.
# They are turned to True in the while loop after this (starts line 25) if their conditions are met. 

length_check = False
upper_check = False
lower_check = False
digit_check = False
special_check = False

special_characters = ["`","~","!","@","#","$","%","^","&","*","_","-","=","+","|","/",":",";","'",'"',",",".","<",">","?","[","]","{","}","(",")"," "]

# This while loop used various string methods along with for loops to check if certain types of characters are in the password.
# If a certain type of character is in the string, it will set the relevant variable to True, increment password_score, and exit the loop.
# If that chracter is not in the string, it will move on to the next character in the string to check if that character is the specific type we are looking for.
# If the for loop goes through the entire string without finding the specific kind of character it is looking for, it will automatically break.

print("Password strength checker")

while True:
    user_password = input("Enter password: ")
    if len(user_password) >= 8:
        password_score += 1
        length_check = True
    else:
        pass


    for a in user_password:
        if a.isupper():
            password_score += 1
            upper_check = True
            break
        else:
            continue


    for b in user_password:
        if b.islower():
            password_score += 1
            lower_check = True
            break
        else:
            continue


    for c in user_password:
        if c.isdigit():
            password_score += 1
            digit_check = True
            break
        else:
            continue


    for d in user_password:
        if d in special_characters:
            password_score += 1
            special_check = True
            break
        else:
            continue


    break


# This section tells the user each check the password is going through, if the pasword passes that check, and a reccomendation of what to do with the password if it doesn't pass.
# It will check if the relevant variable was set to True during the earlier while loop to see if that kind of character or requierment was in your password.

print("Checking password strength...")
while True:
    time.sleep(1)
    if length_check == True:
        print("Length Check: PASSED")
    else:
        print("Length Check: FAILED")
        print("Tip: Make sure your password is at least 8 characters long.")
    print("...")
    time.sleep(1)
    if upper_check == True:
        print("Uppercase Check: PASSED")
    else:
        print("Uppercase Check: FAILED")
        print("Tip: Have a variety of upper and lowercase letters in your password.")
    print("...")
    time.sleep(1)
    if lower_check == True:
        print("Lowercase Check: PASSED")
    else:
        print("Lowercase Check: FAILED")
        print("Tip: Have a variety of upper and lowercase letters in your password.")
    print("...")
    time.sleep(1)
    if digit_check == True:
        print("Digit Check: PASSED")
    else:
        print("Digit Check: FAILED")
        print("Tip: Make sure to have numbers in your password.")
    print("...")
    time.sleep(1)
    if special_check == True:
        print("Special Character Check: PASSED")
    else:
        print("Special Character Check: FAILED")
        print("Tip: Having special characters is good practice for your passwords.")
   
    break



# This section will check the password_score variable, and tell the user different password ratings based on the score.
# It will also give feedback for the password depending on the score the password got.

print("Password Strength: ")
if password_score <= 2:
    print(f"Score: {password_score}/5")
    print("Rating: Weak")
    print("This password needs significant improvement. Make sure to change it so all of the unsatisfied checks are met.")
elif password_score == 3:
    print("Score: 3/5")
    print("Rating: Moderate")
    print("This password needs some improvement. Make sure to change it so all of the unsatisfied checks are met.")
elif password_score == 4:
    print("Score: 4/5")
    print("Rating: Strong")
    print("This password needs only a little improvement. Make sure to change it so all of the unsatisfied checks are met.")
elif password_score == 5:
    print("Score: 5/5")
    print("Rating: Very Strong")
    print("Good job!")
else:
    print("Unexpected error")


