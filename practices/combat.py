# CB 1st Combat Program
import random
import time
fighter_stats = {"Speed":9,"Offense":15,"Defense":16,"Health":100,"Attack":"D20"}
rouge_stats = {"Speed":15,"Offense":12,"Defense":14,"Health":80,"Attack":"D20"}
mage_stats = {"Speed":12,"Offense":21,"Defense":12,"Health":60,"Attack":"D20"}
monsters = ["Dire Wolf","Goblin","Job Application"]
wolf_stats = {"Type":"Dire Wolf","Speed":12,"Offense":15,"Defense":10,"Health":50,"Attack":"D20"}
goblin_stats = {"Type":"Goblin","Speed":10,"Offense":12,"Defense":13,"Health":75,"Attack":"D20"}
job_stats = {"Type":"Job Application","Speed":14,"Offense":18,"Defense":10,"Health":90,"Attack":"D20"}

def player_attack(monster_defense,player_class):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20)
    if attack_roll >= monster_defense:
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
    
def monster_attack(player_defense,monster_type):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20)
    if attack_roll >= player_defense:
        print(f"The {monster_type} {attack_roll}. It hit.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        print(f"The monster dealt {monster_damage}.")
        return monster_damage
    elif attack_roll == 20:
        print("The monster rolled a 20. Critical hit! it will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        monster_damage = monster_damage * 2
        print(f"The monster dealt {monster_damage} damage.")
        return monster_damage
    else:
        print("The monster missed.")
        return 0
    

