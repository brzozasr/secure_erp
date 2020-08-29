len_prod = {"len_id_prod": (1, 6),
            "len_name_prod": (2, 25),
            "len_price_prod": (1, 11),
            "len_quantity_prod": (1, 8)}

len_min = 0
len_max = 1


def display_insert_product(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering product data to insert or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            name = input("Entering product's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_prod["len_name_prod"][len_min],
                                 len_prod["len_name_prod"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a product's name, the length should be " \
                                     f"between {len_prod['len_name_prod'][len_min]} " \
                                     f"and {len_prod['len_name_prod'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            price = input("Entering product's price: ")
            if price == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(price), len_prod["len_price_prod"][len_min],
                                 len_prod["len_price_prod"][len_max]) \
                    and _is_float_two_decimal_places(price) is not None:
                insert_data.append(_is_float_two_decimal_places(price))
                break
            else:
                view.error_message = f"Invalid a product's price it has to be a number, greater than 0 and " \
                                     f"cannot have more than two decimal places. The length should be " \
                                     f"between {len_prod['len_price_prod'][len_min]} " \
                                     f"and {len_prod['len_price_prod'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            quantity = input("Entering product's quantity: ")
            if quantity == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(quantity), len_prod["len_quantity_prod"][len_min],
                                 len_prod["len_quantity_prod"][len_max]) and _is_int(quantity):
                insert_data.append(int(quantity))
                if model.insert_product(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_products(model.products, *_len_max_prod())
                    view.error_message = "The product has been added."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a product's quantity, the length should be " \
                                     f"between {len_prod['len_quantity_prod'][len_min]} " \
                                     f"and {len_prod['len_quantity_prod'][len_max]} and must be an integer!!!"
                view.print_message()


def display_update_product(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering product data to update or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            product_id = input("Entering product's ID: ")
            if product_id == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(product_id), len_prod["len_id_prod"][len_min],
                                 len_prod["len_id_prod"][len_max]):
                insert_data.append(product_id)
                break
            else:
                view.error_message = f"Invalid a product's ID, the length should be " \
                                     f"between {len_prod['len_id_prod'][len_min]} " \
                                     f"and {len_prod['len_id_prod'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            name = input("Entering product's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_prod["len_name_prod"][len_min],
                                 len_prod["len_name_prod"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a product's name, the length should be " \
                                     f"between {len_prod['len_name_prod'][len_min]} " \
                                     f"and {len_prod['len_name_prod'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            price = input("Entering product's price: ")
            if price == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(price), len_prod["len_price_prod"][len_min],
                                 len_prod["len_price_prod"][len_max]) \
                    and _is_float_two_decimal_places(price) is not None:
                insert_data.append(_is_float_two_decimal_places(price))
                break
            else:
                view.error_message = f"Invalid a product's price it has to be a number, greater than 0 and " \
                                     f"cannot have more than two decimal places. The length should be " \
                                     f"between {len_prod['len_price_prod'][len_min]} " \
                                     f"and {len_prod['len_price_prod'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            quantity = input("Entering product's quantity: ")
            if quantity == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(quantity), len_prod["len_quantity_prod"][len_min],
                                 len_prod["len_quantity_prod"][len_max]) and _is_int(quantity):
                insert_data.append(int(quantity))
                if model.update_product(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_products(model.products, *_len_max_prod())
                    view.error_message = "The product has been updated."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a product's quantity, the length should be " \
                                     f"between {len_prod['len_quantity_prod'][len_min]} " \
                                     f"and {len_prod['len_quantity_prod'][len_max]} and must be an integer!!!"
                view.print_message()


def display_delete_product(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering product ID to delete or write \"exit\" to go menu up:\033[0m")
        id_del = input("Entering product ID: ")
        if model.delete_product(id_del):
            is_working = False
            view.clear_console()
            view.display_products(model.products, *_len_max_prod())
            view.error_message = f"The product with ID \"{id_del}\" has been deleted."
            view.print_message()
        else:
            break


def display_all_products(model, view):
    if len(model.products) > 0:
        view.clear_console()
        view.display_products(model.products, *_len_max_prod())
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_select_product(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering product ID to display or write \"exit\" to go menu up:\033[0m")
        id_select = input("Entering product ID: ")
        if selected := model.select_product(id_select):
            is_working = False
            view.clear_console()
            view.display_products(selected, *_len_max_prod())
        else:
            break


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _is_float_two_decimal_places(input_float):
    try:
        no = float(input_float)
        if no > 0:
            no_str = str(no)
            no_split = no_str.split('.')
            if len(no_split[1]) > 2:
                return None
            else:
                return no
        else:
            return None
    except ValueError:
        return None


def _is_int(input_int):
    try:
        _ = int(input_int)
        return True
    except ValueError:
        return False


def _len_max_prod():
    len_max_list = []
    for key, value in len_prod.items():
        len_max_list.append(len_prod[key][len_max])
    return len_max_list

