from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

# object = class()
menu = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

switch = True

# Main loop
while switch:
    options = menu.get_items()
    choice = input(f"\nWhat would you like? ({options}): ").lower()
    if choice == "off":
        switch = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        # Searches for the drink and return all its attributes
        drink = menu.find_drink(choice)

        # Checks if resources are sufficient? & Process the payment
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            # Make Coffee
            coffee.make_coffee(drink)
