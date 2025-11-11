# CB 1st Order Up

drink_menu = {
    # Drinks and their prices
    "Coke": 1.00,
    "Pepsi": 1.00,
    "Root Beer": 1.00,
    "Sprite": 1.00,
    "Chocolate Milkshake": 2.00,
    "Vanilla Milkshake": 2.00,
}

main_menu = {
     # Main meals and their prices
    "Hamburger": 2.00,
    "Cheeseburger": 2.50,
    "Hotdog": 1.50,
    "Chicken Sandwich": 1.50,
}

side_menu = {
    # Sides and their prices
    "Fries": 1.00,
    "Onion Rings": 1.50,
    "Tater Tots": 1.00,
}


user_order = {
    "Drink": " ",
    "Main course": " ",
    "First side dish": " ",
    "Second side dish": " ",
}



def print_menus(drink_menu,main_menu,side_menu):
    print("Resturaunt Menu")

    print("Drinks")
    for item, price in drink_menu.items():
        print(f"{item}: ${price:.2f}")

    print("Mains")
    for item, price in main_menu.items():
        print(f"{item}: ${price:.2f}")

    print("Sides")
    for item, price in side_menu.items():
        print(f"{item}: ${price:.2f}")


def calculate_price(user_order,drink_menu,main_menu,side_menu):
    total = 0
    for item in user_order:
        if item in drink_menu:
            total += drink_menu[item]

        elif item in main_menu:
            total += main_menu[item]

        elif item in side_menu:
            total += side_menu[item]
            
        else:
            print("Unexpected error")
    total = total * 1.08

    return total

    

print("All prices in USD")

print_menus(drink_menu,main_menu,side_menu)

for item in user_order:
    choice = input(f"What would you like for your {item}? Enter 'None' to skip this selection.").capitalize().strip()
    if choice not in drink_menu and choice not in main_menu and choice not in side_menu:
        print("Invalid answer")
        continue
    elif choice == "None":
        user_order[item] = ""
    else:
        user_order[item] = choice

for choice in user_order.keys():
    if choice in drink_menu:
        print(f"{choice}: ${drink_menu[choice]}")

    elif choice in main_menu:
        print(f"{choice}: ${main_menu[choice]}")

    elif choice in side_menu:
        print(f"{choice}: ${side_menu[choice]}")
    
    else:
        print("Unexpected error")

total = calculate_price(user_order,drink_menu,main_menu,side_menu)
print(f"Final Price: {total}")



