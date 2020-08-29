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
    # is_key = False
    # for id_key in sale_dict.keys():
    #     if id_key == str(id_sale):
    #         is_key = True
    # if is_key:
    #     return {str(id_sale): sale_dict[str(id_sale)]}
    # else:
    #     print('\033[31m', f"There is no such key \"{id_sale}\" in the database!", '\033[0m')
    #     return None


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


if __name__ == "__main__":
    crm_dict1 = {"6": {"name_crm": "Dagmara", "surname_crm": "Brzozowska", "company_crm": "Somfy Sp. z o.o.",
                       "email_crm": "d.brzozowska@somfy.com"},
                 "8": {"name_crm": "Magdalena", "surname_crm": "Ba\u0142on", "company_crm": "Dexter",
                       "email_crm": "m.balon@dexter.com"}}
    prod_dict = {"1": {"name_prod": "Chleb razowy", "price_prod": 4.5, "quantity_prod": 340},
                 "2": {"name_prod": "Mas\u0142o", "price_prod": 8.75, "quantity_prod": 85},
                 "3": {"name_prod": "\u015amietana", "price_prod": 4.25, "quantity_prod": 1200}}
    sale_dict1 = {"1": {"id_crm_sale": "6", "id_prod_sale": "2", "quantity_sale": 40, "date_sale": "2020-08-28"},
                  "2": {"id_crm_sale": "8", "id_prod_sale": "1", "quantity_sale": 100, "date_sale": "2020-07-03"}}

    # insert_sale(crm_dict1, prod_dict, sale_dict1, "8", "3", 200, "2020-09-01")
    # print(sale_dict1)
    # print(prod_dict)
    # print('-' * 40)
    # update_sale(crm_dict1, prod_dict, sale_dict1, "2", "8", "1", 440, "2020-09-01")
    # print(sale_dict1)
    # print(prod_dict)
    print(select_data_to_show_sale(crm_dict1, prod_dict, sale_dict1))
