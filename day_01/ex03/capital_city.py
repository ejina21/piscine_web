import sys


def capital_city():
    state = sys.argv
    if len(state) != 2:
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
    if state[1] in states:
        print(capital_cities[states[state[1]]])
    else:
        print('Unknown state')


if __name__ == '__main__':
    capital_city()