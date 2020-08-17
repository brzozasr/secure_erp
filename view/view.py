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
            # [5, 20, 30, 25, 35]
            len_id, len_name, len_surname, len_company, len_email = len_crm_data
            line = f"+{'-' * len_id}+{'-' * len_name}+{'-' * len_surname}+{'-' * len_company}+{'-' * len_email}+"
            title_line = f"|{'ID':^{len_id}}|{'Name':^{len_name}}|{'Surname':^{len_surname}}|{'Company':^{len_company}}|{'Email':^{len_email}}|\n"
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

    v = View()
    v.display_crm(dict_test)
