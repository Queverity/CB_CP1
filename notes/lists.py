# VL 1st Lists Notes


# List Syntax: Item then comma.
sibs = ["Andy","Rosie","Anthony","Viola","Evalyn","Wren","Morgan"]

print(sibs)

# Printing a specific item by calling it's index
print(sibs[5])

# Checking length of the list
print(f"This list is {len(sibs)} people long.")

# Changing an item in the list
sibs[6] = "Honey Badger 1"
print(sibs)
# Changing multiple items in a list
sibs[5:6] = ["Kaiya", "Morgan"]
sibs.pop()
sibs.pop(2)
sibs.remove("Andy")
print(sibs)
# sibs.clear()
sibs.append("Andy")
sibs.insert(2,"Anthony")
print(sibs)

for x in sibs:
    print(x)

