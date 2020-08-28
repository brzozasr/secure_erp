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


def select_sales(id_sale, sale_dict):
    is_key = False
    for id_key in sale_dict.keys():
        if id_key == str(id_sale):
            is_key = True
    if is_key:
        return {str(id_sale): sale_dict[str(id_sale)]}
    else:
        print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
        return None
