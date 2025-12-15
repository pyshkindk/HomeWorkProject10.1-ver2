import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1596837868705199, "1596 83** **** 5199"),
        (7158300734726758, "7158 30** **** 6758"),
        (8990922113665229, "8990 92** **** 5229"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    """Тестирование функции маскировки номера карты (с заданной параметризацией)"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1596837868705199, "**5199"),
        (726758, "**6758"),
        (12222222222222222222122143, "**2143")
    ],
)
def test_get_mask_account(card_number, expected):
    """Тестирование функции вывода последних четырех цифр карты(с заданной параметризацией)"""
    assert get_mask_account(card_number) == expected
