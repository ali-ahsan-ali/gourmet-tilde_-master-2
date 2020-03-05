from src.item import Item


#Raises exception based on business rules listed in user stories
class Side_error(Exception):
    def __init__(self, side_type, side_num, msg=None):
        if msg == None:
            print("Error with Order!")
        self.msg = msg
        self.side_type = side_type
        self.side_num = side_num

    def __str__(self):
        return self.msg


#add stuff about item_types
def check_side_error(side_type, side_num):
    error = []
    try:
        if side_num == 0:
            raise Side_error(side_type, side_num,
                             "You selected a side without entering a number")
    except Side_error as se:
        print(se)
        error.append(se)
    try:
        if side_num < 0:
            raise Side_error(side_type, side_num,
                             "You must select a psoitive integer")
    except Side_error as se:
        print(se)
        error.append(se)
    try:
        if side_type.item_type.lower() != "side":
            raise Side_error(side_type, side_num,
                             "You must select a side type item for a side")
    except Side_error as se:
        print(se)
        error.append(se)
    return error
