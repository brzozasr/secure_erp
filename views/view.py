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
        sum_employees = 0
        for key, value in result_dict.items():
            content += f"|{key:<{len_department}}|{value:>14}|\n"
            sum_employees += value
        footer = f"|{'TOTAL:':<{len_department}}|{sum_employees:>14}|\n"
        print(header + content + line + "\n" + footer + line)

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
                        data_line += f"{product[key]:>{space[counter]}.2f}|"
                    elif key == 'quantity_prod':
                        data_line += f"{product[key]:>{space[counter]}}|\n"
                    counter += 1
            print(header + data_line + line)

    @staticmethod
    def display_sale(sale_dict, *len_sale_data):
        if len(sale_dict) > 0:
            len_id_sale, len_name_crm, len_surname_crm, len_company_crm, len_name_prod, len_quantity_sale, len_date_sale = len_sale_data
            len_client_name = len_name_crm + len_surname_crm + 1
            line = f"+{'-' * len_id_sale}+{'-' * len_client_name}+{'-' * len_company_crm}+" \
                   f"{'-' * len_name_prod}+{'-' * len_quantity_sale}+{'-' * len_date_sale}+"
            title_line = f"|{'ID':^{len_id_sale}}|{'Client Name':^{len_client_name}}|" \
                         f"{'Company':^{len_company_crm}}|{'Product':^{len_name_prod}}|" \
                         f"{'Quantity':^{len_quantity_sale}}|{'Date':^{len_date_sale}}|\n"
            header = line + "\n" + title_line + line + "\n"
            data_line = ""
            for key_sale, value_sale in sale_dict.items():
                data_line += f"|{key_sale:>{len_id_sale}}|"
                for key, value in value_sale.items():
                    if key == 'id_crm_sale':
                        fullname = f"{value_sale[key][0]} {value_sale[key][1]}"
                        data_line += f"{fullname:<{len_client_name}}|{value_sale[key][2]:^{len_company_crm}}|"
                    elif key == "id_prod_sale":
                        data_line += f"{value_sale[key][0]:^{len_name_prod}}|"
                    elif key == "quantity_sale":
                        data_line += f"{value_sale[key]:>{len_quantity_sale}}|"
                    elif key == "date_sale":
                        data_line += f"{value_sale[key]:^{len_date_sale}}|\n"
            print(header + data_line + line)

    @staticmethod
    def display_clients_help(crm_dict):
        if len(crm_dict) > 0:
            clients_list = ""
            for key_crm, value_crm in crm_dict.items():
                clients_list += f"({key_crm}) "
                for key, value in value_crm.items():
                    if key == 'name_crm':
                        clients_list += f"{value_crm[key]} "
                    elif key == 'surname_crm':
                        clients_list += f"{value_crm[key]} "
                    elif key == 'company_crm':
                        clients_list += f"- {value_crm[key]}\n"
            print(f"\033[35m{clients_list}\033[0m", end='')

    @staticmethod
    def display_products_help(prod_dict):
        if len(prod_dict) > 0:
            prod_list = ""
            for key_prod, value_prod in prod_dict.items():
                prod_list += f"({key_prod}) "
                for key, value in value_prod.items():
                    if key == 'name_prod':
                        prod_list += f"{value_prod[key]}\n"
            print(f"\033[35m{prod_list}\033[0m", end='')

    @staticmethod
    def display_sale_help(sale_dict, crm_dict, prod_dict):
        if len(sale_dict) > 0:
            sale_list = ""
            for key_sale, value_sale in sale_dict.items():
                sale_list += f"({key_sale}) "
                for key, value in value_sale.items():
                    if key == 'id_crm_sale':
                        sale_list += f"{crm_dict[value]['name_crm']} {crm_dict[value]['surname_crm']}, " \
                                     f"{crm_dict[value]['company_crm']} "
                    elif key == 'id_prod_sale':
                        sale_list += f"- {prod_dict[value]['name_prod']} "
                    elif key == 'quantity_sale':
                        sale_list += f"- {sale_dict[key_sale]['quantity_sale']} pcs\n"
            print(f"\033[35m{sale_list}\033[0m", end='')

    @staticmethod
    def display_product_biggest_revenue(prod_data):
        if prod_data is not None:
            prod_name, prod_revenue = prod_data
            prod_revenue = f"{prod_revenue:,.2f}"
            prod_revenue = prod_revenue.replace(',', ' ')
            col_first, col_second = (50, 22)
            line = f'+{"-" * col_first}+{"-" * col_second}+'
            title_line = f'|{"Product made the biggest revenue":^{col_first}}|{"Revenue":^{col_second}}|\n'
            header = line + "\n" + title_line + line + "\n"
            content = f'|{prod_name:<{col_first}}|{prod_revenue:^{col_second}}|\n'
            print(header + content + line)

    @staticmethod
    def display_no_transactions_between_dates(no, dates):
        start_date, end_date = dates
        line = f"+{'-' * 58}+{'-' * 10}+"
        txt = f'Number of transactions between {start_date} and {end_date}'
        content = f"|{txt:<58}|{no:^10}|\n"
        print(line + "\n" + content + line)

    @staticmethod
    def display_sum_price_transactions_between_dates(sum_trans, dates):
        start_date, end_date = dates
        line = f"+{'-' * 65}+{'-' * 22}+"
        txt = f'Sum the price of transactions between {start_date} and {end_date}'
        sum_trans = f"{sum_trans:,.2f}"
        sum_trans = sum_trans.replace(',', ' ')
        content = f"|{txt:<65}|{sum_trans:^22}|\n"
        print(line + "\n" + content + line)

    @staticmethod
    def clear_console():
        """Function clears the console."""
        if os.name in ('nt', 'dos'):
            subprocess.call("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call("clear")
        else:
            print("\n" * 120)
