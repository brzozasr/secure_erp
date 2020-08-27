import os
import subprocess


class View:
    def __init__(self, error_message=None):
        self.__error_message = error_message

    @property
    def error_message(self):
        return self.__error_message

    @error_message.setter
    def error_message(self, value):
        self.__error_message = value

    def print_message(self):
        if self.__error_message is not None:
            print(f"\033[31m{self.__error_message}\033[0m")
            self.__error_message = None

    @staticmethod
    def display_crm(crm_dict, *len_crm_data):
        if len(crm_dict) > 0:
            len_id, len_name, len_surname, len_company, len_email = len_crm_data
            line = f"+{'-' * len_id}+{'-' * len_name}+{'-' * len_surname}+{'-' * len_company}+{'-' * len_email}+"
            title_line = f"|{'ID':^{len_id}}|{'Name':^{len_name}}|{'Surname':^{len_surname}}|" \
                         f"{'Company':^{len_company}}|{'Email':^{len_email}}|\n"
            header = line + "\n" + title_line + line + "\n"
            space = [len_name, len_surname, len_company, len_email]
            data_line = ""
            for id_customer, customer in crm_dict.items():
                counter = 0
                data_line += f"|{id_customer:>{len_id}}|"
                for key in customer:
                    if len(space) - 1 > counter:
                        data_line += f"{customer[key]:<{space[counter]}}|"
                    else:
                        data_line += f"{customer[key]:^{space[counter]}}|\n"
                    counter += 1
            print(header + data_line + line)

    @staticmethod
    def display_hr(hr_dict, *len_hr_data):
        if len(hr_dict) > 0:
            len_id, len_name, len_surname, len_birthday, len_department, len_email = len_hr_data
            line = f"+{'-' * len_id}+{'-' * len_name}+{'-' * len_surname}+{'-' * len_birthday}" \
                   f"+{'-' * len_department}+{'-' * len_email}+"
            title_line = f"|{'ID':^{len_id}}|{'Name':^{len_name}}|{'Surname':^{len_surname}}" \
                         f"|{'Birthday':^{len_birthday}}|{'Department':^{len_department}}" \
                         f"|{'Email':^{len_email}}|\n"
            header = line + "\n" + title_line + line + "\n"
            space = [len_name, len_surname, len_birthday, len_department, len_email, 0]
            data_line = ""
            for id_employee, employee in hr_dict.items():
                if int(id_employee) > 0:
                    counter = 0
                    data_line += f"|{id_employee:>{len_id}}|"
                    for key in employee:
                        if len(space) - 2 > counter:
                            data_line += f"{employee[key]:<{space[counter]}}|"
                        else:
                            if key != "password_hr":
                                data_line += f"{employee[key]:^{space[counter]}}|\n"
                        counter += 1
            print(header + data_line + line)

    @staticmethod
    def display_products(products_dict, *len_prod_data):
        if len(products_dict) > 0:
            len_id, len_name, len_price, len_quantity = len_prod_data
            line = f"+{'-' * len_id}+{'-' * len_name}+{'-' * len_price}+{'-' * len_quantity}+"
            title_line = f"|{'ID':^{len_id}}|{'Product':^{len_name}}|{'Price (zł)':^{len_price}}|" \
                         f"{'Quantity':^{len_quantity}}|\n"
            header = line + "\n" + title_line + line + "\n"
            space = [len_name, len_price, len_quantity]
            data_line = ""
            for id_product, product in products_dict.items():
                counter = 0
                data_line += f"|{id_product:>{len_id}}|"
                for key in product:
                    if key == 'name_prod':
                        data_line += f"{product[key]:<{space[counter]}}|"
                    elif key == 'price_prod':
                        data_line += f"{product[key]:>{space[counter]}}|"
                    elif key == 'quantity_prod':
                        data_line += f"{product[key]:>{space[counter]}}|\n"
                    counter += 1
            print(header + data_line + line)

    @staticmethod
    def display_aver_age_hr(aver_age):
        line = f"+{'-' * 38}+{'-' * 7}+"
        content = f"|{'Average age of employees (in years)':<38}|{aver_age:^7}|"
        print(line + "\n" + content + "\n" + line)

    @staticmethod
    def display_employees_by_department_hr(result_dict, len_department):
        line = f"+{'-' * len_department}+{'-' * 14}+"
        title = f"|{'Department':^{len_department}}|{'No employees':^14}|"
        header = line + "\n" + title + "\n" + line + "\n"
        content = ""
        for key, value in result_dict.items():
            content += f"|{key:<{len_department}}|{value:>14}|\n"
        print(header + content + line)

    @staticmethod
    def clear_console():
        """Function clears the console."""
        if os.name in ('nt', 'dos'):
            subprocess.call("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call("clear")
        else:
            print("\n" * 120)


if __name__ == "__main__":
    dict_test = {'1': {'name_crm': 'Sławomir', 'surname_crm': 'Brzozowski', 'company_crm': 'DG RSZ',
                       'email_crm': 'brzozasr@interia.pl'},
                 '2': {'name_crm': 'Marcin', 'surname_crm': 'Jurek', 'company_crm': 'DG RSZ - ORK',
                       'email_crm': 'm.jurek@gmail.com'},
                 '3': {'name_crm': 'Jan', 'surname_crm': 'Kowalski', 'company_crm': 'Somfy Sp. z o.o.',
                       'email_crm': 'dagmara@somfy.pl'},
                 '4': {'name_crm': 'Paweł', 'surname_crm': 'Nowak', 'company_crm': 'Somfy Sp. z o.o.',
                       'email_crm': 'pawel@somfy.pl'}}

    dict_hr = {"0": {"name_hr": "admin", "surname_hr": "admin", "birthday_hr": "1970-01-01",
                     "department_hr": "admin", "email_hr": "admin@secure.erp",
                     "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
               "1": {"name_hr": "Jan", "surname_hr": "Nowak", "birthday_hr": "1972-05-31",
                     "department_hr": "HR", "email_hr": "j.nowak@secure.erp",
                     "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"}
               }

    v = View()
    v.display_hr(dict_hr, *[6, 20, 30, 10, 20, 35])
