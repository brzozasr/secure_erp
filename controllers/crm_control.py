len_crm = {"len_id_crm": (1, 6),
           "len_name_crm": (2, 20),
           "len_surname_crm": (2, 30),
           "len_company_crm": (2, 25),
           "len_email_crm": (6, 35)}

len_min = 0
len_max = 1


def display_insert_crm(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering client data to insert or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            name = input("Entering client's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_crm["len_name_crm"][len_min],
                                 len_crm["len_name_crm"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a client's name, the length should be " \
                                     f"between {len_crm['len_name_crm'][len_min]} " \
                                     f"and {len_crm['len_name_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            surname = input("Entering client's surname: ")
            if surname == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(surname), len_crm["len_surname_crm"][len_min],
                                 len_crm["len_surname_crm"][len_max]):
                insert_data.append(surname)
                break
            else:
                view.error_message = f"Invalid a client's surname, the length should be " \
                                     f"between {len_crm['len_surname_crm'][len_min]} " \
                                     f"and {len_crm['len_surname_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            company = input("Entering client's company name: ")
            if company == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(company), len_crm["len_company_crm"][len_min],
                                 len_crm["len_company_crm"][len_max]):
                insert_data.append(company)
                break
            else:
                view.error_message = f"Invalid a client's company name, the length should be " \
                                     f"between {len_crm['len_company_crm'][len_min]} " \
                                     f"and {len_crm['len_company_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            email = input("Entering client's email: ")
            if email == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(email), len_crm["len_email_crm"][len_min],
                                 len_crm["len_email_crm"][len_max]) and "@" in email and "." in email:
                insert_data.append(email)
                if model.insert_crm(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_crm(model.crm, *_len_max_crm())
                    view.error_message = "The client has been added."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a client's email, the length should be " \
                                     f"between {len_crm['len_email_crm'][len_min]} " \
                                     f"and {len_crm['len_email_crm'][len_max]}, " \
                                     f"\"@\" and \".\" required!!!"
                view.print_message()


def display_update_crm(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering client data to update or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            client_id = input("Entering client's ID: ")
            if client_id == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(client_id), len_crm["len_id_crm"][len_min],
                                 len_crm["len_id_crm"][len_max]):
                insert_data.append(client_id)
                break
            else:
                view.error_message = f"Invalid a client's name, the length should be " \
                                     f"between {len_crm['len_id_crm'][len_min]} " \
                                     f"and {len_crm['len_id_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            name = input("Entering client's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_crm["len_name_crm"][len_min],
                                 len_crm["len_name_crm"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a client's name, the length should be " \
                                     f"between {len_crm['len_name_crm'][len_min]} " \
                                     f"and {len_crm['len_name_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            surname = input("Entering client's surname: ")
            if surname == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(surname), len_crm["len_surname_crm"][len_min],
                                 len_crm["len_surname_crm"][len_max]):
                insert_data.append(surname)
                break
            else:
                view.error_message = f"Invalid a client's surname, the length should be " \
                                     f"between {len_crm['len_surname_crm'][len_min]} " \
                                     f"and {len_crm['len_surname_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            company = input("Entering client's company name: ")
            if company == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(company), len_crm["len_company_crm"][len_min],
                                 len_crm["len_company_crm"][len_max]):
                insert_data.append(company)
                break
            else:
                view.error_message = f"Invalid a client's company name, the length should be " \
                                     f"between {len_crm['len_company_crm'][len_min]} " \
                                     f"and {len_crm['len_company_crm'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            email = input("Entering client's email: ")
            if email == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(email), len_crm["len_email_crm"][len_min],
                                 len_crm["len_email_crm"][len_max]) and "@" in email and "." in email:
                insert_data.append(email)
                if model.update_crm(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    view.display_crm(model.crm, *_len_max_crm())
                    view.error_message = "The client has been updated."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a client's email, the length should be " \
                                     f"between {len_crm['len_email_crm'][len_min]} " \
                                     f"and {len_crm['len_email_crm'][len_max]}, " \
                                     f"\"@\" and \".\" required!!!"
                view.print_message()


def display_delete_crm(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering client ID to delete or write \"exit\" to go menu up:\033[0m")
        id_del = input("Entering client ID: ")
        if model.delete_crm(id_del):
            is_working = False
            view.clear_console()
            view.display_crm(model.crm, *_len_max_crm())
            view.error_message = f"The client with ID \"{id_del}\" has been deleted."
            view.print_message()
        else:
            break


def display_all_crm(model, view):
    if len(model.crm) > 0:
        view.clear_console()
        view.display_crm(model.crm, *_len_max_crm())
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_select_crm(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering client ID to display or write \"exit\" to go menu up:\033[0m")
        id_select = input("Entering client ID: ")
        if selected := model.select_crm(id_select):
            is_working = False
            view.clear_console()
            view.display_crm(selected, *_len_max_crm())
        else:
            break


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


# TODO delete
def _len_max_crm():
    len_max_list = []
    for key, value in len_crm.items():
        len_max_list.append(len_crm[key][1])
    return len_max_list
