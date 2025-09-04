# CB 1st Idiot Proof

first_name = input("What is your first name? \n").capitalize().strip()

last_name = input("What is your last name? \n").capitalize().strip()

phone = input("What is your phone number?").strip()

gpa = input("What is your GPA?").strip()

float_gpa = float(gpa)

rounded_gpa = round(float_gpa,1)

full_name = first_name + " " + last_name

print(f"Name: {full_name} \nPhone Number: {phone} \nGPA: {rounded_gpa}")
