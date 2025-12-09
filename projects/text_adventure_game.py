# CB 1st Text Adventure Final
import random
import time

puzzle_one_status = False
puzzle_two_status = False
puzzle_three_status = False
puzzle_four_status = False
puzzle_five_status = False

gnome_defeated = False
intezar_defeated = False

user_room = 1

player_max_health = 100

player_stats = {
"Health":100,
"Attack":10,
"Defense":10,
"Speed":10
}

gnome_stats = {
"Health":100,
"Attack":8,
"Defense":8,
"Speed":12,
"Type":"Gnome",
}

intezar_stats = {
"Health":150,
"Attack":12,
"Defense":10,
"Speed":12,
"Type":"Fish",
}


inventory = {

}

def game_over(puzzle_one_status,puzzle_two_status,puzzle_three_status,puzzle_four_status,puzzle_five_status,player_stats,gnome_stats,intezar_stats,inventory,user_room,gnome_defeated,intezar_defeated):
        play_again = input("You died! Would you like to play again? Yes/No").strip().capitalize()
        if play_again == "No":
                print("Goodbye!")
                return "Exit"
        else:
                puzzle_one_status = False
                puzzle_two_status = False
                puzzle_three_status = False
                puzzle_four_status = False
                puzzle_five_status = False

                gnome_defeated = False
                intezar_defeated = False

                user_room = 1

                player_stats = {
                "Health":100,
                "Attack":10,
                "Defense":10,
                "Speed":10
                }

                gnome_stats = {
                "Health":100,
                "Attack":8,
                "Defense":8,
                "Speed":12
                }

                intezar_stats = {
                "Health":150,
                "Attack":12,
                "Defense":10,
                "Speed":12
                }

                inventory = {

                }

                return "Reset"

def print_inventory(inventory):
        if bool(inventory) == False:
               print("Your inventory is empty.")
        else:
                print("Inventory:")
                for key,value in inventory.items():
                        print(f"{key}: {value}")

def print_stats(player_stats):
        print("Stats:")
        for key,value in player_stats.items():
                print(f"{key}: {value}")
        
def puzzle_one(inventory):
        print("You head over to the box. On it, you see two small plaques, and a set of wheels with letters on them. One of the plaques reads 'UMMCMISNO', and the other reads 'unscramble these letters into a word and enter them into the box'.")
        while True:
                choice = input("Enter your answer:\n").strip().capitalize()
                if choice != "Communism":
                        print(f"You set the wheels to {choice}, but the box does not open. Try again.")
                        continue
                else:
                        print(f"You set the wheels to {choice}, and the box clicks open. In it, you find a key. You store it in your inventory. P.S: You can look at your inventory to find this again.")
                        inventory["Floor One Key"] = "A key to a door on the first floor."
                        return True

def puzzle_two(player_stats,player_max_health):
        print("You head over to the box. On it, you see two small plaques, and a set of wheels with numbers on them. One of the plaques reads '2x + 4 = 5x - 5', and the other reads 'solve for x and enter it into the box'.")
        while True:
                choice = input("Enter your answer:\n").strip().capitalize()
                if choice != "3":
                        print(f"You set the wheels to {choice}, but the box does not open. Try again.")
                        continue
                else:
                        print(f"You set the wheels to {choice}, and the box clicks open. In it, you find a very tasting looking apple. You eaNt it, and feel yourself become healthier.")
                        print("Health Pool + 25")
                        player_stats["Health"] += 25
                        player_max_health += 25
                        return True
                
def puzzle_three(inventory):
        print("You head over to the box. On it, you see two small plaques, and a set of wheels with letters on them. One of the plaques reads 'gfxpjygfqq', and the other reads 'decipher this word and enter it into the box'. Hint: Ceaser Cipher")
        while True:
                choice = input("Enter your answer:\n").strip().capitalize()
                if choice != "Basketball":
                        print(f"You set the wheels to {choice}, but the box does not open. Try again.")
                        continue
                else:
                        print(f"You set the wheels to {choice}, and the box clicks open. In it, you find the top half of a metal fish. It looks very cartoony. You store it in your inventory. P.S: You can look at your inventory to find this again.")
                        inventory["Top Half Fish"] = "The top half of a metal fish."
                        return True
                
