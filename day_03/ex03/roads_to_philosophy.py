import sys
from bs4 import BeautifulSoup
import requests


def wiki(title, my_list):
    response = requests.get(url=f'https://en.wikipedia.org{title}')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find(id='firstHeading').text
    if title in my_list:
        return print("Произошло зацикливание")
    my_list.append(title)
    print(title)
    if title == 'Philosophy':
        return print(f"{len(my_list)} roads from {my_list[0]} to philosophy !")
    content = soup.find(id='mw-content-text')
    links = content.select('p > a')
    for link in links:
        if link.get('href') is not None \
                and link['href'].startswith('/wiki/') \
                and not link['href'].startswith('/wiki/Wikipedia:')\
                and not link['href'].startswith('/wiki/Help:'):
            return wiki(link['href'], my_list)
    return print("It's a dead end !")


def main():
    args = sys.argv
    if len(args) != 2:
        return print('Введите один аргумент')
    try:
        my_list = []
        wiki(f'/wiki/{args[1]}', my_list)
    except Exception as e:
        print(f'Произошла ошибка: {e}')


if __name__ == '__main__':
    main()
