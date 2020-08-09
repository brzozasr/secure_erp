import json
import os

# set global id's dictionary
ids = {}
current_dir = os.path.dirname(os.path.realpath(__file__))
json_file = os.path.join(current_dir, "id_store.json")


def _write_ids_to_file():
    global ids
    start_ids = {"id_crm_store": 1, "id_prod_store": 1, "id_sale_store": 1, "id_hr_store": 1}
    if not os.path.exists(json_file):
        with open(json_file, "w") as write_file:
            json.dump(start_ids, write_file, indent=4)
    else:
        with open(json_file, "w") as write_file:
            json.dump(ids, write_file, indent=4)


def _set_ids_from_file():
    global ids
    if os.path.exists(json_file):
        with open(json_file, 'r') as read_json:
            ids = json.load(read_json)
    else:
        _write_ids_to_file()
        _set_ids_from_file()


def _set_id(id_enum):
    global ids
    ids[id_enum] += 1


def get_id(id_enum):
    global ids
    _set_ids_from_file()
    new_id = ids.get(id_enum)
    _set_id(id_enum)
    _write_ids_to_file()
    return new_id


if __name__ == "__main__":
    print(get_id("id_crm_store"))
    print(get_id("id_prod_store"))
    print(get_id("id_sale_store"))
    print(get_id("id_hr_store"))
