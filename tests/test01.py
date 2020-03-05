# Importing all the classes required for this test
import sys
sys.path.append("/Users/ali/Desktop/gourmet-tilde_")
from src.main import main
from src.item import Item
from src.inv import Inventory
from src.drink_error_handling import check_drink_error, Drink_error
from src.service import service
from src.drink import Drink
import pytest


#this tests the creation of main sides and drinks and order, all user stories relating to
#the creation of a order from the user stories
def test_create_drink():
    invent = Inventory()  # Initialise the inventory from the Invetory class
    # Creating items for different drinks and sizes:
    cola_can = invent.create_item("Coca Cola", 1, "350mL", "drink")
    fanta_can = invent.create_item("Fanta", 1, "350mL", "drink")
    sprite_can = invent.create_item("Sprite", 1, "350mL", "drink")
    cola_bottle = invent.create_item("Coca Cola", 2, "600mL", "drink")
    fanta_bottle = invent.create_item("Fanta", 2, "600mL", "drink")
    sprite_bottle = invent.create_item("Sprite", 2, "600mL", "drink")
    # Creating items that are not drinks
    not_drink_1 = invent.create_item("Tomatoe", 1, "single", "ingredient")
    not_drink_2 = invent.create_item("Potato Bun", 1, "single", "Bun")
    not_drink_3 = invent.create_item("Beef", 1, "single", "meat")
    # Added a quantity of 100 for each drink below:
    invent.add_item_quantity(cola_can, 100)
    invent.add_item_quantity(fanta_can, 100)
    invent.add_item_quantity(sprite_can, 100)
    invent.add_item_quantity(cola_bottle, 100)
    invent.add_item_quantity(fanta_bottle, 100)
    invent.add_item_quantity(sprite_bottle, 100)

    system = service(invent)  # Pass inventory into service to test our system:

    # Assert statements to determine if the drink has been made in the system
    assert system.create_drink(cola_can, 1) != False
    assert system.create_drink(fanta_can, 1) != False
    assert system.create_drink(sprite_can, 1) != False
    assert system.create_drink(cola_bottle, 1) != False
    assert system.create_drink(fanta_bottle, 1) != False
    assert system.create_drink(sprite_bottle, 1) != False

    assert isinstance(system.create_drink(cola_can, 0), list)
    # Function would not be
    # called and this will return list of errors
    assert isinstance(system.create_drink(cola_can, -1), list)
    # Cannot take in a
    # negative amount and this will return list of erros
    assert isinstance(system.create_drink(cola_can, 100), list)
    # Since I have created 1 drink from the 100 in the inventory
    # there must be 99 remaining so testing for 100 should return list of erros

    # Asserting that the items passed in are drinks and not a side or main
    assert isinstance(system.create_drink(not_drink_1, 1), list)
    assert isinstance(system.create_drink(not_drink_2, 1), list)
    assert isinstance(system.create_drink(not_drink_3, 1), list)


def test_drink_get_price():
    invent = Inventory()  # Initialise the inventory from the Invetory class
    # Creating items for different drinks and sizes:
    cola_can = invent.create_item("Coca Cola", 1, "350mL", "drink")
    fanta_can = invent.create_item("Fanta", 1, "350mL", "drink")
    sprite_can = invent.create_item("Sprite", 1, "350mL", "drink")
    cola_bottle = invent.create_item("Coca Cola", 2, "600mL", "drink")
    fanta_bottle = invent.create_item("Fanta", 2, "600mL", "drink")
    sprite_bottle = invent.create_item("Sprite", 2, "600mL", "drink")
    # Added a quantity of 100 for each item below:
    invent.add_item_quantity(cola_can, 100)
    invent.add_item_quantity(fanta_can, 100)
    invent.add_item_quantity(sprite_can, 100)
    invent.add_item_quantity(cola_bottle, 100)
    invent.add_item_quantity(fanta_bottle, 100)
    invent.add_item_quantity(sprite_bottle, 100)

    system = service(invent)  # Pass inventory into service to test our system:

    # Create drinks with a specific quantity
    cola_can_7 = system.create_drink(cola_can, 7)
    fanta_can_5 = system.create_drink(fanta_can, 5)
    sprite_can_3 = system.create_drink(sprite_can, 3)
    cola_bottle_4 = system.create_drink(cola_bottle, 4)
    fanta_bottle_2 = system.create_drink(fanta_bottle, 2)
    sprite_bottle_8 = system.create_drink(sprite_bottle, 8)

    # Test that the drink prices are calculated correctly with
    # the quantity given previously
    assert cola_can_7.get_price() == cola_can.price * 7
    assert fanta_can_5.get_price() == fanta_can.price * 5
    assert sprite_can_3.get_price() == sprite_can.price * 3

    assert cola_bottle_4.get_price() == cola_bottle.price * 4
    assert fanta_bottle_2.get_price() == fanta_bottle.price * 2
    assert sprite_bottle_8.get_price() == sprite_bottle.price * 8

    # Test to return false when given a negative amount of drinks
    cola_can_negative1 = Drink(cola_can, -1)
    assert cola_can_negative1.get_price() != cola_can.price * -1


