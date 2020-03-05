from src.service import service
from src.inv import Inventory


def bootstrap_system():
    inv = Inventory()
    a = inv.create_item("Tomato", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onion", 1, "single", "ingredient")
    mayo = inv.create_item("Mayonnaise", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potato Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    side1 = inv.create_item("Fries", 0.1, "single", "side")
    side2 = inv.create_item("Nuggets", 0.3, "single", "side")
    side3 = inv.create_item("Salad", 1, "bowl", "side")
    side4 = inv.create_item("Sundae", 2, "scoop", "side")
    cola_can = inv.create_item("Coca Cola", 1, "350mL", "drink")
    fanta_can = inv.create_item("Fanta", 1, "350mL", "drink")
    sprite_can = inv.create_item("Sprite", 1, "350mL", "drink")
    cola_bottle = inv.create_item("Coca Cola", 2, "600mL", "drink")
    fanta_bottle = inv.create_item("Fanta", 2, "600mL", "drink")
    sprite_bottle = inv.create_item("Sprite", 2, "600mL", "drink")
    cola_bottle1 = inv.create_item("Coca Cola", 3, "1L", "drink")
    fanta_bottle1 = inv.create_item("Fanta", 3, "1L", "drink")
    sprite_bottle1 = inv.create_item("Sprite", 3, "1L", "drink")
    inv.add_item_quantity(cola_bottle1, 5)
    inv.add_item_quantity(fanta_bottle1, 5)
    inv.add_item_quantity(sprite_bottle1, 5)
    inv.add_item_quantity(cola_can, 5)
    inv.add_item_quantity(fanta_can, 5)
    inv.add_item_quantity(sprite_can, 5)
    inv.add_item_quantity(cola_bottle, 5)
    inv.add_item_quantity(fanta_bottle, 5)
    inv.add_item_quantity(sprite_bottle, 5)
    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(side1, 50)
    inv.add_item_quantity(side2, 50)
    inv.add_item_quantity(side3, 5)
    inv.add_item_quantity(side4, 5)
    inv.add_item_quantity(mayo, 5)
    system = service(inv)
    return system