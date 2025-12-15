import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("card, expected",
 [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 73654108430135874305", "Счет **4305"),

])
def test_mask_account_card(card, expected):
    """Тестирует корректную работу функции mask_account_card с разными входными данными."""
    assert mask_account_card(card) == expected

