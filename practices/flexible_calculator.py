# CB 1st Flexible Calculator 
import statistics as stat

number = True
numbers = []

def calculate(numbers,function):
    total = 0
    if function == "sum":
        for i in numbers:
            total += i
    elif function == "average":
        total = stat.mean(numbers)
    elif function == "max":
        total = max(numbers)
    elif function == "min":
        total = min(numbers)
    elif function == "product":
        for i in numbers:
            if numbers.index(i) == 0:
                total += i
            else:
                total * i
    
    return total

print("Welcome to the Flexible Calculator!")

while True:

    while number == True:
        append_num = input("Enter a number, or enter 'done' to exit." )
        if append_num == "done":
            break
        
        else:
            print("invalid answer")
            continue

    function = input("What function do you want to perform? sum/average/max/min/product").strip().capitalize()
    print(f"Result: {calculate(numbers,function)}")

    again = input("Would you like to perform another calculation? yes/no").strip().lower()
    if again == "yes":
        print("Cleared number list")
        numbers.clear()
        continue
    else:
        print("Goodbye!")
        break


