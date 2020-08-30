from datetime import datetime

from controllers.crm_control import len_crm
from controllers.prod_control import len_prod

len_sale = {"len_id_sale": (1, 6),
            "len_id_crm_sale": (1, 6),
            "len_id_prod_sale": (1, 6),
            "len_quantity_sale": (1, 8),
            "len_date_sale": (10, 10)}

len_min = 0
len_max = 1

len_date = 10


def display_insert_sale(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering sale data to insert or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            view.display_clients_help(model.crm)
            id_client = input("Entering client's ID: ")
            if id_client == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(id_client), len_sale["len_id_crm_sale"][len_min],
                                 len_sale["len_id_crm_sale"][len_max]):
                insert_data.append(id_client)
                break
            else:
                view.error_message = f"Invalid a client's ID, the length should be " \
                                     f"between {len_sale['len_id_crm_sale'][len_min]} " \
                                     f"and {len_sale['len_id_crm_sale'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            view.clear_console()
            view.display_products_help(model.products)
            id_prod = input("Entering product's ID: ")
            if id_prod == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(id_prod), len_sale["len_id_prod_sale"][len_min],
                                 len_sale["len_id_prod_sale"][len_max]):
                insert_data.append(id_prod)
                break
            else:
                view.error_message = f"Invalid a product's ID, the length should be " \
                                     f"between {len_sale['len_id_prod_sale'][len_min]} " \
                                     f"and {len_sale['len_id_prod_sale'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            view.clear_console()
            quantity = input("Entering sale's quantity: ")
            if quantity == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(quantity), len_sale["len_quantity_sale"][len_min],
                                 len_sale["len_quantity_sale"][len_max]) and _is_int(quantity):
                insert_data.append(int(quantity))
                break
            else:
                view.error_message = f"Invalid a product's quantity, the length should be " \
                                     f"between {len_sale['len_quantity_sale'][len_min]} " \
                                     f"and {len_sale['len_quantity_sale'][len_max]} and must be an integer!!!"
                view.print_message()

        while is_inside_working:
            sale_date = input("Entering sale's date (e.g. 2001-11-29): ")
            if sale_date == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(sale_date), len_sale["len_date_sale"][len_min],
                                 len_sale["len_date_sale"][len_max]) \
                    and _is_date_correct(sale_date):
                insert_data.append(sale_date)
                if model.insert_sale(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_sale(model.show_data_sale(model.sale), *_len_max_sale())
                    view.error_message = "The sale has been added."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a sale's date, the length should be " \
                                     f"between {len_sale['len_date_sale'][len_min]} " \
                                     f"and {len_sale['len_date_sale'][len_max]} and " \
                                     f"data format YYYY-MM-DD!!!"
                view.print_message()


def display_update_sale(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering sale data to update or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            view.display_sale_help(model.sale, model.crm, model.products)
            id_sale = input("Entering sale's ID: ")
            if id_sale == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(id_sale), len_sale["len_id_sale"][len_min],
                                 len_sale["len_id_sale"][len_max]):
                insert_data.append(id_sale)
                break
            else:
                view.error_message = f"Invalid a sale's ID, the length should be " \
                                     f"between {len_sale['len_id_sale'][len_min]} " \
                                     f"and {len_sale['len_id_sale'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            view.display_clients_help(model.crm)
            id_sale = input("Entering client's ID: ")
            if id_sale == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(id_sale), len_sale["len_id_crm_sale"][len_min],
                                 len_sale["len_id_crm_sale"][len_max]):
                insert_data.append(id_sale)
                break
            else:
                view.error_message = f"Invalid a client's ID, the length should be " \
                                     f"between {len_sale['len_id_crm_sale'][len_min]} " \
                                     f"and {len_sale['len_id_crm_sale'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            view.display_products_help(model.products)
            id_prod = input("Entering product's ID: ")
            if id_prod == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(id_prod), len_sale["len_id_prod_sale"][len_min],
                                 len_sale["len_id_prod_sale"][len_max]):
                insert_data.append(id_prod)
                break
            else:
                view.error_message = f"Invalid a product's ID, the length should be " \
                                     f"between {len_sale['len_id_prod_sale'][len_min]} " \
                                     f"and {len_sale['len_id_prod_sale'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            quantity = input("Entering sale's quantity: ")
            if quantity == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(quantity), len_sale["len_quantity_sale"][len_min],
                                 len_sale["len_quantity_sale"][len_max]) and _is_int(quantity):
                insert_data.append(int(quantity))
                break
            else:
                view.error_message = f"Invalid a product's quantity, the length should be " \
                                     f"between {len_sale['len_quantity_sale'][len_min]} " \
                                     f"and {len_sale['len_quantity_sale'][len_max]} and must be an integer!!!"
                view.print_message()

        while is_inside_working:
            sale_date = input("Entering sale's date (e.g. 2001-11-29): ")
            if sale_date == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(sale_date), len_sale["len_date_sale"][len_min],
                                 len_sale["len_date_sale"][len_max]) \
                    and _is_date_correct(sale_date):
                insert_data.append(sale_date)
                if model.update_sale(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_sale(model.show_data_sale(model.sale), *_len_max_sale())
                    view.error_message = "The sale has been updated."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a sale's date, the length should be " \
                                     f"between {len_sale['len_date_sale'][len_min]} " \
                                     f"and {len_sale['len_date_sale'][len_max]} and " \
                                     f"data format YYYY-MM-DD!!!"
                view.print_message()


def display_delete_sale(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering sale's ID to delete or write \"exit\" to go menu up:\033[0m")
        id_del = input("Entering sale ID: ")
        if model.delete_sale(id_del):
            is_working = False
            view.clear_console()
            view.display_sale(model.show_data_sale(model.sale), *_len_max_sale())
            view.error_message = f"The sale with ID \"{id_del}\" has been deleted."
            view.print_message()
        else:
            break


def display_select_sale(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering sale ID to display or write \"exit\" to go menu up:\033[0m")
        id_select = input("Entering sale ID: ")
        if selected := model.select_sale(id_select):
            is_working = False
            view.clear_console()
            view.display_sale(model.show_data_sale(selected), *_len_max_sale())
        else:
            break


def display_all_sales(model, view):
    if len(model.products) > 0:
        view.clear_console()
        view.display_sale(model.show_data_sale(model.sale), *_len_max_sale())
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_get_transaction_biggest_revenue(model, view):
    if len(model.sale) > 0:
        max_revenue = model.get_transaction_biggest_revenue()
        view.clear_console()
        view.display_sale(model.show_data_sale(max_revenue), *_len_max_sale())
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_get_product_biggest_revenue(model, view):
    if len(model.sale) > 0:
        max_product_revenue = model.get_product_biggest_revenue()
        view.clear_console()
        view.display_product_biggest_revenue(max_product_revenue)
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_get_no_transactions_between_dates(model, view):
    is_working = True
    while is_working:
        print(f"\033[36mEntering dates to count number of transactions between two given dates "
              f"or write \"exit\" to go menu up:\033[0m")
        dates_list = []
        is_inside_working = True
        while is_inside_working:
            start_date = input("Enter starting date: ")
            if start_date == "exit":
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(start_date), len_date, len_date) and _is_date_correct(start_date):
                dates_list.append(start_date)
                break
            else:
                view.error_message = f"Invalid date (YYYY-MM-DD), the length should equal {len_date}!!!"
                view.print_message()

        while is_inside_working:
            end_date = input("Enter ending date: ")
            if end_date == "exit":
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(end_date), len_date, len_date) and _is_date_correct(end_date):
                dates_list.append(end_date)
                no_transactions = model.get_no_transactions_between_dates(*dates_list)
                if no_transactions is not None:
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_no_transactions_between_dates(no_transactions, dates_list)
                else:
                    dates_list.clear()
                    view.error_message = "There is no data to display."
                    view.print_message()
                    is_working = False
                    break
            else:
                view.error_message = f"Invalid date (YYYY-MM-DD), the length should equal {len_date}!!!"
                view.print_message()


