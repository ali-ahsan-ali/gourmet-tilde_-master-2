import sys
sys.path.append("/Users/ali/Desktop/gourmet-tilde_")
from src.main import main
from src.item import Item
from src.inv import Inventory
from src.main_error_handling import check_main_error, MainError
from src.order import Order
from src.service import service
import pytest

#testing for
#    def auto_decrement_inventory(self, item, quantity):
# in the service class does not need to be done in this file
# as it only returns a function of inventory
#    reduce_item(item, quantity)
# which means it is thoroughly tested through test_inv file

#testing for both
#   def get_price_order(self, order):
#   def get_price_order_id(self, id_number):
# in the service class does not need to be done in this file
# as it only returns a function of Order
#    def get_price(self):
# which means it is thoroughly tested through test_order file
# basic testing is done anyways

# testing for the functions create_main, create_side, create_drinks and create_order
# will be done in seperate files as it tests their respective classes through the
# service functions


#all values for this functionshould be 5 unless they have been used to create
# a main/side/drink
#below should show the inventory automatically decremented for each item type
# and order type
def test_auto_decrement_inventory():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #normal cases
    #make the mains and see if correct decrementation of inventory was achieved
    #through the create_x function which calls the auto_decrement_inventory
    #function.
    # No point testing the actual function as it just returns an
    # inv.py function
    # this way u can test if it actually works for actual creation of
    # mains sides and drinks
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    print(main1, main2, main3, main4)
    #once created, check to see if each items available inventory is
    # initial quantity (5) - quantity used
    # i.e all mains created used a,b,c which means there
    # should only be 1 inventory stock for a,b,c
    assert inv.get_item_quantity(a) == 1
    assert inv.get_item_quantity(b) == 1
    assert inv.get_item_quantity(c) == 1
    assert inv.get_item_quantity(meat1) == 3
    assert inv.get_item_quantity(meat2) == 4
    assert inv.get_item_quantity(meat3) == 4
    assert inv.get_item_quantity(bun1) == 3
    assert inv.get_item_quantity(bun2) == 3
    assert inv.get_item_quantity(bun3) == 3
    assert inv.get_item_quantity(wrap1) == 4

    #the above sentiment ocntinues for sides and drinks
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    assert inv.get_item_quantity(side1) == 4
    assert inv.get_item_quantity(side2) == 4
    assert inv.get_item_quantity(side3) == 4
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    assert inv.get_item_quantity(drink1) == 4
    assert inv.get_item_quantity(drink2) == 4
    assert inv.get_item_quantity(drink3) == 4

    #edge cases

    #you can get as much as the inventory but not any more
    #there is only 4 drinks3 left, and u can order 4 of them
    drinks4 = system.create_drink(drink3, 4)
    assert inv.get_item_quantity(drinks3) == 0
    print(drinks4)
    #again give inv 4 drinks3 and try get 1 than 4 (5) more
    # in a drinks order
    inv.add_item_quantity(drink3, 4)
    drinks5 = system.create_drink(drink3, 5)
    #drink5 was not created and there is still 4 drink3 left
    assert drinks5 == ['Not enough in inventory']
    assert inv.get_item_quantity(drink3) == 4

    #repeat above case for sides, and main

    #you can get as much as the inventory but not any more
    sides4 = system.create_side(side1, 4)
    assert inv.get_item_quantity(side1) == 0
    #again give it 4 and try get 1 than 4 (5) more
    inv.add_item_quantity(side1, 4)
    sides5 = system.create_side(side1, 5)
    #sides5 was not created and there is still 4 side1 left
    assert sides5 == ['Not enough in inventory']
    assert inv.get_item_quantity(side1) == 4

    #you can get as much as the inventory but not any more
    inv.add_item_quantity(bun2, 1)  #to get buns to 4
    mains4 = system.create_main(burger, meat1, 3, bun2, 4, [])
    assert inv.get_item_quantity(meat1) == 0
    assert inv.get_item_quantity(bun2) == 0
    #again give it 4 meat and buns and try get 1 than 4/3 (5/4) more
    inv.add_item_quantity(meat1, 3)
    inv.add_item_quantity(bun2, 4)
    mains5 = system.create_main(burger, meat1, 4, bun2, 5, [])
    #mains5 was not created and there is still 4 buns2 and 3 meat1 left
    assert mains5 == ['Not enough in inventory']
    assert inv.get_item_quantity(meat1) == 3
    assert inv.get_item_quantity(bun2) == 4

    #negative integer testing does not need to be done as it will be
    #handled by exceptions which is implemented when creating a main, side or drink
    #and is testing in test_main or test_drink and test_side files


