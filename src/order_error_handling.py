#Raises exception based on business rules listed in user stories
class Order_error(Exception):
    def __init__(self, customer, mains, sides, drinks, msg=None):
        if msg == None:
            print("Error with Order!")
        self.msg = msg
        self.customer = customer
        self.mains = mains
        self.sides = sides
        self.drinks = drinks

    def __str__(self):
        return self.msg


#add stuff about item_type
def check_order_error(customer, mains, sides, drinks):
    error = []
    try:
        if not customer and not mains and not sides and not drinks:
            raise Order_error(customer, mains, sides, drinks,
                              "No input - try again")
    except Order_error as oe:
        error.append(oe)

    try:
        if not mains and not sides and not drinks:
            raise Order_error(customer, mains, sides, drinks,
                              "You cannot make an order with no items")
    except Order_error as oe:
        error.append(oe)

    try:
        if not isinstance(customer, str) or customer == '':
            raise Order_error(customer, mains, sides, drinks,
                              "You must input a valid name")
    except Order_error as oe:
        error.append(oe)
    return error
