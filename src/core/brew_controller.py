from .inventory_manager import InventoryManager

class BrewController:
    def __init__(self, inventory: InventoryManager):
        self.inventory = inventory
        self.recipes = {
            "latte": {"water": 200, "coffee": 24, "milk": 150},
            "espresso": {"water": 50, "coffee": 18},
            "cappuccino": {"water": 250, "coffee": 24, "milk": 100},
        }
        self.prices = {"latte": 2.50, "espresso": 1.50, "cappuccino": 3.00}

    def can_brew(self, drink: str) -> bool:
        return drink in self.recipes and self.inventory.has_ingredients(self.recipes[drink])

    def brew(self, drink: str) -> bool:
        if not self.can_brew(drink):
            return False
        return self.inventory.consume(self.recipes[drink])
