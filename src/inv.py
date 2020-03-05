from src.item import Item
import pickle
import os


class Inventory():
    def __init__(self):
        self._inventory = {}

    @property
    def inventory(self):
        return self._inventory

    def __str__(self):
        return f'{self._inventory}'

    def create_item(self, name, price, unit_of_measurement, item_type):
        new_item = Item(name, price, unit_of_measurement, item_type)
        self.inventory[new_item] = 0
        return new_item

    def remove_item(self, item):
        self._inventory.pop(item)

    def add_item_quantity(self, item, quantity):
        prev_quantity = self._inventory.get(item)
        #print("prev:", prev_quantity, "item:", item, "quantity:", quantity)
        new_quantity = quantity + prev_quantity
        self._inventory[item] = new_quantity
        pass

    def reduce_item(self, item, quantity):
        prev_quantity = self._inventory.get(item)
        #print("prev:", prev_quantity, "item:", item, "quantity:", quantity)
        new_quantity = prev_quantity - quantity
        #print(new_quantity)
        self._inventory[item] = new_quantity
        #print(self._inventory[item])
        pass

    def get_item_quantity(self, item):
        #print("ITEM", item)
        #print("DEFAULT", self._inventory.get(item, 0))
        return self._inventory.get(item, 0)

    def get_items(self, item):
        return item.__repr__()