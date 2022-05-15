import sys
import re
import os
import settings


def replace_data(data: str) -> str:
    return re.sub(r'{(\w+)}', lambda x: getattr(settings, x.group(1), None), data)


def check_errors(args) -> tuple:
    if len(args) != 2:
        return False, 'Неверное количество аргументов'
    if not os.path.exists(args[1]):
        return False, 'Файла не существует'
    _, extension = os.path.splitext(args[1])
    if extension != '.template':
        return False, 'Неверное расширение файла'
    return True, ''


def render():
    args = sys.argv
    status, message = check_errors(args)
    if not status:
        return print(message)
    with open(args[1], 'r') as f:
        data = f.read()
    data = replace_data(data)
    with open('myCV.html', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    render()
