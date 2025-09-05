# CB 1st Basic Calculator
global validating
global validating_two
validating = True
validating_two = True




while validating == True:
    digit_one = input("Enter a number: \n").strip()
    if digit_one.isalpha():
        print("Invalid answer")
        continue
    else:
        if digit_one.isdigit():
            digit_one = int(digit_one)
            validating = False
            break
        else:
            digit_one = float(digit_one)
            validating = False
            break
         

while validating_two == True:
    digit_two = input("Enter another number: \n").strip()
    if digit_two.isalpha():
        print("Invalid answer")
        continue
    else:
        if digit_two.isdigit():
            digit_two = int(digit_two)
            validating_two = False
            break
        else:
            digit_two = float(digit_two)
            validating_two = False
            break

num_addition = round(digit_one + digit_two, 2)

num_subtraction = round(digit_one - digit_two, 2)

num_multiplacation = round(digit_one * digit_two, 2)

num_division = round(digit_one / digit_two, 2)

num_floor = round(digit_one // digit_two, 2)

num_modulo = round(digit_one % digit_two, 2)

num_exponent = round(digit_one ** digit_two, 2)



print(str(digit_one) + " + " + str(digit_two) + " = " + str(num_addition))

print(str(digit_one) + " - " + str(digit_two) + " = " + str(num_subtraction))

print(str(digit_one) + " x " + str(digit_two) + " = " + str(num_multiplacation))

print(str(digit_one) + " / " + str(digit_two) + " = " + str(num_division))

print(str(digit_one) + " // " + str(digit_two) + " = " + str(num_floor))

print(str(digit_one) + " % " + str(digit_two) + " = " + str(num_modulo))

print(str(digit_one) + " ^ " + str(digit_two) + " = " + str(num_exponent))

