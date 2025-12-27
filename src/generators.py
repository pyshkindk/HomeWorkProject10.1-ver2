from typing import Generator, Any


def filter_by_currency(transactions: list, currency: str) -> filter[Any]:
    """Функция принимающая на вход список словарей, представляющих транзакции и
    генерирует транзакции по заданной валюты."""

    filtred_curency = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return filtred_curency


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Генератор , который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    yield from (x["description"] for x in transactions)
