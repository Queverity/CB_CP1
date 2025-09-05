# CB 1st Idiot Proof
global phone
global formatted_phone
global gpa
global float_gpa
global rounded_gpa

first_name = input("What is your first name? \n").strip().capitalize()

last_name = input("What is your last name? \n").strip().capitalize()

while True:
    phone = input("What is your phone number?").strip()
    if len(phone) == 10:
        formatted_phone = phone[:3] + " " + phone[3:6] + " " + phone [6:]
        break
    else:
        print("Invalid phone number")
        continue

while True:
    gpa = input("What is your non-weighted GPA?").strip()
    float_gpa = float(gpa)
    if float_gpa < 0 or float_gpa > 4:
        print("Invalid GPA")
        continue
    elif float_gpa <= 4:
        rounded_gpa = round(float_gpa,1)
        break

full_name = first_name + " " + last_name

print(f"Name: {full_name} \nPhone Number: {formatted_phone} \nGPA: {rounded_gpa}")
