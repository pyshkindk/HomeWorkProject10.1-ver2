import time
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
                start_time = time.time()
                result = function(*args, **kwargs)
                end_time = time.time()
                final_message = f"{function.__name__} ok, result - {end_time - start_time}, {result}"
                output(final_message, filename)
                return result
            except Exception as e:
                error_message = f"{function.__name__} Error: {type(e).__name__}, {args}, {kwargs}"
                output(error_message, filename)
                raise e

        return wrapper

    return my_decorator


def output(message: str, filename: Optional[str]) -> None:
    """Функция для вывода сообщений либо в файл, либо в консоль."""
    if filename is not None:
        with open(filename, "a") as file:
            file.write(message + "\n")
    else:
        print(message)
