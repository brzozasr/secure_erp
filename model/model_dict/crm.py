from model.model_dict.id_store import *
from model.model_dict.id_enum import ID

# empty dictionary with CRM
crm = {}
current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "crm.json")


def _is_unique(unique_key, email):
    for id_key, value in crm.items():
        for key in value:
            if key == unique_key and email == value[key]:
                return False
    return True


def _is_crm_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _write_crm_to_file():
    global crm
    with open(json_file, "w") as write_file:
        json.dump(crm, write_file, indent=4)


def _set_crm_from_file():
    global crm
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            crm = json.load(read_json)
    else:
        _write_crm_to_file()


def delete_crm(id_crm):
    _set_crm_from_file()
    is_key = False
    for id_key in crm.keys():
        if id_key == str(id_crm):
            is_key = True
    if is_key:
        del crm[str(id_crm)]
        _write_crm_to_file()
        print('\033[31m', f"The record with the key \"{id_crm}\" was removed!", '\033[0m')
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
        return False


def select_crm(id_crm):
    _set_crm_from_file()
    is_key = False
    for id_key in crm.keys():
        if id_key == str(id_crm):
            is_key = True
    if is_key:
        return {str(id_crm): crm[str(id_crm)]}
    else:
        print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
        return None


def select_all_crm():
    _set_crm_from_file()
    if len(crm) > 0:
        return crm
    else:
        print('\033[31m', "There is no data to select in the database!", '\033[0m')
        return None


def insert_crm(*crm_value):
    """Required arguments for function:
    - "Name":         string,
    - "Surname":      string,
    - "Company name": string,
    - "Email":         string."""
    global crm
    _set_crm_from_file()
    key_list = ["name_crm", "surname_crm", "company_crm", "email_crm"]
    if len(crm_value) == 4:
        name, surname, company, email = crm_value
        min_len_name, max_len_name = (2, 20)
        min_len_surname, max_len_surname = (2, 30)
        min_len_company, max_len_company = (2, 20)
        min_len_email, max_len_email = (6, 35)
        if not _is_crm_len_correct(len(name), min_len_name, max_len_name):
            print('\033[31m',
                  f"The number of characters in a \"Name\" must be in the range "
                  f"of {min_len_name} to {max_len_name}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(surname), min_len_surname, max_len_surname):
            print('\033[31m',
                  f"The number of characters in a \"Surname\" must be in the range "
                  f"of {min_len_surname} to {max_len_surname}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(company), min_len_company, max_len_company):
            print('\033[31m',
                  f"The number of characters in a \"Company name\" must be in the "
                  f"range of {min_len_company} to {max_len_company}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(email), min_len_email, max_len_email) or \
                "@" not in email or "." not in email or not _is_unique("email_crm", email):
            print('\033[31m',
                  f"The number of characters in a \"Email\" must be in the range of "
                  f"{min_len_email} to {max_len_email}, has to consist \"@\" and \".\" and has to be unique!",
                  '\033[0m')
            return False
        else:
            id_crm = get_id(ID.CRM.value)
            crm[id_crm] = {}
            for k, v in zip(key_list, crm_value):
                crm[id_crm][k] = v
            _write_crm_to_file()
            return True
    else:
        print('\033[31m', "Missing argument(s)! There are 4 arguments is required!", '\033[0m')
        return False


def update_crm(*crm_value):
    """Required arguments for function:
    - "Id":           integer,
    - "Name":         string,
    - "Surname":      string,
    - "Company name": string,
    - "Email":        string."""
    global crm
    _set_crm_from_file()
    key_list = ["name_crm", "surname_crm", "company_crm", "email_crm"]
    if len(crm_value) == 5:
        id_crm, name, surname, company, email = crm_value
        min_len_name, max_len_name = (2, 20)
        min_len_surname, max_len_surname = (2, 30)
        min_len_company, max_len_company = (2, 20)
        min_len_email, max_len_email = (6, 35)
        if not _is_crm_len_correct(len(name), min_len_name, max_len_name):
            print('\033[31m',
                  f"The number of characters in a \"Name\" must be in the range "
                  f"of {min_len_name} to {max_len_name}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(surname), min_len_surname, max_len_surname):
            print('\033[31m',
                  f"The number of characters in a \"Surname\" must be in the range "
                  f"of {min_len_surname} to {max_len_surname}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(company), min_len_company, max_len_company):
            print('\033[31m',
                  f"The number of characters in a \"Company name\" must be in the "
                  f"range of {min_len_company} to {max_len_company}!",
                  '\033[0m')
            return False
        elif not _is_crm_len_correct(len(email), min_len_email, max_len_email) or \
                "@" not in email or "." not in email or not _is_unique("email_crm", email):
            print('\033[31m',
                  f"The number of characters in a \"Email\" must be in the range of "
                  f"{min_len_email} to {max_len_email}, has to consist \"@\" and \".\" and has to be unique!",
                  '\033[0m')
            return False
        else:
            is_key = False
            for id_key in crm.keys():
                if id_key == str(id_crm):
                    is_key = True
            if is_key:
                for k, v in zip(key_list, crm_value[1:]):
                    crm[str(id_crm)][k] = v
                _write_crm_to_file()
                return True
            else:
                print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
                return False
    else:
        print('\033[31m', "Missing argument(s)! There are 5 arguments is required!", '\033[0m')
        return False


if __name__ == "__main__":
    insert_crm("Jan", "Kowalski", "Somfy Sp. z o.o.", "dagmara@somfy.pl")
    insert_crm("Paweł", "Nowak", "Somfy Sp. z o.o.", "pawel@somfy.pl")
    # delete_crm(2)
    # print(select_crm(5))
    update_crm(1, "Sławomir", "Brzozowski", "DG RSZ", "brzozasr@interia.pl")
    update_crm(2, "Marcin", "Jurek", "DG RSZ - ORK", "m.jurek@gmail.com")
    print(select_all_crm())
