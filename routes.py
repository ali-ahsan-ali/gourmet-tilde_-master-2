from flask import render_template, request, redirect, url_for, abort
from server import app, system
from src.drink_error_handling import check_drink_error, Drink_error
from src.side_error_handling import check_side_error, Side_error
from src.main_error_handling import MainError, check_main_error
'''
Dedicated page for "page not found"
'''


@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404


#home page that shows options for customer, inv or service
#this is going to be changed to show jut info for customer and then
#a new rroute for inv and service ill add alter
@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')


@app.route('/staff', methods=["GET", "POST"])
def staff():
    if request.method == "POST":
        if "Inventory" in request.form:
            return redirect(url_for('inventory'))
        if "Service" in request.form:
            return redirect(url_for('current_orders'))

    return render_template('staff.html')


@app.route('/staff/current_orders', methods=["GET", "POST"])
def current_orders():
    order = system.order_id  # order dictionary
    if request.method == "POST":
        #its a copy so that it doesnt give an error that size was changed
        #during iteration
        for x in order.copy():
            if 'Complete Order {}'.format(
                    x) in request.form and request.form.get(
                        'Complete Order {}'.format(x)) != '':
                # if complete is clicked then it changes status to "finished"
                system.change_order_status(int(x), "Finished")
            elif 'Picked up! {}'.format(
                    x) in request.form and request.form.get(
                        'Picked up! {}'.format(x)) != '':
                system.delete_order(x)
    return render_template('current_orders.html', order_id=system.order_id)


#this checks to see if u select adding any item or if u
#check the order which basically sends u to a confirm page
@app.route('/customer', methods=["GET", "POST"])
def customer():
    if request.method == "POST":
        #takes u to relevant page based on button
        if 'ADD SIDE' in request.form:
            return redirect(url_for("add_side"))
        elif 'ADD MAIN' in request.form:
            return redirect(url_for("add_main"))
        elif 'ADD DRINK' in request.form:
            return redirect(url_for("add_drink"))
        elif 'CHECK ORDER' in request.form:
            return redirect(url_for("check_order"))
            
    price = 0
    for drink in system.drink:
        price += int(drink.get_price())
    for main in system.main:
        price += int(main.get_price())
    for side in system.side:
        price += int(side.get_price())
    return render_template('order.html',
                           drink=system.drink,
                           main=system.main,
                           side=system.side,
                           price=price)


#this is the order checking page and will do the final check and get customer naame
# to create the actual order then send to the confirmation page, or print out errors
@app.route('/customer/complete_order', methods=["GET", "POST"])
def check_order():
    errors = []
    order_id = 0
    if request.method == "POST":
        #checks if u input customer name, then makes the order or returns and error
        if "customer" in request.form:
            customer = request.form["customer"]
            if customer == '':
                errors.append("Enter customer name")
            elif "CONFIRM ORDER" in request.form:
                order_id = system.create_order(customer, system.main,
                                               system.side, system.drink)
                if isinstance(order_id, list):
                    for x in order_id:
                        errors.append(x)
                else:
                    return redirect(
                        url_for('completed_order', order_id=order_id))
            else:
                pass
        if "CONFIRM ORDER" in request.form and "customer" not in request.form:
            pass
    price = 0
    for drink in system.drink:
        price += drink.get_price()
    for main in system.main:
        price += main.get_price()
    for side in system.side:
        price += side.get_price()
    return render_template('check_order.html',
                           drink=system.drink,
                           main=system.main,
                           side=system.side,
                           price=price,
                           errors=errors)


#this is basically the confirmation page which changes route based on their
#order id so there ar emultiple pages for multiple orders
@app.route('/customer/completed_order/<order_id>', methods=["GET", "POST"])
def completed_order(order_id):
    order_id = int(order_id)
    order_content = system.get_order_from_order_ID(order_id)
    if order_content == "No order for that ID":
        return render_template('404.html')
    status = order_content.status
    mains = order_content.mains
    sides = order_content.sides
    drinks = order_content.drinks
    customer = order_content.customer
    price = order_content.get_price()
    return render_template("completed_order.html",order_id = order_id,
                           customer=customer,
                           status=status,
                           mains=mains,
                           drinks=drinks,
                           sides=sides,
                           price=price)


