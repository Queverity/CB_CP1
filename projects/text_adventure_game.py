# CB 1st Text Adventure Final
import random

puzzle_one_status = False
puzzle_two_status = False
puzzle_three_status = False
puzzle_four_status = False
puzzle_five_status = False

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

def game_over(puzzle_one_status,puzzle_two_status,puzzle_three_status,puzzle_four_status,puzzle_five_status,player_stats,gnome_stats,intezar_stats,inventory,user_room):
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

def puzzle_two(player_stats):
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
                
puzzle_five(player_stats)
print_stats(player_stats)

