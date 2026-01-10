from itertools import count
from typing import Any, Generator, Iterator, Optional


def filter_by_currency(transactions: list, currency: str) -> Iterator[Any]:
    """Функция принимающая на вход список словарей, представляющих транзакции и
    генерирует транзакции по заданной валюты."""
    if not transactions:
        raise ValueError("Список транзакций пуст")
    filtred_curency = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    return filtred_curency


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """Генератор , который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    yield from (x["description"] for x in transactions)


def card_number_generator(start: int = 1, stop: Optional[int] = None) -> Generator[str, None, None]:
    """Генератор , который выдает номера банковских карт в заданном формате и диапозоне"""
    for i in count(start=start):
        if stop is not None and i > stop:
            break
        formatted_number = f"{i:016}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
