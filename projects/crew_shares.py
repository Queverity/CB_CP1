# CB 1st Crew Shares
global validating
global validating_two
validating = True
validating_two = True

while True:

    while validating == True:
        total_profit = input("How much did the crew gain in total? (input in dollars, don't include the dollar sign)").strip()
        if total_profit.isalpha() or int(total_profit) <= 0:
            print("Invalid answer")
            continue
        else:
            if total_profit.isdigit():
                total_profit = int(total_profit)
                validating = False
                break
            elif total_profit.isdecimal() or "." in total_profit:
                total_profit = float(total_profit)
                validating = False
                break


    while validating_two == True:
        crew_size = input("How many members of the crew are there? (Not counting the captain or first mate)").strip()
        if crew_size.isalpha() or crew_size == "0" or "." in crew_size:
            print("Invalid answer")
        else:
            crew_size = int(crew_size)
            validating_two = False
            break

    share = total_profit/crew_size

    captain_income = share * 7

    first_mate_income = share * 3

    crew_income = share - 500

    print(f"Total profit: {total_profit:.2f}\n Crew size (not counting first mate or captain): {crew_size}\n The captain earns: {captain_income:.2f}\n The first mate earns: {first_mate_income:.2f}\n The crew still needs: {crew_income:.2f}")
    break