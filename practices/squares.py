# CB 1st Squared Numbers 

numbers = []
print("List Exponenentiater")

while True:
    while True:
            # ask for number
            append_num = input("Enter a number, or enter 'done' to move onto exponentiation." )
            # if input is "done", break the loop
            if append_num.strip().lower() == "done":
                break
            # if input is not done
            else:
                # check if input is a number
                if append_num.isnumeric():
                    # if it is a number, convert it to a float and then append it to numbers list
                    append_num = int(append_num)
                    numbers.append(append_num)
                else:
                    # if it is not a number, print "invalid answer"
                    print("invalid answer")
    while True:
        # ask user what number they would like to raise numbers to the power of
        power = input("Enter a number to exponentiate your numbers by.")
        # if the ansewr is a number, convert it to an integer then break the loop
        if power.isnumeric():
           power = int(power)
           break
        # if the answer is not a number
        else:
            print("invalid answer") 

    # use mapping and lambda fuctions go through the numbers list and raise each number to the power of power variable
    # make sure to turn this into a list
    exponentiated_numbers = list(map(lambda num:num ** power, numbers))
    # go through exponentiated_numbers list and print original numbers then raised numbers
    for i, x in enumerate(exponentiated_numbers):
        print(f"Orignal: {numbers[i]} Exponentiated: {exponentiated_numbers[i]}")

    # ask if user would like to exponentiate more numbers
    again = input("Would you like to exponentiate another list of numbers? yes/no").strip().lower()
    # if they say yes, clear the number list then go back to the start of the loop
    if again == "yes":
        print("Cleared number list")
        numbers.clear()
        continue
    # if anything else is said, say "goodbye" then break the main loop
    else:
        print("Goodbye!")
        break