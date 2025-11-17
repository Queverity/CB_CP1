# CB 1st Flexible Calculator 
import statistics as stat

number = True
numbers = []

def calculate(*numbers,function):
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

print("Welcome to Flexible Calculator!")

while True:

    while number == True:
        pass