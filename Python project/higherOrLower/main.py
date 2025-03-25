from game_data import data
from art import logo, vs
import random

def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Checks if the user's guess is correct about which account has more followers."""
    if a_followers > b_followers:
        return user_guess == 'a'
    elif b_followers > a_followers:
        return user_guess == 'b'
    else:
        return True  # or False, depending on how you want to handle ties
# Display art
print(logo)

score = 0
continue_game = True
account_b = random.choice(data)

while continue_game is True:
    # Generate a random account from data list
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user to guess
    guess = input("Who has more followers? 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count to check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, you that's wrong! Final score: {score}")
        continue_game = False

# Keep score

# Make the game repeatable

# Making account at position B become the next account at position A