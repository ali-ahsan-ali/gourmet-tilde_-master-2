from src.item import Item


class Drink():
    def __init__(self, drink_type, drink_num):
        self._drink_type = drink_type
        self._drink_num = drink_num

    @property
    def drink_num(self):
        return self._drink_num

    # drink type is subclass of item
    @property
    def drink_type(self):
        return self._drink_type

    def __repr__(self):
        return f'{self._drink_num} {self._drink_type}'

    def get_price(self):
        if self._drink_num <= 0:
            return 0
        else:
            drink_cost = self._drink_type.price * self._drink_num
            return drink_cost

    def get_drink(self):
        return repr(self)
