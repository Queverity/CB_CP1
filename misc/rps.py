import random
running = True

global times_won
global times_lost
global result



times_won = 0
times_lost = 0
result = ""

def win(times_won, times_lost):
    times_won += 1
    times_lost = 0

def lost(times_lost, times_won):
    times_won = 0
    times_lost += 1

while running == True:
    player_input = input("Rock, Paper, or Scissors?").capitalize()
    computer_input = random.randint(0,2)

    if player_input == "Rock":

        if computer_input == 0:
            result = "tied"

        elif computer_input == 1:
            result = "lost"
            lost(times_lost, times_won)

        elif computer_input == 2:
            result = "won"
            win(times_won,times_lost)
         
        
    elif player_input == "Paper":
        if computer_input == 0:
            result = "won"
            win(times_won,times_lost)

        elif computer_input == 1:
            result = "tied"

        elif computer_input == 2:
            result = "lost"
            lost(times_lost, times_won)

        

    elif player_input == "Scissors":
        if computer_input == 0:
            result = "lost"
         
            lost(times_lost, times_won)

        elif computer_input == 1:
            result = "won"
            win(times_won,times_lost)

        elif computer_input == 2:
            result = "tied"

    else:
        print("Invalid answer, please try again. Maybe there was a typo?")
        continue

    print(f"You {result}.")
    
    if times_won >= 2 and times_lost == 0:
        print("You have won " + str(times_won) + " times in a row." )
    elif times_lost >= 2 and times_won == 0:
        print("You have lost " + str(times_lost) + " times in a row.")

    play_again = input("Do you want to play again? Y/N").capitalize()

    if play_again == "Y":
        continue
    elif play_again == "N":
        print("Goodbye!")
        break