# CB 1st Dice Roller
import random
global die_type
global die_amount
global dice
global roll

dice = []


def d_20(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)

def d_12(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)

def d_10(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)

def d_8(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)

def d_6(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)

def d_4(roll,dice):
    roll = random.randint(1,20)
    dice.append(roll)


while True:
    dice_type = input("What kind of dice do you want to roll? Enter as follows: D-20, D-12, D-10, D-8, D-6, D-4").strip().capitalize()
    while True:
        dice_amount = int(input("How many of these dice do you want to roll?"))
        if dice_amount <= 0 or dice_amount.isalpha():
            print("Invalid answer")
            continue
        else:
            break

    match dice_type:
        case "D-20":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")
        case "D-12":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")
        case "D-10":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")
        case "D-8":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")
        case "D-6":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")
        case "D-4":
            for i in range(dice_amount):
                d_20()
                print(f"Your roll(s) are: {dice}.")