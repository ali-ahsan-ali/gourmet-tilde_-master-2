from car import SmallCar, LargeCar, MediumCar, PremiumCar


class Booking(object):

    def __init__(self, customer_name, period, car, location):
        self._customer_name = customer_name
        self._period = period
        self._car = car
        self._location = location

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def period(self):
        return self._period

    @property
    def car(self):
        return self._car

    @customer_name.setter
    def customer_name(self):
        return self._customer_name

    @period.setter
    def period(self):
        return self._period

    @car.setter
    def car(self):
        return self._car

    def __repr__(self):
        return "=========\nBooking details:\n{}\nCar rented: {}\nLocations: {} for {} days \nTotal fee: {}\n=======\n\n".format(self._customer_name, self._car, self._location, self._period, self._car.get_fee(self._period))
