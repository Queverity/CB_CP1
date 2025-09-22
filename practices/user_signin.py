# CB 1st User Sign In
users = {"Pryor":"0319password","Andy":"wordpass0507","Rosie":"inthe4thwall","Viola":"almightyshortone"}
global Welcome
Welcome = False
global tries
tries = 0

while Welcome == False:
    while Welcome == False:
        username = input("What is your username?").strip()
        if username not in users:
            print("Username not found, try again")
        else:
            while True:
                password = input("What is your password?").strip()
                if password != users[username]:
                    print("invalid password")
                    tries += 1
                    if tries == 5:
                        print("Too many failed attempts, goodbye!")
                        Welcome = True
                        break
                    else:
                        continue
                else:
                    print(f"Welcome {username}!")
                    Welcome = True
                    break

    
    
        
    
    

