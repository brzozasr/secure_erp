from datetime import datetime
import hashlib

len_hr = {"len_id_hr": (1, 6),
          "len_name_hr": (2, 20),
          "len_surname_hr": (2, 30),
          "len_birthday_hr": (10, 10),
          "len_department_hr": (2, 20),
          "len_email_hr": (6, 35),
          "len_password_hr": (8, 40)}

len_min = 0
len_max = 1


def display_insert_hr(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering employee data to insert or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            name = input("Entering employee's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_hr["len_name_hr"][len_min],
                                 len_hr["len_name_hr"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a employee's name, the length should be " \
                                     f"between {len_hr['len_name_hr'][len_min]} " \
                                     f"and {len_hr['len_name_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            surname = input("Entering employee's surname: ")
            if surname == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(surname), len_hr["len_surname_hr"][len_min],
                                 len_hr["len_surname_hr"][len_max]):
                insert_data.append(surname)
                break
            else:
                view.error_message = f"Invalid a employee's surname, the length should be " \
                                     f"between {len_hr['len_surname_hr'][len_min]} " \
                                     f"and {len_hr['len_surname_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            birthday = input("Entering employee's birthday (e.g. 2001-11-29): ")
            if birthday == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(birthday), len_hr["len_birthday_hr"][len_min],
                                 len_hr["len_birthday_hr"][len_max]) \
                    and _is_date_correct(birthday):
                insert_data.append(birthday)
                break
            else:
                view.error_message = f"Invalid a employee's birthday, the length should be " \
                                     f"between {len_hr['len_birthday_hr'][len_min]} " \
                                     f"and {len_hr['len_birthday_hr'][len_max]} and " \
                                     f"data format, should be YYYY-MM-DD!!!"
                view.print_message()

        while is_inside_working:
            department = input("Entering employee's department: ")
            if department == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(department), len_hr["len_department_hr"][len_min],
                                 len_hr["len_department_hr"][len_max]):
                insert_data.append(department)
                break
            else:
                view.error_message = f"Invalid a employee's department, the length should be " \
                                     f"between {len_hr['len_department_hr'][len_min]} " \
                                     f"and {len_hr['len_department_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            email = input("Entering employee's email: ")
            if email == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(email), len_hr["len_email_hr"][len_min],
                                 len_hr["len_email_hr"][len_max]) \
                    and "@" in email and "." in email:
                insert_data.append(email)
                break
            else:
                view.error_message = f"Invalid a employee's email, the length should be " \
                                     f"between {len_hr['len_email_hr'][len_min]} " \
                                     f"and {len_hr['len_email_hr'][len_max]}, " \
                                     f"\"@\" and \".\" required!!!"
                view.print_message()

        while is_inside_working:
            password = input("Entering employee's password: ")
            if password == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(password), len_hr["len_password_hr"][len_min],
                                 len_hr["len_password_hr"][len_max]):
                hash_pass = hashlib.sha1(str(password).encode('utf-8'))
                password = hash_pass.hexdigest()
                insert_data.append(password)
                if model.insert_hr(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
                    view.display_hr(model.hr, *new_len)
                    view.error_message = "The employee has been added."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a employee's password, the length should be " \
                                     f"between {len_hr['len_password_hr'][len_min]} " \
                                     f"and {len_hr['len_password_hr'][len_max]}"
                view.print_message()


def display_update_hr(model, view):
    is_working = True
    insert_data = []
    while is_working:
        print("\033[36mEntering employee data to update or write \"exit\" to go menu up:\033[0m")
        is_inside_working = True
        while is_inside_working:
            employee_id = input("Entering employee's ID: ")
            if employee_id == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(employee_id), len_hr["len_id_hr"][len_min],
                                 len_hr["len_id_hr"][len_max]):
                insert_data.append(employee_id)
                break
            else:
                view.error_message = f"Invalid a employee's ID, the length should be " \
                                     f"between {len_hr['len_id_hr'][len_min]} " \
                                     f"and {len_hr['len_id_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            name = input("Entering employee's name: ")
            if name == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(name), len_hr["len_name_hr"][len_min],
                                 len_hr["len_name_hr"][len_max]):
                insert_data.append(name)
                break
            else:
                view.error_message = f"Invalid a employee's name, the length should be " \
                                     f"between {len_hr['len_name_hr'][len_min]} " \
                                     f"and {len_hr['len_name_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            surname = input("Entering employee's surname: ")
            if surname == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(surname), len_hr["len_surname_hr"][len_min],
                                 len_hr["len_surname_hr"][len_max]):
                insert_data.append(surname)
                break
            else:
                view.error_message = f"Invalid a employee's surname, the length should be " \
                                     f"between {len_hr['len_surname_hr'][len_min]} " \
                                     f"and {len_hr['len_surname_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            birthday = input("Entering employee's birthday (e.g. 2001-11-29): ")
            if birthday == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(birthday), len_hr["len_birthday_hr"][len_min],
                                 len_hr["len_birthday_hr"][len_max]) \
                    and _is_date_correct(birthday):
                insert_data.append(birthday)
                break
            else:
                view.error_message = f"Invalid a employee's birthday, the length should be " \
                                     f"between {len_hr['len_birthday_hr'][len_min]} " \
                                     f"and {len_hr['len_birthday_hr'][len_max]} and " \
                                     f"data format, should be YYYY-MM-DD!!!"
                view.print_message()

        while is_inside_working:
            department = input("Entering employee's department: ")
            if department == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(department), len_hr["len_department_hr"][len_min],
                                 len_hr["len_department_hr"][len_max]):
                insert_data.append(department)
                break
            else:
                view.error_message = f"Invalid a employee's department, the length should be " \
                                     f"between {len_hr['len_department_hr'][len_min]} " \
                                     f"and {len_hr['len_department_hr'][len_max]}!!!"
                view.print_message()

        while is_inside_working:
            email = input("Entering employee's email: ")
            if email == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(email), len_hr["len_email_hr"][len_min],
                                 len_hr["len_email_hr"][len_max]) \
                    and "@" in email and "." in email:
                insert_data.append(email)
                break
            else:
                view.error_message = f"Invalid a employee's email, the length should be " \
                                     f"between {len_hr['len_email_hr'][len_min]} " \
                                     f"and {len_hr['len_email_hr'][len_max]}, " \
                                     f"\"@\" and \".\" required!!!"
                view.print_message()

        while is_inside_working:
            password = input("Entering employee's password: ")
            if password == "exit":
                insert_data.clear()
                is_working = False
                is_inside_working = False
            elif _is_len_correct(len(password), len_hr["len_password_hr"][len_min],
                                 len_hr["len_password_hr"][len_max]):
                hash_pass = hashlib.sha1(str(password).encode('utf-8'))
                password = hash_pass.hexdigest()
                insert_data.append(password)
                if model.update_hr(*insert_data):
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                    view.clear_console()
                    new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
                    view.display_hr(model.hr, *new_len)
                    view.error_message = "The employee has been updated."
                    view.print_message()
                else:
                    insert_data.clear()
                    break
            else:
                view.error_message = f"Invalid a employee's password, the length should be " \
                                     f"between {len_hr['len_password_hr'][len_min]} " \
                                     f"and {len_hr['len_password_hr'][len_max]}"
                view.print_message()


