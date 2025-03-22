#guess a number between 1 and 100.
#choose a difficulty
#easy level: 10 attempts
#give feedback: too high or too low
#hard level: 5 attempts
import random

def play_game():
    guess_value = random.randint(1, 100)  # Use randint for inclusive range
    game_mode = input("Welcome to the Number Guessing game! \n I'm thinking of a number between 1 and 100. \n Choose a difficulty. Type 'easy' or 'hard': ")

    if game_mode == "easy":
        attempts = 10
    elif game_mode == "hard":
        attempts = 5
    else:
        print("Invalid mode. Please type 'easy' or 'hard'.")
        return

    while attempts > 0:
        try:
            guess = int(input(f"Guess a number between 1 and 100. You have {attempts} attempts left: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < guess_value:
            print("Too low.")
        elif guess > guess_value:
            print("Too high.")
        else:
            print(f"You got it! The answer was {guess_value}.")
            return

        attempts -= 1

    print(f"You ran out of attempts. The answer was {guess_value}.")

play_game()