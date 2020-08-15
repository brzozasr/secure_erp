class View:
    @staticmethod
    def display_crm(crm):
        if len(crm) > 0:
            len_id = 5
            len_name = 20
            len_surname = 30
            len_company = 25
            len_email = 35
            line = f"+{'-' * len_id}+{'-' * len_name}+{'-' * len_surname}+{'-' * len_company}+{'-' * len_email}+"
            title_line = f"|{'ID':^{len_id}}|{'Name':^{len_name}}|{'Surname':^{len_surname}}|{'Company':^{len_company}}|{'Email':^{len_email}}|\n"
            header = line + "\n" + title_line + line + "\n"
            space = [len_name, len_surname, len_company, len_email]
            data_line = ""
            for id_customer, customer in crm.items():
                counter = 0
                data_line += f"|{id_customer:>{len_id}}|"
                for key in customer:
                    if len(space) - 1 > counter:
                        data_line += f"{customer[key]:<{space[counter]}}|"
                    else:
                        data_line += f"{customer[key]:^{space[counter]}}|\n"
                    counter += 1
            print(header + data_line + line)


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