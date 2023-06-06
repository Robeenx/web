import os
from pathlib import Path


def add(filename: Path) -> None:
    """Создание переменных окружения из файла.

    Разделяет строки на ключ и значение по первому в строке символу
    равенства "=", прочие считаются частью значения. Убирает лишние
    пробелы, а так же перевод строки."""

    if filename.is_file():
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.rstrip('\n').split('=', 1)
                key, val = map(lambda x: x.strip(), line)
                os.environ[key] = val
