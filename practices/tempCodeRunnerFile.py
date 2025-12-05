def player_attack(monster_type,player_class):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20) + 4
    if attack_roll >= monster_type["Defense"]:
        print(f"You rolled a(n) {attack_roll}. You hit!")
        print("Rolling for damage...")
        time.sleep(1)
        player_damage = (player_class["Offense"]/3) + random.randint(1,6)
        print(f"You dealt {player_damage} damage.")
        return player_damage
    elif attack_roll - 4 == 20:
        print("You rolled a natural 20. Critical hit! You will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        player_damage = (player_class["Offense"]/3) + random.randint(1,6)
        player_damage = player_damage * 2
        print(f"You dealt {player_damage} damage.")
        return player_damage
    else:
        print("You missed.")
        return 0
    
def monster_attack(player_class,monster_type):
    print("Rolling 1D20...")
    time.sleep(1)
    attack_roll = random.randint(1,20) + 4
    if attack_roll >= player_class["Defense"]:
        print(f"The {monster_type["Type"]} rolled a(n) {attack_roll}. It hit.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        print(f"The {monster_type["Type"]} dealt {monster_damage} damage.")
        return monster_damage
    elif attack_roll >= 20:
        print(f"The {monster_type["Type"]} rolled a natural 20. Critical hit! it will deal double damage.")
        print("Rolling for damage...")
        time.sleep(1)
        monster_damage = (monster_type["Offense"]/3) + random.randint(1,6)
        monster_damage = monster_damage * 2
        print(f"The {monster_type["Type"]} dealt {monster_damage} damage.")
        return monster_damage
    else:
        print(f"The {monster_type["Type"]} missed.")
        return 0