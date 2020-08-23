import hashlib
from getpass import getpass

from controllers.crm_control import *
from models.model_dict.model_json import *
from views.view import *


class Controller:

    len_hr = {"len_id_hr": (1, 6),
              "len_name_hr": (2, 20),
              "len_surname_hr": (2, 30),
              "len_birthday_hr": (10, 10),
              "len_department_hr": (2, 20),
              "len_email_hr": (6, 35),
              "len_password_hr": (8, 40)}

    is_running = True

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run_erp(self):
        counter = 3
        while Controller.is_running:
            print(f"Login to the SECURE ERP, you have {counter} attempt(s).")
            login = input("Enter your an email as a username: ")
            password = getpass(prompt='Enter your password: ')
            hash_pass = hashlib.sha1(str(password).encode('utf-8'))
            password = hash_pass.hexdigest()
            username, pass_hr = self.model.login_hr(login)
            if counter >= 1 and login == username and password == pass_hr:
                counter = 3
                self.view.clear_console()
                self.display_modules()
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid username or password!!!"
                self.view.print_message()
                counter -= 1
                if counter < 1:
                    self.view.clear_console()
                    Controller.is_running = False

    def display_modules(self):
        while Controller.is_running:
            print("\033[36mSelect a module or write \"exit\" to terminate:\033[0m")
            print("(1) Customer Relationship Management - CRM")
            print("(2) Sales")
            print("(3) Human Resources - HR")
            module = input("Select a module: ")

            if module == "exit":
                Controller.is_running = False
            elif Controller._is_module_correct(module):
                if int(module) == 1:
                    self.view.clear_console()
                    self.display_module_crm()
                elif int(module) == 2:
                    pass
                elif int(module) == 3:
                    self.view.clear_console()
                    self.display_module_hr()
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a module number!!!"
                self.view.print_message()

    def display_module_crm(self):
        while Controller.is_running:
            print("\033[36mThe CRM Module, to terminate write \"exit\":\033[0m")
            print("(1) Insert the client")
            print("(2) Update the client")
            print("(3) Delete the client")
            print("(4) Select the client by ID")
            print("(5) Show all clients")
            print("(6) Go menu up")
            crm_action = input("Select action: ")

            if crm_action == "exit":
                Controller.is_running = False
            elif Controller._is_crm_correct(crm_action):
                if int(crm_action) == 1:
                    self.view.clear_console()
                    display_insert_crm(self.model, self.view)
                elif int(crm_action) == 2:
                    self.view.clear_console()
                    display_update_crm(self.model, self.view)
                elif int(crm_action) == 3:
                    self.view.clear_console()
                    display_delete_crm(self.model, self.view)
                elif int(crm_action) == 4:
                    self.view.clear_console()
                    display_select_crm(self.model, self.view)
                elif int(crm_action) == 5:
                    self.view.clear_console()
                    display_all_crm(self.model, self.view)
                elif int(crm_action) == 6:
                    self.view.clear_console()
                    break
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a CRM module number!!!"
                self.view.print_message()

    def display_module_hr(self):
        while Controller.is_running:
            print("\033[36mThe HR Module, to terminate write \"exit\":\033[0m")
            print("(1) Insert the employee")
            print("(2) Update the employee")
            print("(3) Delete the employee")
            print("(4) Select the employee by ID")
            print("(5) Show all employees")
            print("(6) Names of the youngest and the oldest employees")
            print("(7) The average age of employees")
            print("(8) Employees having birthdays within the two weeks")
            print("(9) The number of employees per department")
            print("(10) Go menu up")
            hr_action = input("Select action: ")

            if hr_action == "exit":
                Controller.is_running = False
            elif Controller._is_hr_correct(hr_action):
                if int(hr_action) == 1:
                    self.view.clear_console()
                    self.display_insert_hr()
                elif int(hr_action) == 2:
                    self.view.clear_console()
                    self.display_update_hr()
                elif int(hr_action) == 3:
                    self.view.clear_console()
                    self.display_delete_hr()
                elif int(hr_action) == 4:
                    self.view.clear_console()
                    self.display_select_hr()
                elif int(hr_action) == 5:
                    self.view.clear_console()
                    self.display_all_hr()
                elif int(hr_action) == 6:
                    self.view.clear_console()
                    self.display_min_max_age_hr()
                elif int(hr_action) == 7:
                    self.view.clear_console()
                    self.display_average_age_hr()
                elif int(hr_action) == 8:
                    self.view.clear_console()
                    self.display_birthday_hr()
                elif int(hr_action) == 9:
                    self.view.clear_console()
                    self.display_employees_in_department_hr()
                elif int(hr_action) == 10:
                    self.view.clear_console()
                    break
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a HR module number!!!"
                self.view.print_message()

    def display_insert_hr(self):
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
                elif self._is_len_correct(len(name), Controller.len_hr["len_name_hr"][0],
                                          Controller.len_hr["len_name_hr"][1]):
                    insert_data.append(name)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's name, the length should be " \
                                              f"between {Controller.len_hr['len_name_hr'][0]} " \
                                              f"and {Controller.len_hr['len_name_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                surname = input("Entering employee's surname: ")
                if surname == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(surname), Controller.len_hr["len_surname_hr"][0],
                                          Controller.len_hr["len_surname_hr"][1]):
                    insert_data.append(surname)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's surname, the length should be " \
                                              f"between {Controller.len_hr['len_surname_hr'][0]} " \
                                              f"and {Controller.len_hr['len_surname_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                birthday = input("Entering employee's birthday (e.g. 2001-11-29): ")
                if birthday == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(birthday), Controller.len_hr["len_birthday_hr"][0],
                                          Controller.len_hr["len_birthday_hr"][1]) \
                        and self._is_date_correct(birthday):
                    insert_data.append(birthday)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's birthday, the length should be " \
                                              f"between {Controller.len_hr['len_birthday_hr'][0]} " \
                                              f"and {Controller.len_hr['len_birthday_hr'][1]} and " \
                                              f"data format, should be YYYY-MM-DD!!!"
                    self.view.print_message()

            while is_inside_working:
                department = input("Entering employee's department: ")
                if department == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(department), Controller.len_hr["len_department_hr"][0],
                                          Controller.len_hr["len_department_hr"][1]):
                    insert_data.append(department)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's department, the length should be " \
                                              f"between {Controller.len_hr['len_department_hr'][0]} " \
                                              f"and {Controller.len_hr['len_department_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                email = input("Entering employee's email: ")
                if email == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(email), Controller.len_hr["len_email_hr"][0],
                                          Controller.len_hr["len_email_hr"][1]) \
                        and "@" in email and "." in email:
                    insert_data.append(email)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's email, the length should be " \
                                              f"between {Controller.len_hr['len_email_hr'][0]} " \
                                              f"and {Controller.len_hr['len_email_hr'][1]}, " \
                                              f"\"@\" and \".\" required!!!"
                    self.view.print_message()

            while is_inside_working:
                password = input("Entering employee's password: ")
                if password == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(password), Controller.len_hr["len_password_hr"][0],
                                          Controller.len_hr["len_password_hr"][1]):
                    hash_pass = hashlib.sha1(str(password).encode('utf-8'))
                    password = hash_pass.hexdigest()
                    insert_data.append(password)
                    if self.model.insert_hr(*insert_data):
                        insert_data.clear()
                        is_working = False
                        is_inside_working = False
                        self.view.clear_console()
                        new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                        self.view.display_hr(self.model.hr, *new_len)
                        self.view.error_message = "The employee has been added."
                        self.view.print_message()
                    else:
                        break
                else:
                    self.view.error_message = f"Invalid a employee's password, the length should be " \
                                              f"between {Controller.len_hr['len_password_hr'][0]} " \
                                              f"and {Controller.len_hr['len_password_hr'][1]}"
                    self.view.print_message()

    def display_update_hr(self):
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
                elif self._is_len_correct(len(employee_id), Controller.len_hr["len_id_hr"][0],
                                          Controller.len_hr["len_id_hr"][1]):
                    insert_data.append(employee_id)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's ID, the length should be " \
                                              f"between {Controller.len_hr['len_id_hr'][0]} " \
                                              f"and {Controller.len_hr['len_id_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                name = input("Entering employee's name: ")
                if name == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(name), Controller.len_hr["len_name_hr"][0],
                                          Controller.len_hr["len_name_hr"][1]):
                    insert_data.append(name)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's name, the length should be " \
                                              f"between {Controller.len_hr['len_name_hr'][0]} " \
                                              f"and {Controller.len_hr['len_name_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                surname = input("Entering employee's surname: ")
                if surname == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(surname), Controller.len_hr["len_surname_hr"][0],
                                          Controller.len_hr["len_surname_hr"][1]):
                    insert_data.append(surname)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's surname, the length should be " \
                                              f"between {Controller.len_hr['len_surname_hr'][0]} " \
                                              f"and {Controller.len_hr['len_surname_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                birthday = input("Entering employee's birthday (e.g. 2001-11-29): ")
                if birthday == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(birthday), Controller.len_hr["len_birthday_hr"][0],
                                          Controller.len_hr["len_birthday_hr"][1]) \
                        and self._is_date_correct(birthday):
                    insert_data.append(birthday)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's birthday, the length should be " \
                                              f"between {Controller.len_hr['len_birthday_hr'][0]} " \
                                              f"and {Controller.len_hr['len_birthday_hr'][1]} and " \
                                              f"data format, should be YYYY-MM-DD!!!"
                    self.view.print_message()

            while is_inside_working:
                department = input("Entering employee's department: ")
                if department == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(department), Controller.len_hr["len_department_hr"][0],
                                          Controller.len_hr["len_department_hr"][1]):
                    insert_data.append(department)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's department, the length should be " \
                                              f"between {Controller.len_hr['len_department_hr'][0]} " \
                                              f"and {Controller.len_hr['len_department_hr'][1]}!!!"
                    self.view.print_message()

            while is_inside_working:
                email = input("Entering employee's email: ")
                if email == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(email), Controller.len_hr["len_email_hr"][0],
                                          Controller.len_hr["len_email_hr"][1]) \
                        and "@" in email and "." in email:
                    insert_data.append(email)
                    break
                else:
                    self.view.error_message = f"Invalid a employee's email, the length should be " \
                                              f"between {Controller.len_hr['len_email_hr'][0]} " \
                                              f"and {Controller.len_hr['len_email_hr'][1]}, " \
                                              f"\"@\" and \".\" required!!!"
                    self.view.print_message()

            while is_inside_working:
                password = input("Entering employee's password: ")
                if password == "exit":
                    insert_data.clear()
                    is_working = False
                    is_inside_working = False
                elif self._is_len_correct(len(password), Controller.len_hr["len_password_hr"][0],
                                          Controller.len_hr["len_password_hr"][1]):
                    hash_pass = hashlib.sha1(str(password).encode('utf-8'))
                    password = hash_pass.hexdigest()
                    insert_data.append(password)
                    print(insert_data)
                    if self.model.update_hr(*insert_data):
                        insert_data.clear()
                        is_working = False
                        is_inside_working = False
                        self.view.clear_console()
                        new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                        self.view.display_hr(self.model.hr, *new_len)
                        self.view.error_message = "The employee has been updated."
                        self.view.print_message()
                    else:
                        break
                else:
                    self.view.error_message = f"Invalid a employee's password, the length should be " \
                                              f"between {Controller.len_hr['len_password_hr'][0]} " \
                                              f"and {Controller.len_hr['len_password_hr'][1]}"
                    self.view.print_message()

    def display_delete_hr(self):
        is_working = True
        while is_working:
            print("\033[36mEntering employee's ID to delete or write \"exit\" to go menu up:\033[0m")
            id_del = input("Entering employee ID: ")
            if self.model.delete_hr(id_del):
                is_working = False
                self.view.clear_console()
                new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                self.view.display_hr(self.model.hr, *new_len)
                self.view.error_message = f"The employee with ID \"{id_del}\" has been deleted."
                self.view.print_message()
            else:
                break

    def display_all_hr(self):
        if len(self.model.hr) > 1:
            self.view.clear_console()
            new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
            self.view.display_hr(self.model.hr, *new_len)
        else:
            self.view.error_message = "There is no data to display."
            self.view.print_message()

    def display_select_hr(self):
        is_working = True
        while is_working:
            print("\033[36mEntering employee ID to display or write \"exit\" to go menu up:\033[0m")
            id_select = input("Entering employee ID: ")
            if selected := self.model.select_hr(id_select):
                is_working = False
                self.view.clear_console()
                new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                self.view.display_hr(selected, *new_len)
            else:
                break

    def display_min_max_age_hr(self):
        if len(self.model.hr) > 0:
            self.view.clear_console()
            if min_max := self.model.min_max_age_hr():
                new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                self.view.display_hr(min_max, *new_len)
            else:
                self.view.error_message = "There is no data to display."
                self.view.print_message()

    def display_average_age_hr(self):
        if len(self.model.hr) > 0:
            self.view.clear_console()
            self.view.display_aver_age_hr(self.model.average_age_hr())
        else:
            self.view.error_message = "There is no data to display."
            self.view.print_message()

    def display_birthday_hr(self):
        if len(self.model.hr) > 1:
            self.view.clear_console()
            if birthday := self.model.birthday_within_two_weeks_hr():
                new_len = self.len_max_hr()[0:len(self.len_max_hr()) - 1]
                self.view.display_hr(birthday, *new_len)
            else:
                self.view.error_message = "No one has a birthday in the next two weeks."
                self.view.print_message()
        else:
            self.view.error_message = "There is no data to display."
            self.view.print_message()

    def display_employees_in_department_hr(self):
        if len(self.model.hr) > 1:
            self.view.clear_console()
            if employees := self.model.employees_in_department_hr():
                self.view.display_employees_by_department_hr(employees, Controller.len_hr['len_department_hr'][1])
        else:
            self.view.error_message = "There is no data to display."
            self.view.print_message()

    @classmethod
    def len_max_hr(cls):
        len_max_list = []
        for key, value in cls.len_hr.items():
            len_max_list.append(cls.len_hr[key][1])
        return len_max_list

    @staticmethod
    def _is_module_correct(module_no):
        try:
            num = int(module_no)
            if num < 1 or num > 3:
                return False
        except ValueError:
            return False
        return True

    @staticmethod
    def _is_crm_correct(module_no):
        try:
            num = int(module_no)
            if num < 1 or num > 6:
                return False
        except ValueError:
            return False
        return True

    @staticmethod
    def _is_hr_correct(module_no):
        try:
            num = int(module_no)
            if num < 1 or num > 10:
                return False
        except ValueError:
            return False
        return True

    # TODO delete
    @staticmethod
    def _is_len_correct(length, min_length, max_length):
        if min_length <= length <= max_length:
            return True
        else:
            return False

    @staticmethod
    def _is_date_correct(date_string):
        date_format = '%Y-%m-%d'
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    con = Controller(ModelJSON(), View())
    con.run_erp()
