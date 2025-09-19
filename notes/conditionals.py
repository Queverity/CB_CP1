# CB 1st Conditionals Notes
import random

player_stats = {"hp": 20, "attack": 2, "damage": 5, "defense": 5}
monster_stats = {"hp": 15, "attack": 3, "damage": 10, "defense": 2}

hit_roll = random.randint(1,20)

if hit_roll == 20:
    print("You crit! You damage is doubled!")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_stats["damage"]
    print(f"You did {damage_roll - monster_stats["defense"]} damage.")
    monster_stats["hp"] -= damage_roll - monster_stats["defense"]
elif hit_roll == 1:
    print("You rolled a critical failure! Now the monster gets to attack you!")
    damage_roll = random.randint(1,12) + monster_stats["damage"]
    player_stats["hp"] = damage_roll - player_stats["defense"]
    print(f"The monster rolled {damage_roll}, your hp is now {player_stats["hp"]}")

elif hit_roll >= 12:
    print("You hit! Roll for damage")
    damage_roll = random.randint(1,8) + player_stats["damage"]
    if damage_roll > monster_stats["defense"]:
        print(f"You did {damage_roll - monster_stats["defense"]} damage.")
        monster_stats["hp"] -= damage_roll - monster_stats["defense"]
    else:
        print("You did no damage.")

 
else:
    print("You missed.")

print("Your turn is over.")

if monster_stats["hp"] > 0:
    attack_roll = random.randint(1,20)