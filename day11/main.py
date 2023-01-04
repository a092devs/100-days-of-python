from art import logo
import random
from replit import clear

cards = [
    2, 3, 4, 5, 6, 7, 8,
    9, 10, "J", "Q", "K", "A"
]

points = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
    "7": 7, "8": 8, "9": 9, "10": 10, "J": 10,
    "Q": 10, "K": 10, "A": 11,
}

def calculate_score(player, card):
    player["score"] += points[str(card)]
    return player

def deal_card(player):
    card = random.choice(cards)
    player["cards"].append(card)
    calculate_score(player, card)
    return player

def who_win(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "It's a draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    player = {"cards": [], "score": 0, }
    computer = {"cards": [], "score": 0, }

    for _ in range(2):
        deal_card(player)
    deal_card(computer)

    continue_play = True

    print(logo)
    while continue_play and player["score"] < 21:
        print(f"\tYour cards: {player['cards']}, current_score: {player['score']}")
        print(f"\tComputer's first card: {computer['cards']}")
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            deal_card(player)
            if player["score"] > 21:
                for num, card in enumerate(player['cards']):
                    if card == "A":
                        player["score"] -= 10
                        player["cards"][num] = 1
        else:
            continue_play = False

    continue_play = True
    while computer["score"] < 17 and player["score"] <= 21:
        deal_card(computer)
        if computer["score"] > player["score"]:
            break

    print(f"\tYour cards: {player['cards']}, final score: {player['score']}")
    print(f"\tComputer's first card: {computer['cards']}, final score: {computer['score']}")
    print(who_win(player["score"], computer["score"]))

    return None

while input("Do you want to play a game Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()
