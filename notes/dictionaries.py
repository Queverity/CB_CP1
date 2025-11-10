# CB 1st Dictionaries Notes

# Key:Value Pairs

person = {
    #key:value,
    "Name": "Xavier",
    "Age": 22,
    "Job": "Maverick",
    "Sibling": ["Alex","Katie","Andrew","Vienna","Tia","Treyson","Jake"],
}

person_two = {
    #key:value,
    "Name": "Jake",
    "Age": 21,
    "Job": "Hobo",
    "Sibling": ["Alex","Katie","Andrew","Vienna","Tia","Treyson","Xavier"],
}

print(f"Name is {person["Name"]}")
print(person.keys())
for key in person.keys():
    if key == "Sibling":
        for name in person[key]:
            print(f"{person['Name']} has a sibling named {name}.")
    else:
        print(f"{key} is {person[key]}.")

for item in person_two.items():
    print(item)
