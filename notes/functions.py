# CB 1st Functions Notes

# Set variables
player_health = 100
monster_health = 100

# Define functions

def add(x,y):
    return x + y
    
def initials(name):
    names = name.split(" ")
    initials = ""
    for name in names:
        initials += name[0]
    
    return initials

def calculate_Rectangle_Area(length,width):
    return length * width

def damage(amount,turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount

monster_health, player_health = damage(10, "player")
print(f"Monster health: {monster_health}")
print(f"Player health: {player_health}")

x = int(input("Enter a whole number."))
y = int(input("Enter another whole number."))
print(f"{x} + {y} = {add(x,y)}")

print(add(5,5))

total = add(6,7)

print(total)

print(f"498572 + 987459827 = {add(498572,987459827)}")

user_name = input("What is your name?").strip().upper()
print(f"Your initals are {initials(user_name)}.")



length = int(input("What is the length of your rectangle?"))
width = int(input("What is the width of your rectangle?"))

rectangle_Area = calculate_Rectangle_Area(length,width)
print(f"The area of your rectangle is {rectangle_Area}.")