# The testing for a lot of the functions/methods in the Order class
# relies on its implementation in an order system (service).

# Therefore, a lot of the testing here pertains to how the Order class
# interacts with the service system.


def test_create_order():

    #initialise inv
    inv = Inventory()
    # add main ingredients
    #    salads
    ingr1 = inv.create_item("Tomato", 1, "single", "ingredient")
    inv.add_item_quantity(ingr1, 5)
    ingr2 = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    inv.add_item_quantity(ingr2, 5)
    ingr3 = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(ingr3, 5)
    #    buns/wraps
    bun1 = inv.create_item("Potato Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    #    meat/patties
    beef = inv.create_item("Beef", 3, "single", "meat")
    chicken = inv.create_item("Chicken", 3, "single", "meat")
    lamb = inv.create_item("Lamb", 3, "single", "meat")
    inv.add_item_quantity(beef, 5)
    inv.add_item_quantity(chicken, 5)
    inv.add_item_quantity(lamb, 5)
    #    drinks
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    #    sides
    fries = inv.create_item("Fries", 3, "large", "side")
    nugs = inv.create_item("Nuggets", 3, "20 pack", "side")
    salad = inv.create_item("Salad", 3, "single", "side")
    inv.add_item_quantity(fries, 5)
    inv.add_item_quantity(nugs, 5)
    inv.add_item_quantity(salad, 5)

    # initialise the order system
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    # create some mains
    main1 = system.create_main(burger, beef, 1, bun1, 2, [ingr1])
    main2 = system.create_main(burger, chicken, 2, bun2, 3, [ingr1, ingr2])
    main3 = system.create_main(burger, lamb, 1, bun1, 2, [ingr1, ingr2, ingr3])
    main4 = system.create_main(wrap, beef, 1, wrap1, 1, [ingr1])
    main5 = system.create_main(wrap, chicken, 1, wrap1, 1, [ingr2, ingr3])
    # create some sides
    side1 = system.create_side(fries, 1)
    side2 = system.create_side(nugs, 1)
    side3 = system.create_side(salad, 1)
    # create some drinks
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)

    # THE IMPORTANT BIT
    # - create some orders
    order1 = system.create_order("Cust 1", [main1], [side1], [drinks1]) - 1
    order2 = system.create_order("Cust 2", [main1, main2], [side1, side2],
                                 [drinks1, drinks2]) - 1
    order3 = system.create_order("Cust 3", [main1, main2, main3],
                                 [side1, side2, side3],
                                 [drinks1, drinks2, drinks3]) - 1
    order4 = system.create_order("Cust 4", [main4], [side1], [drinks1]) - 1
    order5 = system.create_order("Cust 5", [main1, main5], [side2, side3],
                                 [drinks1, drinks3]) - 1

    # Check if order has correct:
    # customer
    #print('order 1 customer is {}'.format(system.orders[order1].customer))
    assert system.orders[order1].customer == "Cust 1"
    assert system.orders[order2].customer == "Cust 2"
    assert system.orders[order3].customer == "Cust 3"
    assert system.orders[order4].customer == "Cust 4"
    assert system.orders[order5].customer == "Cust 5"
    # mains
    assert system.orders[order1].mains == [main1]
    assert system.orders[order2].mains == [main1, main2]
    assert system.orders[order3].mains == [main1, main2, main3]
    assert system.orders[order4].mains == [main4]
    assert system.orders[order5].mains == [main1, main5]
    # sides
    assert system.orders[order1].sides == [side1]
    assert system.orders[order2].sides == [side1, side2]
    assert system.orders[order3].sides == [side1, side2, side3]
    assert system.orders[order4].sides == [side1]
    assert system.orders[order5].sides == [side2, side3]
    # drinks
    assert system.orders[order1].drinks == [drinks1]
    assert system.orders[order2].drinks == [drinks1, drinks2]
    assert system.orders[order3].drinks == [drinks1, drinks2, drinks3]
    assert system.orders[order4].drinks == [drinks1]
    assert system.orders[order5].drinks == [drinks1, drinks3]
    # status ("In Progress")
    assert system.orders[order1].status == "In Progress"
    assert system.orders[order2].status == "In Progress"
    assert system.orders[order3].status == "In Progress"
    assert system.orders[order4].status == "In Progress"
    assert system.orders[order5].status == "In Progress"

    # Check that valid customer name is input
    order6 = system.create_order('', main1, side1, drinks1)  # empty string
    assert isinstance(order6, list)
    #list of errors
    order7 = system.create_order(45, main2, side2,
                                 drinks2)  # wrong variable type
    assert isinstance(order7, list)

    # Check that items must be ordered
    order8 = system.create_order('John', None, None, None)
    assert isinstance(order8, list)

    # Check that not all kinds of items must be ordered
    order9 = system.create_order('Jim', main1, None, None)
    assert order9 >= 0
    order10 = system.create_order('Pam', main2, [side1, side2], None)
    assert order10 >= 0
    order11 = system.create_order('Dwight', None, None,
                                  [drinks1, drinks2, drinks3])
    assert order11 >= 0

    pass


