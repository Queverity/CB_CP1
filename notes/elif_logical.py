# CB 1st Elifs and Logical Operators Notes

grade = 100

if grade > 100:
    print(f"You did extra credit. . . you did {grade - 100}% extra credit!")
elif grade == 100:
    print("You have a perfect grade!")
else:
    print(f"git gud you {grade}% noob")

username = "MsLaRose"
password = "1234"

user = input("Enter your username: ")
pword = input("Enter your password: ")

if not user or not pword:
    print("Please enter a valid input")
elif user == username and pword == password:
    print(f"Welcome {username}!")
elif user == username:
    print("Password incorrect")
else:
    print("Invalid credentials")