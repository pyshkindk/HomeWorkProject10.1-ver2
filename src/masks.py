def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера карты"""

    string_code = str(card_number)

    return f"{string_code[:4]} {string_code[4:6]}** **** {string_code[-4:]}"


def get_mask_account(card_number: str) -> str:
    """Функция возвращающая последнии 4 цифры номера карты"""

    string_code_2 = str(card_number)
    return f"**{string_code_2[-4:]}"
