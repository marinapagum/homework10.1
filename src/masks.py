def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    masks_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masks_card


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account = f"**{account_number[-4:]}"
    return mask_account
