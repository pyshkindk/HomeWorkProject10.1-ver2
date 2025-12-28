import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import test_list_of_transactions


def test_filter_by_currency_usd(filter_transactions_by_usd, test_list_of_transactions):
    """Проверка на генерацию транзакций с заданной валютой - USD"""
    result = list(filter_by_currency(test_list_of_transactions, "USD"))
    assert result == filter_transactions_by_usd


def test_filter_by_currency_rub(filter_transactions_by_rub, test_list_of_transactions):
    """Проверка на генерацию транзакций с заданной валютой - RUB"""
    result = list(filter_by_currency(test_list_of_transactions, "RUB"))
    assert result == filter_transactions_by_rub


def test_filter_by_currency_empty():
    """Проверка на пустой список"""
    with pytest.raises(ValueError):
        filter_by_currency([], "")


def test_transaction_descriptions(test_list_of_transactions):
    """Проверка работы генератора вывода описания транзакций"""
    result = transaction_descriptions(test_list_of_transactions)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод со счета на счет"
    assert next(result) == "Перевод с карты на карту"
    assert next(result) == "Перевод организации"


@pytest.mark.parametrize(
    "start, stop, expected_cards",
    [
        (1000000000000000, 1000000000000002, ["1000 0000 0000 0000", "1000 0000 0000 0001", "1000 0000 0000 0002"]),
        (2000000000000005, 2000000000000007, ["2000 0000 0000 0005", "2000 0000 0000 0006", "2000 0000 0000 0007"]),
    ],
)
def test_card_number_generator_1(start, stop, expected_cards):
    result = list(card_number_generator(start, stop))
    assert result == expected_cards


def test_card_number_generator_2():
    result = card_number_generator(1, 5)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
    assert next(result) == "0000 0000 0000 0003"
    assert next(result) == "0000 0000 0000 0004"
    assert next(result) == "0000 0000 0000 0005"
