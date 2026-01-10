from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор функции автоматически логирующий начало
    и конец выполнения функции, а также ее результаты
    или возникшие ошибки."""

    def my_decorator(function: Callable) -> Callable:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)
                final_message = f"Начало выполнения функции\n{function.__name__} ok\nОкончание выполнения функции"
                output(final_message, filename)
                return result
            except Exception as e:
                error_message = f"{function.__name__} Error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                output(error_message, filename)
                raise e

        return wrapper

    return my_decorator


def output(message: str, filename: Optional[str]) -> None:
    """Функция для вывода сообщений либо в файл, либо в консоль."""
    if filename is not None:
        with open(filename, "a", encoding="utf--8") as file:
            file.write(message + "\n")
    else:
        print(message)


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
