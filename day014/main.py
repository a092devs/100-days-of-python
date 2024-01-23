from random import choice
from art import *
from game_data import data
from replit import clear


def guessed(guess, followers_a, followers_b):
    return followers_a > followers_b if guess == "a" else followers_a < followers_b


def print_info(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def play_game():
    score = 0
    option_a = choice(data)
    option_b = choice(data)

    print(logo)

    while True:
        option_a = option_b
        option_b = choice(data)

        while option_a == option_b:
            option_b = choice(data)

        print(f"Compare A: {print_info(option_a)}")
        print(vs)
        print(f"Against B: {print_info(option_b)}")

        guess = input("Who has more follower? Type 'A' or 'B': ").lower()

        followers_a = option_a["follower_count"]
        followers_b = option_b["follower_count"]

        clear()
        print(logo)

        if guessed(guess, followers_a, followers_b):
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, thats's wrong. Final score: {score}")
            break


play_game()
