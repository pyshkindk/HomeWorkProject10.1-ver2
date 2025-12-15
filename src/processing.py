from typing import Dict, List


def filter_by_state(list_of_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция принимающая список словарей и возвращающая новый список
    отсортированный по заданному параметру ключа state"""

    # Отсортированный список словарей.
    filtred_list = []

    for status in list_of_dicts:
        if status["state"] == state:
            filtred_list.append(status)

    return filtred_list


def sort_by_date(list_of_dicts: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимающая список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание) и
    возвращающая новый список, отсортированный по дате.
    """
    return sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse)
