from replit import clear
from art import logo


def check_winner(_bid_dict):
    winner = ""
    winner_list = []
    highest_price = 0
    for person in _bid_dict:
        if _bid_dict[person] > highest_price:
            winner = person
            highest_price = bid_dict[person]
            winner_list = [person]

        elif bid_dict[person] == highest_price:
            winner_list.append(person)

    if highest_price == 0:
        print("Nobody win.")
        exit()
    elif len(winner_list) == 1:
        print(f"The winner is {winner} with a bid of ${highest_price}")
        exit()
    else:
        winners = ", ".join(winner_list)
        print(f"The Winners are {winners} with a bid of ${highest_price}")
        return winner_list, highest_price


def rebid(_winner_list, _minimum_price):
    print("To decide a winner, rebidding will take place now.")
    _bid_dict = {}

    for bidder in _winner_list:
        print(f"Please input more than ${_minimum_price}\n")
        price = float(input(f"{bidder}, What is your bid? $"))
        if price < _minimum_price:
            price = 0
        _bid_dict[bidder] = price
        clear()
    return _bid_dict


print(logo)
bid_dict = {}

while True:
    name = input("What is your name? ")
    price = float(input("What is your bid? $"))
    bid_dict[name] = price

    input_continue = input("Are thare any other bidders? Type 'Yes' or 'No': ").lower()
    if input_continue in ["no", "n"]:
        break
    clear()

(winner_list, minimum_price) = check_winner(bid_dict)

while True:
    bid_dict = rebid(winner_list, minimum_price)
    (winner_list, minimum_price) = check_winner(bid_dict)
