from model.model_dict.crm import *


class ModelJSON:
    def __init__(self):
        self.crm = None

    @staticmethod
    def delete_crm(id_crm):
        return delete_crm(id_crm)

    @staticmethod
    def select_crm(id_crm):
        return select_crm(id_crm)

    @staticmethod
    def select_all_crm():
        return select_all_crm()

    @staticmethod
    def insert_crm(*crm_value):
        return insert_crm(*crm_value)

    @staticmethod
    def update_crm(*crm_value):
        return update_crm(*crm_value)
