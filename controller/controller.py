from model.model_dict.model_json import *
from view.view import *


class Controller:
    len_crm = {"len_id_crm": (1, 6),
               "len_name_crm": (2, 20),
               "len_surname_crm": (2, 30),
               "len_company_crm": (2, 25),
               "len_email_crm": (6, 35)}

    len_hr = {"len_id_hr": (1, 6),
              "len_name_hr": (2, 20),
              "len_surname_hr": (2, 30),
              "len_birthday_hr": (10, 10),
              "len_department_hr": (2, 20),
              "len_email_hr": (6, 35),
              "len_password": (40, 40)}

    def __init__(self, model, view):
        self.model = model
        self.view = view

    @classmethod
    def len_max_crm(cls):
        len_max = []
        for key, value in cls.len_crm.items():
            len_max.append(cls.len_crm[key][1])
        return len_max

    @classmethod
    def len_max_hr(cls):
        len_max = []
        for key, value in cls.len_hr.items():
            len_max.append(cls.len_hr[key][1])
        return len_max


if __name__ == "__main__":
    con = Controller("test", "test1")
    print(con.len_max_crm())
    print(con.len_max_hr())

    # import hashlib
    #
    # hash_object = hashlib.sha1(b'Hello World')
    # hex_dig = hash_object.hexdigest()
    # print(hex_dig)
