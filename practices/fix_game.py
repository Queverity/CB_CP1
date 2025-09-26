# CB 1st Fix the Game
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        # The input was made to be a string, when it should be an integer if we want to do arithmatic on it. It's a runtime error.
        guess = int(input("Enter your guess: "))
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        # The program was not incrementing attempts each time the user guessed incorrectly, making it so the user had an effectively infinite number of attempts. This is a logic error.
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
        # The program was not incrementing attempts each time the user guessed incorrectly, making it so the user had an effectively infinite number of attempts. This is a logic error.
        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts += 1
        # There was a continue statement here serving no purpose. I removed it. This was a logic error.
    print("Game Over. Thanks for playing!")
start_game()