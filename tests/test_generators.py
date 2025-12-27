import pytest

from src.generators import filter_by_currency
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
