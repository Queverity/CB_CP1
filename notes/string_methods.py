# CB 1st String Methods Notes

subject = "Computer Programming 1!"

print(subject.upper())

print(subject.center(100))

# Stupid/Idiot Proofing Inputs
# lower() = all lower case
# upper() = all upper case
# capitalize() = capitalize the first letter of the first word
# title() = capitalize the first letter of every word
# format(variable=variable, variable2=variable2) = 
color = input("What is your favorite color? \n").strip().title()
full_name = input("What is your full name?").strip().title()

print("That is cool, {full_name} I like {color} too!".format(full_name=full_name,color=color))

# f-strings

print(f"That is cool, {full_name}. I like {color} too!")

pi = "3.14159"

print(f"We all know pi is equal to {pi}.")
print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."
print(sentence.find("lazy"))

start = sentence.index("lazy")
length = len("lazy")
print(sentence[start:start+length])
print(sentence.replace("lazy","dead"))