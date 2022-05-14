import sys


def search_key(dict_items, elem):
    elem = elem.upper()
    for key, value in dict_items.items():
        if value.upper() == elem:
            return key
    return None


def search_state(dict_items, elem):
    elem = elem.upper()
    for key in dict_items.keys():
        if key.upper() == elem:
            return key
    return None


def print_obj(el):
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
    key = search_key(capital_cities, el)
    state = search_key(states, key) if key else search_state(states, el)
    if state:
        print(f'{capital_cities[states[state]]} is the capital of {state}')
    else:
        print(f'{el} is neither a capital city nor a state')


def all_in():
    args = sys.argv
    if len(args) != 2:
        return
    for el in map(str.strip, args[1].split(',')):
        if el:
            print_obj(el)


if __name__ == '__main__':
    all_in()