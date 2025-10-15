from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffeeMachine():
    m = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()

    while True:
        print("Welcome to the Coffee Machine!")
        for item in m.menu:
            print(f"{item.name}: ${item.cost:.2f}")

        option = input(f"What would you like? ({m.get_items()}): ")

        if option == 'exit':
            return
        elif option == 'report':
            cm.report()
            mm.report()
        else:
            drink = m.find_drink(option)

            resourceFlag = cm.is_resource_sufficient(drink)

            if resourceFlag:

                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)

coffeeMachine()
