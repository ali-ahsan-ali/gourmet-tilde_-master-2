class Item():
    def __init__(self, name, price, unit_of_measurement, item_type):
        self._price = price
        self._name = name
        self._unit_of_measurement = unit_of_measurement
        self._item_type = item_type

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @property
    def unit_of_measurement(self):
        return self._unit_of_measurement

    @property
    def item_type(self):
        return self._item_type

    def get_price(self):
        return self._price

    def get_name(self):
        return self._name

    def get_unit_of_measurement(self):
        return self._unit_of_measurement

    def get_item_type(self):
        return self._item_type

    def __repr__(self):
        return f'{self._name} of {self._price} price and is in {self._unit_of_measurement} units and used as {self._item_type}'
