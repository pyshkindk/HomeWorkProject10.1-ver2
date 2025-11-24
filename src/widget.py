import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функиция скрывающая название карты и
    ее номер и выдающая замаскированный номер"""
    filter_type = re.split(r"[0-9]", card)
    number_card = ""
    for i in card:
        if i.isdigit():
            number_card += i
    if len(number_card) == 16:
        return "".join(filter_type) + get_mask_card_number(number_card)
    else:
        return "".join(filter_type) + get_mask_account(number_card)


filter_card = mask_account_card("MasterCard 7158300734726758")
print(filter_card)


def get_date(date: str) -> str:
    """Функция возвращающая дату"""
    date_filter = "".join(re.findall(r"\d{4}-\d{2}-\d{2}", date))
    return f"{date_filter[-2:]}.{date_filter[5:7]}.{date_filter[:4]}"


result = get_date("2024-03-11T02:26:18.671407")
print(result)
