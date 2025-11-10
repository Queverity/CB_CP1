# CB 1st Order Up

menu = {
    
}

user_order = {
    "drink": " ",
    "main course": " ",
    "first side dish": " ",
    "second side dish": " ",
}

for item in user_order:
    choice = (f"What would you like for your {item}? Enter 'None' to skip this selection.")
    if item not in menu:
        print("Invalid answer")
        continue
    elif choice == "None":
        user_order[item] = ""
    else:
        user_order[item] = choice

