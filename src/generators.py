from typing import Any


def filter_by_currency(transactions: list, currency: str) -> filter[Any]:
    """Функция принимающая на вход список словарей, представляющих транзакции и
    генерирует транзакции по заданной валюты."""

    filtred_curency = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return filtred_curency
