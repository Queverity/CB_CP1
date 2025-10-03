# CB 1st Rock Paper Scissors
import random

user_score = 0
bot_score = 0
print("Welcome to Rock Paper Scissors!")

while True:
    player_choice = input("Rock, Paper, or Scissors?").strip().capitalize()
    bot_answer = random.randint(1,3)
    match player_choice:
        case "Rock":
            match bot_answer:
                case 1:
                    print("Bot played rock. It's a tie!")
                case 2:
                    print("Bot played paper. You lost.")
                    bot_score += 1
                case 3:
                    print("Bot played scissors. You win!")
                    user_score += 1
        case "Paper":
            match bot_answer:
                case 1:
                    print("Bot played rock. You win!")
                    user_score += 1
                case 2:
                    print("Bot played paper. It's a tie!")
                case 3:
                    print("Bot played scissors. You lost.")
                    bot_score += 1
        case "Scissors":
            match bot_answer:
                case 1:
                    print("Bot played rock. You lost.")
                    bot_score += 1
                case 2:
                    print("Bot played paper. You win!")
                    user_score += 1
                case 3:
                    print("Bot played scissors. It's a tie!")
        case _:
            print("Unexpected answer")
            continue
    print(f"Player Score: {user_score}\n Bot Score: {bot_score}")
    play_again = input("Play again? Y/N").strip().capitalize()
    if play_again == "Y":
        continue
    elif play_again == "N":
        print("Goodbye!")
        break
    else:
        print("Unexpected answer")
        continue