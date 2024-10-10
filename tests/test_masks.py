import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize(
    "card_number, masks_card", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("6831982476737658", "6831 98** **** 7658"),
    ("8990922113665229", "8990 92** **** 5229"),
    ("5999414228426353", "5999 41** **** 6353"),
]
)

def test_get_mask_card_number(card_number, masks_card):
    assert get_mask_card_number(card_number) == masks_card

@pytest.mark.parametrize(
    "account_number, mask_account",[
         ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305")
])


def test_get_mask_account(account_number, mask_account):
    assert get_mask_account(account_number) == mask_account