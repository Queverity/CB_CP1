# CB 1st Text Adventure Final
import random
import time

puzzle_one_status = False
puzzle_two_status = False
puzzle_three_status = False
puzzle_four_status = False
puzzle_five_status = False

gnome_defeated = False

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

def game_over(puzzle_one_status,puzzle_two_status,puzzle_three_status,puzzle_four_status,puzzle_five_status,player_stats,gnome_stats,intezar_stats,inventory,user_room,gnome_defeated,intezar_dfeated):
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
        print("You have been defeated.")
        return 1
    elif monster_stats["Health"] <= 0:
        print("You have defeated your foe!")
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
                                                        if win == 1:
                                                                return 0
                                                        elif win == 2:
                                                                gnome_defeated == True
                                                                break
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
                                                                game_over(puzzle_one_status,puzzle_two_status,puzzle_three_status,puzzle_four_status,puzzle_five_status,player_stats,gnome_stats,intezar_stats,inventory,user_room,gnome_defeated,intezar_defeated)
                                                        elif win == 2:
                                                                gnome_defeated == True
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
                                                                intezar_defeated == True
                                                                break
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
                                                                game_over(puzzle_one_status,puzzle_two_status,puzzle_three_status,puzzle_four_status,puzzle_five_status,player_stats,intezar_stats,intezar_stats,inventory,user_room,gnome_defeated,intezar_defeated)
                                                        elif win == 2:
                                                                intezar_defeated == True
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

def room_one(player_stats,inventory):
       input("You find yourself in what appears to be the lobby of the Triple-Decker Walmart. Around you, you can see scattered and shattered furniture lying on the floor, giving the impression that some sort of attack force barged into here with disregard for property damage. The only other items of interest you can see are doors to your left and right.")
       while True:
                choice = input("Enter number for action:\n1. Check Stats\n2. Check Inventory\n3. Go Right\n4. Go Left")
                        match choice:
                                case 1:
                                        print_stats(player_stats)
                                case 2:
                                        print_inventory(inventory)
                                case 3:
                                        return 2
                                case 4:
                                        return 3
                                case _:
                                        print("Invalid answer. Please try again.")
                                        continue

room_one(player_stats,inventory)
        

                        


