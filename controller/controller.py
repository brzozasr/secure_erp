from model.model_dict.model_json import *
from view.view import *
import hashlib
from getpass import getpass


class Controller:
    len_crm = {"len_id_crm": (1, 6),
               "len_name_crm": (2, 20),
               "len_surname_crm": (2, 30),
               "len_company_crm": (2, 25),
               "len_email_crm": (6, 35)}

    len_hr = {"len_id_hr": (1, 6),
              "len_name_hr": (2, 20),
              "len_surname_hr": (2, 30),
              "len_birthday_hr": (10, 10),
              "len_department_hr": (2, 20),
              "len_email_hr": (6, 35),
              "len_password": (40, 40)}

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
            elif Controller.is_module_correct(module):
                if int(module) == 1:
                    self.view.clear_console()
                    self.display_crm()
                elif int(module) == 2:
                    pass
                elif int(module) == 3:
                    pass
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a module number!!!"
                self.view.print_message()

    def display_crm(self):
        while Controller.is_running:
            print("\033[36mThe CRM Module, to terminate write \"exit\":\033[0m")
            print("(1) Insert the client")
            print("(2) Update the client")
            print("(3) Delete the client")
            print("(4) Select the client by ID")
            print("(5) Show all clients")
            crm_action = input("Select action: ")

            if crm_action == "exit":
                Controller.is_running = False

    @classmethod
    def len_max_crm(cls):
        len_max = []
        for key, value in cls.len_crm.items():
            len_max.append(cls.len_crm[key][1])
        return len_max

    @classmethod
    def len_max_hr(cls):
        len_max = []
        for key, value in cls.len_hr.items():
            len_max.append(cls.len_hr[key][1])
        return len_max

    @staticmethod
    def is_module_correct(module_no):
        try:
            num = int(module_no)
            if num < 1 or num > 3:
                return False
        except ValueError:
            return False
        return True


if __name__ == "__main__":
    con = Controller(ModelJSON(), View())
    con.run_erp()

    # test = "12345678"
    # hash_object = hashlib.sha1(str(test).encode('utf-8'))
    # print('Hash', hash_object.hexdigest())



