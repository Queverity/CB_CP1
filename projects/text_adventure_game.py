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