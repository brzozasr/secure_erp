from model.model_dict.id_store import *
from model.model_dict.id_enum import ID

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "hr.json")


def write_hr_to_file(hr_dict):
    with open(json_file, "w") as write_file:
        json.dump(hr_dict, write_file, indent=4)


def set_hr_from_file():
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            return json.load(read_json)
    else:
        return {"0": {"name_hr": "admin", "surname_hr": "admin", "birthday_hr": "1970-01-01", "department_hr": "admin",
                      "email_hr": "admin@secure.erp", "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"}}


def login_hr(dict_hr, email_hr):
    if len(dict_hr) > 0:
        for id_hr in dict_hr.keys():
            if dict_hr[id_hr]["email_hr"] == email_hr:
                return dict_hr[id_hr]["email_hr"], dict_hr[id_hr]["password_hr"]
        return None, None
    else:
        return None, None


def delete_hr(id_hr, hr_dict):
    is_key = False
    for id_key in hr_dict.keys():
        if id_key == str(id_hr):
            is_key = True
    if is_key:
        del hr_dict[str(id_hr)]
        print('\033[31m', f"The record with the key \"{id_hr}\" was removed!", '\033[0m')
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_hr}\" in the database!", '\033[0m')
        return False


def select_hr(id_hr, hr_dict):
    is_key = False
    for id_key in hr_dict.keys():
        if id_key == str(id_hr):
            is_key = True
    if is_key:
        return {str(id_hr): hr_dict[str(id_hr)]}
    else:
        print('\033[31m', f"There is no such key \"{id_hr}\" in the database!", '\033[0m')
        return None


def select_all_hr(hr_dict):
    if len(hr_dict) > 0:
        return hr_dict
    else:
        print('\033[31m', "There is no data to select in the database!", '\033[0m')
        return None


if __name__ == "__main__":
    test_dict = {"0": {"name_hr": "admin", "surname_hr": "admin", "birthday_hr": "1970-01-01", "department_hr": "admin",
                       "email_hr": "admin@secure.erp", "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"}}

    print(login_hr(test_dict, "admin@secure.erp"))
