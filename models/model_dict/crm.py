from models.model_dict.id_store import *
from models.model_dict.id_enum import ID

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "crm.json")


def _is_unique(crm_dict, unique_key, email):
    for id_key, value in crm_dict.items():
        for key in value:
            if key == unique_key and email == value[key]:
                return False
    return True


def write_crm_to_file(crm_dict):
    with open(json_file, "w") as write_file:
        json.dump(crm_dict, write_file, indent=4)


def set_crm_from_file():
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            return json.load(read_json)
    else:
        return {}


def delete_crm(id_crm, crm_dict, sale_dict):
    if _is_id_crm_in_sale(id_crm, sale_dict):
        print('\033[31m', f"The client with ID {id_crm} cannot be deleted because it is used in sale!", '\033[0m')
        return False
    elif id_crm in crm_dict:
        del crm_dict[str(id_crm)]
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_crm}\" in the database!", '\033[0m')
        return False


def select_crm(id_crm, crm_dict):
    if id_crm in crm_dict:
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
        print('\033[31m', "Missing argument(s)! 4 arguments are required!", '\033[0m')
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
        print('\033[31m', "Missing argument(s)! 5 arguments are required!", '\033[0m')
        return False


def _is_id_crm_in_sale(id_crm, sale_dict):
    for value_sale in sale_dict.values():
        if value_sale['id_crm_sale'] == id_crm:
            return True
    return False

