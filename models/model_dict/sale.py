from models.model_dict.id_enum import ID
from models.model_dict.id_store import *
from datetime import datetime

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "sale.json")


def write_sale_to_file(sale_dict):
    with open(json_file, "w") as write_file:
        json.dump(sale_dict, write_file, indent=4)


def set_sale_from_file():
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            return json.load(read_json)
    else:
        return {}


def delete_sale(id_sale, sale_dict, products_dict):
    if id_sale in sale_dict:
        products_dict[sale_dict[str(id_sale)]['id_prod_sale']]['quantity_prod'] += sale_dict[str(id_sale)][
            'quantity_sale']
        del sale_dict[str(id_sale)]
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
        return False


def select_sale(id_sale, sale_dict):
    if id_sale in sale_dict:
        return {str(id_sale): sale_dict[str(id_sale)]}
    else:
        print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
        return None


def insert_sale(crm_dict, products_dict, sale_dict, *sale_value):
    """Required arguments for function:
    - "CRM's ID":       string,
    - "Product's ID":   string,
    - "Quantity":       integer,
    - "Date of sale":   string."""
    key_list = ["id_crm_sale", "id_prod_sale", "quantity_sale", "date_sale"]
    if len(sale_value) == 4:
        id_crm, id_prod, quantity_sale, date_sale = sale_value
        if not _id_exists(id_crm, crm_dict):
            print('\033[31m', f"The client's ID \"{id_crm}\" not in the database!", '\033[0m')
            return False
        elif not _id_exists(id_prod, products_dict):
            print('\033[31m', f"The product's ID \"{id_prod}\" not in the database!", '\033[0m')
            return False
        elif not _is_quantity_correct(quantity_sale, id_prod, products_dict):
            print('\033[31m', "The quantity of product available in the stock is less than you want to sell!",
                  '\033[0m')
            return False
        else:
            id_prod = str(get_id(ID.SALE.value))
            sale_dict[id_prod] = {}
            for k, v in zip(key_list, sale_value):
                sale_dict[id_prod][k] = v
            return True
    else:
        print('\033[31m', "Missing argument(s)! 4 arguments are required!", '\033[0m')
        return False


def update_sale(crm_dict, products_dict, sale_dict, *sale_value):
    """Required arguments for function:
    - "Sale's ID":      string,
    - "CRM's ID":       string,
    - "Product's ID":   string,
    - "Quantity":       integer,
    - "Date of sale":   string."""
    key_list = ["id_crm_sale", "id_prod_sale", "quantity_sale", "date_sale"]
    if len(sale_value) == 5:
        id_sale, id_crm, id_prod, quantity_sale, date_sale = sale_value
        if id_prod == sale_dict[str(id_sale)]['id_prod_sale']:
            tmp_quantity = sale_dict[str(id_sale)]['quantity_sale'] + products_dict[id_prod]['quantity_prod']
        else:
            tmp_quantity = products_dict[id_prod]['quantity_prod']

        if not _id_exists(id_sale, sale_dict):
            print('\033[31m', f"The sale's ID \"{id_crm}\" not in the database!", '\033[0m')
            return False
        elif not _id_exists(id_crm, crm_dict):
            print('\033[31m', f"The client's ID \"{id_crm}\" not in the database!", '\033[0m')
            return False
        elif not _id_exists(id_prod, products_dict):
            print('\033[31m', f"The product's ID \"{id_prod}\" not in the database!", '\033[0m')
            return False
        elif quantity_sale > tmp_quantity:
            print('\033[31m', "The quantity of product available in the stock is less than you want to sell!",
                  '\033[0m')
            return False
        else:
            if id_prod == sale_dict[str(id_sale)]['id_prod_sale']:
                products_dict[id_prod]['quantity_prod'] += sale_dict[str(id_sale)]['quantity_sale']
                sale_dict[str(id_sale)]['quantity_sale'] = 0
            else:
                products_dict[sale_dict[str(id_sale)]['id_prod_sale']]['quantity_prod'] += sale_dict[str(id_sale)][
                    'quantity_sale']
                sale_dict[str(id_sale)]['quantity_sale'] = 0
            _is_quantity_correct(quantity_sale, id_prod, products_dict)
            for k, v in zip(key_list, sale_value[1:]):
                sale_dict[str(id_sale)][k] = v
            return True
    else:
        print('\033[31m', "Missing argument(s)! 5 arguments are required!", '\033[0m')
        return False


