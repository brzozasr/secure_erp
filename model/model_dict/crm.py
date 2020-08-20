from model.model_dict.id_store import *
from model.model_dict.id_enum import ID

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "crm.json")


def _is_unique(crm_dict, unique_key, email):
    for id_key, value in crm_dict.items():
        for key in value:
            if key == unique_key and email == value[key]:
                return False
    return True


def _is_crm_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def write_crm_to_file(crm_dict):
    with open(json_file, "w") as write_file:
        json.dump(crm_dict, write_file, indent=4)


def set_crm_from_file():
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            return json.load(read_json)
    else:
        return {}


def delete_crm(id_crm, crm_dict):
    is_key = False
    for id_key in crm_dict.keys():
        if id_key == str(id_crm):
            is_key = True
    if is_key:
        del crm_dict[str(id_crm)]
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
        return False


def select_crm(id_crm, crm_dict):
    is_key = False
    for id_key in crm_dict.keys():
        if id_key == str(id_crm):
            is_key = True
    if is_key:
        return {str(id_crm): crm_dict[str(id_crm)]}
    else:
        print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
        return None


def insert_crm(crm_dict, *crm_value):
    """Required arguments for function:
    - "Name":         string,
    - "Surname":      string,
    - "Company name": string,
    - "Email":         string."""
    key_list = ["name_crm", "surname_crm", "company_crm", "email_crm"]
    if len(crm_value) == 4:
        name, surname, company, email = crm_value
        if not _is_unique(crm_dict, "email_crm", email):
            print('\033[31m', "The \"Email\" has to be unique!", '\033[0m')
            return False
        else:
            id_crm = str(get_id(ID.CRM.value))
            crm_dict[id_crm] = {}
            for k, v in zip(key_list, crm_value):
                crm_dict[id_crm][k] = v
            return True
    else:
        print('\033[31m', "Missing argument(s)! There are 4 arguments are required!", '\033[0m')
        return False


def update_crm(crm_dict, *crm_value):
    """Required arguments for function:
    - "Id":           integer,
    - "Name":         string,
    - "Surname":      string,
    - "Company name": string,
    - "Email":        string."""
    key_list = ["name_crm", "surname_crm", "company_crm", "email_crm"]
    if len(crm_value) == 5:
        id_crm, name, surname, company, email = crm_value
        if not _is_unique(crm_dict, "email_crm", email):
            print('\033[31m', f"The \"Email\" has to be unique!", '\033[0m')
            return False
        else:
            is_key = False
            for id_key in crm_dict.keys():
                if id_key == str(id_crm):
                    is_key = True
            if is_key:
                for k, v in zip(key_list, crm_value[1:]):
                    crm_dict[str(id_crm)][k] = v
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
    # print(select_all_crm())
