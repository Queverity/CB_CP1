# CB 1st Factorial Calculator

# define function for calculating factorial (Franco)
def fact_calc(num):
    result = 1
    # Since we're decreasing the number in the for_loop, we'll want to set a variable for the original number so we can print it out later in the function. (Pryor)
    original_num = num # Pryor
    # use a for loop to iterate over num, if it's infinite do i = 1 (Franco)
    for i in range(num):
        # For the factorial to work correctly, you need to decrease the number by one each time you loop over it. (Pryor)
        result *= num
        num -= 1 # Pryor
    return f"{original_num}! = {result}"

print("This is a factorial calculator; Please enter a whole number.")
while True:
    # optionally, strip & remove to wittle down inputs to just numbers (Franco)
    num = input("Enter number:\n")
    # Most of the code works off a variable called "num", while the actual input was "number". (Pryor)
    # The function for checking if it is a numberis ".isdigit()", not ".isint()". (Pryor)
    if num.isdigit() == True:
        # You need to convert the input into an integer for it to work properly. (Pryor)
        num = int(num) # Pryor
        break
    else:
        continue

# You need to print out the function result for it to show anything.(Pryor)
print(fact_calc(num))