def test_get_price_order():

    #initialise inv
    inv = Inventory()
    # add main ingredients
    #    salads
    ingr1 = inv.create_item("Tomato", 1, "single", "ingredient")
    inv.add_item_quantity(ingr1, 5)
    ingr2 = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    inv.add_item_quantity(ingr2, 5)
    ingr3 = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(ingr3, 5)
    #    buns/wraps
    bun1 = inv.create_item("Potato Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    #    meat/patties
    beef = inv.create_item("Beef", 3, "single", "meat")
    chicken = inv.create_item("Chicken", 3, "single", "meat")
    lamb = inv.create_item("Lamb", 3, "single", "meat")
    inv.add_item_quantity(beef, 5)
    inv.add_item_quantity(chicken, 5)
    inv.add_item_quantity(lamb, 5)
    #    drinks
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    #    sides
    fries = inv.create_item("Fries", 3, "large", "side")
    nugs = inv.create_item("Nuggets", 3, "20 pack", "side")
    salad = inv.create_item("Salad", 3, "single", "side")
    inv.add_item_quantity(fries, 5)
    inv.add_item_quantity(nugs, 5)
    inv.add_item_quantity(salad, 5)

    # initialise the order system
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    # create some mains
    main1 = system.create_main(burger, beef, 1, bun1, 2, [ingr1])
    main2 = system.create_main(burger, chicken, 2, bun2, 3, [ingr1, ingr2])
    main3 = system.create_main(burger, lamb, 1, bun1, 2, [ingr1, ingr2, ingr3])
    main4 = system.create_main(wrap, beef, 1, wrap1, 1, [ingr1])
    main5 = system.create_main(wrap, chicken, 1, wrap1, 1, [ingr2, ingr3])
    # create some sides
    side1 = system.create_side(fries, 1)
    side2 = system.create_side(nugs, 1)
    side3 = system.create_side(salad, 1)
    # create some drinks
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)

    # THE IMPORTANT BIT
    # - create some (full) orders
    id1 = system.create_order("Cust 1", [main1], [side1], [drinks1])
    order1 = system.get_order_from_order_ID(id1)
    id2 = system.create_order("Cust 2", [main1, main2], [side1, side2],
                              [drinks1, drinks2])
    order2 = system.get_order_from_order_ID(id2)
    order3 = system.create_order("Cust 3", [main1, main2, main3],
                                 [side1, side2, side3],
                                 [drinks1, drinks2, drinks3])
    order3 = system.get_order_from_order_ID(order3)
    order4 = system.create_order("Cust 4", [main4], [side1], [drinks1])
    order4 = system.get_order_from_order_ID(order4)
    order5 = system.create_order("Cust 5", [main1, main5], [side2, side3],
                                 [drinks1, drinks3])
    order5 = system.get_order_from_order_ID(order5)

    # Check returns correct order prices for full orders
    assert order1.get_price() == 16
    assert order2.get_price() == 36
    assert order3.get_price() == 54
    assert order4.get_price() == 13
    assert order5.get_price() == 30

    # Check returns correct prices for partial orders
    order6 = system.create_order('Jim', main1, None, None)
    order6 = system.get_order_from_order_ID(order6)
    assert order6.get_price() == 10
    order7 = system.create_order('Pam', main2, [side1, side2], None)
    order7 = system.get_order_from_order_ID(order7)
    assert order7.get_price() == 20
    order8 = system.create_order('Dwight', None, None,
                                 [drinks1, drinks2, drinks3])
    order8 = system.get_order_from_order_ID(order8)
    assert order8.get_price() == 9
    system.delete_order(id1)
    system.delete_order(id2)
    system.delete_order(order3)
    system.delete_order(order4)
    system.delete_order(order5)

    from src.main import main


