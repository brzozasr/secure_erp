from model.model_dict.model_json import *
from view.view import *


class Controller:
    len_crm = {"len_id_crm": (1, 6),
               "len_name_crm": (2, 20),
               "len_surname_crm": (2, 30),
               "len_company_crm": (2, 25),
               "len_email_crm": (6, 35)}

    def __init__(self, model, view):
        self.model = model
        self.view = view

    @classmethod
    def len_max_crm(cls):
        len_max = []
        for key, value in cls.len_crm.items():
            len_max.append(cls.len_crm[key][1])
        return len_max


if __name__ == "__main__":
    con = Controller("test", "test1")
    print(con.len_max_crm())
