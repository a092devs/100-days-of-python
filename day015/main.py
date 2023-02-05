from coffee import *
from replit import clear

def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"

def check_coin(cents, nickels, dimes, quarters, coffee):
    total_cents = 0.01 * cents
    total_nickels = 0.05 * nickels
    total_dimes = 0.10 * dimes
    total_quarters = 0.25 * quarters

    total = total_cents + total_nickels + total_dimes + total_quarters

    coffee_price = coffee["cost"]

    if total < coffee_price:
        print("Sorry, that's not enough money. Money refunded!")
        return False
    else:
        change = round(total - coffee_price, 2)
        if change > 0:
            print(f"Here is ${change} in change!")
        return True

def check_sufficient_ingredient(coffee_ingredients):
    for item in coffee_ingredients:
        if coffee_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def adjust_resources(coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]

clear()
print(logo)

in_menu = True

while in_menu:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option in ["espresso", "latte", "cappuccino"]:
        coffee = MENU[option]

        if check_sufficient_ingredient(coffee["ingredients"]):
            print("\tPlease insert coin.")

            quarters = int(input("\thow many quarters? "))
            dimes = int(input("\thow many dimes? "))
            nickels = int(input("\thow many nickels? "))
            cents = int(input("\thow many cents? "))
 
            if check_coin(cents, nickels, dimes, quarters, coffee):
                print(f"\tHere is your {option} ☕. Enjoy!")
                resources["money"] += coffee["cost"]
                adjust_resources(coffee["ingredients"])

    elif option == "report":
        print(report())
    elif option == "off":
        in_menu = False
    else:
        clear()
        print("You didn't type a valid input! Exiting now...")
        break