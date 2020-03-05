from src.item import Item
from src.inv import Inventory


class InventoryError(Exception):
    def __init__(self, inventory, msg=None):
        if msg == None:
            print("Error with inventory!")
        self.inventory = {}
        self.msg = msg

    def __str__(self):
        return self.msg


'''  
def check_inv_error(inventory)
    error = False
# TODO Create item
# making an item that already exists
    try:
        if new_item in inventory and inv.create_item(
    
# negative price
# item type not valid


# TODO Remove item
# try to remove an item thats not there

# TODO Add Item Quantity  <-- change name to increase

# TODO Reduce Item Quantity
# try to decrement by a 'negative' amount
'''
