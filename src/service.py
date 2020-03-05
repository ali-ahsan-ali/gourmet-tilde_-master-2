from src.order import Order
from src.main import main
from src.side import Side
from src.drink import Drink
from src.item import Item
from src.main_error_handling import check_main_error, MainError
from src.inv import Inventory
from src.order_error_handling import check_order_error, Order_error
from src.side_error_handling import Side_error, check_side_error
from src.drink_error_handling import Drink_error, check_drink_error
import pickle
import os


class service():
    def __init__(self, inv):
        self._inventory = inv

        self._order_id = {}

        self._main = []

        self._side = []

        self._drink = []
        self._orders = []
        self._id = 0

    @property
    def main(self):
        return self._main

    @property
    def side(self):
        return self._side

    @property
    def drink(self):
        return self._drink

    @property
    def order_id(self):
        return self._order_id

    @property
    def inv(self):
        return self._inventory

    @property
    def orders(self):
        return self._orders

    @property
    def id(self):
        return self._id

    def next(self):
        self._id += 1
        return self._id

    def create_main(self, burger_or_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredients):
        #check for business rules for burger/wrap mains
        #add more exceptions about item type being in business rules
        #when selecting an ingredient it is automatically choosing 1 unit
        error = check_main_error(burger_or_wrap, meat_filling_type,
                                 meat_filling_num, bun_or_wrap_type,
                                 bun_or_wrap_num, ingredients)
        if error != []:
            return error
        else:
            error = False
        print(error)
        #inventory check for each item
        inv_check = False
        ing_check = True
        meat_filling_check = False
        bun_check = False
        if self.check_if_enough_item_quantity_in_inv(bun_or_wrap_type,
                                                     bun_or_wrap_num) == True:
            bun_check = True
        if self.check_if_enough_item_quantity_in_inv(meat_filling_type,
                                                     meat_filling_num) == True:
            meat_filling_check = True
        for x in ingredients:
            print(x)
            if self.check_if_enough_item_quantity_in_inv(x, 1) == True:
                pass
            else:
                ing_check = False
        if ing_check == True and bun_check == True and meat_filling_check == True:
            inv_check = True
        #if inventory check passes and no errors then make it
        print(inv_check)
        if inv_check == True and error == False:
            new_main = main(burger_or_wrap, meat_filling_type,
                            meat_filling_num, bun_or_wrap_type,
                            bun_or_wrap_num, ingredients)
            self.auto_decrement_inventory(meat_filling_type, meat_filling_num)
            self.auto_decrement_inventory(bun_or_wrap_type, bun_or_wrap_num)
            for x in ingredients:
                self.auto_decrement_inventory(x, 1)
            self.main.append(new_main)
            print(self.main)
            return new_main
        if error == True or inv_check == False:
            #error and do nothing
            #return false is for testing purposes
            error = []
            error.append("Not enough in inventory")
            return error

    def create_drink(self, drink_type, drink_num):
        error = check_drink_error(drink_type, drink_num)
        if error != []:
            print("returning erro")
            return error
        else:
            error = False
        if self.check_if_enough_item_quantity_in_inv(
                drink_type, drink_num) == True and error == False:
            new_drink = Drink(drink_type, drink_num)
            self.auto_decrement_inventory(drink_type, drink_num)
            self._drink.append(new_drink)
            return new_drink
        else:
            error = []
            error.append("Not enough in inventory")
            return error

    def create_side(self, side_type, side_num):
        error = check_side_error(side_type, side_num)
        if error != []:
            print("returning erro")
            return error
        else:
            error = False
        if self.check_if_enough_item_quantity_in_inv(
                side_type, side_num) == True and error == False:
            new_side = Side(side_type, side_num)
            self.auto_decrement_inventory(side_type, side_num)
            self.side.append(new_side)
            return new_side
        else:
            error = []
            error.append("Not enough in inventory")
            return error

    def check_if_enough_item_quantity_in_inv(self, item, quantity):
        available_quantity = self._inventory.get_item_quantity(item)
        if available_quantity >= quantity and quantity >= 0:
            return True
        else:
            return False

    def auto_decrement_inventory(self, item, quantity):
        self._inventory.reduce_item(item, quantity)

    def create_order(self, customer, main, sides, drinks):
        error = check_order_error(customer, main, sides, drinks)
        if error != []:
            return error
        else:
            error = False
        if error == False:
            new_order = Order(customer, main, sides, drinks)
            self._orders.append(new_order)
            assigned_order_id = self.next()
            self._order_id[assigned_order_id] = new_order
            #print("\n\n\n\n!!!!!A", self._order_id, "A!!!!\n\n\n\n\n")
            self._main = []
            self._side = []
            self._drink = []
            return assigned_order_id
        else:
            return False

    def delete_order(self, id_number):
        order = self._order_id.get(id_number, "No order for that ID")
        self._order_id.pop(id_number, "No order for that ID")
        for x in self._orders:
            if x == order:
                self._orders.remove(x)
                return True
        return False

    def get_order_ID_from_cust(self, customer):
        correct_order = None
        for order in self._orders:
            if customer == order.customer:
                correct_order = order
        for key, value in self._order_id.items():
            if value == correct_order:
                return key
        return False

    def get_order_ID_from_order(self, order):
        for key, value in self._order_id.items():
            if value == order:
                return key
        return False

    def get_order_from_order_ID(self, id_number):
        print("\n\n\n\n\n\n", id_number, self._order_id, "\n\n\n\n\n\n")
        return self._order_id.get(id_number, "No order for that ID")

    def change_order_status(self, id_number, status):
        order_requested = self._order_id.get(id_number, "No order for that ID")
        if status.lower() == "finished" or status.lower(
        ) == "in progress" or status.lower() == "picked up":
            order_requested.set_status(status.capitalize())
            return True
        else:
            return False

    def get_price_order(self, order):
        if order in self._orders:
            return order.get_price()
        else:
            return False

    def get_price_order_id(self, id_number):
        if id_number in self._order_id:
            order_request = self._order_id[id_number]
            return self.get_price_order(order_request)
        else:
            return False

    def display_orders(self):
        return str(self)

    def get_item_from_inv(self, item_name, unit_of_measurement):
        for x in self._inventory.inventory.keys():
            if x.name.lower() == item_name.lower():
                if x.unit_of_measurement == unit_of_measurement:
                    return x
        pass

    def __repr__(self):
        return f'{self._order_id}'
