from booking import Booking
from car import SmallCar, LargeCar, MediumCar, PremiumCar


class CarRentalSystem():

    def __init__(self):
        self._cars = []
        self._customers = []
        self._bookings = []
    '''
    Properties
    '''
    @property
    def cars(self):
        return self._cars

    @property
    def customers(self):
        return self._customers

    @property
    def bookings(self):
        return self._bookings

    @bookings.setter
    def bookings(self):
        return self._bookings

    def make_booking(self, customer, car, period, location):
        # implement this function
        new_booking = Booking(customer, period, car, location)
        self._bookings.append(new_booking)
        return new_booking

    def get_customer(self, licence):
        for customer in self._customers:
            if customer.licence is licence:
                return customer
        return None

    def get_car(self, registration_number):
        for car in self._cars:
            if car.registration_number is registration_number:
                l = []
                for booking in self._bookings:
                    if car in booking:
                        print(booking)
                        l.append(booking)
                return l

    def add_car(self, car):
        self._cars.append(car)

    def add_customer(self, customer):
        self._customers.append(customer)

    def search_car(self, name=None, model=None):
        if (name == None) and (model == None):
            return self._cars
        for car in self._cars:
            if name == None:
                l = []
                for model in car.model:
                    l.append(car)
                return l
            elif name in car.make:
                l = []
                if model == None:
                    l.append(car)
                elif model in car.model:
                    return car
                return l

    def __str__(self):
        return "{0},{1},{2}".format(self._cars, self._customers, self._bookings)
