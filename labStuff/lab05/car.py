
class Car:
    def __init__(self, make, model, rate_per_day, registration_number, car_type):
        self._make = make
        self._model = model
        self._rate_per_day = rate_per_day
        self._registration_number = registration_number
        self._car_type = car_type

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, new_make):
        self._make = new_make

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, new_car_type):
        self._car_type = new_car_type

    @property
    def model(self):
        return self._model

    @model.setter
    def licence(self, new_model):
        self._model = new_model

    @property
    def rate(self):
        return self._rate_per_day

    @rate.setter
    def rate(self, new_rate):
        self._rate_per_day = new_rate

    @property
    def registration_number(self):
        return self._registration_number

    @registration_number.setter
    def registration_number(self, new_registration_number):
        self._registration_number = new_registration_number

    def get_fee(self, period):
        return period * self._rate_per_day

    def __repr__(self):
        return "< {} Car, {}, {}, rego: {} >".format(self._car_type, self._make, self._model, self._registration_number)


class SmallCar(Car):
    def __init__(self, make, model, rate_per_day, registration_number, car_type):
        Car.__init__(self, make, model, 100, registration_number, "Small")


class MediumCar(Car):
    def __init__(self, make, model, rate_per_day, registration_number, car_type):
        Car.__init__(self, make, model, 200, registration_number, "Medium")


class LargeCar(Car):
    def __init__(self, make, model, rate_per_day, registration_number, car_type):
        Car.__init__(self, make, model, 300, registration_number, "Large")


class PremiumCar(Car):
    def __init__(self, make, model, rate_per_day, registration_number, car_type):
        Car.__init__(self, make, model, 400, registration_number, "Premium")
        self._premium_tariff = 1.15
        self._registration_number = registration_number

    def get_fee(self, period):
        if period >= 7:
            return Car.get_fee(self, period) * 0.95 * self._premium_tariff
        else:
            return Car.get_fee(self, period) * self._premium_tariff
