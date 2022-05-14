import sys


def search_key(dict_items, elem):
    for key, value in dict_items.items():
        if value == elem:
            return key
    return None


def state():
    capital_sity = sys.argv
    if len(capital_sity) != 2:
        return
    states = {
        'Oregon': 'OR',
        'Alabama': 'AL',
        'New Jersey': 'NJ',
        'Colorado': 'CO',
    }
    capital_cities = {
        'OR': 'Salem',
        'AL': 'Montgomery',
        'NJ': 'Trenton',
        'CO': 'Denver',
    }
    key = search_key(capital_cities, capital_sity[1])
    if key:
        print(search_key(states, key))
    else:
        print('Unknown capital city')


if __name__ == '__main__':
    state()