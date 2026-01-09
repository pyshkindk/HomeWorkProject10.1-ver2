import pytest

from decorators.log import log, my_function


def test_log_correct(capsys):
    """Проверка на корректность работы декоратора"""

    @log()
    def success_function():
        success_function()
        captured = capsys.readouterr()
        assert "Начало выполнения функции\nmy_function ok\nОкончание выполнения функции" in captured.out


def test_log_error():
    """Проверка на возникновение ошибки"""

    @log()
    def fail_function():
        raise Exception("Error")

    with pytest.raises(Exception):
        fail_function()


def test_log_2():
    """Проверка создание файла и выводимой информации"""

    @log(filename=None)
    def function():
        function()
        result = my_function
        assert result == 3

    @log(filename="mylog.txt")
    def test_log():
        with open("mylog.txt", "r", encoding="utf--8") as file:
            log_content = file.read()
        assert "Начало выполнения функции\nmy_function ok\nОкончание выполнения функции" in log_content
