from model.model_dict.id_store import *
from model.model_dict.id_enum import ID
from datetime import datetime, timedelta

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "hr.json")


def _is_unique(hr_dict, unique_key, email):
    for id_key, value in hr_dict.items():
        for key in value:
            if key == unique_key and email == value[key]:
                return False
    return True


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


def insert_hr(hr_dict, *hr_value):
    """Required arguments for function:
    - "Name":         string,
    - "Surname":      string,
    - "Birthday":     string,
    - "Department":   string,
    - "Email":        string,
    - "Password":     string."""
    key_list = ["name_hr", "surname_hr", "birthday_hr", "department_hr", "email_hr", "password_hr"]
    if len(hr_value) == 6:
        name, surname, birthday, department, email, password = hr_value
        if not _is_unique(hr_dict, "email_hr", email):
            print('\033[31m', "The \"Email\" has to be unique!", '\033[0m')
            return False
        else:
            id_hr = str(get_id(ID.HR.value))
            hr_dict[id_hr] = {}
            for k, v in zip(key_list, hr_value):
                hr_dict[id_hr][k] = v
            return True
    else:
        print('\033[31m', "Missing argument(s)! There are 6 arguments are required!", '\033[0m')
        return False


def update_hr(hr_dict, *hr_value):
    """Required arguments for function:
    - "Id":           string,
    - "Name":         string,
    - "Surname":      string,
    - "Birthday":     string,
    - "Department":   string,
    - "Email":        string,
    - "Password":     string."""
    key_list = ["name_hr", "surname_hr", "birthday_hr", "department_hr", "email_hr", "password_hr"]
    if len(hr_value) == 7:
        id_hr, name, surname, birthday, department, email, password = hr_value
        if not _is_unique(hr_dict, "email_hr", email):
            print('\033[31m', f"The \"Email\" has to be unique!", '\033[0m')
            return False
        else:
            is_key = False
            for id_key in hr_dict.keys():
                if id_key == str(id_hr):
                    is_key = True
            if is_key:
                for k, v in zip(key_list, hr_value[1:]):
                    hr_dict[str(id_hr)][k] = v
                return True
            else:
                print('\033[31m', f"There is no such key \"{id_hr}\" in the database!", '\033[0m')
                return False
    else:
        print('\033[31m', "Missing argument(s)! There are 7 arguments is required!", '\033[0m')
        return False


def min_max_employees_age(hr_dict):
    max_dict = {}
    min_dict = {}
    date_max = '1000-01-01'
    date_min = '4000-01-01'
    for id_key, value in hr_dict.items():
        if id_key != "0":
            for key in value:
                if key == "birthday_hr":
                    d_max_1 = datetime(*map(int, date_max.split('-')))
                    d_max_2 = datetime(*map(int, value['birthday_hr'].split('-')))
                    if d_max_1 < d_max_2:
                        max_dict.clear()
                        max_dict.update({id_key: value})
                        date_max = str(d_max_2)[0:10]
                    elif d_max_1 == d_max_2:
                        max_dict.update({id_key: value})

                    d_min_1 = datetime(*map(int, date_min.split('-')))
                    d_min_2 = datetime(*map(int, value['birthday_hr'].split('-')))
                    if d_min_1 > d_min_2:
                        min_dict.clear()
                        min_dict.update({id_key: value})
                        date_min = str(d_min_2)[0:10]
                    elif d_min_1 == d_min_2:
                        max_dict.update({id_key: value})
    return {**max_dict, **min_dict}


def average_age_employees(hr_dict):
    sum_age = 0
    for id_key, value in hr_dict.items():
        if id_key != "0":
            for key in value:
                if key == "birthday_hr":
                    sum_age += (datetime.now() - datetime(*map(int, value['birthday_hr'].split('-')))).days
    if sum_age > 0:
        return round((sum_age / 365) / len(hr_dict), 2)
    else:
        return sum_age


def birthday_into_two_weeks(hr_dict):
    current_year = datetime.today().year
    birthday_dict = {}
    for id_key, value in hr_dict.items():
        if id_key != "0":
            for key in value:
                if key == "birthday_hr":
                    year, month, day = value['birthday_hr'].split('-')
                    birthday = datetime(current_year, int(month), int(day))
                    new_today = datetime(datetime.today().year, datetime.today().month, datetime.today().day)
                    two_weeks = new_today + timedelta(days=14)
                    if new_today <= birthday < two_weeks:
                        birthday_dict.update({id_key: value})
    if len(birthday_dict) > 0:
        return birthday_dict
    else:
        return {}


def employees_by_department(hr_dict):
    if len(hr_dict) > 1:
        department_set = set()
        department_dict = {}
        for id_key, value in hr_dict.items():
            if id_key != "0":
                department_set.add(value['department_hr'])

        for department in department_set:
            for v in hr_dict.values():
                print(f"{department} == {v['department_hr']} ")
                if department in department_dict and department == v['department_hr']:
                    department_dict[department] += 1
                elif department == v['department_hr']:
                    department_dict[department] = 1

        return department_dict
    else:
        return {}


if __name__ == "__main__":
    test_dict = {"0": {"name_hr": "admin", "surname_hr": "admin", "birthday_hr": "1970-01-01", "department_hr": "admin",
                       "email_hr": "admin@secure.erp", "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "2": {"name_hr": "Stefan", "surname_hr": "Siw\u0105cha", "birthday_hr": "1972-05-31",
                       "department_hr": "Sale", "email_hr": "s.siwacha@secure.erp",
                       "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "4": {"name_hr": "Andrzej", "surname_hr": "Weso\u0142owski", "birthday_hr": "2002-10-01",
                       "department_hr": "Sale", "email_hr": "a.wesolowski@secure.erp",
                       "password_hr": "a7d579ba76398070eae654c30ff153a4c273272a"},
                 "5": {"name_hr": "Piotr", "surname_hr": "Chi\u0142\u0142a", "birthday_hr": "2000-12-12",
                       "department_hr": "HR", "email_hr": "p.chilla@secure.erp",
                       "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "7": {"name_hr": "Marian", "surname_hr": "Stan", "birthday_hr": "2002-10-01",
                       "department_hr": "Sale", "email_hr": "m.stan@secure.erp",
                       "password_hr": "a7d579ba76398070eae654c30ff153a4c273272a"},
                 "8": {"name_hr": "Wiktor", "surname_hr": "Kotlarz", "birthday_hr": "1990-02-10",
                       "department_hr": "Accountant", "email_hr": "w.kotlarz@secure.erp",
                       "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "9": {"name_hr": "Halina", "surname_hr": "Rycerz", "birthday_hr": "1972-05-31",
                       "department_hr": "Accountant", "email_hr": "h.rycerz@secure.erp",
                       "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "10": {"name_hr": "Laura", "surname_hr": "Brzoza", "birthday_hr": "1989-05-10",
                        "department_hr": "Accountant", "email_hr": "l.brzoza@secure.erp",
                        "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "11": {"name_hr": "Mateusz", "surname_hr": "Morgan", "birthday_hr": "1989-08-22",
                        "department_hr": "Accountant", "email_hr": "m.morgan@secure.erp",
                        "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"},
                 "12": {"name_hr": "Janusz", "surname_hr": "Biznesu", "birthday_hr": "1989-09-04",
                        "department_hr": "Accountant", "email_hr": "j.biznesu@secure.erp",
                        "password_hr": "7c222fb2927d828af22f592134e8932480637c0d"}}

    test_dict1 = {}

    print(employees_by_department(test_dict))