def puzzle_four(inventory):
        print("You head over to the box. On it, you see two small plaques, and four buttons. The buttons have numbers 1 - 4 on them, one number on each. One of the plaques reads 'What assasination triggered World War I?', and the other reads: \n1. Abraham Lincoln \n2. Archduke Franz Ferdinand \n3. Martin Luther King Jr. \n4. The Pope")
        while True:
                choice = input("Enter your answer (number):\n").strip().capitalize()
                if choice != "2":
                        print(f"You push button number {choice}, but the box does not open. Try again.")
                        continue
                else:
                        print(f"You push button number {choice}, and the box clicks open. In it, you find the bottom half of a metal fish. You store it in your inventory. P.S: You can look at your inventory to find this again.")
                        inventory["Bottom Half Fish"] = "The bottom half of a metal fish."
                        return True
                
def puzzle_five(player_stats):
        print("You head over to the box. On it, you see two small plaques, and four buttons. The buttons have numbers 1 - 4 on them, one number on each. One of the plaques reads 'What is the powerhouse of the cell?', and the other reads: \n1. Chloroplast \n2. Nucleus \n3. Mitochondria \n4. Nuclear Energy")
        while True:
                choice = input("Enter your answer (number):\n").strip().capitalize()
                if choice != "3":
                        print(f"You push button number{choice}, but the box does not open. Try again.")
                        continue
                else:
                        print(f"You set the wheels to {choice}, and the box clicks open. In it, you find a minecraft speed potion. You drink it, and become speedier.")
                        print("Speed + 3")
                        player_stats["Speed"] += 3
                        return True
                
