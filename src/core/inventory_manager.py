class InventoryManager:
    def __init__(self, water=500, coffee=200, milk=300):
        self.levels = {"water": water, "coffee": coffee, "milk": milk}

    def has_ingredients(self, recipe: dict) -> bool:
        return all(self.levels.get(k, 0) >= v for k, v in recipe.items())

    def consume(self, recipe: dict) -> bool:
        if not self.has_ingredients(recipe):
            return False
        for k, v in recipe.items():
            self.levels[k] -= v
        return True

    def get_levels(self) -> dict:
        return dict(self.levels)
