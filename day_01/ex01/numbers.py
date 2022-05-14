def my_number():
    with open('day_01/ex01/numbers.txt', 'r') as f: #Todo path change
        numbers = f.read()
        print(numbers.replace(',', '\n')[:-1])


if __name__ == '__main__':
    my_number()