def display_get_sum_price_transactions_between_dates(model, view):
    is_working = True
    while is_working:
        print(f"\033[36mEntering dates to sum the price of transactions between two given dates "
              f"or write \"exit\" to go menu up:\033[0m")
        dates_list = []
        is_inside_working = True
        while is_inside_working:
            start_date = input("Enter starting date: ")
            if start_date == "exit":
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(start_date), len_date, len_date) and _is_date_correct(start_date):
                dates_list.append(start_date)
                break
            else:
                view.error_message = f"Invalid date (YYYY-MM-DD), the length should equal {len_date}!!!"
                view.print_message()

        while is_inside_working:
            end_date = input("Enter ending date: ")
            if end_date == "exit":
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(end_date), len_date, len_date) and _is_date_correct(end_date):
                dates_list.append(end_date)
                sum_transactions = model.get_sum_price_transactions_between_dates(*dates_list)
                if sum_transactions is not None:
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_sum_price_transactions_between_dates(sum_transactions, dates_list)
                else:
                    dates_list.clear()
                    view.error_message = "There is no data to display."
                    view.print_message()
                    is_working = False
                    break
            else:
                view.error_message = f"Invalid date (YYYY-MM-DD), the length should equal {len_date}!!!"
                view.print_message()


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _is_int(input_int):
    try:
        _ = int(input_int)
        return True
    except ValueError:
        return False


def _is_date_correct(date_string):
    date_format = '%Y-%m-%d'
    try:
        _ = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


def _len_max_sale():
    len_max_list = [len_sale['len_id_sale'][len_max], len_crm['len_name_crm'][len_max],
                    len_crm['len_surname_crm'][len_max], len_crm['len_company_crm'][len_max],
                    len_prod['len_name_prod'][len_max], len_sale['len_quantity_sale'][len_max],
                    len_sale['len_date_sale'][len_max]]
    return len_max_list
