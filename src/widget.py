from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number: str) -> str:
    """Функцию, которая умеет обрабатывать информацию как о картах, так и о счетах."""
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_card = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{mask_card}"
    return result


def get_date(old_data: str) -> str:
    """Функция, которая меняет формат даты"""
    data_slice = old_data[0:10].split("-")
    data_slice_join = ".".join(data_slice[::-1])
    return data_slice_join
