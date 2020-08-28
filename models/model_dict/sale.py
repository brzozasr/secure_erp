from models.model_dict.id_enum import ID
from models.model_dict.id_store import *

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


def delete_sale(id_sale, sale_dict):
    is_key = False
    for id_key in sale_dict.keys():
        if id_key == str(id_sale):
            is_key = True
    if is_key:
        del sale_dict[str(id_sale)]
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
        return False


def select_sale(id_sale, sale_dict):
    is_key = False
    for id_key in sale_dict.keys():
        if id_key == str(id_sale):
            is_key = True
    if is_key:
        return {str(id_sale): sale_dict[str(id_sale)]}
    else:
        print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
        return None


def insert_sale(products_dict, sale_dict, *sale_value):
    """Required arguments for function:
    - "CRM's ID":       string,
    - "Product's ID":   string,
    - "Quantity":       integer,
    - "Date of sale":   string."""
    key_list = ["id_crm_sale", "id_prod_sale", "quantity_sale", "date_sale", "price_sale"]
    if len(sale_value) == 4:
        id_crm, id_prod, quantity_sale, date_sale = sale_value
        sale_value = list(sale_value)
        sale_value.append(_get_prod_price(id_prod, products_dict))
        if not _is_quantity_correct(quantity_sale, id_prod, products_dict):
            print('\033[31m', "The quantity of product available in the stock is less than you want to sell", '\033[0m')
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


def _is_quantity_correct(quantity_sale, id_prod, products_dict):
    if len(products_dict) > 0:
        for key, value in products_dict.items():
            if key == id_prod:
                if quantity_sale <= value['quantity_prod']:
                    products_dict[key]['quantity_prod'] -= quantity_sale
                    return True
        return False
    return False


def _get_prod_price(id_prod, products_dict):
    if len(products_dict) > 0:
        for key, value in products_dict.items():
            if key == id_prod:
                return value['price_prod']
        return None
    return None
