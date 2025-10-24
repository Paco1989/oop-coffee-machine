from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def print_menu(m: Menu):
    print("Welcome to the Coffee Machine!")
    for item in m.menu:
        print(f"{item.name.title()}: ${item.cost:.2f}")

def coffeeMachine():
    m = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()

    while True:
        print_menu(m)

        option = input(f"What would you like? ({m.get_items()}): ").strip().lower()

        if option == 'exit':
            return
        elif option == 'report':
            cm.report()
            mm.report()
        else:
            drink = m.find_drink(option)
            if not drink:
                print("Sorry, I didn't get that. Please try again.\n")
                continue

            resourceFlag = cm.is_resource_sufficient(drink)

            if resourceFlag:

                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)

coffeeMachine()
