# CB 1st Who are You?
user_info = [{"name":"Dave", "age":"15", "fav_color":"blue"}]
running = True

while running:

    name = input(f"What is your name?").capitalize()
    for info in user_info:
        if name == info["name"]:
            print(f"You have already used this program.")
            print(f"You are {user_info[name]}, {user_info[age]}, and your favorite color is {user_info[fav_color]}.")
    age = int(input(f"What is your age in years?"))
    fav_color = input(f"What is your favorite color?")

    info_dict = {"name": name, "age": str(age), "fav_color": fav_color}
    user_info.append(info_dict)

    print(f"You are {name}, {age} years old, and your favorite color is {fav_color}.")
     
