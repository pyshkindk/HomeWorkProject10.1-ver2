from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(get_executed, test_list):
    """Проверка правильности работы функции сортировки списка словарей по ключу 'EXECUTED'"""
    assert filter_by_state(test_list) == get_executed


def test_filter_by_state_canceled(get_canceled, test_list):
    """Дополнительная проверка правильности работы функции
    сортировки списка словарей по ключу 'CANCELED'"""
    assert filter_by_state(test_list, "CANCELED") == get_canceled


def test_sort_by_date_descending(sort_date_in_descending_order, test_list):
    """Проверка работы функции сортировки
    списка словарей по дате в порядке убывания"""
    assert sort_by_date(test_list) == sort_date_in_descending_order


def test_sort_by_date_ascending(sort_date_in_ascending_order, test_list):
    """Проверка работы функции сортировки
    списка словарей по дате в порядке возрастания"""
    assert sort_by_date(test_list, reverse=False) == sort_date_in_ascending_order
