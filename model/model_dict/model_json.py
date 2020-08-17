from model.model_dict.crm import *
from model.model_dict.hr import *


class ModelJSON:
    def __init__(self):
        self.crm = set_crm_from_file()
        self.hr = set_hr_from_file()

    # CRM MODEL
    def delete_crm(self, id_crm):
        result = delete_crm(id_crm, self.crm)
        if result:
            self.write_crm()
        return result

    def select_crm(self, id_crm):
        result = select_crm(id_crm, self.crm)
        if result is not None:
            self.write_crm()
        return result

    def select_all_crm(self):
        result = select_all_crm(self.crm)
        if result is not None:
            self.write_crm()
        return result

    def insert_crm(self, *crm_value):
        result = insert_crm(self.crm, *crm_value)
        if result:
            self.write_crm()
        return result

    def update_crm(self, *crm_value):
        result = update_crm(self.crm, *crm_value)
        if result:
            self.write_crm()
        return result

    def write_crm(self):
        write_crm_to_file(self.crm)

    # HR MODEL
    def login_hr(self, email_hr):
        username, password = login_hr(self.hr, email_hr)
        if username is not None:
            self.write_hr()
        return username, password

    def delete_hr(self, id_hr):
        result = delete_hr(id_hr, self.hr)
        if result:
            self.write_hr()
        return result

    def write_hr(self):
        write_hr_to_file(self.hr)


if __name__ == "__main__":
    m = ModelJSON()
    m.insert_crm("Jan", "Kowalski", "Somfy Sp. z o.o.", "dagmara@somfy.pl")
    m.insert_crm("Paweł", "Nowak", "Somfy Sp. z o.o.", "pawel@somfy.pl")
    m.update_crm(1, "Sławomir", "Brzozowski", "DG RSZ", "brzozasr@interia.pl")
    m.update_crm(2, "Marcin", "Jurek", "DG RSZ - ORK", "m.jurek@gmail.com")
    # m.delete_crm(2)
