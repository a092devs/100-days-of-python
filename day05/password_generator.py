# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']

print("Welcome to the PyPassword Generator!")
num_of_letters = int(input("How many letters would you like in your password?\n")) 
num_of_symbols = int(input(f"How many symbols would you like?\n"))
num_of_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for letter in range(num_of_letters):
    password.append(random.choice(letters))

for symbol in range(num_of_symbols):
    password.append(random.choice(symbols))

for number in range(num_of_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
password = ''.join(password)

print(f"Your password is: {password}")
