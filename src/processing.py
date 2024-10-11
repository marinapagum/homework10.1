def filter_by_state(list_dict: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""
    filtered_list = list()
    for ld in list_dict:
        if ld.get("state") == state:
            filtered_list.append(ld)
    return filtered_list


def sort_by_date(list_dict_data: list, direction: bool = True) -> list:
    """Функция, которая принимает список словарей и возвращает новый список, отсортированный по дате."""
    sorted_list_data = sorted(list_dict_data, key=lambda x: x["date"], reverse=direction)
    return sorted_list_data
