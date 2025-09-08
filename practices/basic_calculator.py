# CB 1st Basic Calculator
global validating
global validating_two
validating = True
validating_two = True
global operations

while True:

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

   
    while True:
        equation = input("What math operation do you want to perform? Enter as follows: Addition, Subtraction, Multiplacation, Division, Floor Division, Modulo, Exponent").strip().title()
        match equation:
            case "Addition":
                num_addition = round(digit_one + digit_two, 2)
                print(f"{str(digit_one)} + {str(digit_two)} = {num_addition:.2f}")
                break
            case "Subtraction":
                 num_subtraction = round(digit_one - digit_two, 2)
                 print(f"{str(digit_one)} - {str(digit_two)} = {num_subtraction:.2f}")
                 break
            case "Multiplacation":
                    num_multiplacation = round(digit_one * digit_two, 2)
                    print(f"{str(digit_one)} x {str(digit_two)} = {num_multiplacation:.2f}")
                    break
            case "Division":
                    num_division = round(digit_one / digit_two, 2)
                    print(f"{str(digit_one)} / {str(digit_two)} = {num_division:.2f}")
                    break
            case "Floor Division":
                  num_floor = round(digit_one // digit_two, 2)
                  print(f"{str(digit_one)} // {str(digit_two)} = {num_floor:.2f}")
                  break
            case "Modulo":
                  num_modulo = round(digit_one % digit_two, 2)
                  print(f"{str(digit_one)} % {str(digit_two)} = {num_modulo:.2f}")
                  break
            case "Exponent":
                  num_exponent = round(digit_one ** digit_two, 2)
                  print(f"{str(digit_one)} ^ {str(digit_two)} = {num_exponent:.2f}")
                  break
            case _:
                  print("Invalid answer")
                  continue
             
   
    print("goodbye!")
    break