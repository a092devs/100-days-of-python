import random
from art import logo
from replit import clear

random_number = random.randint(1, 100)

def get_diffculty():
    print(logo)
    while True:
        difficulty = input("Choose the difficulty level from 'easy', 'medium' or 'hard': ").lower()
        if difficulty == "easy":
            global lives
            lives = 10
            break
        elif difficulty == "medium":
            lives = 7
            break
        elif difficulty == "hard":
            lives = 5
            break
        else:
            print("Please enter valid diffiulty level.")
    clear()

    print(f"\tYou selected '{difficulty}' level with {lives} lives.")

get_diffculty()

def play_game(lives, random_number):
    while lives > 0:
        guess = int(input("\nGuess a number between 1 to 100: "))
        if guess == random_number:
            print(f"\tAmazing, you guessed it right. The number was {guess}. 🫢")
            break
        elif guess > random_number:
            print(f"\tThe number {guess} is too high. Guess a lower number. 😤")
            lives -= 1
        elif guess < random_number:
            print(f"\tThe number {guess} is too low. Guess a higher number. 😤")
            lives -= 1
    if lives == 0:
        print("\nYou ran out of lives. You lose. 😭")

play_game(lives, random_number)

while True:
    play_again = input("\nDo you want to play again? Type 'y' for yes and 'n' for no: ").lower()
    if play_again in ['y', 'yes']:
        clear()
        get_diffculty()
        play_game(lives, random_number)
    elif play_again in ['n', 'no']:
        clear()
        print("\nThank you for playing the Guessing Number Game. Goodbye!")
        break
    else:
        clear()
        print("\nYou didn't select a valid input. Exiting now!")
        break