# this file tests the create_side function in service
# and it also tests the get_price function in the side class


def test_side_get_price():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    b = inv.create_item("Potato Bun", 1, "single", "Bun")
    c = inv.create_item("Beef", 1, "single", "meat")
    inv.add_item_quantity(a, 5)
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    fries1 = inv.create_item("Fries", 1, "single", "side")
    nuggets1 = inv.create_item("Nuggets", 1, "single", "side")
    salad1 = inv.create_item("Salad", 3, "single", "side")
    inv.add_item_quantity(fries1, 10)
    inv.add_item_quantity(nuggets1, 10)
    inv.add_item_quantity(salad1, 10)
    #added 5 of each item to be used
    system = service(inv)

    fries10 = system.create_side(fries1, 10)
    salad2 = system.create_side(salad1, 2)
    nuggets10 = system.create_side(nuggets1, 10)

    assert fries10.get_price() == fries1.price * 10
    assert salad2.get_price() == salad1.price * 2
    assert nuggets10.get_price() == nuggets1.price * 10


def test_create_side():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    b = inv.create_item("Potato Bun", 1, "single", "Bun")
    c = inv.create_item("Beef", 1, "single", "meat")
    inv.add_item_quantity(a, 5)
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    fries1 = inv.create_item("Fries", 1, "single", "side")
    nuggets1 = inv.create_item("Nuggets", 1, "single", "side")
    salad1 = inv.create_item("Salad", 3, "single", "side")
    inv.add_item_quantity(fries1, 10)
    inv.add_item_quantity(nuggets1, 10)
    inv.add_item_quantity(salad1, 10)
    #added 5 of each item to be used
    system = service(inv)

    assert system.create_side(fries1, 1) != False
    assert system.create_side(nuggets1, 1) != False
    assert system.create_side(salad1, 1) != False

    #try make sides 1 quantity above inventory
    assert system.create_side(fries1, 10) == ['Not enough in inventory']
    #try make negaitve sides
    assert isinstance(system.create_side(fries1, -1), list)
    #try make 0 sides
    # (fails as u can just not call the function if u dont want a side)
    assert isinstance(system.create_side(fries1, 0), list)
    #list of errors
    #try make non-side type item into sides
    assert isinstance(system.create_side(a, 1), list)
    assert isinstance(system.create_side(b, 1), list)
    assert isinstance(system.create_side(c, 1), list)


