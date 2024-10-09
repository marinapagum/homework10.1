def filter_by_state(list_dict: list, state =  "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа
state и возвращает новый список словарей, содержащий только те словари, у которых ключ
state соответствует указанному значению."""
    filtered_list = list()
    for ld in list_dict:
         if ld.get("state") == state:
             filtered_list. append(ld)
    return filtered_list

print(filter_by_state([{'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': '594226727', 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': '615064591', 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(list_dict: list, direction: bool = True) -> list:
    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате."""
    sorted_list = sorted(list_dict,  key=lambda x: x["date"], reverse=direction)
    return sorted_list

print(sort_by_date([{'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                    {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                    {'id': '594226727', 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                    {'id': '615064591', 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
