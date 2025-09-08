# CB 1st Formatting Outputs Notes

# How to write the format method
name = "Eric"
age = 912789
money = 25
percent = .67

# {:,}: places commas in a large number where they should be
# {:E}: turns a number into scientific notation
# {:b}: turns a number into binary
# {:.numf}: tells the computer you want to see (num) decimal places
# {:%}: puts a percentage sign in front of a number

print("Hello {}, you are {} years old. That is so old! You have ${:.2f}. You must be rich! Random percent is {:%}".format(name, age, money,percent)) # <- This is an old, outdated method.

# f-strings

print(f"Hello {name}. You are {age:,} years old. That is so old. You have ${money:.2f}, you must be rich. Random percent is {67/100:%}.")