def test_check_if_enough_item_quantity_in_inv():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #test 0 - 5 quantity available returns true and anything else returns false
    #this is repeated for each item type
    assert system.check_if_enough_item_quantity_in_inv(bun1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(bun1, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(bun1, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(bun1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(bun1, 0) == True
    assert system.check_if_enough_item_quantity_in_inv(bun1, 1) == True

    assert system.check_if_enough_item_quantity_in_inv(c, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(c, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(c, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(c, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(c, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(c, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(c, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(c, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(c, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(wrap1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(wrap1, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(wrap1, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(drink1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(drink1, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(drink1, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(drink1, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(drink1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(drink1, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(drink1, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(drink1, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(drink1, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(drink1, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(side1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(side1, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(side1, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(side1, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(side1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(side1, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(side1, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(side1, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(side1, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(side1, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(meat1, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(meat1, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(meat1, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(meat1, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(meat1, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(meat1, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(meat1, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(meat1, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(meat1, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(meat1, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(a, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(a, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(a, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(a, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(a, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(a, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(a, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(a, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(a, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(a, 0) == True

    assert system.check_if_enough_item_quantity_in_inv(b, 1) == True
    assert system.check_if_enough_item_quantity_in_inv(b, -1) == False
    assert system.check_if_enough_item_quantity_in_inv(b, 99) == False
    assert system.check_if_enough_item_quantity_in_inv(b, 2000) == False
    assert system.check_if_enough_item_quantity_in_inv(b, 2) == True
    assert system.check_if_enough_item_quantity_in_inv(b, 3) == True
    assert system.check_if_enough_item_quantity_in_inv(b, 4) == True
    assert system.check_if_enough_item_quantity_in_inv(b, 5) == True
    assert system.check_if_enough_item_quantity_in_inv(b, 6) == False
    assert system.check_if_enough_item_quantity_in_inv(b, 0) == True


def test_delete_order():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    #create an order
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order3 = system.create_order("Pete", main1, [], [])
    order4 = system.create_order("Ocean", [], [], drinks1)
    #assert that they are given an order_id
    assert order1 == 1
    assert order2 == 2
    assert order3 == 3
    assert order4 == 4

    #testing length of order_id dict and order list
    #test to see if order actually exists
    #test to see if order still exists after calling delete_order function
    assert len(system.orders) == 4
    assert len(system.order_id) == 4
    #assert that an order1 actually exists
    assert system.get_order_from_order_ID(order1) != 'No order for that ID'
    #delete the order
    assert system.delete_order(order1) == True
    #check if the len is lower as one order was deleted
    assert len(system.orders) == 3
    assert len(system.order_id) == 3
    #check to see if the correct output of 'No order for that ID"
    # is returned rather than the deleted order
    assert system.get_order_from_order_ID(order1) == 'No order for that ID'

    #again check that the order exists before the order is deleted
    assert system.get_order_from_order_ID(order2) != 'No order for that ID'
    assert system.delete_order(order2) == True
    #once deleted check len is 1 lower
    assert len(system.orders) == 2
    assert len(system.order_id) == 2
    #check that returns deleted order status
    assert system.get_order_from_order_ID(order2) == 'No order for that ID'

    #above sentiment continues
    assert system.get_order_from_order_ID(order3) != 'No order for that ID'
    assert system.delete_order(order3) == True
    assert len(system.orders) == 1
    assert len(system.order_id) == 1
    assert system.get_order_from_order_ID(order3) == 'No order for that ID'
    assert system.get_order_from_order_ID(order4) != 'No order for that ID'
    assert system.delete_order(order4) == True
    assert len(system.orders) == 0
    assert len(system.order_id) == 0
    assert system.get_order_from_order_ID(order4) == 'No order for that ID'

    #check if random ID numbers can be input
    #less than 0 is never created and 99 isnt created yet
    assert system.delete_order(99) == False
    assert system.delete_order(-1) == False
    assert system.delete_order(0) == False
    assert system.delete_order(-99) == False



def test_get_order_ID_from_cust():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order3 = system.create_order("Pete", main1, [], [])
    order4 = system.create_order("Ocean", [], [], drinks1)
    #check if the right customer names return the right order ID
    assert system.get_order_ID_from_cust("Frank") == order1
    assert system.get_order_ID_from_cust("Bob") == order2
    assert system.get_order_ID_from_cust("Pete") == order3
    assert system.get_order_ID_from_cust("Ocean") == order4
    #returns False or failure when an incorrect customer name is given
    assert system.get_order_ID_from_cust("asrgfae") == False
    assert system.get_order_ID_from_cust("") == False


def test_get_order_ID_from_order():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order_1 = system.get_order_from_order_ID(order1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order_2 = system.get_order_from_order_ID(order2)
    order3 = system.create_order("Pete", main1, [], [])
    order_3 = system.get_order_from_order_ID(order3)
    order4 = system.create_order("Ocean", [], [], drinks1)
    order_4 = system.get_order_from_order_ID(order4)
    #check if correct order_id returns the right order
    assert system.get_order_ID_from_order(order_1) == order1
    assert system.get_order_ID_from_order(order_2) == order2
    assert system.get_order_ID_from_order(order_3) == order3
    assert system.get_order_ID_from_order(order_4) == order4
    #5/0 doesnt exist as 5/0 orders have not been made
    assert system.get_order_ID_from_order(5) == False
    assert system.get_order_ID_from_order(0) == False
    #negative int testing
    assert system.get_order_ID_from_order(-1) == False
    assert system.get_order_ID_from_order(-200) == False



def test_change_order_status():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order_1 = system.get_order_from_order_ID(order1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order_2 = system.get_order_from_order_ID(order2)
    order3 = system.create_order("Pete", main1, [], [])
    order_3 = system.get_order_from_order_ID(order3)
    order4 = system.create_order("Ocean", [], [], drinks1)
    order_4 = system.get_order_from_order_ID(order4)
    #initial status is always in progress
    assert order_1.status == "In Progress"
    assert order_2.status == "In Progress"
    assert order_3.status == "In Progress"
    assert order_4.status == "In Progress"
    #change status and check if the status is correct
    assert system.change_order_status(order1, "Finished") == True
    assert order_1.status == "Finished"
    assert system.change_order_status(order2, "Picked up") == True
    assert order_2.status == "Picked up"
    #check it capitalises the first word automatically
    assert system.change_order_status(order3, "finished") == True
    assert order_3.status == "Finished"
    assert system.change_order_status(order4, "in progress") == True
    assert order_4.status == "In progress"

    #anything not In Progress/Cancelled/Finished should not be allowed
    #to be put in as an input
    assert system.change_order_status(order4, "aefwaefawfaw") == False
    #retains previous progress status
    assert order_4.status == "In progress"
    assert system.change_order_status(order3, "") == False
    assert order_3.status == "Finished"


def test_get_order_from_order_ID():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order_1 = system.get_order_from_order_ID(order1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order_2 = system.get_order_from_order_ID(order2)
    order3 = system.create_order("Pete", main1, [], [])
    order_3 = system.get_order_from_order_ID(order3)
    order4 = system.create_order("Ocean",[] , [], drinks1)
    order_4 = system.get_order_from_order_ID(order4)
    #order not in the service system/order_id dict but is of correct class to be
    # input
    order5 = Order("PRANK", [main1, main4], [sides1, sides2], [drinks1, drinks3])
    # this will return "no order for that ID" if given an order that
    # does not exist in the dict
    order_5 = system.get_order_from_order_ID(order5)



    #check if order ID given has an order which is then checked
    # to see if its the same that get_order_from_order_ID returns
    assert order_1 == system.order_id.get(order1, "No order for that ID")
    assert order_2 == system.order_id.get(order2, "No order for that ID")
    assert order_3 == system.order_id.get(order3, "No order for that ID")
    assert order_4 == system.order_id.get(order4, "No order for that ID")

    #test for order that isnt in the dict
    #check it returns "no order for that ID"
    assert order_5 == system.order_id.get(order_5, "No order for that ID")
    assert order_5 == "No order for that ID"
    assert system.order_id.get(order_5, "No order for that ID") == "No order for that ID"


def test_get_price_order():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order3 = system.create_order("Pete", main1, [], [])
    order4 = system.create_order("Ocean", [], [], drinks1)

    #check the get_price function works by adding the price of mains, sides and drinks
    assert system.get_price_order(system.get_order_from_order_ID(order1)) == main1.get_price() + sides1.get_price() + drinks1.get_price()
    assert system.get_price_order(system.get_order_from_order_ID(
        order2))  == main1.get_price() + main4.get_price() + sides1.get_price(
        ) + sides2.get_price() + drinks1.get_price() + drinks3.get_price()
    assert system.get_price_order(
        system.get_order_from_order_ID(order3)) == main1.get_price()
    assert system.get_price_order(
        system.get_order_from_order_ID(order4)) == drinks1.get_price()
    # a fake order not in service system or dict or order list
    order5 = Order("PRANK", [main1, main4], [sides1, sides2], [drinks1, drinks3])
    #test its price
    assert system.get_price_order(
        system.get_order_from_order_ID(order5)) == False



def test_get_price_order_ID():
    #initialise inv
    inv = Inventory()
    a = inv.create_item("Tomatoe", 1, "single", "ingredient")
    inv.add_item_quantity(a, 5)
    b = inv.create_item("Lettuce", 1, "single leaf", "ingredient")
    c = inv.create_item("Onions", 1, "single", "ingredient")
    inv.add_item_quantity(b, 5)
    inv.add_item_quantity(c, 5)
    bun1 = inv.create_item("Potatoe Bun", 3, "single", "bun")
    bun2 = inv.create_item("Sesame Bun", 2, "single", "bun")
    bun3 = inv.create_item("Muffin Bun", 1, "single", "bun")
    wrap1 = inv.create_item("Tortilla", 3, "single", "wrap")
    meat1 = inv.create_item("Beef", 3, "single", "meat")
    meat2 = inv.create_item("Chicken", 3, "single", "meat")
    meat3 = inv.create_item("Lamb", 3, "single", "meat")
    drink1 = inv.create_item("Cola", 3, "375ml can", "drink")
    drink2 = inv.create_item("Cola", 3, "1L bottle", "drink")
    drink3 = inv.create_item("Sprite", 3, "375ml can", "drink")
    side1 = inv.create_item("Fries", 3, "large", "side")
    side2 = inv.create_item("Nuggets", 3, "20 pack", "side")
    side3 = inv.create_item("Salad", 3, "single", "side")

    inv.add_item_quantity(bun1, 5)
    inv.add_item_quantity(bun2, 5)
    inv.add_item_quantity(bun3, 5)
    inv.add_item_quantity(wrap1, 5)
    inv.add_item_quantity(meat1, 5)
    inv.add_item_quantity(meat2, 5)
    inv.add_item_quantity(meat3, 5)
    inv.add_item_quantity(drink1, 5)
    inv.add_item_quantity(drink2, 5)
    inv.add_item_quantity(drink3, 5)
    inv.add_item_quantity(side1, 5)
    inv.add_item_quantity(side2, 5)
    inv.add_item_quantity(side3, 5)
    #added 5 of each item to be used
    system = service(inv)
    burger = "Burger"
    wrap = "Wrap"

    #make mains for order
    main1 = system.create_main(burger, meat1, 1, bun1, 2, [a, b, c])
    main2 = system.create_main(burger, meat2, 1, bun2, 2, [a, b, c])
    main3 = system.create_main(burger, meat3, 1, bun3, 2, [a, b, c])
    main4 = system.create_main(wrap, meat1, 1, wrap1, 1, [a, b, c])
    sides1 = system.create_side(side1, 1)
    sides2 = system.create_side(side2, 1)
    sides3 = system.create_side(side3, 1)
    drinks1 = system.create_drink(drink1, 1)
    drinks2 = system.create_drink(drink2, 1)
    drinks3 = system.create_drink(drink3, 1)
    order1 = system.create_order("Frank", main1, sides1, drinks1)
    order2 = system.create_order("Bob", [main1, main4], [sides1, sides2],
                                 [drinks1, drinks3])
    order3 = system.create_order("Pete", main1, [], [])
    order4 = system.create_order("Ocean", [], [], drinks1)

    a = system.get_order_from_order_ID(order1)
    print(a)
    assert system.get_price_order_id(order1) == main1.get_price() + sides1.get_price() + drinks1.get_price()
    assert system.get_price_order_id(
        order2) == main1.get_price() + main4.get_price() + sides1.get_price(
        ) + sides2.get_price() + drinks1.get_price() + drinks3.get_price()
    assert system.get_price_order_id(order3) == main1.get_price()
    assert system.get_price_order_id(order4) == drinks1.get_price()

    #test negative numbers and number not related to an order
    assert system.get_price_order(
        system.get_order_from_order_ID(5)) == False
    assert system.get_price_order(
        system.get_order_from_order_ID(0)) == False
    assert system.get_price_order(
        system.get_order_from_order_ID(-1)) == False
    assert system.get_price_order(
        system.get_order_from_order_ID(-99)) == False
    assert system.get_price_order(
        system.get_order_from_order_ID(99)) == False
    assert system.get_price_order(system.get_order_from_order_ID(2000)) == False
