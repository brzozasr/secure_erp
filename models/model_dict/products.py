from models.model_dict.id_enum import ID
from models.model_dict.id_store import *

current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "products.json")


def _is_unique(products_dict, unique_key, product):
    product = product.lower()
    for id_key, value in products_dict.items():
        for key in value:
            if key == unique_key and product == value[key].lower():
                return False
    return True


def write_products_to_file(products_dict):
    with open(json_file, "w") as write_file:
        json.dump(products_dict, write_file, indent=4)


def set_products_from_file():
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            return json.load(read_json)
    else:
        return {}


def delete_product(id_prod, products_dict, sale_dict):
    if _is_id_prod_in_sale(id_prod, sale_dict):
        print('\033[31m', f"The product with ID {id_prod} cannot be deleted because it is used in sale!", '\033[0m')
        return False
    elif id_prod in products_dict:
        del products_dict[str(id_prod)]
        return True
    else:
        print('\033[31m', f"There is no such key \"{id_prod}\" in the database!", '\033[0m')
        return False


def select_product(id_prod, products_dict):
    if id_prod in products_dict:
        return {str(id_prod): products_dict[str(id_prod)]}
    else:
        print('\033[31m', f"There is no such key \"{id_prod}\" in the database!", '\033[0m')
        return None


def insert_product(products_dict, *prod_value):
    """Required arguments for function:
    - "Product's name":    string,
    - "Price":             float,
    - "Quantity":          integer."""
    key_list = ["name_prod", "price_prod", "quantity_prod"]
    if len(prod_value) == 3:
        product, price, quantity = prod_value
        if not _is_unique(products_dict, "name_prod", product):
            print('\033[31m', "The \"Product's name\" has to be unique!", '\033[0m')
            return False
        else:
            id_prod = str(get_id(ID.PRODUCT.value))
            products_dict[id_prod] = {}
            for k, v in zip(key_list, prod_value):
                products_dict[id_prod][k] = v
            return True
    else:
        print('\033[31m', "Missing argument(s)! 3 arguments are required!", '\033[0m')
        return False


def update_product(products_dict, *prod_value):
    """Required arguments for function:
    - "Id":                string,
    - "Product's name":    string,
    - "Price":             float,
    - "Quantity":          integer."""
    key_list = ["name_prod", "price_prod", "quantity_prod"]
    if len(prod_value) == 4:
        id_prod, product, price, quantity = prod_value
        if not _is_unique(products_dict, "name_prod", product):
            print('\033[31m', f"The \"Product's name\" has to be unique!", '\033[0m')
            return False
        else:
            is_key = False
            for id_key in products_dict.keys():
                if id_key == str(id_prod):
                    is_key = True
            if is_key:
                for k, v in zip(key_list, prod_value[1:]):
                    products_dict[str(id_prod)][k] = v
                return True
            else:
                print('\033[31m', f"There is no such key \"{id_prod}\" in the database!", '\033[0m')
                return False
    else:
        print('\033[31m', "Missing argument(s)! 4 arguments are required!", '\033[0m')
        return False


def _is_id_prod_in_sale(id_prod, sale_dict):
    for value_sale in sale_dict.values():
        if value_sale['id_prod_sale'] == id_prod:
            return True
    return False
