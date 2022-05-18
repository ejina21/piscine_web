import sys
import dewiki
import json
import requests


def get_data(name):
    params = {
        'action': 'parse',
        'page': name,
        'format': 'json',
        'prop': 'wikitext',
        'redirects': 1
    }
    responce = requests.get('https://en.wikipedia.org/w/api.php', params=params)
    responce.raise_for_status()
    responce = json.loads(responce.text)
    if 'error' in responce:
        raise Exception('Такой страницы не существует, передайте другой параметр')
    write_data = dewiki.from_string(responce['parse']['wikitext']['*'])
    with open(f'{name}.wiki', 'w') as f:
        f.write(write_data)


def main():
    args = sys.argv
    if len(args) != 2:
        return print('Введите верное количество аргументов')
    try:
        get_data(args[1])
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    main()