def display_delete_hr(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering employee's ID to delete or write \"exit\" to go menu up:\033[0m")
        id_del = input("Entering employee ID: ")
        if model.delete_hr(id_del):
            is_working = False
            view.clear_console()
            new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
            view.display_hr(model.hr, *new_len)
            view.error_message = f"The employee with ID \"{id_del}\" has been deleted."
            view.print_message()
        else:
            break


def display_all_hr(model, view):
    if len(model.hr) > 1:
        view.clear_console()
        new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
        view.display_hr(model.hr, *new_len)
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_select_hr(model, view):
    is_working = True
    while is_working:
        print("\033[36mEntering employee ID to display or write \"exit\" to go menu up:\033[0m")
        id_select = input("Entering employee ID: ")
        if selected := model.select_hr(id_select):
            is_working = False
            view.clear_console()
            new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
            view.display_hr(selected, *new_len)
        else:
            break


def display_min_max_age_hr(model, view):
    if len(model.hr) > 0:
        view.clear_console()
        if min_max := model.min_max_age_hr():
            new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
            view.display_hr(min_max, *new_len)
        else:
            view.error_message = "There is no data to display."
            view.print_message()


def display_average_age_hr(model, view):
    if len(model.hr) > 1:
        view.clear_console()
        view.display_aver_age_hr(model.average_age_hr())
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_birthday_hr(model, view):
    if len(model.hr) > 1:
        view.clear_console()
        if birthday := model.birthday_within_two_weeks_hr():
            new_len = _len_max_hr()[0:len(_len_max_hr()) - 1]
            view.display_hr(birthday, *new_len)
        else:
            view.error_message = "No one has a birthday in the next two weeks."
            view.print_message()
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def display_employees_in_department_hr(model, view):
    if len(model.hr) > 1:
        view.clear_console()
        if employees := model.employees_in_department_hr():
            view.display_employees_by_department_hr(employees, len_hr['len_department_hr'][len_max])
    else:
        view.error_message = "There is no data to display."
        view.print_message()


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _len_max_hr():
    len_max_list = []
    for key, value in len_hr.items():
        len_max_list.append(len_hr[key][len_max])
    return len_max_list


def _is_date_correct(date_string):
    date_format = '%Y-%m-%d'
    try:
        _ = datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False