#this takes u to a page where u can press three buttons to customise the main
#or select premade burgers or wraps
@app.route('/customer/add_main', methods=["GET", "POST"])
def add_main():
    if request.method == "POST":
        if "Customise" in request.form:
            return redirect(url_for("add_main_custom"))
        elif "Buy Base Burger" in request.form:
            Beef = system.get_item_from_inv("Beef", "single")
            Muffin_Bun = system.get_item_from_inv("Muffin Bun", "single")
            mayo = system.get_item_from_inv("Mayonnaise", "single")
            lettuce = system.get_item_from_inv("Lettuce", "single leaf")
            system.create_main("Burger", Beef, 1, Muffin_Bun, 2,
                               [mayo, lettuce])
            return redirect(url_for("customer"))
        elif "Buy Base Wrap" in request.form:
            Beef = system.get_item_from_inv("Beef", "single")
            Tortilla = system.get_item_from_inv("Tortilla", "single")
            mayo = system.get_item_from_inv("Mayonnaise", "single")
            lettuce = system.get_item_from_inv("Lettuce", "single leaf")
            system.create_main("Wrap", Beef, 1, Tortilla, 1, [mayo, lettuce])
            return redirect(url_for("customer"))
        else:
            pass
    return render_template("add_main.html")


#this is the custom burger page, it gets all the info and makes sure
#its its put into the right format to be entered into the python class
# it also saves values and errors to be printed out at the end if there are
# any errors.
@app.route('/customer/add_main_custom', methods=["GET", "POST"])
def add_main_custom():
    values = {}
    inv = system.inv
    ingredient = []
    errors = []
    bun_wrap_num = 0
    meat_num = 0
    if request.method == "POST":
        #gets every single field or makes the field = none or 0
        #saves every value in a dict to be displayed on page refresh
        #gets item from inventory, if it an item_type identifier
        if "burger_or_wrap" in request.form:
            burger_or_wrap = request.form['burger_or_wrap']
            values["burger_or_wrap"] = burger_or_wrap
            if burger_or_wrap == '':
                errors.append("Please select a burger or a wrap")
        else:
            burger_or_wrap = None
            errors.append("Please select a burger or a wrap")

        if "bun_wrap_type" in request.form:
            bun_wrap_type = request.form['bun_wrap_type']
            values["bun_wrap_type"] = bun_wrap_type
            bun_wrap = system.get_item_from_inv(bun_wrap_type, "single")
            if bun_wrap_type == '':
                errors.append("Please select a bun or a wrap")
        else:
            bun_wrap = None
            errors.append("Please select a bun or a wrap")
        for x in inv.inventory:
            if "bun_wrap_num{}".format(
                    x.name) in request.form and request.form.get(
                        "bun_wrap_num{}".format(
                            x.name)) != '' and x.name == bun_wrap_type:
                bun_wrap_num = request.form['bun_wrap_num{}'.format(x.name)]
                values["bun_wrap_num"] = bun_wrap_num
        if "meat_filling" in request.form:
            meat_filling = request.form['meat_filling']
            values["meat_filling"] = meat_filling
            #get from inv example
            meat = system.get_item_from_inv(meat_filling, "single")
        else:
            meat = None
            meat_filling = None
        meat_num = None
        for x in inv.inventory:
            if "meat_num{}".format(
                    x.name) in request.form and request.form.get(
                        "meat_num{}".format(
                            x.name)) != '' and x.name == meat_filling:
                meat_num = request.form['meat_num{}'.format(x.name)]
                values["meat_num{}".format(x.name)] = meat_num
                meat_num = int(meat_num)
        if not isinstance(meat_num, int):
            for x in inv.inventory:
                if "meat_num{}".format(
                        x.name) in request.form and request.form.get(
                            "meat_num{}".format(x.name)) != '':
                    values["meat_num{}".format(
                        x.name)] = request.form['meat_num{}'.format(x.name)]
                    meat_num = request.form['meat_num{}'.format(x.name)]
                    meat_num = int(meat_num)

        for x in inv.inventory:
            if '{}{}'.format(
                    x.name, x.unit_of_measurement
            ) in request.form and request.form.get('{}{}'.format(
                    x.name, x.unit_of_measurement)) != "":
                item = system.get_item_from_inv(x.name, x.unit_of_measurement)
                ingredient.append(item)
                values[x.name] = x.name
        #once you have appropriate inputs, you sort to see if they are none,
        # dont add them to ingredients and then check to see if they are None not to input
        # as it will break.

        #making meat num == 0 as inputing meat_filling as none crashes the program
        #this way tis caught in error handling and not output at all
        if meat == None:
            if meat_num != None:
                errors.append("Please select a meat type for your number")
            meat_num = 0
            meat = system.get_item_from_inv("Beef", "single")
        if meat_num == None:
            if meat != None:
                errors.append("Please select anumber for your meat type")
            meat_num = 0

        check = check_main_error(burger_or_wrap, meat, int(meat_num), bun_wrap,
                                 int(bun_wrap_num), ingredient)
        #makes main and returns errors if there is an error or redirects
        # back to customer to add more items or complete order
        if check != []:
            for x in check:
                errors.append(x)
        elif errors != []:
            pass
        else:
            inv1 = system.check_if_enough_item_quantity_in_inv(meat, int(meat_num))
            inv2 = system.check_if_enough_item_quantity_in_inv(bun_wrap, int(bun_wrap_num))
            if inv1 == False:
                errors.append("Not enough {} in inv".format(meat))
            if inv2 == False:
                errors.append("Not enough {} in inv".format(bun_wrap))
            for x in ingredient:
                inv = system.check_if_enough_item_quantity_in_inv(x,1)
                if inv == False:
                    errors.append("Not enough {} in inv".format(x))
                    break
            
        if errors == []:
            system.create_main(burger_or_wrap, meat,
                                          int(meat_num), bun_wrap,
                                          int(bun_wrap_num), ingredient)
            return redirect(url_for('customer'))

    return render_template("add_main_custom.html",
                           errors=errors,
                           values=values,
                           inv=system.inv)


