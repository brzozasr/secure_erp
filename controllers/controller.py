from getpass import getpass

from controllers.crm_control import *
from controllers.hr_control import *
from controllers.prod_control import *
from controllers.sale_control import *
from models.model_dict.model_json import *
from views.view import *


class Controller:

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
                    self.view.clear_console()
                    self.display_module_sale()
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
                    display_insert_hr(self.model, self.view)
                elif int(hr_action) == 2:
                    self.view.clear_console()
                    display_update_hr(self.model, self.view)
                elif int(hr_action) == 3:
                    self.view.clear_console()
                    display_delete_hr(self.model, self.view)
                elif int(hr_action) == 4:
                    self.view.clear_console()
                    display_select_hr(self.model, self.view)
                elif int(hr_action) == 5:
                    self.view.clear_console()
                    display_all_hr(self.model, self.view)
                elif int(hr_action) == 6:
                    self.view.clear_console()
                    display_min_max_age_hr(self.model, self.view)
                elif int(hr_action) == 7:
                    self.view.clear_console()
                    display_average_age_hr(self.model, self.view)
                elif int(hr_action) == 8:
                    self.view.clear_console()
                    display_birthday_hr(self.model, self.view)
                elif int(hr_action) == 9:
                    self.view.clear_console()
                    display_employees_in_department_hr(self.model, self.view)
                elif int(hr_action) == 10:
                    self.view.clear_console()
                    break
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a HR module number!!!"
                self.view.print_message()

    def display_module_sale(self):
        while Controller.is_running:
            print("\033[36mThe SALE Module, to terminate write \"exit\":\033[0m")
            print("(1) Insert the product")
            print("(2) Update the product")
            print("(3) Delete the product")
            print("(4) Select the product by ID")
            print("(5) Show all products")
            print("-" * 57)
            print("(6) Insert the sale")
            print("(7) Update the sale")
            print("(8) Delete the sale")
            print("(9) Select the sale by ID")
            print("(10) Show all sale")
            print("-" * 57)
            print("(11) The transaction that made the biggest revenue")
            print("(12) The product that made the biggest revenue altogether")
            print("(13) Number of transactions between two dates")
            print("(14) Sum the price of transactions between two dates")
            print("-" * 57)
            print("(15) Go menu up")
            sale_action = input("Select action: ")

            if sale_action == "exit":
                Controller.is_running = False
            elif Controller._is_sale_correct(sale_action):
                if int(sale_action) == 1:
                    self.view.clear_console()
                    display_insert_product(self.model, self.view)
                elif int(sale_action) == 2:
                    self.view.clear_console()
                    display_update_product(self.model, self.view)
                elif int(sale_action) == 3:
                    self.view.clear_console()
                    display_delete_product(self.model, self.view)
                elif int(sale_action) == 4:
                    self.view.clear_console()
                    display_select_product(self.model, self.view)
                elif int(sale_action) == 5:
                    self.view.clear_console()
                    display_all_products(self.model, self.view)
                elif int(sale_action) == 6:
                    self.view.clear_console()
                    display_insert_sale(self.model, self.view)
                elif int(sale_action) == 7:
                    self.view.clear_console()
                    display_update_sale(self.model, self.view)
                elif int(sale_action) == 8:
                    self.view.clear_console()
                    display_delete_sale(self.model, self.view)
                elif int(sale_action) == 9:
                    self.view.clear_console()
                    display_select_sale(self.model, self.view)
                elif int(sale_action) == 10:
                    self.view.clear_console()
                    display_all_sales(self.model, self.view)
                elif int(sale_action) == 11:
                    self.view.clear_console()
                    display_get_transaction_biggest_revenue(self.model, self.view)
                elif int(sale_action) == 12:
                    self.view.clear_console()
                    display_get_product_biggest_revenue(self.model, self.view)
                elif int(sale_action) == 13:
                    self.view.clear_console()
                    # display_all_sales(self.model, self.view)
                elif int(sale_action) == 14:
                    self.view.clear_console()
                    # display_all_sales(self.model, self.view)
                elif int(sale_action) == 15:
                    self.view.clear_console()
                    break
            else:
                self.view.clear_console()
                self.view.error_message = "Invalid a SALE module number!!!"
                self.view.print_message()

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

    @staticmethod
    def _is_sale_correct(module_no):
        try:
            num = int(module_no)
            if num < 1 or num > 15:
                return False
        except ValueError:
            return False
        return True


if __name__ == "__main__":
    con = Controller(ModelJSON(), View())
    con.run_erp()
