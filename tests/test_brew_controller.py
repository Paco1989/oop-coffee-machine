from src.core.inventory_manager import InventoryManager
from src.core.brew_controller import BrewController

def test_brew_latte_depletes_inventory():
    inv = InventoryManager(water=600, coffee=200, milk=300)
    brew = BrewController(inv)
    assert brew.can_brew("latte")
    assert brew.brew("latte")
    lv = inv.get_levels()
    assert lv["water"] == 400 and lv["coffee"] == 176 and lv["milk"] == 150
