from src.item import Item
from src.main_error_handling import check_main_error, MainError


class main():
    def __init__(self, burger_wrap, meat_filling_type, meat_filling_num,
                 bun_or_wrap_type, bun_or_wrap_num, ingredient):
        self._burger_wrap = burger_wrap
        self._meat_filling_type = meat_filling_type
        self._meat_filling_num = meat_filling_num
        self._bun_or_wrap_type = bun_or_wrap_type
        self._bun_or_wrap_num = bun_or_wrap_num
        self._ingredient = ingredient

    @property
    def burger_wrap(self):
        return self._burger_wrap

    @property
    def meat_filling_type(self):
        return self._meat_filling_type

    @property
    def meat_filling_num(self):
        return self._meat_filling_num

    @property
    def bun_or_wrap_type(self):
        return self._bun_or_wrap_type

    @property
    def bun_or_wrap_num(self):
        return self._bun_or_wrap_num

    @property
    def ingredient(self):
        return self._ingredient

    def __repr__(self):
        if self._meat_filling_num == 0:
            return f'''\nBun/Wrap:{self._bun_or_wrap_num} {self._bun_or_wrap_type}\nIngredients: {self._ingredient}\n'''
        else:
            return f'''\nBun/Wrap:{self._bun_or_wrap_num} {self._bun_or_wrap_type} \nmeat_filling:{self._meat_filling_num} {self._meat_filling_type} \nIngredients: {self._ingredient}\n'''  # {self._ingredient}'''

    def get_price(self):
        ingredient_cost = 0
        bun_cost = self._bun_or_wrap_type.price * self._bun_or_wrap_num
        meat_filling_cost = self._meat_filling_type.price * self._meat_filling_num
        for x in self._ingredient:
            ingredient_cost = ingredient_cost + x.price
        return bun_cost + ingredient_cost + meat_filling_cost


#a = Item("huh", 1, 2)
#b = main("Burger", a, 1, a, 2, a, a, a, a, a)
#print(b.get_price())