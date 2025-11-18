# CB 1st Flexible Calculator 
import statistics as stat

numbers = []
functions = ["sum","average","max","min","product"]

def calculate(numbers):
    total = 0
    while True:
        function = input("What function do you want to perform? sum/average/max/min/product").strip().lower()
        if function not in functions:
            print("invalid answer")
            continue
        else:
            if function == "sum":
                for i in numbers:
                    total += i
                break
            elif function == "average":
                total = stat.mean(numbers)
                break
            elif function == "max":
                total = max(numbers)
                break
            elif function == "min":
                total = min(numbers)
                break
            elif function == "product":
                for i in numbers:
                    if numbers.index(i) == 0:
                        total += i
                    else:
                        total = total * i
                break
    
    return total

print("Welcome to the Flexible Calculator!")

while True:

    while True:
        append_num = input("Enter a number, or enter 'done' to move onto calculations." )
        if append_num.strip().lower() == "done":
            break
        else:
            if append_num.isnumeric():
                append_num = float(append_num)
                numbers.append(append_num)
                print(numbers)
            else:
                print("invalid answer")

            
   
    total = calculate(numbers)
    print(f"Result: {total}")

    again = input("Would you like to perform another calculation? yes/no").strip().lower()
    if again == "yes":
        print("Cleared number list")
        numbers.clear()
        continue
    else:
        print("Goodbye!")
        break


