from models.model_dict.crm import *
from models.model_dict.hr import *
from models.model_dict.products import *
from models.model_dict.sale import *


class ModelJSON:
    def __init__(self):
        self.crm = set_crm_from_file()
        self.hr = set_hr_from_file()
        self.products = set_products_from_file()
        self.sale = set_sale_from_file()

    # CRM MODEL
    def delete_crm(self, id_crm):
        result = delete_crm(id_crm, self.crm, self.sale)
        if result:
            self.write_crm()
        return result

    def select_crm(self, id_crm):
        result = select_crm(id_crm, self.crm)
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

    def select_hr(self, id_hr):
        result = select_hr(id_hr, self.hr)
        if result is not None:
            self.write_hr()
        return result

    def insert_hr(self, *hr_value):
        result = insert_hr(self.hr, *hr_value)
        if result:
            self.write_hr()
        return result

    def update_hr(self, *hr_value):
        result = update_hr(self.hr, *hr_value)
        if result:
            self.write_hr()
        return result

    def min_max_age_hr(self):
        result = min_max_employees_age(self.hr)
        if len(result) > 0:
            self.write_hr()
        return result

    def average_age_hr(self):
        result = average_age_employees(self.hr)
        if result > 0:
            self.write_hr()
        return result

    def birthday_within_two_weeks_hr(self):
        result = birthday_into_two_weeks(self.hr)
        if len(result) > 0:
            self.write_hr()
        return result

    def employees_in_department_hr(self):
        result = employees_by_department(self.hr)
        if len(result) > 0:
            self.write_hr()
        return result

    def write_hr(self):
        write_hr_to_file(self.hr)

    # PRODUCTS MODEL
    def delete_product(self, id_prod):
        result = delete_product(id_prod, self.products, self.sale)
        if result:
            self.write_products()
        return result

    def select_product(self, id_prod):
        result = select_product(id_prod, self.products)
        if result is not None:
            self.write_products()
        return result

    def insert_product(self, *prod_value):
        result = insert_product(self.products, *prod_value)
        if result:
            self.write_products()
        return result

    def update_product(self, *prod_value):
        result = update_product(self.products, *prod_value)
        if result:
            self.write_products()
        return result

    def write_products(self):
        write_products_to_file(self.products)

    # SALE MODEL
    def delete_sale(self, id_sale):
        result = delete_sale(id_sale, self.sale, self.products)
        if result:
            self.write_sale()
            self.write_products()
        return result

    def select_sale(self, id_sale):
        result = select_sale(id_sale, self.sale)
        if result is not None:
            self.write_sale()
        return result

    def insert_sale(self, *sale_value):
        result = insert_sale(self.crm, self.products, self.sale, *sale_value)
        if result:
            self.write_sale()
            self.write_products()
        return result

    def update_sale(self, *sale_value):
        result = update_sale(self.crm, self.products, self.sale, *sale_value)
        if result:
            self.write_sale()
            self.write_products()
        return result

    def show_data_sale(self, sale_dict):
        return select_data_to_show_sale(self.crm, self.products, sale_dict)

    def get_transaction_biggest_revenue(self):
        return transaction_biggest_revenue(self.crm, self.products, self.sale)

    def get_product_biggest_revenue(self):
        return product_biggest_revenue(self.crm, self.products, self.sale)

    def get_no_transactions_between_dates(self, start_date, end_date):
        return no_transactions_between_dates(start_date, end_date, self.crm, self.products, self.sale)

    def get_sum_price_transactions_between_dates(self, start_date, end_date):
        return sum_price_transactions_between_dates(start_date, end_date, self.crm, self.products, self.sale)

    def write_sale(self):
        write_sale_to_file(self.sale)


if __name__ == "__main__":
    m = ModelJSON()
    m.insert_crm("Jan", "Kowalski", "Somfy Sp. z o.o.", "dagmara@somfy.pl")
    m.insert_crm("Paweł", "Nowak", "Somfy Sp. z o.o.", "pawel@somfy.pl")
    m.update_crm(1, "Sławomir", "Brzozowski", "DG RSZ", "brzozasr@interia.pl")
    m.update_crm(2, "Marcin", "Jurek", "DG RSZ - ORK", "m.jurek@gmail.com")
    # m.delete_crm(2)
