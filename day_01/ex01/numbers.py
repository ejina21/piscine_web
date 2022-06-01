def my_number():
    with open('numbers.txt', 'r') as f: #Todo path change
        numbers = f.read()
        print(numbers.replace(',', '\n')[:-1])


if __name__ == '__main__':
    my_number()