import pandas as pd

nato_data = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (_, row) in nato_data.iterrows()}
user_input = input("Enter a word: ").upper()
nato_alphabet = [nato_dict[letter] for letter in user_input]
print(nato_alphabet)