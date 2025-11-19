# CB 1st Flexible Calculator 

# import statistics library
import statistics as stat

# list to put numbers in
numbers = []

# list for stupid-proofing purposes
functions = ["sum","average","max","min","product"]

# function for performing different math functions
def calculate(functions,*numbers):
    total = 0
    while True:
        # take user input for what math function to do
        function = input("What function do you want to perform? sum/average/max/min/product").strip().lower()
        # if user input is not in functions list, tell "invalid answer", then continue (go back to the start of the loop)
        if function not in functions:
            print("invalid answer")
            continue
        # if user entered a valid answer
        else:
            # if user entered sum, go through numbers list and add each number to total
            if function == "sum":
                for i in numbers:
                    total += i
                break
            # if user entered average, use mean functions from statistics library to calculate average and set total to that
            elif function == "average":
                total = stat.mean(numbers)
                break
            elif function == "max":
                # if user entered max, use max function and set total to that
                total = max(numbers)
                break
            elif function == "min":
                # if user entered min, use min function and set total to that
                total = min(numbers)
                break
            elif function == "product":
                # if user entered product, check if the index of an item is 0 (meaning it is the first item). If it is, just add it to total. If it is not, multiply the number by total.
                for i in numbers:
                    if numbers.index(i) == 0:
                        total += i
                    else:
                        total = total * i
                break
    # return final answer
    return total

# telling the user what the program does
print("Welcome to the Flexible Calculator!")

# main loop
while True:

    # while loop for taking in numbers
    while True:
        # ask for number
        append_num = input("Enter a number, or enter 'done' to move onto calculations." )
        # if input is "done", break the loop
        if append_num.strip().lower() == "done":
            break
        # if input is not done
        else:
            # check if input is a number
            if append_num.isnumeric():
                # if it is a number, convert it to a float and then append it to numbers list
                append_num = float(append_num)
                numbers.append(append_num)
            else:
                # if it is not a number, print "invalid answer"
                print("invalid answer")

            
    # set global total variable to calculate function
    total = calculate(functions,*numbers)
    # print the total variable
    print(f"Result: {total}")

    # ask if user would like to run another calculation
    again = input("Would you like to perform another calculation? yes/no").strip().lower()
    # if they say yes, clear the number list then go back to the start of the loop
    if again == "yes":
        print("Cleared number list")
        numbers.clear()
        continue
    # if anything else is said, say "goodbye" then break the main loop 
    else:
        print("Goodbye!")
        break


