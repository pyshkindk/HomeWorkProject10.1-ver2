import pytest

from decorators.log import log


def test_log(capsys):
    """Проверка на корректность работы декоратора"""

    @log()
    def function():
        function()
        result = capsys.readouterr()
        assert result.out == "Success"


def test_log_error():
    """Проверка на возникновение ошибки"""

    @log()
    def fail_function():
        raise Exception("Error")

    with pytest.raises(Exception):
        fail_function()