def player_attack(player_stats,monster_stats):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20) + 4
    if attack_roll >= monster_stats["Defense"]:
        print(f"You rolled a(n) {attack_roll}. You hit!")
        print("Rolling for damage...")
        time.sleep(1)
        player_damage = (player_stats["Attack"]/3) + random.randint(1,6)
        player_damage = round(player_damage,1)
        print(f"You dealt {player_damage} damage.")
        return round(player_damage,0)
    elif attack_roll - 4 == 20:
        print("You rolled a natural 20. Critical hit! You will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        player_damage = (player_stats["Attack"]/3) + random.randint(1,6)
        player_damage = player_damage * 2
        player_damage = round(player_damage,0)
        print(f"You dealt {player_damage} damage.")
        return round(player_damage,1)
    else:
        print("You missed.")
        return 0
    
def monster_attack(player_stats,monster_stats):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20) + 4
    if attack_roll >= player_stats["Defense"]:
        print(f"The {monster_stats["Type"]} rolled a(n) {attack_roll}. It hit.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_stats["Attack"]/3) + random.randint(1,6)
        monster_damage = round(monster_damage,0)
        print(f"The {monster_stats["Type"]} dealt {monster_damage} damage.")
        return round(monster_damage,1)
    elif attack_roll >= 20:
        print(f"The {monster_stats["Type"]} rolled a natural 20. Critical hit! it will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_stats["Attack"]/3) + random.randint(1,6)
        monster_damage = monster_damage * 2
        monster_damage = round(monster_damage,0)
        print(f"The {monster_stats["Type"]} dealt {monster_damage} damage.")
        return monster_damage
    else:
        print(f"The {monster_stats["Type"]} missed.")
        return 0
    
def win_condition(player_stats,monster_stats):
    if player_stats["Health"] <= 0:
        return 1
    elif monster_stats["Health"] <= 0:
        return 2
    else:
        return 0
    
def gnome_combat(player_stats,gnome_stats):
        turn = 1
        heals = 3
        if player_stats["Speed"] > gnome_stats["Speed"]:
                turn = 1
        elif player_stats["Speed"] < gnome_stats["Speed"]:
                turn = 0
        else:
                turn = random.randint(0,1)
        while True:
                if gnome_defeated == True:
                       return 1
                else:
                        if turn == 0:
                                print("Gnome's Turn")
                                dialouge = random.randint(1,3)
                                if dialouge == 1:
                                       print("Gnome: 'rahhhh down with Wewart!")
                                elif dialouge == 2:
                                       print("Gnome: 'Intezar above all!'")
                                else:
                                       print("Gnome: 'Intezar is the fish man that took over this Triple-Decker Walmart'")
                                damage = monster_attack(player_stats,monster_stats=gnome_stats)
                                player_stats["Health"] -= damage
                                print(f"You have {player_stats["Health"]} hit points left.")
                                turn = 1
                        elif turn == 1:
                                while True:
                                        print("Player's Turn")
                                        print(f"1. Basic Attack\n2. Crazed Attack (x2 damage, you take some damage as well)\n3. Heal ({heals} left)\n4. Flee")
                                        action = input("Enter number for action:\n").strip()
                                        match action:
                                                case "1":
                                                        damage = player_attack(player_stats,monster_stats=gnome_stats)
                                                        gnome_stats["Health"] -= damage
                                                        print(f"The gnome has {gnome_stats["Health"]} hit points left.")
                                                        win = win_condition(player_stats,monster_stats=gnome_stats)
                                                        win = win_condition(player_stats,monster_stats=intezar_stats)
                                                        if win == 1:
                                                                return 0
                                                        elif win == 2:
                                                                gnome_defeated = True
                                                                return 1
                                                        else:
                                                                turn = 0
                                                                break
                                                case "2":
                                                        damage = player_attack(player_stats,monster_stats=gnome_stats) * 2
                                                        gnome_stats["Health"] -= damage
                                                        self_damage = round(damage/3,1)
                                                        player_stats["Health"] -= self_damage
                                                        print(f"The gnome has {gnome_stats["Health"]} hit points left.")
                                                        print(f"You took {self_damage} damage. You have {player_stats["Health"]} hit points left.")
                                                        win = win_condition(player_stats,monster_stats=gnome_stats)
                                                        if win == 1:
                                                                return 0
                                                        elif win == 2:
                                                                gnome_defeated = True
                                                                return 1
                                                        else:
                                                                turn = 0
                                                                break
                                                case "3":
                                                        if heals == 0 or player_stats["Health"] == player_max_health:
                                                                print("You cannot health right now.")
                                                                continue
                                                        else:
                                                                player_stats["Health"] += 12
                                                                while player_stats["Health"] > player_max_health:
                                                                        player_stats["Health"] -= 1
                                                                print(f"You healed 12 damage. You now have {player_stats["Health"]} hit points left.")
                                                                turn = 0
                                                                break
                                                case "4":
                                                        print("Attempting to flee...")
                                                        time.sleep(1)
                                                        print("You failed.")
                                                        turn = 0
                                                        break

def intezar_combat(player_stats,intezar_stats):
        turn = 1
        heals = 3
        if player_stats["Speed"] > intezar_stats["Speed"]:
                turn = 1
        elif player_stats["Speed"] < intezar_stats["Speed"]:
                turn = 0
        else:
                turn = random.randint(0,1)
        while True:
                if intezar_defeated == True:
                       return 1
                else:
                        if turn == 0:
                                print("Intezar's Turn")
                                dialouge = random.randint(1,3)
                                if dialouge == 1:
                                       print("Intezar: 'Wewart and the Dave Legion will fall to me.")
                                elif dialouge == 2:
                                       print("Intezar: 'Even attempting to stop me is foolish, mortal.'")
                                else:
                                       print("Intezar: 'Walmartville shall be mine!'")
                                damage = monster_attack(player_stats,monster_stats=intezar_stats)
                                player_stats["Health"] -= damage
                                print(f"You have {player_stats["Health"]} hit points left.")
                                turn = 1
                        elif turn == 1:
                                while True:
                                        print("Player's Turn")
                                        print(f"1. Basic Attack\n2. Crazed Attack (x2 damage, you take some damage as well)\n3. Heal ({heals} left)\n4. Flee")
                                        action = input("Enter number for action:\n").strip()
                                        match action:
                                                case "1":
                                                        damage = player_attack(player_stats,monster_stats=intezar_stats)
                                                        intezar_stats["Health"] -= damage
                                                        print(f"The fish has {intezar_stats["Health"]} hit points left.")
                                                        win = win_condition(player_stats,monster_stats=intezar_stats)
                                                        if win == 1:
                                                                return 0
                                                        elif win == 2:
                                                                return 1
                                                        else:
                                                                turn = 0
                                                                break
                                                case "2":
                                                        damage = player_attack(player_stats,monster_stats=intezar_stats) * 2
                                                        intezar_stats["Health"] -= damage
                                                        self_damage = round(damage/3,1)
                                                        player_stats["Health"] -= self_damage
                                                        print(f"The gnome has {intezar_stats["Health"]} hit points left.")
                                                        print(f"You took {self_damage} damage. You have {player_stats["Health"]} hit points left.")
                                                        win = win_condition(player_stats,monster_stats=intezar_stats)
                                                        if win == 1:
                                                                return 0
                                                        elif win == 2:
                                                                return 1
                                                        else:
                                                                turn = 0
                                                                break
                                                case "3":
                                                        if heals == 0 or player_stats["Health"] == player_max_health:
                                                                print("You cannot health right now.")
                                                                continue
                                                        else:
                                                                player_stats["Health"] += 12
                                                                while player_stats["Health"] > player_max_health:
                                                                        player_stats["Health"] -= 1
                                                                print(f"You healed 12 damage. You now have {player_stats["Health"]} hit points left.")
                                                                turn = 0
                                                                break
                                                case "4":
                                                        print("Attempting to flee...")
                                                        time.sleep(1)
                                                        print("You failed.")
                                                        turn = 0
                                                        break

print("Some backstory:\n Intezar, the inverse mermaid leader of the Nouijelevad clan and ex-Dave Legion member, has invaded and taken over Walmartville, home of Wewart and the Dave Legion. He has taken up residence in the Triple-Decker Walmart, and you are the only applicable fighter that could take him down. It is your job to infiltrate the Walmart, get to the top floor, and defeat Intezar.")

print("")

def room_one(player_stats,inventory):
       print("You find yourself in what appears to be the lobby of the Triple-Decker Walmart. Around you, you can see scattered and shattered furniture lying on the floor, giving the impression that some sort of attack force barged into here with disregard for property damage. The only other items of interest you can see are doors to your left and right. What would you like to do?")
       while True:
                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Right\n4. Go Left\n").strip()
                match choice:
                        case "1":
                                print_stats(player_stats)
                        case "2":
                                print_inventory(inventory)
                        case "3":
                                return 2
                        case "4":
                                return 3
                        case _:
                                print("Invalid answer. Please try again.")
                                continue
                       
def room_two(player_stats,inventory):
       if "Shield" not in inventory:
                print("You find yourself in what appears to have been an electronics array, though the electronics, along with plenty of glass, are arrayed on the floor now. You can see a door to your left, a door leading back to the room you just exited and, for some unknown reason, a shield just lying on the ground.")
       else:
                print("You find yourself in what appears to have been an electronics array, though the electronics, along with plenty of glass, are arrayed on the floor now. You can see a door to your left and the door leading back to the room you just exited.")       
       while True:
                if "Shield" not in inventory:
                        choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Left\n4. Go Back\n5. Pick Up Shield\n").strip()
                        match choice:
                                case "1":
                                        print_stats(player_stats)
                                case "2":
                                        print_inventory(inventory)
                                case "3":
                                        if "Floor One Key" in inventory:
                                                return 4
                                        else:
                                                print("The door is locked. Perhaps there is a key elsewhere on the floor?")
                                                continue
                                case "4":
                                        return 1
                                case "5":
                                        print("You pick up the shield, and release it will work perfectly for you. You store it in your inventory. P.S: You can inspect your inventory later to look at this.")
                                        print("Defense + 2")
                                        player_stats["Defense"] += 2
                                        inventory["Shield"] = "A shield you found on the floor that grants +2 defense."
                                case _:
                                        print("Invalid answer. Please try again.")
                                        continue
                else:
                       choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Left\n4. Go Back\n").strip()
                       match choice:
                                case "1":
                                        print_stats(player_stats)
                                case "2":
                                        print_inventory(inventory)
                                case "3":
                                        return 2
                                case "4":
                                        return 1
                                case _:
                                        print("Invalid answer. Please try again.")
                                        continue
                               
def room_three(player_stats,inventory,puzzle_one_status,puzzle_two_status):
        while True:
                if puzzle_one_status == False and puzzle_two_status == False:
                        print("You find yourself in a room that seems to be a furniture display that is in suprisingly good condition, relative to the other rooms in this place. It seems whoever barged into here took care not damaging this room. The items of interest you can see in this room are two puzzle boxes, one to your left and one to your right, and the door leading back to the lobby. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Inspect the puzzle box to your left\n4. Inspect the puzzle box to your right\n5. Head back to the lobby\n").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                        case "3":
                                                puzzle_one_status = puzzle_one(inventory)
                                                break
                                        case "4":
                                                puzzle_two_status = puzzle_two(player_stats,player_max_health)
                                                break
                                        case "5":
                                                return 1

                if puzzle_one_status == True and puzzle_two_status == True:
                        print("You find yourself in a room that seems to be a furniture display that is in suprisingly good condition, relative to the other rooms in this place. It seems whoever barged into here took care not damaging this room. The only item of interest you can see in this room in the door leading back to the lobby. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Head back to the lobby\n").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                return 1

                if puzzle_one_status == True and puzzle_two_status == False:
                        print("You find yourself in a room that seems to be a furniture display that is in suprisingly good condition, relative to the other rooms in this place. It seems whoever barged into here took care not damaging this room. The items of interest you can see in this room are two puzzle boxes, one to your left that you've already solved and one to your right that has not been completed, and the door leading back to the lobby. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Inspect the puzzle box to your right\n4. Head back to the lobby\n").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                puzzle_two_status = puzzle_two(player_stats,player_max_health)
                                                
                                                break
                                        case "4":
                                                return 1

                if puzzle_one_status == False and puzzle_two_status == True:
                        print("You find yourself in a room that seems to be a furniture display that is in suprisingly good condition, relative to the other rooms in this place. It seems whoever barged into here took care not damaging this room. The items of interest you can see in this room are two puzzle boxes, one to your left that you have not solved and one to your right that you have solved, and the door leading back to the lobby. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Inspect the puzzle box to your left\n4. Head back to the lobby\n").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                puzzle_one_status = puzzle_one(inventory)
                                                
                                                break
                                        case "4":
                                                return 1
                continue

def room_four(player_stats,inventory,gnome_defeated):
        if gnome_defeated:
                print("You find yourself in a spacious, empty room, with a very sleepy gnome lying on the floor. The only items of interest you can see in the room is the door leading back to the room you just came from and an elevator. What would you like to do?")
        else:
                print("You find yourself in a specious, mostly empty room, with an... oh hey that's a rabid gnome sprinting at you.")
                print("Combat START")
                gnome_combat(player_stats,gnome_stats)
        while True:            
                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go back\n4. Go to the elevator (P.S: You cannot head back to this floor after going up.)").strip()
                match choice:
                        case "1":
                                print_stats(player_stats)
                                continue
                        case "2":
                                print_inventory(inventory)
                        case "3":
                                return 3
                        case "4":
                                return "Floor Two"

def room_five(player_stats,inventory):
        print("After stepping out of the elevator (which proceeds to plummet back down to the first floor, it broke), you find yourself in what seems to be a fairly small grocery store. Whoever barged into the Walmart obviously did not take care in this room, as there are fruits and vegetables strewn across the floor. Besides this, the only items of interest you can see are doors to your left and right. What would you like to do?")
        while True:
               choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Right\n4. Go Left\n").strip()
               match choice:
                        case "1":
                                print_stats(player_stats)
                        case "2":
                                print_inventory(inventory)
                        case "3":
                                return 6
                        case "4":
                                return 7
                        case _:
                                print("Invalid answer. Please try again.")
                                continue 
                       
def room_six(player_stats,inventory,puzzle_three_status):
        while True:
                if puzzle_three_status:
                        print("You find yourself in a room made of basically entirely fluffy things. You can see blankets, pillows, plushies, and at least one mattress. The only item of interest that you can see is a door to your right, and the door leading back to the grocery area. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Right\n4. Go Back").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                return 8
                                        case "4":
                                                return 5
                                        
                else:
                        print("You find yourself in a room made of basically entirely fluffy things. You can see blankets, pillows, plushies, and at least one mattress. The only items of interest that you can see is a door to your right, the door leading back to the grocery area, and a puzzle box. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Inspect Puzzle Box\n4. Go Right\n5. Go Back").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                puzzle_three_status = puzzle_three(inventory)
                                                break
                                        case "4":
                                                return 8
                                        case "5":
                                                return 5
                                        
def room_seven(player_stats,inventory,puzzle_four_status):
         while True:
                if puzzle_four_status:
                        print("You find yourself in a room full of pet supplies. For an unknown reason, this room is in good condition. The only items of interest that you can see is a door to your left and the door leading back to the grocery area. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Left\n4. Go Back").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                return 8
                                        case "4":
                                                return 5
                                        
                else:
                        print("You find yourself in a room full of pet supplies. For an unknown reason, this room is in good condition. The only items of interest that you can see is a door to your left, the door leading back to the grocery area, and a puzzle box. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Inspect Puzzle Box\n4. Go Left\n5. Go Back").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                puzzle_four_status = puzzle_four(inventory)
                                                break
                                        case "4":
                                                return 8
                                        case "5":
                                                return 5

def room_eight(player_stats,inventory,puzzle_five_status):
        while True:
                if puzzle_five_status:
                        print("You find yourself in a room full of flags of all different kinds. As the flags are posed very high up, they are basically unscathed. Besides this, you can see a door (to your left) leading back to the fluffy room, a door (to your right) leading back to the pet supplies room, and an elevator in the center of the room that has a metal fish carved out of the center of the door. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Left\n4. Go Right\n5. Inspect Elevator").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                return 6
                                        case "4":
                                                return 7
                                        case "5":
                                                if "Top Half Fish" in inventory and "Bottom Half Fish" in inventory:
                                                        print("You take out the two halfs of a metal fish you got from the puzzle boxes and put them in the fish shaped slot in the elevator door. Once you put them in, it clicks, hisses, then opens. Would you like to step into the elevator? You will not be able to head back down after. Yes/No")
                                                        while True:
                                                                choice = input("Yes/No").strip().capitalize()
                                                                if choice == "Yes":
                                                                        print("You walk into the elevator, the doors close, and it starts going up.")
                                                                        return 9
                                                                elif choice == "No":
                                                                        print("You back away from the elevator")
                                                                        break
                                                                else:
                                                                        print("Invalid answer")
                                                                        continue
                if not puzzle_five_status:
                        print("You find yourself in a room full of flags of all different kinds. As the flags are posed very high up, they are basically unscathed. Besides this, you can see a door (to your left) leading back to the fluffy room, a door (to your right) leading back to the pet supplies room, an elevator in the center of the room that has a metal fish carved out of the center of the door, and another odd puzzle box. What would you like to do?")
                        while True:
                                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Left\n4. Go Right\n5. Inspect Elevator\n6. Inspect Puzzle Box").strip()
                                match choice:
                                        case "1":
                                                print_stats(player_stats)
                                                continue
                                        case "2":
                                                print_inventory(inventory)
                                                continue
                                        case "3":
                                                return 6
                                        case "4":
                                                return 7
                                        case "5":
                                                if "Top Half Fish" in inventory and "Bottom Half Fish" in inventory:
                                                        print("You take out the two halfs of a metal fish you got from the puzzle boxes and put them in the fish shaped slot in the elevator door. Once you put them in, it clicks, hisses, then opens. Would you like to step into the elevator? You will not be able to head back down after. Yes/No")
                                                        while True:
                                                                choice = input("Yes/No").strip().capitalize()
                                                                if choice == "Yes":
                                                                        return 9
                                                                elif choice == "No":
                                                                        print("You back away from the elevator")
                                                                        break
                                                                else:
                                                                        print("Invalid answer")
                                                                        continue
                                        case "6":
                                                puzzle_five_status = puzzle_five(player_stats)
                                                break
                        
def room_nine(player_stats,intezar_stats):
        print("The elevator dings, and the doors open up. You walk out, and find yourself in some sort of penthouse. Looking around, you see a very fancy wooden desk in the center of the room, and sitting behind it, Intezarr. He's some sort of... inverse mermaid, with human legs connec to a fish head. How that works, no one knows, not even Intezarr.")
        print("Intezarr: 'I'm impressed by your tenacity in getting up here. Will it be enough to defeat me, though? I doubt it.'")
        print("Combat START")

        winner = intezar_combat(player_stats,intezar_stats)

        if winner == 1:
                return "Loss"
        if winner == 2:
                return "Win"

def master_function(user_room):
        user_room = 1
        while True:
                match user_room:
                        case 1:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 2:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 3:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 4:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 5:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 6:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 7:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 8:
                                user_room = room_one(player_stats,inventory)
                                continue
                        case 9:
                                user_room = room_one(player_stats,inventory)
                                continue