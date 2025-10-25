# CB 1st Combat Program
import random
import time
fighter_stats = {"Class":"Fighter","Speed":9,"Offense":15,"Defense":16,"Health":100,"Attack":"D20"}
rouge_stats = {"Class":"Rouge","Speed":15,"Offense":12,"Defense":14,"Health":80,"Attack":"D20"}
mage_stats = {"Class":"Mage","Speed":12,"Offense":21,"Defense":12,"Health":60,"Attack":"D20"}
monsters = ["Dire Wolf","Goblin","Job Application"]
wolf_stats = {"Type":"Dire Wolf","Speed":12,"Offense":15,"Defense":10,"Health":50,"Attack":"D20"}
goblin_stats = {"Type":"Goblin","Speed":10,"Offense":12,"Defense":13,"Health":75,"Attack":"D20"}
job_stats = {"Type":"Job Application","Speed":14,"Offense":18,"Defense":10,"Health":90,"Attack":"D20"}
turn = 0
heals = 3
monster_health = 0
player_health = 0
monster_type = ""

def player_attack(monster_type,player_class,player_action):
    if player_action == 1:
        print("Rolling 1D20...")
        time.sleep(1)
        attack_roll = random.randint(1,20)
        if attack_roll >= monster_type["Defense"]:
            print(f"You rolled a(n) {attack_roll}. You hit!")
            print("Rolling for damage...")
            time.sleep(1)
            player_damage = (player_class["Offense"]/3) + random.randint(1,6)
            print(f"You dealt {player_damage} damage.")
            return player_damage
        elif attack_roll == 20:
            print("You rolled a 20. Critical hit! You will deal double damage.")
            print("Rolling for damage...")
            time.sleep(1)
            player_damage = (player_class["Offense"]/3) + random.randint(1,6)
            player_damage = player_damage * 2
            print(f"You dealt {player_damage} damage.")
            return player_damage
        else:
            print("You missed.")
            return 0
    elif player_action == 2:
        print("Rolling 1D20...")
        time.sleep(1)
        attack_roll = random.randint(1,20)
        if attack_roll >= monster_type:
            print(f"You rolled a(n) {attack_roll}. You hit!")
            print("Rolling for damage...")
            time.sleep(1)
            player_damage = (player_class["Offense"]/3) + random.randint(1,6)
            self_damage = player_damage - 5
            print(f"You dealt {player_damage} damage.")
            print(f"You take {self_damage} damage.")
            return player_damage * 2, self_damage
        elif attack_roll == 20:
            print("You rolled a 20. Critical hit! You will deal double damage.")
            print("Rolling for damage...")
            time.sleep(1)
            player_damage = (player_class["Offense"]/3) + random.randint(1,6)
            self_damage = player_damage - 5
            player_damage = player_damage * 2
            print(f"You dealt {player_damage} damage.")
            print(f"You took {self_damage} damage.")
            return player_damage * 2,self_damage
        else:
            print("You missed.")
            return 0
    
def monster_attack(player_class,monster_type):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20)
    if attack_roll >= player_class["Defense"]:
        print(f"The {monster_type["Type"]} rolled a(n) {attack_roll}. It hit.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        print(f"The monster dealt {monster_damage}.")
        return monster_damage
    elif attack_roll == 20:
        print(f"The {monster_type["Type"]} rolled a 20. Critical hit! it will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        monster_damage = monster_damage * 2
        print(f"The {monster_type["Type"]} dealt {monster_damage} damage.")
        return monster_damage
    else:
        print(f"The {monster_type["Type"]} missed.")
        return 0
    
print("Combat Game thingy")

while True:
    print("Classes: \n1 Fighter\n2 Rouge\n3 Mage")
    while True:
        player_class = input("Pick your class! 1/2/3").strip()
        match player_class:
            case "1":
                player_class = fighter_stats
                player_health = fighter_stats["Health"]
                break
            case "2":
                player_class = rouge_stats
                player_health = rouge_stats["Health"]
                break
            case "3":
                player_class = mage_stats
                player_health = mage_stats["Health"]
                break
            case _:
                print("invalid anwswer")
                continue
    print("Here are your stats!")
    print(f"Speed: {player_class["Speed"]}\nOffense: {player_class["Offense"]}\nDefense: {player_class["Defense"]}\nHealth: {player_class["Health"]}")
    monster_randomizer = random.randint(1,3)
    while True:
        match monster_randomizer:
            case 1:
                monster_type = wolf_stats
                monster_health = wolf_stats["Health"]
                break
            case 2:
                monster_type = goblin_stats
                monster_health = goblin_stats["Health"]
                break
            case 3:
                monster_type = job_stats
                monster_health = job_stats["Health"]
                break
            case _:
                print("unexpected error")
    print(f"You have encountered a {monster_type["Type"]}!")
    if monster_type["Speed"] > player_class["Speed"]:
        turn = 2
    elif monster_type["Speed"] < player_class["Speed"]:
        turn = 1
    else:
        coin = random.randint(1,2)
        if coin == 1:
            turn = 1
        else:
            turn = 2
    while True:
        if monster_health <= 0:
            print(f"The {monster_type["Type"]} has been defeated!")
            break
        elif player_health <= 0:
            print(f"You have been defeated by the {monster_type["Type"]}.")
            break
        else:
            if turn == 1:
                print("Player's Turn")
                print("1. Basic attack")
                while True:
                    if player_class["Class"] == "Fighter":
                        print("2. Wild strike (deal double damage but take damage as well)") 
                        break
                    elif player_class["Class"] == "Rouge":
                        print("2. Risky slash (eouble damage, take damage as well)")
                        break
                    else:
                        print("2. Fireball (double damage, take damage as well)")
                        break
                print("3. Use healing potion (10 health, 3 uses max)")
                print("4. Flee (may or may not work)") 
                player_action = input("Which would you like to do? 1/2/3/4").strip()
                if player_action == "1" or player_action == "2":
                    monster_health -= player_attack(monster_type,player_class,player_action)
                    print(f"The {monster_type["Type"]} now has {monster_health} health left.")
                    print(f"Player Health: {player_health}")
                    turn = 2
                if player_action == "3":
                    while True:
                        if player_health == player_class["Health"]:
                            print("You are at max health and cannot heal.")
                            break
                        else:
                            player_health += 10
                            print(f"New health: {player_health}")
                            turn = 2
                            break
                elif player_action == "4":
                    print("Rolling 1D20 against monster speed...")
                    time.sleep(1)
                    escape_attempt = random.randint(1,20)
                    if escape_attempt > monster_type["Speed"]:
                        print("Succesful escape!")
                        print("Well that was kind of boring")
                        break
                    else:
                        print("Escape was not succesful.")
                        turn = 2
            if turn == 2:
                print("Monster's turn")
                monster_attack(player_class,monster_type)
                print(f"Player Health: {player_health}")
                turn = 1

    go_again = input("Would you like to play again? Yes/No").strip().capitalize()
    if go_again == "Yes":
        continue
    else:
        print("Goodbye!")
        break