#initialise inv
inv = Inventory()
a = inv.create_item("Tomatoe", 1, "single", "ingredient")
inv.add_item_quantity(a, 100)
b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
c = inv.create_item("Onions", 1, "single", "ingredient")
inv.add_item_quantity(b, 100)
inv.add_item_quantity(c, 100)
bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
meat1 = inv.create_item("Beef", 3, "single", "meat")
meat2 = inv.create_item("Chicken", 3, "single", "meat")
meat3 = inv.create_item("Lamb", 3, "single", "meat")
inv.add_item_quantity(bun1, 100)
inv.add_item_quantity(bun2, 100)
inv.add_item_quantity(bun3, 100)
inv.add_item_quantity(wrap1, 100)
inv.add_item_quantity(meat1, 100)
inv.add_item_quantity(meat2, 100)
inv.add_item_quantity(meat3, 100)
#added 100 of each item to be used
system = service(inv)
burger = "Burger"
wrap = "Wrap"


def test_main_class_through_service_main_creation():
    #check if there is enough ingredients which is true
    assert system.check_if_enough_item_quantity_in_inv(meat1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(a, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(b, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(c, 1) == True
    #creates the item decreasing inventory automatically
    main = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    #check that the main creation has the right input items
    assert main.bun_or_wrap_type == bun1
    assert main.meat_filling_type == meat1
    assert main.ingredient == [a, b, c]
    #check it has the right amount of patties/buns according to exceptions
    assert main.bun_or_wrap_num == (main.meat_filling_num + 1)
    assert main.bun_or_wrap_num < 6
    assert main.meat_filling_num < 5
    #check auto decrementation works perfectly
    assert inv.get_item_quantity(meat1) == 99
    assert inv.get_item_quantity(bun1) == 98
    assert inv.get_item_quantity(a) == 99
    assert inv.get_item_quantity(b) == 99
    assert inv.get_item_quantity(c) == 99
    #below are two tests which show that the main class public functions work fine
    #make sure the corect price is displayed
    assert main.get_price() == (meat1.price + (bun1.price * 2) + a.price +
                                b.price + c.price)


# check each function in main thingo


def test_create_main_burger():
    # BURGER!!!
    #checks for exception handling to make sure main burger follows business rules
    # create a normal burger main type
    d = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    assert d != False

    # burger with no  of 1 patty and has ingredients
    e = system.create_main(burger, meat1, 0, bun1, 2, [a, b, c])
    assert e != False

    # burger with no ingredients but has a patty
    f = system.create_main(burger, meat1, 1, bun1, 2, [])
    assert f != False

    # burger with no ingredeints or 0 meat (just buns)
    g = system.create_main(burger, meat1, 0, bun1, 2, [])
    assert isinstance(g, list)  #list of errors

    # create a burger with no patty and 1 buns
    h = system.create_main(burger, meat1, 0, bun1, 1, [a, b, c])
    assert isinstance(h, list)  #list of errors

    # create a burger with ingrendeitns and 0 bun_num
    i = system.create_main(burger, meat1, 1, bun1, 0, [a, b, c])
    assert isinstance(i, list)  #list of errors

    # create a burger with ingrendeitns and 0 bun_num
    j = system.create_main(burger, meat1, 1, bun1, 6, [a, b, c])
    assert isinstance(j, list)  #list of errors

    # create a burger with ingredient as the bun
    k = system.create_main(burger, meat1, 1, a, 2, [a, b, c])
    assert isinstance(k, list)  #list of errors

    # create a burger with bun as the ingredient
    l = system.create_main(burger, meat1, 1, bun1, 2, [bun1])
    assert isinstance(l, list)  #list of errors

    # create a burger with ingredient as the meat filling
    m = system.create_main(burger, a, 1, bun1, 2, [a, b, c])
    assert isinstance(m, list)  #list of errors


def test_create_main_wrap():

    # check if u can make a wrap main
    d = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    assert d != False  #True
    # check if u can make a wrap with more than 1 wrap
    e = system.create_main(wrap, meat1, 1, wrap1, 2, [a, b, c])
    assert isinstance(e, list)
    # check if u can make a wrap with 0 wraps
    f = system.create_main(wrap, meat1, 1, wrap1, 0, [a, b, c])
    assert isinstance(f, list)  #list of errors
    # check if u can make a wrap with -1 wraps
    g = system.create_main(wrap, meat1, 1, wrap1, -1, [a, b, c])
    assert isinstance(g, list)  #list of errors
    #try and make a burger
    i = system.create_main(burger, meat1, 1, wrap1, -1, [a, b, c])
    assert isinstance(i, list)  #list of errors
    # check if u can make a wrap with 0 meat and ingredients
    j = system.create_main(wrap, meat1, 0, wrap1, 1, [a, b, c])
    assert j != False  #True
    # check if u can make a wrap with  0 meat filling and no ingredients
    k = system.create_main(wrap, meat1, 0, wrap1, 1, [])
    assert isinstance(k, list)  #list of errors
    # check if u can make a wrap with 0 meat and multiple ingredients
    m = system.create_main(wrap, meat1, 0, wrap1, 1, [a, b, c])
    assert m != False  #True
    # check if u can make a wrap with patty_num 3
    n = system.create_main(wrap, meat1, 3, wrap1, 1, [a, b, c])
    assert isinstance(n, list)  #list of errors
    # check if u can make a wrap with a bun
    o = system.create_main(wrap, meat1, 3, bun1, 1, [a, b, c])
    assert isinstance(o, list)  #list of errors


def test_create_main_negative_integer():
    # check for negative integers for bun num and patty num
    d = system.create_main(wrap, meat1, -1, bun1, 1, [a, b, c])
    assert isinstance(d, list)  #list of errors
    e = system.create_main(wrap, meat1, 1, bun1, -1, [a, b, c])
    assert isinstance(e, list)  #list of errors
    f = system.create_main(wrap, meat1, -1, bun1, -1, [a, b, c])
    assert isinstance(f, list)  #list of errors
    z = system.create_main(burger, meat1, -1, bun1, 1, [a, b, c])
    assert isinstance(z, list)  #list of errors
    e = system.create_main(burger, meat1, 1, bun1, -1, [a, b, c])
    assert isinstance(e, list)  #list of errors
    f = system.create_main(burger, meat1, -1, bun1, -1, [a, b, c])
    assert isinstance(f, list)  #list of errors


def test_create_main_random():
    # random
    d = system.create_main(burger, meat2, 1, bun2, 2, [a, c])
    assert d != False
    e = system.create_main(burger, meat3, 1, bun3, 2, [c, b])
    assert e != False
    f = system.create_main(wrap, meat1, 1, wrap1, 1, [c, b])
    assert f != False


def test_get_price_in_main_class():
    d = system.create_main(wrap, meat2, 1, wrap1, 1, [a, c])
    assert d.get_price() == (meat2.price + wrap1.price + a.price + c.price)
    e = system.create_main(wrap, meat3, 1, wrap1, 1, [c])
    assert e.get_price() == (meat3.price + wrap1.price + c.price)
    f = system.create_main(wrap, meat1, 1, wrap1, 1, [])
    assert f.get_price() == (meat1.price + wrap1.price)
    g = system.create_main(burger, meat2, 1, bun1, 2, [a, c])
    assert g.get_price() == (meat2.price + (2 * bun1.price) + a.price +
                             c.price)
    h = system.create_main(burger, meat3, 2, bun2, 3, [c])
    assert h.get_price() == ((2 * meat3.price) + (3 * bun2.price) + c.price)
    i = system.create_main(burger, meat1, 3, bun3, 4, [])
    assert i.get_price() == ((3 * meat1.price) + (4 * bun3.price))


def test_create_main_wrong_item_type():
    # check for wrong item types being input as parameters in creating
    # a main
    d = system.create_main(wrap, meat1, 1, bun1, 1, [meat2, b, c])
    assert isinstance(d, list)  #list of errors
    e = system.create_main(wrap, bun1, 1, bun1, 1, [a, b, c])
    assert isinstance(e, list)  #list of errors
    f = system.create_main(wrap, bun1, 1, bun1, 1, [a, b, c])
    assert isinstance(f, list)  #list of errors
    g = system.create_main(burger, meat1, 1, bun1, 2, [meat2])
    assert isinstance(g, list)  #list of errors
    h = system.create_main(burger, bun1, 1, bun1, 2, [a, b, c])
    assert isinstance(h, list)  #list of errors
    i = system.create_main(burger, meat1, 1, meat1, 2, [a, b, c])
    assert isinstance(i, list)  #list of errors
