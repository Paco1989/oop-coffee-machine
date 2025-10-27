from src.core.inventory_manager import InventoryManager

def test_has_ingredients_and_consume():
    inv = InventoryManager(water=300, coffee=100, milk=100)
    assert inv.has_ingredients({"water": 200, "coffee": 50})
    assert inv.consume({"water": 200, "coffee": 50})
    levels = inv.get_levels()
    assert levels["water"] == 100 and levels["coffee"] == 50
