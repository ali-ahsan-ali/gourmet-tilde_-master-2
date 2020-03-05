import sys
sys.path.append("/Users/ali/Desktop/gourmet-tilde_")
from src.item import Item
from src.inv import Inventory
from src.inv_error import InventoryError

# initialise inventory
print('========== Initialising test cases ==========')
inv = Inventory()
a = inv.create_item("Tomato", 1, "single", "ingredient")
inv.add_item_quantity(a, 100)
b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
c = inv.create_item("Onions", 1, "single", "ingredient")
inv.add_item_quantity(b, 100)
inv.add_item_quantity(c, 100)
bun1 = inv.create_item("Potato Bun", 3, "single", "bun")
bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
meat1 = inv.create_item("Beef", 3, "single", "meat")
meat2 = inv.create_item("Chicken", 3, "single", "meat")
meat3 = inv.create_item("Lamb", 3, "single", "meat")
inv.add_item_quantity(bun1, 100)
inv.add_item_quantity(bun2, 200)
inv.add_item_quantity(bun3, 300)
inv.add_item_quantity(wrap1, 100)
inv.add_item_quantity(meat1, 100)
inv.add_item_quantity(meat2, 200)
inv.add_item_quantity(meat3, 300)
print('\n========= Beginning testing ==========')

# View Inventory
# All stocked items are displayed WITH inventory level
assert inv.inventory[bun1] == 100
assert inv.inventory[bun2] == 200
assert inv.inventory[bun3] == 300
assert inv.inventory[meat1] == 100
assert inv.inventory[meat2] == 200
assert inv.inventory[meat3] == 300
# Each stocked item's inventory level in appropriate units
#print(inv.inventory[meat3].)
# Different sized items stocked seperately

# Edit Inventory
# Option to edit??
# Staff able to decrease or increase the inventory level of product
inv.reduce_item(bun1, 10)
assert inv.get_item_quantity(bun1) == 90
inv.reduce_item(bun1, 10)
assert inv.get_item_quantity(bun1) == 80
# Staff can't decrease to a negative number
# Staff log in - NA

# Decrement inv levels automatically
# The inventory level decreases by the correct amount when cust orders
# Updated after every orders
#huh