#this does the exact same thing as main but for sides and there are more options to filter from,
#also the side number is a multiplication of the size (2 scoops) by the amount they want (2 sundaes)
@app.route('/customer/add_side', methods=["GET", "POST"])
def add_side():
    errors = []
    error = False
    redir = False
    values = {}
    inv = system.inv
    create = {}
    something = False
    if request.method == "POST":
        #(request.form)
        for x in inv.inventory:
            if 'BUY {} of {} size'.format(
                    x.name, x.unit_of_measurement
            ) in request.form and request.form.get('BUY {} of {} size'.format(
                    x.name, x.unit_of_measurement)) != "":
                values['BUY {} of {} size'.format(
                    x.name, x.unit_of_measurement)] = request.form.get(
                        'BUY {} of {} size'.format(x.name,
                                                   x.unit_of_measurement))
                if 'BUY {} of {} num'.format(
                        x.name, x.unit_of_measurement
                ) in request.form and request.form.get(
                        'BUY {} of {} num'.format(
                            x.name, x.unit_of_measurement)) != "":

                    values['BUY {} of {} num'.format(
                        x.name, x.unit_of_measurement)] = request.form.get(
                            'BUY {} of {} num'.format(x.name,
                                                      x.unit_of_measurement))
                    something = True
                    val = request.form.get('BUY {} of {} size'.format(
                        x.name, x.unit_of_measurement))
                    num = int(
                        request.form.get('BUY {} of {} num'.format(
                            x.name, x.unit_of_measurement)))
                    #if its a single unit, therefore small multiply buy certain alrge values
                    #otherwise multiple by smaller values
                    #i.e fries multiply by 25 singles for a small or
                    #for sundae multiply by 1 scoop for small
                    if val == "small" and x.unit_of_measurement == "single":
                        val = 25
                    elif val == "medium" and x.unit_of_measurement == "single":
                        val = 35
                    elif val == "large" and x.unit_of_measurement == "single":
                        val = 50
                    elif val == "small":
                        val = 1
                    elif val == "medium":
                        val = 2
                    elif val == "large":
                        val = 3
                    else:
                        val = 0
                    num = num * val
                    create[x] = num
                else:
                    error = True
                    errors.append("Enter a value for your selection")

            elif 'BUY {} of {} num'.format(
                    x.name, x.unit_of_measurement
            ) in request.form and request.form.get('BUY {} of {} num'.format(
                    x.name, x.unit_of_measurement)) != "":
                values['BUY {} of {} num'.format(
                    x.name, x.unit_of_measurement)] = request.form.get(
                        'BUY {} of {} num'.format(x.name,
                                                  x.unit_of_measurement))
                errors.append("Please select a size for the side")
                error = True
            else:
                pass
        for x, y in create.items():
            side = check_side_error(x, y)
            check = system.check_if_enough_item_quantity_in_inv(x, y)
            if side != []:
                error = True
                for z in side:
                    errors.append(z)
            elif check == False:
                error = True
                errors.append('Not enough in inventory for {}'.format(x))
            else:
                redir = True

    if request.method == "POST" and something == False and values == {} and create == {}:
        error = True
        errors.append("Please select something or leave the page")
    if redir == True and error == False:
        for x, y in create.items():
            system.create_side(x, y)
        return redirect(url_for("customer"))
    return render_template("add_side.html",
                           errors=errors,
                           values=values,
                           inv=system.inv)


