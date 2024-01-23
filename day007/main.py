import random
from hangman_words import word_list
from hangman_art import stages, logo, logo1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
lives = 6

print(logo1)
print("\nTo win, guess the word before the person is hung.\n")

display = []
wrong_guesses = []

for _ in range(word_length):
    display += "_"

while not game_over:
    guess = input("Guess a letter. ").lower()

    if guess in wrong_guesses:
        print(f"{' '.join(display)}")
        print(stages[lives])
        print(f"You've already guessed with the letter '{guess}', pick another letter.")
    else:
        wrong_guesses.append(guess)

        for index in range(word_length):
            letter = chosen_word[index]
            if letter == guess:
                display[index] = letter

        print(f"{' '.join(display)}")

        if "_" not in display:
            game_over = True
            print("\nAmazing! You won!")
            print(logo)

        if guess not in chosen_word:
            lives -= 1

        if not game_over:
            print(stages[lives])
            if guess not in chosen_word:
                print(f"'{guess}' is not in the word, you lost a life.")

        if lives == 0:
            game_over = True
            print("The man has been hung, you lose.")
            print(f"\nThe word was '{chosen_word}'")
