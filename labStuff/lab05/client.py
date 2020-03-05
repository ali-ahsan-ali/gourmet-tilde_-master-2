import weakref
from car import SmallCar, LargeCar, MediumCar, PremiumCar
from car_rental_system import CarRentalSystem
from customer import Customer
from location import Location


# from Booking import Booking
# no need for the above as it is already called within Car_rental_system
# TODO write a series of tests for car_rental_system

# Use all the ones already include in the lab spec
# Add tests for SIZE of lists
# Create more than 2 Bookings lol
# Print all bookings

system = CarRentalSystem()

license_number = 1
registration_number = 1


for name in ["A", "B", "C", "D", "E"]:
    system.add_customer(Customer(name, license_number))
    license_number += 1

for make in ["Tesla", "Maserati", "Lamborghini"]:
    for model in ["Model 1", "Model 2", "Model 3"]:
        system.add_car(PremiumCar(make, model, 999,
                                  registration_number, "Premium"))
        # system.carsprint()
        registration_number += 1

for make in ["Honda", "Toyota", "Ford"]:
    for model in ["Model 11", "Model 12", "Model 13"]:
        system.add_car(SmallCar(make, model, 1, registration_number, "Small"))
        registration_number += 1

for make in ["Honda", "Toyota", "Ford", "Mitsubishi", "Mazda"]:
    for model in ["Model 21", "Model 22", "Model 23"]:
        system.add_car(
            MediumCar(make, model, 1, registration_number, "Medium"))
        registration_number += 1

for make in ["Honda", "Toyota", "Ford"]:
    for model in ["Model 31", "Model 32", "Model 33"]:
        system.add_car(LargeCar(make, model, 1, registration_number, "Large"))
        registration_number += 1

    # def __init__(self, make, model, rate_per_day, registration_number):

customer_1 = system.get_customer(1)
customer_2 = system.get_customer(2)
customer_3 = system.get_customer(3)
print(customer_1)
print(customer_2)
print(customer_3)

print(system.search_car(None, "Model 1"))
print(system.search_car("Tesla", None))
print(system.search_car(None, None))


car_1 = system.get_car(3)
car_2 = system.get_car(8)
car_3 = system.get_car(13)


print(car_1)
print(car_2)
print(car_3)

booking_1 = system.make_booking(customer_1, car_1, 4, Location("UNSW", "UNSW"))
booking_2 = system.make_booking(customer_2, car_2, 7, Location("UNSW", "CSE"))
booking_3 = system.make_booking(customer_3, car_3, 9, Location("CSE", "UNSW"))

print(booking_1)
print(booking_2)
print(booking_3)

# Checks if customers exist
