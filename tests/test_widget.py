import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card, expected):
    """Тестирует корректную работу функции mask_account_card с разными входными данными."""
    assert mask_account_card(card) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-01-06T10:23:87.123765", "06.01.2020"),
        ("2015-10-25T15:46:34.216578", "25.10.2015"),
    ],
)
def test_get_date(date, expected):
    """Тестирует преобразование даты."""
    assert get_date(date) == expected
