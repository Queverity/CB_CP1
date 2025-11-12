# CB 1st Order Up

# Menu for drinks
drink_menu = {
    # Drinks and their prices
    "Coke": 1.00,
    "Pepsi": 1.00,
    "Root Beer": 1.00,
    "Sprite": 1.00,
}

# Menu for main courses
main_menu = {
     # Main meals and their prices
    "Hamburger": 1.99,
    "Cheeseburger": 2.49,
    "Hotdog": 1.49,
}

# Menu for sides
side_menu = {
    # Sides and their prices
    "Fries": 1.00,
    "Chips": 1.00,
    "Salad": 1.49,

}

# Dictionary to save user order
user_order = {
    "Drink": " ",
    "Main course": " ",
    "First side dish": " ",
    "Second side dish": " ",
}



# function to print out the menu
def print_menus(drink_menu,main_menu,side_menu):
    print("Resturaunt Menu")

    # for loop that lopos through the drink menu and prints out each item and its price in a visually appealing way
    print("Drinks")
    for item, price in drink_menu.items():
        print(f"{item}: ${price:.2f}")

    # for loop that lopos through the main menu and prints out each item and its price in a visually appealing way
    print("Mains")
    for item, price in main_menu.items():
        print(f"{item}: ${price:.2f}")

    # for loop that lopos through the side menu and prints out each item and its price in a visually appealing way
    print("Sides")
    for item, price in side_menu.items():
        print(f"{item}: ${price:.2f}")


# function for calculating final price
def calculate_price(user_order,drink_menu,main_menu,side_menu):
    # set total variable to add onto later
    total = 0
    for item in user_order.values():
        # if the user didn't order anything for a selection, bypass it
        if item == "Nothing":
            pass
        # if the user ordered a drink, check which drink, then add the value to total
        elif item in drink_menu:
            total += drink_menu[item]

        # if the user ordered a main course, check which main, then add the value to total
        elif item in main_menu:
            total += main_menu[item]

        # if the user ordered a side, check which side, then add the value to total
        elif item in side_menu:
            total += side_menu[item]
            
        # if something gets through somehow
        else:
            print("Unexpected error")
    
    # calculate tax
    total = total * 1.08

    # return final price to be printed to user
    return total

    
# context for prices
print("All prices in USD")

# call print menu function
print_menus(drink_menu,main_menu,side_menu)

# for loop for ordering
for item in user_order:
    # while item in user_order dictionary is "drink"
    while item == "Drink":
        # ask what they would like for the item, with some string methods for fool-proofing
        choice = input(f"What would you like for your {item}? Enter 'None' to skip this selection.").capitalize().strip()
        # if the user doesn't want anything for the item, set item value to nothing, then break the loop
        if choice == "None":
            user_order[item] = "Nothing"
            break
        # if the answer the user enters is not in the drink menu, print "invalid answer" then continueop
        elif choice not in drink_menu:
            print("Invalid answer")
            continue
        # if the first two conditions are passed, set item value to the value of the drink from the drink menu, then break the loop
        else:
            user_order[item] = choice
            break
    # while item in user_order dictionary is "main course"
    while item == "Main course":
        # ask what user wants for item, string methods used for stupid-proofing
        choice = input(f"What would you like for your {item}? Enter 'None' to skip this selection.").capitalize().strip()
        # if the user doesn't want anything, set item value to "nothing", then break the loop
        if choice == "None":
            user_order[item] = "Nothing"
            break
        # if answer the user gives is not "none" or in the main_menu dictionary, print "invalid ansewr", then continue loop
        elif choice not in main_menu:
            print("Invalid answer")
            continue
        # if the first two condtions are passed, set item value to the value of the main from the main menu, then break the loop
        else:
            user_order[item] = choice
            break
    # while item in user_order dictionary is "first side dish" or "second side dish"
    while item == "First side dish" or item == "Second side dish":
        # ask what user wants for item, string methods used for stupid-proofing
        choice = input(f"What would you like for your {item}? Enter 'None' to skip this selection.").capitalize().strip()
        # if the user doesn't want anything, set item value to "nothing", then break the loop
        if choice == "None":
            user_order[item] = "Nothing"
            break
        # if ansewr the user enters in not "None" or in the side_menu dictionary, print "invalid answer", then continue loop
        elif choice not in side_menu:
            print("Invalid answer")
            continue
        # if the first two condtions are passed, set item value to the value of the side from the side menu, then break the loop
        else:
            user_order[item] = choice
            break

print("Your Order:")
# for loop to loop through user_order values
for choice in user_order.values():
    # if the value is something in the drink menu, print choice name and its price from the drink menu
    if choice in drink_menu:
        print(f"{choice}: ${drink_menu[choice]:.2f}")

    # if the value is something in the main menu, print choice name and its price from the main menu
    elif choice in main_menu:
        print(f"{choice}: ${main_menu[choice]:.2f}")

    # if the value is something in the side menu, print choice name and its price from the side menu
    elif choice in side_menu:
        print(f"{choice}: ${side_menu[choice]:.2f}")

    # if the choice is nothing, print the word "nothing"
    elif choice == "Nothing":
        print(f"Nothing")
    
    # if all the other conditions are passed, throw error mesage
    else:
        print("Unexpected error")

# loop for printing out price
while True:
    # call calculate_price function are set global variable total to the return of calculat eprice
    total = calculate_price(user_order,drink_menu,main_menu,side_menu)
    # if the total is not equal to 0, print out final price and break the loop
    if total != 0:
        print(f"Final Price (tax included): ${total:.2f}")
        break
    # if the total is equal to or below 0 somehow, print mildy snarky message, then break loop
    else:
        print("You came to a restaraunt and didn't buy anything. Why?")
        break




