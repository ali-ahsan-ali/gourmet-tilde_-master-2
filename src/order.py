from src.main import main
from src.item import Item
from src.drink import Drink
from src.side import Side
from src.inv import Inventory
from src.main_error_handling import MainError, check_main_error


class Order():
    def __init__(self, customer, mains, sides, drinks):
        self._customer = customer
        self._mains = mains
        self._sides = sides
        self._drinks = drinks
        self._status = "In Progress"

    @property
    def customer(self):
        return self._customer

    @property
    def mains(self):
        return self._mains

    @property
    def sides(self):
        return self._sides

    @property
    def drinks(self):
        return self._drinks

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self):
        return self._status

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status
        return self._status

    def get_price(self):
        main_price = 0
        side_price = 0
        drink_price = 0
        #is instance is incase someone puts an item in
        #which isnt in lsit form
        #    mains
        if isinstance(self._mains, list):
            print(self._mains)
            for main in self._mains:
                main_price += main.get_price()
        elif self._mains == None:
            pass
        else:
            main_price += self._mains.get_price()

        #    sides
        if isinstance(self._sides, list):
            for side in self._sides:
                side_price += side.get_price()
        elif self._sides == None:
            pass
        else:
            side_price += self._sides.get_price()

        #    drinks
        if isinstance(self._drinks, list):
            for drink in self._drinks:
                drink_price += drink.get_price()
        elif self._drinks == None:
            pass
        else:
            drink_price += self._drinks.get_price()

        #print('In get_price, return:', drink_price + main_price + side_price)
        return (drink_price + main_price + side_price)

    def __str__(self):
        return f'~~~~~ Order ~~~~~\nCustomer: {self._customer}\nMains: {self._mains}\nDrinks:{self._drinks}\nSides: {self._sides}\nTotal price: ${self.get_price()}\nStatus: {self._status}'

    def __repr__(self):
        return str(self)
