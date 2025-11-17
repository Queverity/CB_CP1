# CB 1st *args and **kwargs Notes
"""
def hello(name = "Sigma", age = 67):
    return f"Hello {name}! You are {age} years old."

print(hello())
print(hello(age = 69, name = "Skibidi"))
print(hello("Baby Gronk"))
print(hello(age = 420))"""

def hello(*names, **kwargs):
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"Hello {n} {kwargs['last_name']}!")

def full_name(age=67,**names):
    if 'middle' in names.keys():
             return f"{names['first']} {names['middle']} {names['last']} is {age} years old"
    else:
         return f"{names['first']} {names['last']} is {age} years old"

hello("Alex","Katie","Andrew","Vienna","Tia","Treyson","Xavier","Jake", last_name="LaRose", dad = "Eric", num_cats=5)

print(full_name(first = "Koro",last = "Sensei", age = "???"))
print(full_name(first="Albus",middle="Brian",last="Dumbledore", age="old"))