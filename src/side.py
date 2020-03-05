from src.item import Item


class Side():
    def __init__(self, side_type, side_num):
        self._side_type = side_type
        self._side_num = side_num

    @property
    def side_num(self):
        return self._side_num

    @property
    def side_type(self):
        return self._side_type

    def __repr__(self):
        return f'{self.side_num} {self.side_type}'

    def get_price(self):
        side_cost = self.side_type.price * self.side_num
        return side_cost

    def get_drink(self):
        return repr(self)