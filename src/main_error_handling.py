from src.item import Item


#Raises exception based on business rules listed in user stories
class MainError(Exception):
    def __init__(self,
                 burger_wrap,
                 meat_filling_type,
                 meat_filling_num,
                 bun_or_wrap_type,
                 bun_or_wrap_num,
                 ingredient,
                 msg=None):
        if msg == None:
            print("Error with Main!")
        self.msg = msg
        self.burger_wrap = burger_wrap
        self.meat_filling_type = meat_filling_type
        self.meat_filling_num = meat_filling_num
        self.bun_or_wrap_type = bun_or_wrap_type
        self.bun_or_wrap_num = bun_or_wrap_num
        self.ingredient = ingredient

    def __str__(self):
        return self.msg


#add stuff about item_type
def check_main_error(burger_wrap, meat_filling_type, meat_filling_num,
                     bun_or_wrap_type, bun_or_wrap_num, ingredient):
    error = []
    try:
        if meat_filling_num < 0:
            raise MainError(burger_wrap, meat_filling_type, meat_filling_num,
                            bun_or_wrap_type, bun_or_wrap_num, ingredient,
                            '''You must select a positive integer''')
    except MainError as me:
        print(me)
        error.append(me)
    try:
        if bun_or_wrap_num < 0:
            raise MainError(burger_wrap, meat_filling_type, meat_filling_num,
                            bun_or_wrap_type, bun_or_wrap_num, ingredient,
                            '''You must select a positive integer''')
    except MainError as me:
        print(me)
        error.append(me)
        #Item type must be bun to be used in burger as a  bun
    try:
        if meat_filling_type.item_type.lower() != "meat":
            raise MainError(
                burger_wrap, meat_filling_type, meat_filling_num,
                bun_or_wrap_type, bun_or_wrap_num, ingredient,
                '''You must select a meat type for meat filling in a main''')
    except MainError as me:
        print(me)
        error.append(me)
    try:
        for x in ingredient:
            if x.item_type.lower() != "ingredient":
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select an ingredient type items to be used as an ingredient'''
                )
    except MainError as me:
        print(me)
        error.append(me)

    if burger_wrap.lower() == "burger":
        #Item type must be bun to be used in burger as a  bun
        try:
            if bun_or_wrap_type.item_type.lower() != "bun":
                raise MainError(burger_wrap, meat_filling_type,
                                meat_filling_num, bun_or_wrap_type,
                                bun_or_wrap_num, ingredient,
                                '''You must select a bun type for a burger''')
        except MainError as me:
            print(me)
            error.append(me)
        # if less than two buns given, give error
        try:
            if bun_or_wrap_num < 2:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select 2 or more buns for a burger''')
        except MainError as me:
            print(me)
            error.append(me)
        # cannot have more than 4 patties
        try:
            if meat_filling_num != 0 and meat_filling_num > 4:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You cannot select more than 4 patties for a burger''')
        except MainError as me:
            print(me)
            error.append(me)
        # cannot have more than 5 buns
        try:
            if bun_or_wrap_num > 5:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You cannot select more than 5 buns for a burger''')
        except MainError as me:
            print(me)
            error.append(me)
        # meat_filling num is 0 not given and ingredient empty
        try:
            if meat_filling_num == 0 and ingredient == []:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select a meat_filling type or select an ingredient'''
                )
        except MainError as me:
            print(me)
            error.append(me)

        # if meat_filling num is given and it does not fit the business rules
        # i.e 3 buns = 2 patties
        # disregard if meat_filling num is not given
        try:
            if meat_filling_num != 0 and meat_filling_num != None and bun_or_wrap_num != None and bun_or_wrap_num != 0:
                if meat_filling_num != (bun_or_wrap_num - 1):
                    raise MainError(
                        burger_wrap, meat_filling_type, meat_filling_num,
                        bun_or_wrap_type, bun_or_wrap_num, ingredient,
                        '''You must have appropriate patties for the number of buns you have selected.\ni.e 1 meat_filling for 2 buns\n2 patties for 3 buns and so on.\n'''
                    )
        except MainError as me:
            print(me)
            error.append(me)
    elif burger_wrap.lower() == "wrap":
        try:
            # must be wrap type
            if bun_or_wrap_type.item_type.lower() != "wrap":
                raise MainError(burger_wrap, meat_filling_type,
                                meat_filling_num, bun_or_wrap_type,
                                bun_or_wrap_num, ingredient,
                                '''You must select a wrap item for a wrap ''')
        except MainError as me:
            print(me)
            error.append(me)
        try:
            # only one bun/wrap item for a wrap
            if bun_or_wrap_num == 0:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select a single wrap item for a wrap ''')
        except MainError as me:
            print(me)
            error.append(me)
        try:
            # only 1 bun for a wrap
            if bun_or_wrap_num > 1 or bun_or_wrap_num < 1:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select a single wrap item for a wrap ''')
        except MainError as me:
            print(me)
            error.append(me)
        try:
            # less than or equal to 2 patties for a wrap
            if meat_filling_num != 0 and meat_filling_num > 2:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You cannot select more than 2 meat units for a wrap''')
        except MainError as me:
            print(me)
            error.append(me)
        try:
            # meat_filling not given and ingredient empty
            if meat_filling_num == 0 and ingredient == []:
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select a meat_filling type or select an ingredient'''
                )
        except MainError as me:
            print(me)
            error.append(me)
    else:
        try:
            if burger_wrap.lower() != "burger" and burger_wrap.lower != "wrap":
                raise MainError(
                    burger_wrap, meat_filling_type, meat_filling_num,
                    bun_or_wrap_type, bun_or_wrap_num, ingredient,
                    '''You must select a 'Burger' or a 'Wrap' for a main''')
        except MainError as me:
            print(me)
            error.append(me)
    return error