#same as side
@app.route('/customer/add_drink', methods=["GET", "POST"])
def add_drink():
    errors = []
    error = False
    redir = False
    values = {}
    create = {}
    inv = system.inv
    something = False
    if request.method == "POST":
        for x in inv.inventory:
            if 'BUY {} of {}'.format(
                    x.name, x.unit_of_measurement
            ) in request.form and request.form.get('BUY {} of {}'.format(
                    x.name, x.unit_of_measurement)) != "":

                something = True
                val = int(
                    request.form.get('BUY {} of {}'.format(
                        x.name, x.unit_of_measurement)))
                values['BUY {} of {}'.format(x.name,
                                             x.unit_of_measurement)] = val
                create[x] = val
            else:
                pass
        #x is the item and y is the vlaue needed to be made
        for x, y in create.items():
            drink = check_drink_error(x, y)
            check = system.check_if_enough_item_quantity_in_inv(x, y)
            if drink != []:
                error = True
                for error in drink:
                    errors.append(error)
            elif check == False:
                error = True
                errors.append('Not enough in inventory for {}'.format(x))
            else:
                redir = True
        if something == False:
            error = True
            errors.append("Please select something or leave the page")
        if redir == True and error == False:
            for x, y in create.items():
                system.create_drink(x, y)
            return redirect(url_for("customer"))
    return render_template("add_drink.html",
                           errors=errors,
                           values=values,
                           inv=system.inv)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ INVENTORY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/staff/inventory', methods=["GET", "POST"])
def inventory():
    inv = system.inv
    if request.method == "POST":

        for x in inv.inventory:
            if 'EDIT {}'.format(x.name) in request.form and request.form.get(
                    'EDIT {}'.format(x.name)) != "":

                val = int(request.form.get('EDIT {}'.format(x.name)))
                if val > 0:
                    inv.add_item_quantity(x, val)
                else:
                    inv.reduce_item(x, -val)
            else:
                pass
        if 'CREATE ITEM' in request.form:
            return redirect(url_for("create_item"))
        elif 'REMOVE ITEM' in request.form:
            return redirect(url_for("remove_item"))

    return render_template("inventory.html", inv=system.inv)


@app.route('/staff/inventory/create_item', methods=["GET", "POST"])
def create_item():
    values = {}
    if request.method == "POST":
        # name
        name = request.form.get('name')
        if name == '':
            pass
        # units
        if "Units" in request.form:
            units = request.form['Units']
            values["Units"] = units
        else:
            units = None
        #price
        price = request.form.get('Price')
        price = int(price)
        # type
        if "Type" in request.form:
            type_of = request.form["Type"]
            values["Type"] = type_of
        else:
            type_of = None
        # quantity
        quantity = (request.form.get("Quantity"))
        if quantity == "":
            quantity = 0
        else:
            quantity = int(quantity)

        new_item = system.inv.create_item(name, price, units, type_of)
        system.inv.add_item_quantity(new_item, quantity)


    return render_template("create_item.html", values=values)


@app.route('/staff/inventory/remove_item', methods=["GET", "POST"])
def remove_item():
    inv = system.inv
    if request.method == "POST":
        delete = []
        for x in inv.inventory:
            if request.form.get('REMOVE {}'.format(x.name)) != None:
                delete.append(x)
            else:
                pass
        for item in delete:
            inv.remove_item(item)
    return render_template("remove_item.html", inv=system.inv)
