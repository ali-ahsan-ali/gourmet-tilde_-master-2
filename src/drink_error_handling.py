from src.item import Item


#Raises exception based on business rules listed in user stories
# specifically for drinks
class Drink_error(Exception):
    def __init__(self, drink_type, drink_num, msg=None):
        if msg == None:
            print("Error with Order!")
        self.msg = msg
        self.drink_type = drink_type
        self.drink_num = drink_num

    def __str__(self):
        return self.msg


#add stuff about item_type
def check_drink_error(drink_type, drink_num):
    error = []
    try:
        if drink_num == 0:
            raise Drink_error(
                drink_type, drink_num,
                "You selected a drink without entering a number")
    except Drink_error as de:
        error.append(de)
    try:
        if drink_num < 0:
            raise Drink_error(drink_type, drink_num,
                              "You must select a positive integer ")
    except Drink_error as de:
        error.append(de)

    try:
        if drink_type.item_type.lower() != "drink":
            raise Drink_error(
                drink_type, drink_num,
                "You must select a drink_type for a drink to be made")
    except Drink_error as de:
        error.append(de)
    print(error)
    return error
