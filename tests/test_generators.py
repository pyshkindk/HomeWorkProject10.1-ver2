import pytest

from src.generators import filter_by_currency, transaction_descriptions
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
