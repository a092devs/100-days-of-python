from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        print("Have a good day!")
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
