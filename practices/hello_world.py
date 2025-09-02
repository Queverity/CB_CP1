# CB 1st Hello World Assignment

# These lists contain returning users and program admins, and are called upon when checking if a name is in them or not.
returning = ["Darius","Cecily","Nick","Matthew","Parker"]
admin = ["Pryor","Ms. LaRose"]

# I didn't use a .capitlize() function here because it messes with the name Ms. LaRose.
name = input("What is your name:\n")


# These if-then statements will capitlize the name unless it is Ms. LaRose, as that name is case sensitive.
if name == "Ms. LaRose":
    name = name
else:
    name = name.capitalize()

# The top two if statements check if a name is in the "returning list", then it checks if the name is in the "admin" list. If it is in neither lists, it will just greet them.
if name in returning:
    print(f"Welcome back {name}!")

elif name in admin:
    print(f"Greetings, Admin {name}.")
else:
    print(f"Welcome to the program, {name}!")