def select_data_to_show_sale(crm_dict, products_dict, sale_dict):
    result_dict = {}
    for key_sale, value_sale in sale_dict.items():
        result_dict[key_sale] = {}
        for key, value in value_sale.items():
            if key == "id_crm_sale":
                result_dict[key_sale][key] = [crm_dict[value]['name_crm'], crm_dict[value]['surname_crm'],
                                              crm_dict[value]['company_crm']]
            elif key == "id_prod_sale":
                result_dict[key_sale][key] = [products_dict[value]['name_prod'], products_dict[value]['price_prod']]
            else:
                result_dict[key_sale][key] = value
    return result_dict


def transaction_biggest_revenue(crm_dict, products_dict, sale_dict):
    full_sale_dict = select_data_to_show_sale(crm_dict, products_dict, sale_dict)
    if len(full_sale_dict) > 0:
        max_revenue = 0
        key = ""
        for key_sale, value_sale in full_sale_dict.items():
            revenue = value_sale['id_prod_sale'][1] * value_sale['quantity_sale']
            if revenue > max_revenue:
                max_revenue = revenue
                key = key_sale
        return {key: sale_dict[key]}
    return full_sale_dict


def product_biggest_revenue(crm_dict, products_dict, sale_dict):
    full_sale_dict = select_data_to_show_sale(crm_dict, products_dict, sale_dict)
    if len(full_sale_dict) > 0:
        products_set = set()
        for value_sale in full_sale_dict.values():
            products_set.add(value_sale['id_prod_sale'][0])
        max_product_revenue = 0
        product_name = ""
        for product in products_set:
            product_revenue = 0
            for key, value in full_sale_dict.items():
                if value['id_prod_sale'][0] == product:
                    revenue = value['id_prod_sale'][1] * value['quantity_sale']
                    product_revenue += revenue
            if product_revenue > max_product_revenue:
                max_product_revenue = product_revenue
                product_name = product
        return product_name, max_product_revenue
    return None


def no_transactions_between_dates(start_date, end_date, crm_dict, products_dict, sale_dict):
    full_sale_dict = select_data_to_show_sale(crm_dict, products_dict, sale_dict)
    if len(full_sale_dict) > 0:
        start_date = datetime(*map(int, start_date.split('-')))
        end_date = datetime(*map(int, end_date.split('-')))
        counter = 0
        for key_sale, value_sale in full_sale_dict.items():
            date_sale = datetime(*map(int, value_sale['date_sale'].split('-')))
            if start_date <= date_sale <= end_date:
                counter += 1
        return counter
    return None


def sum_price_transactions_between_dates(start_date, end_date, crm_dict, products_dict, sale_dict):
    full_sale_dict = select_data_to_show_sale(crm_dict, products_dict, sale_dict)
    if len(full_sale_dict) > 0:
        start_date = datetime(*map(int, start_date.split('-')))
        end_date = datetime(*map(int, end_date.split('-')))
        price_sum = 0
        for key_sale, value_sale in full_sale_dict.items():
            date_sale = datetime(*map(int, value_sale['date_sale'].split('-')))
            if start_date <= date_sale <= end_date:
                price_sum += value_sale['id_prod_sale'][1] * value_sale['quantity_sale']
        return price_sum
    return None


def _is_quantity_correct(quantity_sale, id_prod, products_dict):
    if len(products_dict) > 0:
        if products_dict[id_prod]['quantity_prod'] >= quantity_sale:
            products_dict[id_prod]['quantity_prod'] -= quantity_sale
            return True
        else:
            return False
    return False


def _id_exists(id_key, checked_dict):
    if len(checked_dict) > 0:
        if id_key in checked_dict:
            return True
        else:
            return False
    return False


def _get_prod_price(id_prod, products_dict):
    if len(products_dict) > 0:
        if products_dict[id_prod]['price_prod']:
            return products_dict[id_prod]['price_prod']
        else:
            return None
    return None

