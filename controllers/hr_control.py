len_hr = {"len_id_hr": (1, 6),
          "len_name_hr": (2, 20),
          "len_surname_hr": (2, 30),
          "len_birthday_hr": (10, 10),
          "len_department_hr": (2, 20),
          "len_email_hr": (6, 35),
          "len_password_hr": (8, 40)}

len_min = 0
len_max = 1


def _is_len_correct(length, min_length, max_length):
    if min_length <= length <= max_length:
        return True
    else:
        return False


def _len_max_hr():
    len_max_list = []
    for key, value in len_hr.items():
        len_max_list.append(len_hr[key][1])
    return len_max_list
