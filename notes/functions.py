# CB 1st Functions Notes

# Set variables

# Define functions

def add(x,y):
    return x + y
    
def initials(name):
    names = name.split(" ")
    initals = ""
    for name in names:
        intials += name[0]
    
    return intials


x = int(input("Enter a whole number."))
y = int(input("Enter another whole number."))
print(f"{x} + {y} = {add(x,y)}")

print(add(5,5))

total = add(6,7)

print(total)

print(f"498572 + 987459827 = {add(498572,987459827)}")

def calculate_Rectangle_Area(length,width):
    return length * width

length = int(input("What is the length of your rectangle?"))
width = int(input("What is the width of your rectangle?"))

rectangle_Area = calculate_Rectangle_Area(length,width)
print(f"The area of your rectangle is {rectangle_Area}.")